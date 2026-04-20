# Requirements

This is the folder that contains requirements for CEOS-ARD as building blocks.
The requirements are structured into folders and are described through YAML files.

## YAML file structure

The YAML files consist of the following components:

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
- `dependencies`: A mapping of named dependencies. See section [Dependencies](#dependencies).
- `glossary`: Any terms that are relevant for this requirement (e.g. are used in the text). Use any file name (without extension) from the [glossary](../glossary/) folder.
- `references`: Any relevant references for this requirement and are referred to in the text using the @ notation (see [Markdown](#markdown)). Use any file name (without extension) from the [references](../references/) folder.
- `changes`: The changelog that describes the changes over time for this building block.
- `history`: Refers to old identifiers of this requirement in case it has been renamed.

todo: Remove goal/threshold from requirements and make each part a separate requirement where the document.yaml in the PFS can then choose whether a requirement is goal or threshold.

## Markdown

The flavor of Markdown that is implemented here has some additional features.

See [References / Citation](#references-and-citation) and [Dependencies](#dependencies) for more details.

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

Dependencies are requirements that must be met for this requirement and are usually mentioned in the text using the @ notation.

Dependencies are defined as a mapping of alias to requirement path:

```yaml
dependencies:
  my-alias: metadata/time
```

The alias is a short name used to reference the dependency in text (e.g. `[@my-alias]`).
The requirement path is the folder name (if applicable) and the file name (without file extension). For example, `metadata/time` for the file [metadata/time.yaml](metadata/time.yaml).

Using named aliases allows a PFS to override individual dependency targets
via the `replace` mechanism without changing the requirement text.

Due to the fact that requirements don't include the category ID and could be ambiguous, the dependencies are resolved as follows:

1. The dependency will refer to the requirement with the given path in the same requirement category if it exists.
2. Otherwise, the dependency will refer to the requirement with the given path in any other category.

This means if a requirement is used both in the same requirement category and in another category, you can't refer to the requirement that is used in the other requirement category.

An example:

```yaml
# todo: remove once the example is no longer needed
id: example
title: Example Requirement
description: This is an example requirement.
requirements:
  threshold:
    description: |-
      This is a threshold requirement.
    metadata:
  goal:
    description: |-
      This is a goal requirement.
    notes:
      - This is a note.
    metadata:
    optional: true
dependencies:
  other-requirement: example/other-requirement
glossary:
  - doi
references:
  - iso19115_2_2009
changes:
history:
  - SAR 1.2
```
