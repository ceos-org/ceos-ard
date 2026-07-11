# Versioning <!-- omit in toc -->

The CEOS-ARD Product Family Specifications (PFS) follow [Semantic Versioning 2.0.0](https://semver.org/) (SemVer).
Each PFS is versioned independently as `MAJOR.MINOR.PATCH` (e.g. 5.0.2) and released with a Git tag following the pattern `<PFS>-v<major>.<minor>.<patch>` (see [CONTRIBUTING.md](CONTRIBUTING.md#release-process)).

This document defines what counts as a **major** (i.e. breaking), **minor**, or **patch** change, both for the PFS documents and for the individual building blocks they are compiled from.

- [Guiding Principle](#guiding-principle)
- [How Versions Are Determined](#how-versions-are-determined)
- [Classification by Building Block Type](#classification-by-building-block-type)
  - [Requirements](#requirements)
  - [Glossary](#glossary)
  - [References](#references)
  - [Editorial Content](#editorial-content)
  - [PFS Documents](#pfs-documents)
  - [Templates and Assets](#templates-and-assets)
- [Quick Reference](#quick-reference)
- [Recording Changes](#recording-changes)

## Guiding Principle

SemVer is defined in terms of a "public API". For CEOS-ARD, the public API of a PFS is its **normative content**: everything a data provider assesses their product against in a self-assessment, and everything a data user relies on when they see a product labelled as CEOS-ARD compliant.

Self-assessments are made against a specific version of a PFS and remain valid for that version indefinitely; a new release never retroactively invalidates them. The version number instead signals what it takes for an already assessed product to claim compliance with the *new* version. The anchor question for classifying a change is:

> **Can a product that is compliant with the previous version claim compliance with the new version without a re-assessment?**

- **Major (breaking):** No. A product that was compliant with the previous version may not meet the new threshold requirements. Data providers have to redo (parts of) their self-assessment - and possibly change their product - to claim compliance with the new version.
- **Minor:** Yes. The normative content changes, but every product that was compliant before is also compliant with the new version. This includes *relaxations* of requirements: removing a threshold requirement, loosening a limit, or downgrading a threshold requirement to a goal requirement never forces a re-assessment, so these are minor - even though data users should be aware that the guarantees provided by compliance have changed. It also includes changes to goal requirements: these may lead to a better or worse goal classification under the new version, so providers may *optionally* re-assess to update their score, but they are not required to.
- **Patch:** The normative meaning does not change at all. Editorial fixes, wording clarifications, formatting, identifier housekeeping, and corrections to non-normative content.

Three consequences of this principle are worth spelling out:

1. **Classify by effect, not by intent or by size.** A one-character typo fix that accidentally changes a limit from `10 m` to `100 m` is a normative change, not a patch. A large restructuring of the whole document that leaves every requirement semantically intact is a patch.
2. **When in doubt, pick the higher level.** It is always safe to release a major version for a non-breaking change; the reverse silently lets products claim compliance with a version whose requirements they may not meet.
3. **Product assessments are irrelevant.** Classification depends on the normative effect of the change, not on whether any product assessment currently exists. A change can still be major even if no assessment has been published yet.

## How Versions Are Determined

Building blocks are shared across PFS and are **not versioned individually**. Instead:

1. Every change to a building block or to a PFS `document.yaml` is recorded in the corresponding `changes` list, with a `level` of `major`, `minor`, or `patch` (enforced by the CEOS-ARD CLI schema).
2. When a PFS is released, its new version number is determined by the **highest level** among all direct or indirect changes that affect that PFS since its last release.

Because building blocks are shared, note:

- A change to a shared building block propagates to **every PFS that uses it**. For example, a single breaking change to `requirements/per-pixel/nodata.yaml` will eventually trigger a new major release of several PFS.
- The `level` recorded on the change describes the change itself. Whether it actually affects a given PFS depends on whether that PFS includes the building block. A new building block that is not (yet) referenced by any `document.yaml` has no version impact at all. Changes to a building block impact the version of a PFS only after the building block has been part of a release of that PFS for the first time.

## Classification by Building Block Type

### Requirements

Requirement files (in folder [`requirements`](./requirements/)) contain the threshold and goal sub-requirements, notes, dependencies, and links to glossary terms and references.

Threshold requirements are mandatory; goal requirements are optional. Self-assessments also record which goal requirements a product meets, and providers may advertise goal-level compliance.

**Major** - a compliant product may become non-compliant:

- Tightening a threshold requirement, e.g.:
  - a numeric limit becomes stricter (geometric accuracy of 5 m instead of 10 m; time to the millisecond instead of the second);
  - a normative verb is strengthened (*should* → *must*, *recommended* → *required*);
  - an additional condition is added ("… and the offset from UTC must be unambiguously identified");
  - a choice is removed ("either X or Y" becomes "X only").
- Adding a new threshold sub-requirement to an existing requirement file.
- Upgrading a goal requirement to a threshold requirement.
- Broadening what a threshold requirement applies to, so that it now constrains product aspects it did not constrain before (e.g. a masking requirement that applied to clouds now also applies to cloud shadows).
- Adding a note that effectively introduces a new constraint. Notes are meant to be informative. If a note changes what a provider has to do, it is a normative change and should usually be moved into the requirement description instead.
- Changing a dependency (i.e. the list in `dependencies`) so that it points to a stricter requirement, when the dependency is normatively invoked by the requirement text.

**Minor** - normative content changes, but compliant products remain compliant:

- Relaxing a threshold requirement, e.g.:
  - a numeric limit becomes more lenient (geometric accuracy of 10 m instead of 5 m; time to the second instead of the millisecond);
  - an alternative means of compliance is added ("X" becomes "either X or Y");
  - a condition is removed.
- Removing a threshold sub-requirement entirely.
- Downgrading a threshold requirement to a goal requirement.
- Adding a new goal sub-requirement, tightening an existing goal requirement, relaxing a goal requirement, or removing one.
- Changing a dependency so that it points to a more lenient requirement.

**Patch** - no change to normative meaning:

- Fixing typos, grammar, or punctuation.
- Rewording for clarity without changing meaning (e.g. making the "no threshold requirement applies" wording consistent across requirements).
- Formatting changes.
- Renaming a requirement file or identifier, provided the old identifier is recorded in `history` and all referencing PFS and dependencies are updated.
- Adding, removing, or reordering entries in `glossary` or `references` lists (the linked content itself is classified separately, see below).
- Adding or improving the introductory `description` of a requirement, as long as it only provides context.
- Adding a note that clarifies or documents existing flexibility without changing what is required.
- Filling in `changes` or `history` fields.

Changes to entries in the `metadata` section generally follow the same pattern.

> [!IMPORTANT]
> Requirement category descriptions must not contain normative requirements. If a requirement-like statement is discovered in a category, move it into a proper requirement file under `requirements` and classify that move by the normative effect of the requirement change. See also the chapter ["Editorial Content"](#editorial-content) for more details.

### Glossary

Glossary entries (in the folder [`glossary`](./glossary/)) define terms used in requirements. A definition change can silently change the meaning of every requirement that uses the term, so classify by the **effect on the requirements that use it**:

- **Major:** Changing a definition so that a threshold requirement effectively becomes stricter. Example: a threshold requirement demands that clouds are flagged per pixel; redefining *cloud* to include thin cirrus tightens that requirement for every provider whose cloud mask excluded cirrus.
- **Minor:** Changing a definition so that requirements using the term effectively become more lenient, or so that only goal requirements are affected. Example: narrowing the definition of *cloud* so fewer pixels must be flagged.
- **Patch:**
  - Fixing typos or improving the wording of a definition without changing its meaning.
  - Expanding or correcting the long form of an abbreviation (e.g. DEM → Digital Elevation Model).
  - Adding a new glossary entry (making an already-used term explicit, or preparing a term for future use).
  - Removing a glossary entry that is no longer referenced anywhere.
  - Renaming a glossary file (with all referencing building blocks updated).

### References

The BibTeX-based references (in folder [`references`](./references/)) are only relevant for compliance where a requirement normatively cites them ("metadata must be provided according to @iso19115"). Everything else is bibliographic housekeeping:

- **Major:** Replacing a normatively cited document with a different edition or successor whose provisions are stricter or incompatible (e.g. pointing a **threshold** metadata requirement from ISO 19115:2003 to a newer edition that mandates additional fields). The requirement text may be unchanged, but its meaning is not.
- **Minor:** Replacing a normatively cited document with an edition whose relevant provisions are more lenient for the affected **threshold** requirement, replacing a document that is normatively cited only by goal requirements, or adding an alternative normative reference a provider may follow instead.
- **Patch:**
  - Correcting BibTeX metadata: authors, title, year, DOI, URL, page numbers.
  - Fixing a broken link or pointing to a better-accessible copy of the *same* document.
  - Adding an informative (non-normatively cited) reference.
  - Removing a reference that is no longer cited.
  - Renaming a reference id/file (with the BibTeX entry identifier and all referencing building blocks updated).

### Editorial Content

Everything in [`sections`](./sections/) is editorial and non-normative by default, including:

- introduction chapters (in [`sections/introduction`](./sections/introduction/)),
- requirement categories (in [`sections/requirement-categories`](./sections/requirement-categories/)),
- annexes (in [`sections/annexes`](./sections/annexes/)), and
- other or related narrative content.

Changes to content in `sections` are therefore usually **patch** changes: rewriting explanatory text, updating examples, improving figures, restructuring chapters, or reordering sections.

> [!IMPORTANT]
> There is one **exception**: if a requirement normatively references specific content in `sections/` (for example, "must follow the procedure in Annex A"), that referenced content is relevant for compliance and must be classified by effect just like requirement text (major/minor).

Requirements must remain self-contained in the `requirements` folder (optionally using glossary/reference links). If normative semantics would otherwise depend on text in any editorial content, that normative text must be moved into a requirement and versioned as a requirement change.

### PFS Documents

The `document.yaml` in each PFS folder ([`pfs/<PFS>`](./pfs/)) selects which building blocks make up a PFS, so list changes here are often the ones that actually change what a provider is assessed against:

**Major:**

- Adding a requirement (with a threshold part) to the `requirements` list.
- Replacing a requirement with a stricter variant (e.g. swapping `metadata/time` for a variant that additionally demands per-pixel times at threshold level), including via dependency `replace` overrides.
- Narrowing `applies_to`. Products that fall outside the new scope can no longer be assessed against the new version of this PFS at all.

**Minor:**

- Removing a requirement from the `requirements` list (a relaxation).
- Replacing a requirement with a more lenient variant.
- Adding a requirement that only has goal parts.
- Broadening `applies_to`. Existing products remain in scope and compliant; new kinds of products become eligible.

**Patch:**

- Moving requirements between categories, reordering requirements or categories, or renaming categories (presentation/numbering only).
- Adding, removing, or reordering `introduction` and `annexes` entries.
- Changes to `title`, `type`, `background`, `authors`, document-level `glossary`/`references` lists, and `changes` entries themselves.

### Templates and Assets

- Templates (layout, styles, HTML/PDF/DOCX rendering) are purely presentational and never require a version bump on their own. If a PFS is re-released for other reasons, template improvements ride along; if a re-release is needed *only* to fix broken rendering, it is a **patch**.
- Replacing or improving an illustrative figure is a **patch**. If a figure carries normative content (e.g. a decision tree that a requirement tells providers to follow), classify changes to it like requirement changes.

## Quick Reference

| Change | Level |
| ------ | ----- |
| Threshold requirement tightened, added, or goal upgraded to threshold | major |
| Glossary/reference/annex change that effectively tightens a threshold requirement | major |
| `applies_to` narrowed | major |
| Threshold requirement relaxed, removed, or downgraded to goal | minor |
| Goal requirement added, removed, tightened, or relaxed | minor |
| `applies_to` broadened | minor |
| Wording, typos, formatting, restructuring without change in meaning | patch |
| Identifier/file renames with `history` and references updated | patch |
| Bibliographic corrections, informative references, and non-normative edits in `sections` | patch |
| Non-normative metadata updates (bookkeeping/provenance) | patch |
| Notes, descriptions, and glossary edits that only clarify | patch |
| Template/styling changes | patch (only if a release is needed at all) |

## Recording Changes

Every change must be recorded in the `changes` list of the affected building block (or of `document.yaml` for document-level changes):

```yaml
changes:
  - date: 2026-07-11
    author: Jane Doe
    level: minor
    change: |-
      Relaxed the threshold geometric accuracy from 10 m to 12 m.
    reason: Aligned with the capabilities of currently operating missions.
```

Guidelines:

- Classify each entry individually; do not pre-aggregate. The release process derives the version bump from the highest `level` among all pending changes.
- In the change description, state the normative effect explicitly so the classification can be verified.
