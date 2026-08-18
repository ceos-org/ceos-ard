"""Generate DIFFERENCES.md, an overview of the differences between similar
building blocks (e.g. time-ar/-sar/-sr/-st), including PFS-specific overrides.

Usage:
    python scripts/compare-building-blocks.py                  # generate + verify
    python scripts/compare-building-blocks.py --verify         # verify existing DIFFERENCES.md only
    python scripts/compare-building-blocks.py --baseline REF   # generate; additionally mark manual
        # content as potentially outdated when the group's compared content changed between the
        # git ref REF (the state the manual content was written against) and the working tree.
        # Only needed for manual content that has no stored state fingerprint yet; afterwards the
        # fingerprints handle this automatically.

HTML version: convert DIFFERENCES.md with https://www.netsmarter.com/md-to-html/
and add the following to the header:
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
    <style>
    body { grid-template-columns: 1fr min(60rem,90%) 1fr; }
    h1 { margin: 2rem; }
    h2, h3 { margin: 3rem 0 0.5rem; }
    h4, h5, h6 { margin: 2rem 0 0.5rem; }
    p, ul, ol, dl, blockquote { margin: 0.5em 0; }
    pre { margin: 0.5em 0; padding: 0.5rem; white-space: pre-wrap; overflow-wrap: break-word; }
    li > p { margin: 0.25em 0; }
    </style>
Add id attributes to the h2/h3 headings (same slugs as the TOC anchors) so the
table of contents links work.

Compared fields: title, description, and per requirement level (threshold/goal/
image) the description, the optional flag, and the notes.
Ignored fields: id, dependencies, glossary, references, changes, history,
remarks, and YAML comments.

For each differing field one variant is quoted verbatim as baseline and the
other variants are shown as word-level diffs against it (<del>/<ins> markup).
The verification step reconstructs both texts from the diff markup and compares
them against the YAML files, so the document is guaranteed to exactly mirror
the file contents.

The "Proposal" and "Internal notes" sections of each group are manual content
and preserved when the document is regenerated (keyed by the group heading;
content of removed/renamed groups is moved to an "Orphaned manual content"
section). A fingerprint of the group's compared content is stored next to
manual content; if the compared files change later, a review warning is
prepended to the manual text and stays until deleted by hand.
Do not use markdown headings inside these sections.
"""

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "DIFFERENCES.md"

# PFS/sensor suffixes used to group variants of the same building block
SUFFIXES = ["nrb-pol", "optical", "insar", "gslc", "nlsr", "sar", "orb", "pol", "cb", "ar", "sr", "st", "nrb"]

# Groups that cannot be derived from a shared base filename
EXTRA_GROUPS = {
    "corrections/atmosphere-*": [
        "requirements/corrections/atmosphere.yaml",
        "requirements/corrections/atmospheric.yaml",
    ],
    "metadata/data-access-*": [
        "requirements/metadata/data-access.yaml",
        "requirements/metadata/data-access-product.yaml",
        "requirements/metadata/data-access-source.yaml",
    ],
    "per-pixel/acquisition-id-*": [
        "requirements/per-pixel/acquisition-id-composite.yaml",
        "requirements/per-pixel/acquisition-id-mosaic.yaml",
    ],
    "corrections/radiometric-terrain-algorithm-*": [
        "requirements/corrections/radiometric-terrain-algorithm-applied.yaml",
        "requirements/corrections/radiometric-terrain-algorithm-minimal.yaml",
    ],
}

# Files merged into an automatically derived group
MERGE_INTO = {
    "requirements/per-pixel/machine-readability.yaml": ("requirements/metadata", "machine-readability"),
    "requirements/metadata/time-source.yaml": ("requirements/metadata", "time"),
}

# The measurement/measurand/backscatter building blocks are intentionally different per product
EXCLUDE = {
    "requirements/measurements/measurement-ar.yaml",
    "requirements/measurements/measurement-nlsr.yaml",
    "requirements/measurements/measurement-sr.yaml",
    "requirements/measurements/measurand-st.yaml",
    "requirements/measurements/backscatter-cb.yaml",
    "requirements/measurements/backscatter-gslc.yaml",
    "requirements/measurements/backscatter-insar.yaml",
    "requirements/measurements/backscatter-nrb.yaml",
    "requirements/measurements/backscatter-orb.yaml",
    "requirements/measurements/backscatter-pol.yaml",
}

LEVEL_ORDER = ["threshold", "goal", "image"]
NOT_SET = "*(not set)*"
NO_NOTES = "*(no notes)*"
MANUAL_FIELDS = ["Proposal", "Internal notes"]
MANUAL_KEYS = {f.lower() for f in MANUAL_FIELDS}
# an empty code fence for proposals, so the proposed text can be filled in directly
PLACEHOLDERS = {"Proposal": "```\n```", "Internal notes": "*none yet*"}
ORPHAN_SECTION = "Orphaned manual content"
STALE_WARNING = ("> ⚠️ The compared files have changed since this was written. "
                 "Review whether it still applies, then delete this line.")
SAR_TYPE = "Synthetic Aperture Radar"
# SAR-only building blocks are omitted entirely: their differences are
# intentional, as the SAR PFS were a combined document before being split
SAR_SECTION = "SAR building blocks"
GROUP_SECTIONS = {
    "SAR and Optical building blocks":
        "Variants used by both SAR and Optical PFS — differences here affect "
        "alignment across the two families.",
    "Optical building blocks": "Variants used only by Optical PFS.",
}
# a diff is only rendered if at least this share of the shorter text is
# covered by equal runs; below that, texts are too different for a useful diff
DIFF_THRESHOLD = 0.5
# equal runs shorter than this (between two changes) are folded into the change;
# this suppresses accidental matches like "tion" between unrelated sentence parts
MIN_EQUAL = 10
# red/green colors where inline styles are honored (e.g. VS Code preview);
# GitHub strips them and falls back to plain strikethrough/underline
DEL_TAG = '<del style="background:#ffd7d5;color:#82071e">'
INS_TAG = '<ins style="background:#ccffd8;color:#055d20;text-decoration:none">'
MARK_TAG = '<mark style="background:#ddf4ff;color:#0a3069">'
# placeholder line replaced by the table of contents once all sections are built
TOC_MARKER = "<!-- toc -->"


def load(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def norm_str(v):
    return v if isinstance(v, str) and v != "" else None


def base_name(stem):
    for s in sorted(SUFFIXES, key=len, reverse=True):
        if stem.endswith("-" + s):
            return stem[: -len(s) - 1]
    return stem


def build_groups(paths):
    auto = {}
    for rel in paths:
        if rel in EXCLUDE or "_template" in rel:
            continue
        folder, name = rel.rsplit("/", 1)
        key = MERGE_INTO.get(rel, (folder, base_name(name[:-len(".yaml")])))
        auto.setdefault(key, []).append(rel)
    groups = {}
    for (folder, base), files in auto.items():
        if len(files) > 1:
            groups[f"{folder.split('/', 1)[1]}/{base}-*"] = sorted(files)
    groups.update(EXTRA_GROUPS)
    return dict(sorted(groups.items(), key=lambda kv: kv[1][0]))


def collect_groups():
    return build_groups(sorted(p.relative_to(ROOT).as_posix()
                               for p in (ROOT / "requirements").rglob("*.yaml")))


def extract_fields(doc, levels):
    fields = {"title": norm_str(doc.get("title")), "description": norm_str(doc.get("description"))}
    reqs = doc.get("requirements") or {}
    for lvl in levels:
        data = reqs.get(lvl) or {}
        fields[f"{lvl}.description"] = norm_str(data.get("description"))
        fields[f"{lvl}.optional"] = bool(data.get("optional", False))
        fields[f"{lvl}.notes"] = [str(n) for n in (data.get("notes") or [])]
    return fields


def field_keys(levels):
    keys = ["title", "description"]
    for lvl in LEVEL_ORDER:
        if lvl in levels:
            keys += [f"{lvl}.description", f"{lvl}.optional", f"{lvl}.notes"]
    return keys


def field_label(key):
    if "." not in key:
        return key.capitalize()
    lvl, sub = key.split(".")
    return f"{lvl.capitalize()} — {sub}"


def label_to_key(label):
    if "—" not in label:
        return label.lower()
    lvl, sub = (p.strip() for p in label.split("—"))
    return f"{lvl.lower()}.{sub}"


def group_levels(docs):
    levels = set()
    for doc in docs.values():
        levels |= set(doc.get("requirements") or {})
    return levels


def fence(text):
    ticks = max([3] + [len(m) + 1 for m in re.findall(r"`+", text)])
    return "`" * ticks


def code_block(text):
    # multi-line blocks use <pre> so rendering matches the highlighted sections
    if "\n" in text:
        return f"<pre>{esc_html(text)}</pre>"
    f = fence(text)
    return f"{f}\n{text}\n{f}"


def join_notes(notes):
    return "\n\n".join(notes)


# ---------------------------------------------------------------------------
# Word-level diff with <del>/<ins> markup, reconstructable for verification
# ---------------------------------------------------------------------------

def esc_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def unesc_html(text):
    return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def diff_segments(base, new):
    sm = difflib.SequenceMatcher(a=base, b=new, autojunk=False)
    segments = []  # ("equal", text) or ("change", old, new)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        old, cur = base[i1:i2], new[j1:j2]
        if op == "equal":
            segments.append(("equal", old))
        else:
            segments.append(("change", old, cur))
    # fold short equal runs between two changes into one change, so that
    # character noise reads as a single clean <del>/<ins> pair
    merged = []
    i = 0
    while i < len(segments):
        seg = segments[i]
        if (seg[0] == "equal" and len(seg[1]) < MIN_EQUAL and merged and merged[-1][0] == "change"
                and i + 1 < len(segments) and segments[i + 1][0] == "change"):
            prev, nxt = merged[-1], segments[i + 1]
            merged[-1] = ("change", prev[1] + seg[1] + nxt[1], prev[2] + seg[1] + nxt[2])
            i += 2
        else:
            merged.append(seg)
            i += 1
    return merged


def char_diff(base, new):
    parts = []
    for seg in diff_segments(base, new):
        if seg[0] == "equal":
            parts.append(esc_html(seg[1]))
        else:
            if seg[1]:
                parts.append(f"{DEL_TAG}{esc_html(seg[1])}</del>")
            if seg[2]:
                parts.append(f"{INS_TAG}{esc_html(seg[2])}</ins>")
    return "".join(parts)


def similarity(base, new):
    """Share of the shorter text covered by equal runs that survive folding."""
    equal = sum(len(seg[1]) for seg in diff_segments(base, new) if seg[0] == "equal")
    return equal / min(len(base), len(new))


def reconstruct(diff, side):
    """Rebuild the base ('base') or compared ('new') text from diff markup."""
    drop, keep = ("ins", "del") if side == "base" else ("del", "ins")
    text = re.sub(rf"<{drop}[^>]*>.*?</{drop}>", "", diff, flags=re.S)
    text = re.sub(rf"</?{keep}[^>]*>", "", text)
    return unesc_html(text)


def strip_md_links(text):
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)


def heading_slug(text):
    """GitHub-style anchor slug for a heading text."""
    t = text.replace("`", "").lower()
    t = re.sub(r"[^a-z0-9 _-]", "", t)
    return t.replace(" ", "-")


def build_toc(lines):
    """Table of contents from the H2/H3 headings of the generated document."""
    toc = ["## Table of Contents", ""]
    seen = {}
    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            indent = "" if line.startswith("## ") else "  "
            text = strip_md_links(line.split(" ", 1)[1])
            slug = heading_slug(text)
            n = seen.get(slug, 0)
            seen[slug] = n + 1
            if n:
                slug = f"{slug}-{n}"
            toc.append(f"{indent}- [{text}](#{slug})")
    return toc


def collect_pfs():
    """Return (usage: file -> [pfs], overrides, cat_overrides, types: pfs -> type)."""
    usage, overrides, cat_overrides, types = {}, [], [], {}
    for doc_path in sorted((ROOT / "pfs").glob("*/document.yaml")):
        pfs = doc_path.parent.name
        doc = load(doc_path.relative_to(ROOT).as_posix())
        types[pfs] = doc.get("type")
        for cat in doc.get("requirements") or []:
            category = cat.get("category")
            if isinstance(category, dict):
                for mode in ("append", "replace"):
                    if category.get(mode):
                        cat_overrides.append((pfs, category["ref"], mode, category[mode]))
            for entry in cat.get("requirements") or []:
                ref = entry if isinstance(entry, str) else entry["ref"]
                used = usage.setdefault(f"requirements/{ref}.yaml", [])
                if pfs not in used:
                    used.append(pfs)
                if isinstance(entry, dict):
                    for mode in ("append", "replace"):
                        if entry.get(mode):
                            overrides.append((pfs, f"requirements/{ref}.yaml", mode, entry[mode]))
    return usage, overrides, cat_overrides, types


def group_section(files, usage, types):
    """Section title for a group, based on the types of the PFS that use it."""
    used_types = {types[p] for f in files for p in usage.get(f, [])}
    if used_types == {"Optical"}:
        return "Optical building blocks"
    if used_types == {SAR_TYPE}:
        return SAR_SECTION
    return "SAR and Optical building blocks"


def drop_sar_only(groups, overrides, usage, types):
    """Omit SAR-only groups and overrides that only affect SAR-only files."""
    groups = {label: files for label, files in groups.items()
              if group_section(files, usage, types) != SAR_SECTION}
    overrides = [o for o in overrides
                 if group_section([o[1]], usage, types) != SAR_SECTION]
    return groups, overrides


def usage_text(usage, target):
    return ", ".join(usage.get(target, [])) or "*not referenced by any PFS*"


def flatten_override(data):
    """Split an append/replace payload into compared fields and other keys."""
    compared, other = [], []
    for key, value in data.items():
        if key in ("title", "description") and norm_str(value) is not None:
            compared.append((key, norm_str(value)))
        elif key == "requirements":
            for lvl, lvl_data in (value or {}).items():
                if not lvl_data:
                    continue
                if norm_str(lvl_data.get("description")) is not None:
                    compared.append((f"{lvl}.description", norm_str(lvl_data["description"])))
                if lvl_data.get("optional") is not None:
                    compared.append((f"{lvl}.optional", bool(lvl_data["optional"])))
                if lvl_data.get("notes"):
                    compared.append((f"{lvl}.notes", [str(n) for n in lvl_data["notes"]]))
        else:
            other.append(key)
    return compared, other


def short_names(files):
    names = [f.rsplit("/", 1)[1] for f in files]
    if len(set(names)) < len(names):
        return dict(zip(files, files))
    return dict(zip(files, names))


def note_count(notes):
    return f"{len(notes)} note{'s' if len(notes) != 1 else ''}"


def file_link(f, shorts):
    return f"[`{shorts[f]}`]({f})"


def render_verbatim(files, value, shorts):
    names = ", ".join(file_link(f, shorts) for f in files)
    if isinstance(value, bool):
        return f"**{names}**: `{str(value).lower()}`"
    if isinstance(value, list):
        if not value:
            return f"**{names}**: {NO_NOTES}"
        blocks = "\n\n".join(code_block(n) for n in value)
        return f"**{names}** ({note_count(value)}):\n\n{blocks}"
    if value is None:
        return f"**{names}**: {NOT_SET}"
    return f"**{names}**:\n\n{code_block(value)}"


def render_diff(files, value, base_file, base_value, shorts):
    names = ", ".join(file_link(f, shorts) for f in files)
    base = file_link(base_file, shorts)
    if isinstance(value, list):
        head = f"**{names}** ({note_count(value)}, differences to {base}):"
        diff = char_diff(join_notes(base_value), join_notes(value))
    else:
        head = f"**{names}** (differences to {base}):"
        diff = char_diff(base_value, value)
    return f"{head}\n\n<pre>{diff}</pre>"


def sim_markup(base, new):
    parts = []
    for seg in diff_segments(base, new):
        if seg[0] == "equal" and len(seg[1]) >= MIN_EQUAL:
            parts.append(f"{MARK_TAG}{esc_html(seg[1])}</mark>")
        else:
            parts.append(esc_html(seg[1] if seg[0] == "equal" else seg[2]))
    return "".join(parts)


def render_similarity(files, value, base_file, base_value, shorts):
    names = ", ".join(file_link(f, shorts) for f in files)
    base = file_link(base_file, shorts)
    if isinstance(value, list):
        head = f"**{names}** ({note_count(value)}, similarities to {base} highlighted):"
        markup = sim_markup(join_notes(base_value), join_notes(value))
    else:
        head = f"**{names}** (similarities to {base} highlighted):"
        markup = sim_markup(base_value, value)
    return f"{head}\n\n<pre>{markup}</pre>"


def render_override(pfs, mode, key, value):
    verb = "appends to" if mode == "append" else "replaces"
    header = f"**{pfs}** {verb} **{field_label(key)}**"
    if isinstance(value, bool):
        return f"{header}: `{str(value).lower()}`"
    if isinstance(value, list):
        blocks = "\n\n".join(code_block(str(n)) for n in value)
        return f"{header} ({note_count(value)}):\n\n{blocks}"
    return f"{header}:\n\n{code_block(str(value))}"


# ---------------------------------------------------------------------------
# Manual content ("Proposal" / "Internal notes"), preserved across regeneration
# ---------------------------------------------------------------------------

def group_state(files, fields):
    """Fingerprint of a group's compared content, to detect later changes."""
    payload = json.dumps({f: fields[f] for f in files}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def baseline_groups(ref):
    """Group membership computed from the file list at the given git ref."""
    r = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", ref, "requirements"],
                       capture_output=True, text=True, encoding="utf-8")
    return build_groups(sorted(p for p in r.stdout.split("\n") if p.endswith(".yaml")))


def baseline_state(ref, files):
    """Group fingerprint computed from the YAML contents at the given git ref."""
    docs = {}
    for f in files:
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{f}"],
                           capture_output=True, text=True, encoding="utf-8")
        doc = yaml.safe_load(r.stdout) if r.returncode == 0 else None
        if not isinstance(doc, dict):
            return None  # file missing or empty at the ref -> treat as changed
        docs[f] = doc
    levels = group_levels(docs)
    return group_state(files, {f: extract_fields(d, levels) for f, d in docs.items()})


def extract_manual(text):
    manual = {}  # heading -> {manual field -> content}
    states = {}  # heading -> fingerprint at the time the content was written
    h3, field, buf = None, None, []

    def flush():
        content = "\n".join(buf).strip()
        # the separator between groups follows the last manual section; not content
        content = re.sub(r"\n*---$", "", content).strip()
        if h3 and field and content and content not in PLACEHOLDERS.values():
            manual.setdefault(h3, {})[field] = content
        buf.clear()

    for line in text.split("\n"):
        if line.startswith("## "):
            flush()
            h3, field = None, None
        elif line.startswith("### "):
            flush()
            h3, field = line[4:], None
        elif line.startswith("#### "):
            flush()
            field = line[5:] if line[5:] in MANUAL_FIELDS else None
        elif line.startswith("<!-- state: ") and h3 and not field:
            states[h3] = line[len("<!-- state: "):-len(" -->")]
        elif field:
            buf.append(line)
    flush()
    return manual, states


def generate(baseline=None):
    groups = collect_groups()
    usage, overrides, cat_overrides, types = collect_pfs()
    groups, overrides = drop_sar_only(groups, overrides, usage, types)
    manual, states = extract_manual(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else ({}, {})
    old_groups = baseline_groups(baseline) if baseline else {}
    used_headings = set()
    stale_groups = []
    out = []
    out.append("# Differences between similar building blocks")
    out.append("")
    out.append("<!-- Generated by scripts/compare-building-blocks.py. Only edit the Proposal and Internal notes sections manually. -->")
    out.append("")
    out.append("This document lists **only the differences** between building blocks that exist "
               "in several variants (e.g. `time-ar`/`-sar`/`-sr`/`-st`), as a basis for discussing "
               "how to align them. Fields that are identical across all files of a group are omitted.")
    out.append("")
    out.append("- The groups are split into sections by the type of the PFS that use them: "
               "only Optical, or both SAR and Optical. Building blocks used only by SAR PFS are "
               "omitted (as are PFS overrides that only affect them): their differences are "
               "intentional, as the SAR PFS were a combined document before being split.")
    out.append("- Compared fields: title, description, and per requirement level (threshold/goal/image) "
               "the description, the `optional` flag, and the notes.")
    out.append("- Ignored fields: id, dependencies, glossary, references, changes, history, and YAML comments. "
               "The remarks fields are not compared, but shown per group.")
    out.append("- Not compared: `measurements/measurement-*`, `measurements/measurand-st`, and "
               "`measurements/backscatter-*` (intentionally different per product).")
    out.append(f"- Per field, one variant is quoted verbatim as the baseline; similar variants only "
               f"highlight the differences to it: {DEL_TAG}red/struck-through</del> text only appears "
               f"in the baseline file, {INS_TAG}green/underlined</ins> text only in the compared file "
               f"(the colors are shown e.g. in the VS Code markdown preview; GitHub only shows "
               f"strikethrough/underline). For variants that are substantially different a diff "
               f"would be too noisy; they are quoted in full with the passages they share with the "
               f"baseline {MARK_TAG}highlighted in blue</mark> instead.")
    out.append(f"- {NOT_SET} means the field (or the whole requirement level) is absent or empty in that file.")
    out.append("- The *Proposal* and *Internal notes* sections are for manual input and are preserved "
               "when the document is regenerated. Fill the proposed text into the prepared code block. "
               "If the compared files change afterwards, a review warning is added on regeneration; "
               "if a group disappears (differences resolved), its manual content moves to an "
               "*Orphaned manual content* section at the end. "
               "Do not use markdown headings inside these sections.")
    out.append("")
    out.append(TOC_MARKER)
    ordered = []  # (section title, None) headers interleaved with (label, files)
    for sec in GROUP_SECTIONS:
        members = [g for g in groups.items() if group_section(g[1], usage, types) == sec]
        if members:
            ordered.append((sec, None))
            ordered.extend(members)
    first_in_section = True
    for label, files in ordered:
        if files is None:
            out.append("")
            out.append(f"## {label}")
            out.append("")
            out.append(GROUP_SECTIONS[label])
            first_in_section = True
            continue
        if not first_in_section:
            out.append("")
            out.append("---")
        first_in_section = False
        docs = {f: load(f) for f in files}
        levels = group_levels(docs)
        fields = {f: extract_fields(doc, levels) for f, doc in docs.items()}
        shorts = short_names(files)

        titles = {fields[f]["title"] for f in files}
        heading = titles.pop() if len(titles) == 1 else f"`{label}`"
        used_headings.add(heading)
        out.append("")
        out.append(f"### {heading}")
        out.append("")
        for f in files:
            out.append(f"- [`{f}`]({f}) — used by {usage_text(usage, f)}")

        for key in field_keys(levels):
            values = [fields[f][key] for f in files]
            if all(v == values[0] for v in values):
                continue
            out.append("")
            out.append(f"#### {field_label(key)}")
            out.append("")
            variants = []  # [files, value] with identical values grouped
            for f in files:
                value = fields[f][key]
                for entry in variants:
                    if entry[1] == value:
                        entry[0].append(f)
                        break
                else:
                    variants.append([[f], value])
            diffable = [v for v in variants
                        if (isinstance(v[1], str) or isinstance(v[1], list)) and v[1]]
            base_variant = max(diffable, key=lambda v: len(v[0])) if diffable else None
            if base_variant is not None:
                variants.remove(base_variant)
                variants.insert(0, base_variant)
            for variant in variants:
                as_text = (lambda v: join_notes(v) if isinstance(v, list) else v)
                if variant is base_variant or variant not in diffable:
                    out.append(render_verbatim(variant[0], variant[1], shorts))
                elif similarity(as_text(base_variant[1]), as_text(variant[1])) < DIFF_THRESHOLD:
                    out.append(render_similarity(variant[0], variant[1],
                                                 base_variant[0][0], base_variant[1], shorts))
                else:
                    out.append(render_diff(variant[0], variant[1],
                                           base_variant[0][0], base_variant[1], shorts))
                out.append("")
            while out[-1] == "":
                out.pop()

        remark_lines = []
        for f in files:
            remark = (docs[f].get("remarks") or "").rstrip()
            if remark:
                parts = remark.split("\n")
                remark_lines.append(f"- `{shorts[f]}`: {parts[0]}")
                remark_lines += ["  " + p for p in parts[1:]]
        if remark_lines:
            out.append("")
            out.append("#### Remarks from the building blocks")
            out.append("")
            out.extend(remark_lines)

        entries = manual.get(heading, {})
        state = group_state(files, fields)
        stale = bool(entries) and heading in states and states[heading] != state
        if not stale and baseline and entries and heading not in states:
            stale = (old_groups.get(label) != files
                     or baseline_state(baseline, files) != state)
        if stale:
            stale_groups.append(heading)
        if entries:
            out.append("")
            out.append(f"<!-- state: {state} -->")
        for name in MANUAL_FIELDS:
            content = entries.get(name, PLACEHOLDERS[name])
            if stale and name in entries and STALE_WARNING not in content:
                content = f"{STALE_WARNING}\n\n{content}"
            out.append("")
            out.append(f"#### {name}")
            out.append("")
            out.append(content)

    by_target = {}
    for pfs, target, mode, data in overrides:
        by_target.setdefault(target, []).append((pfs, mode, data))
    if by_target:
        out.append("")
        out.append("## PFS-specific overrides")
        out.append("")
        out.append("The PFS documents (`pfs/*/document.yaml`) can append to or replace parts of the "
                   "building blocks they reference, so the same file can render differently per PFS.")
    for n, target in enumerate(sorted(by_target)):
        if n:
            out.append("")
            out.append("---")
        out.append("")
        out.append(f"### [`{target}`]({target})")
        out.append("")
        out.append(f"Used by {usage_text(usage, target)}.")
        for pfs, mode, data in by_target[target]:
            compared, other = flatten_override(data)
            for key, value in compared:
                out.append("")
                out.append(render_override(pfs, mode, key, value))
            if other:
                out.append("")
                out.append(f"**{pfs}** also modifies: {', '.join(sorted(other))}.")

    if cat_overrides:
        out.append("")
        out.append("## PFS-specific overrides of requirement categories")
        for n, (pfs, ref, mode, data) in enumerate(cat_overrides):
            target = f"sections/requirement-categories/{ref}.yaml"
            if n:
                out.append("")
                out.append("---")
            out.append("")
            out.append(f"### [`{target}`]({target}) ({pfs})")
            compared, other = flatten_override(data)
            for key, value in compared:
                out.append("")
                out.append(render_override(pfs, mode, key, value))
            if other:
                out.append("")
                out.append(f"**{pfs}** also modifies: {', '.join(sorted(other))}.")
            heading = f"[`{target}`]({target}) ({pfs})"
            used_headings.add(heading)
            for name in MANUAL_FIELDS:
                out.append("")
                out.append(f"#### {name}")
                out.append("")
                out.append(manual.get(heading, {}).get(name, PLACEHOLDERS[name]))

    orphans = {h: m for h, m in manual.items() if h not in used_headings}
    if orphans:
        out.append("")
        out.append(f"## {ORPHAN_SECTION}")
        out.append("")
        out.append("Manual content whose group no longer exists (removed or renamed). "
                   "Move it to the right place or delete it.")
        for heading, fields_ in sorted(orphans.items()):
            out.append("")
            out.append(f"### {heading}")
            for name, content in fields_.items():
                out.append("")
                out.append(f"#### {name}")
                out.append("")
                out.append(content)
        print(f"WARNING: manual content for {len(orphans)} removed/renamed group(s) "
              f"moved to '{ORPHAN_SECTION}': {', '.join(sorted(orphans))}")
    if stale_groups:
        print(f"WARNING: compared files changed under manual content of {len(stale_groups)} group(s), "
              f"review warnings added: {', '.join(sorted(stale_groups))}")

    out.append("")
    idx = out.index(TOC_MARKER)
    out[idx:idx + 1] = build_toc(out[idx + 1:])
    OUTPUT.write_text("\n".join(out), encoding="utf-8", newline="\n")
    preserved = sum(len(v) for h, v in manual.items() if h in used_headings)
    out_name = OUTPUT.relative_to(ROOT) if OUTPUT.is_relative_to(ROOT) else OUTPUT.name
    print(f"Wrote {out_name} ({len(groups)} groups, "
          f"{len(overrides)} requirement overrides, {len(cat_overrides)} category overrides, "
          f"{preserved} manual entr{'ies' if preserved != 1 else 'y'} preserved)")


# ---------------------------------------------------------------------------
# Verification: parse DIFFERENCES.md and check every claim against the files
# ---------------------------------------------------------------------------

def parse_markdown(text):
    """Parse the generated document back into verifiable claims."""
    lines = text.split("\n")
    claims = []  # (kind, group/target, field, files, value)
    doc_groups = {}  # heading -> [files]
    doc_usage = {}  # file -> "used by" text
    doc_sections = {}  # heading -> section title it appears under
    section = h3 = None
    group_files = []
    field = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if field in MANUAL_KEYS and not line.startswith(("## ", "### ", "#### ")):
            i += 1
            continue
        if line.startswith("## "):
            section, h3, field = line[3:], None, None
        elif line.startswith("### "):
            h3, field = line[4:], None
            group_files = []
        elif line.startswith("#### "):
            field = label_to_key(line[5:])
        elif section == ORPHAN_SECTION:
            pass
        elif line.startswith("Used by ") and section == "PFS-specific overrides":
            target = re.sub(r"\[`([^`]+)`\]\([^)]*\)", r"\1", h3)
            doc_usage[target] = line[len("Used by "):-1]
        elif line.startswith("- [`") and section in GROUP_SECTIONS:
            m = re.match(r"- \[`([^`]+)`\]\([^)]*\) — used by (.*)$", line)
            group_files.append(m.group(1))
            doc_usage[m.group(1)] = m.group(2)
            doc_groups[h3] = list(group_files)
            doc_sections[h3] = section
        elif line.startswith("**"):
            m = re.match(r"\*\*(.+?)\*\*(.*)$", line)
            head, rest = m.group(1), m.group(2)
            names = re.findall(r"`([^`]+)`", head)
            if section in GROUP_SECTIONS:
                kind, ident, fkey = "group", h3, field
            else:
                if "also modifies" in rest:
                    i += 1
                    continue
                om = re.match(r" (appends to|replaces) \*\*(.+?)\*\*(.*)$", rest)
                mode = "append" if om.group(1) == "appends to" else "replace"
                kind, ident, fkey = "override:" + mode, h3, label_to_key(om.group(2))
                names = [head]  # PFS name
                rest = om.group(3)
            dm = re.fullmatch(r" (?:\((\d+) notes?, )?\(?differences to \[`([^`]+)`\]\([^)]*\)\):", rest)
            sm = re.fullmatch(r" (?:\((\d+) notes?, )?\(?similarities to \[`([^`]+)`\]\([^)]*\) highlighted\):", rest)
            if rest.strip() == f": {NOT_SET}":
                claims.append((kind, ident, fkey, names, None))
            elif rest.strip() == f": {NO_NOTES}":
                claims.append((kind, ident, fkey, names, []))
            elif re.fullmatch(r": `(true|false)`", rest.strip()):
                claims.append((kind, ident, fkey, names, rest.strip() == ": `true`"))
            elif dm:
                diff, i = read_pre(lines, i + 1)
                value = {"base": dm.group(2),
                         "new_text": reconstruct(diff, "new"),
                         "base_text": reconstruct(diff, "base"),
                         "notes": int(dm.group(1)) if dm.group(1) else None}
                claims.append((kind, ident, fkey, names, value))
            elif sm:
                markup, i = read_pre(lines, i + 1)
                value = {"sim": True, "base": sm.group(2),
                         "new_text": unesc_html(re.sub(r"</?mark[^>]*>", "", markup)),
                         "marked": [unesc_html(m) for m in
                                    re.findall(r"<mark[^>]*>(.*?)</mark>", markup, flags=re.S)],
                         "notes": int(sm.group(1)) if sm.group(1) else None}
                claims.append((kind, ident, fkey, names, value))
            else:
                nm = re.search(r"\((\d+) notes?\):$", rest)
                blocks, i = read_blocks(lines, i + 1, int(nm.group(1)) if nm else 1)
                value = blocks if nm else blocks[0]
                claims.append((kind, ident, fkey, names, value))
        i += 1
    return doc_groups, doc_usage, doc_sections, claims


def read_blocks(lines, i, count):
    """Read `count` verbatim blocks, each either fenced or a plain <pre> block."""
    blocks = []
    while len(blocks) < count:
        while not (re.fullmatch(r"`{3,}", lines[i]) or lines[i].startswith("<pre>")):
            i += 1
        if lines[i].startswith("<pre>"):
            raw, i = read_pre(lines, i)
            blocks.append(unesc_html(raw))
        else:
            f, i = lines[i], i + 1
            start = i
            while lines[i] != f:
                i += 1
            blocks.append("\n".join(lines[start:i]))
        if len(blocks) < count:
            i += 1
    return blocks, i


def read_pre(lines, i):
    while not lines[i].startswith("<pre>"):
        i += 1
    buf = []
    while not lines[i].endswith("</pre>"):
        buf.append(lines[i])
        i += 1
    buf.append(lines[i])
    return "\n".join(buf)[len("<pre>"):-len("</pre>")], i


def check_claim(fields, path, fkey, value, by_short, heading, errors):
    actual = fields[path][fkey]
    if isinstance(value, dict):  # diff or similarity claim
        expected = join_notes(actual) if isinstance(actual, list) else actual
        if value["new_text"] != expected:
            errors.append(f"{heading}/{fkey}: diff does not mirror {path}\n"
                          f"  document: {value['new_text']!r}\n  file:     {expected!r}")
        if isinstance(actual, list) and value["notes"] != len(actual):
            errors.append(f"{heading}/{fkey}: {path} has {len(actual)} notes, document claims {value['notes']}")
        base_path = by_short.get(value["base"])
        base_actual = fields[base_path][fkey] if base_path else None
        base_expected = join_notes(base_actual) if isinstance(base_actual, list) else base_actual
        if value.get("sim"):
            for segment in value["marked"]:
                if segment not in (base_expected or ""):
                    errors.append(f"{heading}/{fkey}: highlighted similarity not found in {value['base']}\n"
                                  f"  segment: {segment!r}")
        elif base_expected != value["base_text"]:
            errors.append(f"{heading}/{fkey}: diff baseline does not mirror {value['base']}\n"
                          f"  document: {value['base_text']!r}\n  file:     {base_expected!r}")
    elif actual != value:
        errors.append(f"{heading}/{fkey}: document does not mirror {path}\n"
                      f"  document: {value!r}\n  file:     {actual!r}")


def verify():
    text = OUTPUT.read_text(encoding="utf-8")
    doc_groups, doc_usage, doc_sections, claims = parse_markdown(text)
    errors = []

    groups = collect_groups()
    usage, overrides, cat_overrides, types = collect_pfs()
    groups, overrides = drop_sar_only(groups, overrides, usage, types)

    for heading, files in doc_groups.items():
        expected_section = group_section(files, usage, types)
        if doc_sections.get(heading) != expected_section:
            errors.append(f"{heading}: listed under {doc_sections.get(heading)!r}, "
                          f"expected {expected_section!r}")

    for f, used in doc_usage.items():
        if used != usage_text(usage, f):
            errors.append(f"{f}: 'used by' is {used!r}, expected {usage_text(usage, f)!r}")

    # 1. The document contains exactly the computed groups
    expected = {tuple(v) for v in groups.values()}
    actual = {tuple(v) for v in doc_groups.values()}
    for missing in expected - actual:
        errors.append(f"group missing from document: {missing}")
    for extra in actual - expected:
        errors.append(f"unexpected group in document: {extra}")

    # 2. Every group claim mirrors the file, and covers exactly the differing fields
    group_claims = {}
    for kind, ident, fkey, names, value in claims:
        if kind == "group":
            group_claims.setdefault(ident, []).append((fkey, names, value))
    for heading, files in doc_groups.items():
        missing = [f for f in files if not (ROOT / f).exists()]
        if missing:
            errors.append(f"{heading}: file(s) referenced in document no longer exist: {', '.join(missing)}")
            continue
        docs = {f: load(f) for f in files}
        levels = group_levels(docs)
        fields = {f: extract_fields(doc, levels) for f, doc in docs.items()}
        shorts = short_names(files)
        by_short = {s: f for f, s in shorts.items()}
        differing = {k for k in field_keys(levels)
                     if not all(fields[f][k] == fields[files[0]][k] for f in files)}
        claimed = group_claims.get(heading, [])
        claimed_fields = {fkey for fkey, _, _ in claimed}
        for k in differing - claimed_fields:
            errors.append(f"{heading}: differing field '{k}' missing from document")
        for k in claimed_fields - differing:
            errors.append(f"{heading}: field '{k}' in document but identical in all files")
        covered = {k: [] for k in claimed_fields}
        for fkey, names, value in claimed:
            for name in names:
                path = by_short.get(name)
                if path is None:
                    errors.append(f"{heading}/{fkey}: unknown file '{name}'")
                    continue
                covered[fkey].append(path)
                check_claim(fields, path, fkey, value, by_short, heading, errors)
        for fkey, paths in covered.items():
            if sorted(paths) != sorted(files):
                errors.append(f"{heading}/{fkey}: files covered {sorted(paths)} != group {sorted(files)}")

    # 3. Override claims mirror pfs/*/document.yaml, and all overrides are present
    expected_overrides = set()
    for pfs, target, mode, data in overrides:
        for key, value in flatten_override(data)[0]:
            expected_overrides.add((f"override:{mode}", target, key, pfs))
    for pfs, ref, mode, data in cat_overrides:
        target = f"sections/requirement-categories/{ref}.yaml"
        for key, value in flatten_override(data)[0]:
            expected_overrides.add((f"override:{mode}", f"{target} ({pfs})", key, pfs))
    override_data = {(f"override:{m}", t, p): d for p, t, m, d in overrides}
    override_data.update({(f"override:{m}", f"sections/requirement-categories/{r}.yaml ({p})", p): d
                          for p, r, m, d in cat_overrides})
    for kind, ident, fkey, names, value in claims:
        if kind == "group":
            continue
        pfs = names[0]
        target = re.sub(r"\[`([^`]+)`\]\([^)]*\)", r"\1", ident)
        expected_overrides.discard((kind, target, fkey, pfs))
        data = override_data.get((kind, target, pfs))
        if data is None:
            errors.append(f"override in document not found in PFS: {pfs} {kind} {target}")
            continue
        actual_value = dict(flatten_override(data)[0]).get(fkey)
        if actual_value != value:
            errors.append(f"override {pfs}/{target}/{fkey}: document does not mirror PFS document\n"
                          f"  document: {value!r}\n  pfs:      {actual_value!r}")
    for kind, target, key, pfs in expected_overrides:
        errors.append(f"override missing from document: {pfs} {kind} {target} {key}")

    if errors:
        print(f"VERIFICATION FAILED ({len(errors)} error(s)):")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"Verification passed: {sum(1 for c in claims if c[0] == 'group')} group claims and "
          f"{sum(1 for c in claims if c[0] != 'group')} override claims exactly mirror the files.")


if __name__ == "__main__":
    if "--verify" not in sys.argv:
        baseline = None
        if "--baseline" in sys.argv:
            baseline = sys.argv[sys.argv.index("--baseline") + 1]
        generate(baseline)
    verify()
