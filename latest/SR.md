---
title: >-
  CEOS-ARD - Optical - Surface Reflectance - Version 5.1-draft
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

# CEOS-ARD - Optical - Surface Reflectance

&nbsp;

## Document Status

Product Family Specification, Optical, Surface Reflectance

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

Not available yet

## <!-- edit:pfs/SR/authors.yaml -->Contributing Authors

- Adam Lewis, Geoscience Australia, Australia
- Jonathon Ross, Geoscience Australia, Australia
- Andreia Siqueira, Geoscience Australia, Australia
- Darcie Bontje, USGS, USA
- Steve Labahn, USGS, USA
- Mary Metzger, USGS, USA
- Matt Steventon, LSI-VC Secretariat

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

<!-- edit:pfs/SR/document.yaml -->
**Product Family Specification:**
Optical, Surface Reflectance (SR)

**Version:**
5.1-draft

**Applies to:**
Data collected by Optical sensors

## Background

Data collected with multispectral optical sensors operating in the VIS/NIR/SWIR wavelengths at all ground sample distances and resolutions.

&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ceos-ard.yaml -->
CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/doi.yaml -->
DOI
:   Digital Object Identifier

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/nir.yaml -->
NIR
:   Near Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/si.yaml -->
SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/sr.yaml -->
SR
:   Surface Reflectance

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/swir.yaml -->
SWIR
:   Shortwave Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/vis.yaml -->
VIS
:   Visible

&#12;

## <!-- edit:pfs/SR/requirements.yaml -->Requirements

**WARNING:** The requirement numbers below are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided in brackets directly after the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability.yaml-->`1.1.` Traceability {#sec:meta.metadata-traceability label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard.

Notes:

1. Relationship to [@sec:rac.measurements-uncertainty]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/source-metadata.yaml-->`2.` Source Metadata {#sec:src label="|Source Metadata"}

These are metadata records describing (detailing) **each** acquisition (source data) used to generate the ARD product.
This may be one or mutliple acquisitions.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/example.yaml-->`2.1.` Example Requirement {#sec:src.example label="|Source Metadata: Example Requirement"}

Identifier: `src.example`



This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/product-metadata.yaml-->`3.` Product Metadata {#sec:prd label="|Product Metadata"}

Information related to the CEOS-ARD product generation procedure and geographic parameters.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/example.yaml-->`3.1.` Example Requirement {#sec:prd.example label="|Product Metadata: Example Requirement"}

Identifier: `prd.example`



This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`4.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.

*Cloud optimized file formats are recommended.*


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/example.yaml-->`4.1.` Example Requirement {#sec:pxl.example label="|Per-Pixel Metadata: Example Requirement"}

Identifier: `pxl.example`



This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometric-atmospheric-corrections.yaml-->`5.` Radiometric and Atmospheric Corrections {#sec:rac label="|Radiometric and Atmospheric Corrections"}

The following requirements must be met for all pixels in a collection.
The requirements indicate both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes. Radiometric corrections must lead to a valid measurement of surface reflectance.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/uncertainty.yaml-->`5.1.` Measurement Uncertainty {#sec:rac.measurements-uncertainty label="|Radiometric and Atmospheric Corrections: Measurement Uncertainty"}

Identifier: `rac.measurements-uncertainty`



Note: In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.

##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

An estimate of the certainty of the values is provided in measurement units.

Notes:

1. This is a requirement for SI traceability. See also [@sec:meta.metadata-traceability].
2. Information on measurement uncertainty should be available in the metadata as a single DOI landing page.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`6.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/example.yaml-->`6.1.` Example Requirement {#sec:gcor.example label="|Geometric Corrections: Example Requirement"}

Identifier: `gcor.example`



This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

&#12;


## Introduction

This section aims to provide background and specific information on the processing steps that can be
used to achieve analysis ready data for a specific and well-developed Product Family Specification.
This Guidance material does not replace or override the specifications.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/introduction/what-are-ceos-ard-products.yaml-->What is CEOS Analysis Ready Data? {#sec:intro-what-are-ceos-ard-products label="|What is CEOS Analysis Ready Data?"}

CEOS-ARD are products that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort.
In general, these products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets.

CEOS-ARD products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development.
They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures.
They may not be suitable for all purposes and are not intended as a _replacement_ for other types of satellite products.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/introduction/when-is-a-product-ceos-ard.yaml-->When can a product be called CEOS-ARD? {#sec:intro-when-is-a-product-ceos-ard label="|When can a product be called CEOS-ARD?"}

The CEOS-ARD branding is applied to a particular product once:

- that product has been assessed as meeting CEOS-ARD requirements by the agency responsible for production and distribution of the product, and
- that the assessment has been peer reviewed by the relevant CEOS team(s).

Agencies or other entities considering undertaking an assessment process should consult the [CEOS-ARD Governance Framework](https://ceos.org/ard/files/CEOS_ARD_Governance_Framework_18-October-2021.pdf).

A product can continue to use CEOS-ARD branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/introduction/difference-threshold-goal.yaml-->What is the difference between Threshold and Goal? {#sec:intro-difference-threshold-goal label="|What is the difference between Threshold and Goal?"}

**Threshold** (Minimum) requirements are the **minimum** that is needed for the data to be analysis ready.
This must be practical and accepted by the data producers.

**Goal** (Desired) requirements (previously referred to as “Target”) are the ideal; where we would like to be.
Some providers may already meet these.

Products that meet all _threshold_ requirements should be immediately useful for scientific analysis or decision-making.

Products that meet _goal_ requirements will reduce the overall product uncertainties and enhance broad-scale applications.
For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the _threshold_ level.

Goal requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field.
Over time, _goal_ specifications may (and subject to due process) become accepted as _threshold_ requirements.

&#12;

## References

::: {#refs}
:::

