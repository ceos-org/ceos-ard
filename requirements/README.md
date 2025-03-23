# Requirements

This is the folder that contains requirements for CEOS-ARD as building blocks.
The requirements are structured into folders and are described through YAML files.

## YAML file structure

The YAML files consist of the following components:

- `title` (required): A short title for the requirement
- `description`: An introduction for the requirement that sets the context.
  Due to historical reasons, most requirements don't provide such an introduction yet.
- `threshold` (required): The threshold requirement(s). Can be set to `null` to indicate that the there is no threshold requirement.
  - `description` (required): The requirements with Markdown formatting
  - `notes`: A list of additional notes. A note should be short and not be longer than one paragraph. Limited Markdown formatting is available.
- `goal` (required): The goal requirement(s). Can be set to `null` to indicate that the there are no additional goal requirements.
  - `description` (required): See `description` in `threshold` above for further details.
  - `notes`: See `notes` in `threshold` above for further details.
- `dependencies`: A list of requirement IDs. See section [Dependencies](#dependencies).
- `glossary`: Any terms that are relevant for this requirement (e.g. are used in the text). Use any file name (without extension) from the [glossary](../glossary/) folder.
- `glossary`: Any relevant references for this requirement and are referred to in the text using the @ notation (see [Markdown](#markdown)). Use any file name (without extension) from the [references](../references/) folder.
- `metadata`: Placeholder for future use.
- `legacy`: A temporary way to refer to the old requirement numbers in the combined SAR and/or Optical PFS. Set to `null` if not applicable.

todo: Remove goal/threshold from requirements and make each part a separate requirement where the requirements.yaml in the PFS can then choose whether a requirement is goal or threshold.

## Markdown

The flavor of Markdown that is implemented here has some additional features.
You can reference to other sections of the document or other requirements using the @ notation.
For example, `[@example/other-requirement]`.

todo: add more details

## Dependencies

Dependencies are requirements that must be met for this requirement and are usually mentioned in the text using the @ notation.

Dependencies are identified by the requirement ID but without the category ID.
The requirement ID is the folder name (if applicable) and the file name (without file extension). For example, `metadata/time` for the file [metadata/time.yaml](metadata/time.yaml).

Due to the fact that requirements don't include the category ID and could be ambiguous, the sependencies are resolved as follows:

1. The dependency will refer to the requirement with the given ID in the same requirement category if it exists.
2. Otherwise, the dependency will refer to the requirement with the given ID in any other category.

This means if a requirement is used both in the same requirement category and in another category, you can't refer to the requirement that is used in the other requirement category.

A full example:

```yaml
title: Example
description: This introduces the requirement or describes the context of this requirement.
threshold:
  description: |-
    This is a threshold requirement.
  notes:
goal:
  description: |-
    This is a goal requirement.
  notes:
    - This is a note.
dependencies:
glossary:
  - doi
references:
  - iso19115_2_2009
metadata:
legacy:
  sar:
  optical:
```
