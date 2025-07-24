---
title: >-
  CEOS-ARD - ~{ type }~ - ~{ title }~ - Version ~{ version }~
lang: en
format:
  - markdown # markdown_mmd doesn't support citations, so we use pandoc's markdown and add extentions
  - definition_lists # for the glossaty
  - yaml_metadata_block # for the header that lists title and langugage in markdown
  - blank_before_header # allow headers without a preceding blank link, often an issue with jinja
  - lists_without_preceding_blankline # allow lists without a preceding blank line, often done wrong by authors
  - autolink_bare_uris # link URIs automatically
  - backtick_code_blocks # backtick code blocks as in GitHub for example
  - pipe_tables # tables
  - table_captions # table captions
  - strikeout # strikeout text with ~...~
link-citations: true
linkReferences: true
tblPrefix:
  - Table
  - Tables
eqnPrefix: Eq.
figPrefix:
  - Figure
  - Figures
lstPrefix:
  - Listing
  - Listings
secPrefix:
  - Section
  - Sections
secPrefixTemplate: $$p$$&nbsp;"$$i$$"
# we want to include all citations regardless of usage, see https://pandoc.org/chunkedhtml-demo/9.6-including-uncited-items-in-the-bibliography.html
nocite: |
  @*
---

![](assets/CEOS_logo_colour_black_text_right.png)

# CEOS-ARD - ~{ type }~ - ~{ title }~

&nbsp;

## Document Status

Product Family Specification, ~{ type }~, ~{ title }~

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

~{ history }~

## <!-- edit:pfs/~{ id }~/authors.yaml -->Contributing Authors

~( for org in authors )~
~(   for member in org.members )~
- ~{ member }~, ~{ org.name }~~( if org.country )~, ~{ org.country }~~( endif )~

~(   endfor )~
~( endfor )~

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

<!-- edit:pfs/~{ id }~/document.yaml -->
**Product Family Specification:**
~{type}~, ~{ title }~ (~{ id }~)

**Version:**
~{ version }~

**Applies to:**
Data collected by ~{type}~ sensors

## Background

~( if combined )~
~(   for key, value in applies_to.items() )~
### ~{ key }~

~{     value }~

~(   endfor )~
~( else )~
~{   applies_to }~
~( endif )~

&#12;

## Definitions and Abbreviations

~( for term in glossary )~
<!-- edit:~{ term.filepath }~ -->
~{ term.term }~
:   ~{ term.description | rstrip }~

~( endfor )~
&#12;

## <!-- edit:pfs/~{ id }~/requirements.yaml -->Requirements

**WARNING:** The requirement numbers below are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided in brackets directly after the title.

<!-- todo: remove requirement numbers -->

~( for block in requirements )~
~( set i = loop.index )~
### <!-- edit:~{ block.category.filepath }~-->`~{ i }~.` ~{ block.category.title }~ {#sec:~{ block.category.id }~ label="|~{ block.category.title }~"}

~{ block.category.description | rstrip }~

~(   for requirement in block.requirements )~
~(     if loop.index != 1 )~
---
~(     endif )~

#### <!-- edit:~{ requirement.filepath }~-->`~{ i }~.~{ loop.index }~.` ~{ requirement.title }~ {#sec:~{ requirement.uid }~ label="|~{ block.category.title }~: ~{ requirement.title }~"}

Identifier: `~{ requirement.uid }~`

~(     if combined )~
Applies to: ~{ ", ".join(requirement.applies_to) }~
~(     endif )~

~(     if requirement.description | rstrip )~

~{ requirement.description | rstrip }~
~(     endif )~
~(     for type in ['threshold', 'goal'] )~

##### ~{ type|title }~ requirements:

~(       if requirement[type] )~
~{ requirement[type].description | rstrip }~

~(         if requirement[type].notes )~
Notes:

~(           for note in requirement[type].notes )~
~{ loop.index }~. ~{ note }~
~(           endfor )~

~(         endif )~
~(       else )~

~{ "As threshold." if type == "goal" else "Not required." }~
<!-- *None* -->

~(       endif )~
~(     endfor )~
~(     if editable )~
##### Assessment:

- Threshold Self-Assessment:
- Goal Self-Assessment:
- Self-Assessment Explanation/ Justification:
- Recommended Requirement Modification:

~(     endif )~
~(   endfor )~
~( endfor )~
&#12;

~( if editable )~
## Summary Self-Assessment Table

~( for block in requirements )~
### ~{ block.category.title }~

| Requirement ID | Requirement Title | Threshold | Goal |
| -------------- | ----------------- | :-------: | :--: |
~(   for requirement in block.requirements )~
| `~{ requirement.uid }~` | ~{ requirement.title }~ | ~( if not requirement.threshold )~_not required_~( endif )~ | ~( if not requirement.goal )~_as threshold_~( endif )~ |
~(   endfor )~

~( endfor )~
&#12;
~( endif )~

## Introduction

This section aims to provide background and specific information on the processing steps that can be
used to achieve analysis ready data for a specific and well-developed Product Family Specification.
This Guidance material does not replace or override the specifications.

~( for section in introduction )~
### <!-- edit:~{ section.filepath }~-->~{ section.title }~ {#sec:intro-~{ section.id | slugify }~ label="|~{ section.title }~"}

~{ section.description | rstrip }~

~( endfor )~
&#12;

## References

::: {#refs}
:::

~( if annexes )~
&#12;

## Annexes

~(   for annex in annexes )~

### <!-- edit:~{ annex.filepath }~-->~{ annex.title }~ {#sec:annex-~{ annex.id | slugify }~ label="|~{ annex.title }~"}

~{ annex.description | rstrip }~

~(   endfor )~

~( endif )~
