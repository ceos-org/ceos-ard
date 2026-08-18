# Requirements

This is the folder that contains requirements for CEOS-ARD as building blocks.
The requirements are structured into folders and are described through YAML files.

## YAML file structure

The YAML files consist of the following components:

- `id` (required): A unique identifier for the requirement. Must be unique across all requirements. Recommendation is to keep it between 6 and 10 characters and make it "pronouncable" so that it's easier to communicate them. If unsure about uniqueness, conflicts will be flagged by the validator.
- `title` (required): A short title for the requirement
- `description`: An introduction for the requirement that sets the context.
  Due to historical reasons, most requirements don't provide such an introduction yet.
- `requirements:` (required): The list of sub-requirements.
  - Each requirement has a unique key, often `goal` or `threshold`, but can be anything.
    Each value is a sub-requirement with the following components:
    - `description` (required): The requirements with Markdown formatting
    - `notes`: A list of additional notes. A note should be short and not be longer than one paragraph. Limited Markdown formatting is available.
    - `optional`: If set to `true`, a goal requirement. If not set or `false`, a threshold requirement.
    - `metadata`: Placeholder for future use.
- `dependencies`: A mapping of named links to requirements. See section [Dependencies](#dependencies).
- `sections`: A mapping of named links to sections (introduction, annexes, requirement categories). See section [Dependencies](#dependencies).
- `glossary`: Any terms that are relevant for this requirement (e.g. are used in the text). Use any file name (without extension) from the [glossary](../glossary/) folder.
- `references`: Any relevant references for this requirement and are referred to in the text using the @ notation (see [Markdown](#markdown)). Use any file name (without extension) from the [references](../references/) folder.
- `changes`: The changelog that describes the changes over time for this building block. See section [Changelog](#changelog).
- `history`: Refers to old identifiers of this requirement in case it has been renamed.
- `remarks`: Internal editorial notes, todos, or other remarks. Only for internal use, they are not included in the generated documents.
- `deprecated`: Flags a requirement as deprecated. It should not be used anymore and transitioned out of usage as soon as possible. The `changes` should explain the deprecation and direct towards alternatives / successors.

The other building blocks share most of these components:

- Sections (introduction, annexes, requirement categories) consist of `title`, `description`, `glossary`, `references`, `changes`, `remarks`, and `deprecated`.
- Glossary terms consist of `term`, `description`, `references`, `changes`, and `remarks`, and `deprecated`.

## Changelog

The `changes` component describes the changes over time for a building block.
Each entry in the list consists of the following components (all required):

- `date`: The date of the change in ISO format (`YYYY-MM-DD`).
- `author`: The name of the editor who made the change.
- `change`: A description of the change. Markdown is supported for formatting.
- `reason`: A short justification for the change.
- `level`: The severity of the change, one of `major` (breaking change), `minor`, or `patch`.

## Markdown

The flavor of Markdown that is implemented here has some additional features.

See [References / Citation](#references-and-citation), [Dependencies](#dependencies), and [Embedding titles](#embedding-titles) for more details.

<!-- todo: add more details -->

## References and Citation

You can use references and citations as in scientific writing.

1. Download the BibTeX file for the reference.
2. Save it to the [`references`](../references/) folder.
   The filename (without `.bib` extension) is the reference id and must match the BibTeX entry identifier.
3. Add the id to the `references` list in the YAML file of the building block.
4. Optionally, cite the reference inline in any Markdown field (e.g. `description` and `notes`) using `@id` or `[@id]`, where `id` is the reference id:
   - `@id` renders as `Name (Year)` with the year linking to the reference.
   - `[@id]` renders as `(Name, Year)` with name and year linking to the reference.
   - References listed in `references` but not cited inline will still appear in the References section.

## Dependencies

Dependencies are links to other building blocks that are usually mentioned in the text using the @ notation.
They are available in requirements, sections (introduction, annexes, requirement categories), and the PFS document itself:

- `dependencies` links to requirements.
- `sections` links to sections. The paths are relative to the [sections](../sections/) folder,
  so the first path segment (`introduction`, `annexes`, or `requirement-categories`) determines the type of the target.

Both are defined as a mapping of alias to path(s):

```yaml
dependencies:
  my-alias: metadata/time
  # a list defines candidates, of which the first one
  # included in the compiled document is selected:
  orbit:
    - metadata/orbit-gslc
    - metadata/orbit
sections:
  topo: annexes/sar-topographic-phase-removal
  pxl: requirement-categories/per-pixel-metadata
  what-is: introduction/what-are-ceos-ard-products
```

The alias is a short name used to reference the link in text (e.g. `[@my-alias]` or `@my-alias`).
The path is the folder name (if applicable) and the file name (without file extension). For example, `metadata/time` for the file [metadata/time.yaml](metadata/time.yaml).
During generation, the aliases are replaced with the actual section anchors of the targets in the compiled document.
A link to a building block that is not included in the compiled document fails the generation and is reported by the validation.

Using named aliases allows a PFS to override individual link targets
via the `replace` mechanism without changing the requirement text.

Due to the fact that requirements don't include the category ID and could be ambiguous, the requirement links are resolved as follows:

1. The link will refer to the requirement with the given path in the same requirement category if it exists.
2. Otherwise, the link will refer to the requirement with the given path in any other category.

This means if a requirement is used both in the same requirement category and in another category, you can't refer to the requirement that is used in the other requirement category.

## Embedding titles

To mention another building block by name without linking to it (e.g. a block in a different PFS that is not part of the compiled document), embed its title with `@title:path` in any Markdown field:

```md
see annex "@title:sections/annexes/sar-topographic-phase-removal" in the applicable PFS
```

The path is relative to the repository root, without the `.yaml` extension. During generation, the placeholder is replaced with the `title` (or `term` for glossary terms) read from the referenced file, so the text stays consistent when the title changes.

This is a soft reference: unlike [Dependencies](#dependencies), the referenced building block does not need to be included in the compiled document and no link is generated. However, the file must exist on disk, otherwise generation and validation fail.

## Append / Replace

A PFS document (`pfs/*/document.yaml`) lists the requirement categories and requirements it consists of by their path.
By default, a building block is included as-is:

```yaml
requirements:
  - category: general-metadata
    requirements:
      - metadata/data-access
```

To adapt a building block for a specific PFS without changing the shared file,
provide a mapping with a `ref` and the changes in `replace` and/or `append` instead of the plain path.
This works for both requirements and requirement categories.

```yaml
requirements:
  - category:
      ref: general-metadata
      append:
        description: |-
          This paragraph is added to the category description.
        glossary:
          - doi
    requirements:
      - metadata/data-access
      - ref: per-pixel/ellipsoidal-incident-angle
        replace:
          requirements:
            image:
              optional: true
        append:
          requirements:
            image:
              description: |-
                This paragraph is added to the description of the `image` sub-requirement.
```

The structure inside `replace` and `append` follows the normal YAML structure of the building block,
but all components are optional. They are merged into the referenced building block as follows:

- `replace`: The given values replace the existing values entirely.
  Mappings are merged recursively, so you only need to specify the components you want to change.
  All other values (strings, lists, booleans) are replaced as a whole.
- `append`: The given values are added to the existing values.
  Strings are appended as a new paragraph, lists are extended, and mappings are merged recursively.
  Values that can't be appended (e.g. booleans) are replaced.

If both are given, `replace` is applied first, then `append`.

An examplary requirement file can be found in [_template.yaml](_template.yaml).
