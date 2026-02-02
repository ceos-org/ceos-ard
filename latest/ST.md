---
title: >-
  CEOS-ARD - Optical - Surface Temperature - Version 5.0-draft
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

# CEOS-ARD - Optical - Surface Temperature

&nbsp;

## Document Status

Product Family Specification, Optical, Surface Temperature

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

Not available yet

## <!-- edit:pfs/ST/authors.yaml -->Contributing Authors

- Adam Lewis, Geoscience Australia, Australia
- Jonathon Ross, Geoscience Australia, Australia
- Andreia Siqueira, Geoscience Australia, Australia
- Darcie Bontje, USGS, USA
- Steve Labahn, USGS, USA
- Mary Metzger, USGS, USA

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

<!-- edit:pfs/ST/document.yaml -->
**Product Family Specification:**
Optical, Surface Temperature (ST)

**Version:**
5.0-draft

**Applies to:**
Data collected by Optical sensors

## Background

Applies to data collected with multispectral sensors operating in the thermal infrared (TIR) wavelengths.
These typically operate with ground sample distance and resolution in the order of 10-100m;
however, the Specification is not inherently limited to this resolution.

At present, surface temperature measurements tend to be provided as either surface brightness temperature (SBT) or as land surface temperatures (LST) requiring the SBT to be modified according to the emissivity of the target.
This specification identifies the Surface Temperature (ST) as being the minimum or Threshold requirement for analysis ready land surface data. Nevertheless, both SBT and LST are land measurements, requiring atmospheric corrections.

&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/auxiliary-data.yaml -->
Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ceos-ard.yaml -->
CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/cep.yaml -->
CEP
:   Circular Error Probability, often provided with an additional percentage (e.g. CEP90 for 90% probability)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/dem.yaml -->
DEM
:   Digital Elevation Model

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/doi.yaml -->
DOI
:   Digital Object Identifier

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gis.yaml -->
GIS
:   Geographic Information System

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/lst.yaml -->
LST
:   Land Surface Temperature

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rmse.yaml -->
RMSE
:   Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rrmse.yaml -->
rRMSE
:   Radial Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/sbt.yaml -->
SBT
:   Surface Brightness Temperature

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/si.yaml -->
SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/st.yaml -->
ST
:   Surface Temperature

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/tir.yaml -->
TIR
:   Thermal Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/utc.yaml -->
UTC
:   Coordinated Universal Time

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/wgs84.yaml -->
WGS84
:   World Geodetic System 1984

&#12;

## <!-- edit:pfs/ST/document.yaml -->Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-st.yaml-->`1.1.` Traceability {#sec:meta.metadata-traceability-st label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard.
Information on traceability should be available in the metadata as a single DOI landing page.

- [Policy on measurement traceability](https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6536)
- [Guidance on measurement traceability](https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6532)

Notes:

1. SI Traceability requires an estimate of measurement uncertainty.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-optical.yaml-->`1.2.` Metadata Machine Readability {#sec:meta.metadata-machine-readability-optical label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta.metadata-machine-readability-optical`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.


##### Goal requirements:

As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-st.yaml-->`1.3.` Data Collection Time {#sec:meta.metadata-time-st label="|General Metadata: Data Collection Time"}

Identifier: `meta.metadata-time-st`



##### Threshold requirements:

The start and stop time of data collection is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified.


##### Goal requirements:

Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-area-st.yaml-->`1.4.` Geographical Area {#sec:meta.metadata-geo-area-st label="|General Metadata: Geographical Area"}

Identifier: `meta.metadata-geo-area-st`



##### Threshold requirements:

The surface location to which the data relate is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84 coordinates).


##### Goal requirements:

The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) expressed in projection coordinates with reference datum.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/crs-optical.yaml-->`1.5.` Coordinate Reference System {#sec:meta.metadata-crs-optical label="|General Metadata: Coordinate Reference System"}

Identifier: `meta.metadata-crs-optical`



##### Threshold requirements:

The metadata lists the coordinate reference system that has been used.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/map-projection-st.yaml-->`1.6.` Map Projection {#sec:meta.metadata-map-projection-st label="|General Metadata: Map Projection"}

Identifier: `meta.metadata-map-projection-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata lists the map projection that has been used, if any, and any relevant parameters required in relation to use of data in that map projection.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-methods-st.yaml-->`1.7.` Geometric Correction Methods {#sec:meta.metadata-geometric-correction-methods-st label="|General Metadata: Geometric Correction Methods"}

Identifier: `meta.metadata-geometric-correction-methods-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on geometric correction methods should be available in the metadata as a single DOI landing page containing information on geodetic correction methods used, including reference database and auxiliary data such as elevation model(s) and reference chip-sets.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-accuracy-st.yaml-->`1.8.` Geometric Accuracy of the Data {#sec:meta.metadata-geometric-accuracy-st label="|General Metadata: Geometric Accuracy of the Data"}

Identifier: `meta.metadata-geometric-accuracy-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data.
Accuracy is assessed by independent verification (as well as internal model-fit where applicable).
Uncertainties are expressed as root mean square error (RMSE) or Circular Error 90% Probability (CEP90).

Notes:

1. Information on geometric accuracy of the data should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/instrument-optical.yaml-->`1.9.` Instrument {#sec:meta.metadata-instrument-optical label="|General Metadata: Instrument"}

Identifier: `meta.metadata-instrument-optical`



##### Threshold requirements:

The instrument used to collect the data is identified in the metadata.


##### Goal requirements:

As threshold, but information should be available in the metadata as a single DOI landing page with references to the relevant CEOS Missions, Instruments, and Measurements Database record.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/spectral-bands.yaml-->`1.10.` Spectral Bands {#sec:meta.metadata-spectral-bands label="|General Metadata: Spectral Bands"}

Identifier: `meta.metadata-spectral-bands`



##### Threshold requirements:

The central wavelength for each band for which data is included is identified in the metadata, expressed in SI units.


##### Goal requirements:

As threshold, with instrument spectral response details (e.g., full spectral response function) also included or directly accessible using details in the metadata. 
Central wavelength and bandwidth at full-width half maximum value of the relative spectral response function are provided at least.

Notes:

1. Information on spectral bands should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sensor-calibration-optical.yaml-->`1.11.` Sensor Calibration {#sec:meta.metadata-sensor-calibration-optical label="|General Metadata: Sensor Calibration"}

Identifier: `meta.metadata-sensor-calibration-optical`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata.
Ideally this would support machine-to-machine access.

Notes:

1. Information on sensory calibration should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-accuracy-st.yaml-->`1.12.` Radiometric Accuracy {#sec:meta.metadata-radiometric-accuracy-st label="|General Metadata: Radiometric Accuracy"}

Identifier: `meta.metadata-radiometric-accuracy-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on radiometric accuracy should be available in the metadata as a single DOI landing page providing information on metrics describing the assessed absolute radiometric accuracy of the data, expressed as absolute radiometric uncertainty relative to a known reference standard.

Notes:

1. For example, this may come from comparison with routine and rigorously collected in situ measurements.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/algorithms.yaml-->`1.13.` Algorithms {#sec:meta.metadata-algorithms label="|General Metadata: Algorithms"}

Identifier: `meta.metadata-algorithms`



##### Threshold requirements:

All algorithms and versions, and the sequence in which they were applied in the generation process, are identified in the metadata.


##### Goal requirements:

As threshold, but only algorithms that have been published in a peer-reviewed journal.

Notes:

1. It is possible that high-quality corrections are applied through non-disclosed processes. CEOS-ARD does not per-se require full and open data and methods.
2. Information on algorithms should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/auxiliary-data-optical.yaml-->`1.14.` Auxiliary Data {#sec:meta.metadata-auxiliary-data-optical label="|General Metadata: Auxiliary Data"}

Identifier: `meta.metadata-auxiliary-data-optical`



##### Threshold requirements:

The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as a single DOI landing page.

Notes:

1. Auxiliary data includes DEMs, aerosols, etc. data sources.


##### Goal requirements:

As threshold, but information on auxiliary data should be available in the metadata as a single DOI landing page and is also available for free online download, contemporaneously with the product or through a link to the source.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-chain-prov-st.yaml-->`1.15.` Processing Chain Provenance {#sec:meta.metadata-processing-chain-prov-st label="|General Metadata: Processing Chain Provenance"}

Identifier: `meta.metadata-processing-chain-prov-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on processing chain provenance should be available in the metadata as a single DOI landing page containing description of the processing chain used to generate the product, including the versions of the software used and information on the data collection baseline, giving full transparency to the users.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access.yaml-->`1.16.` Data Access {#sec:meta.metadata-data-access label="|General Metadata: Data Access"}

Identifier: `meta.metadata-data-access`



##### Threshold requirements:

Information on data access should be available in the metadata as a single DOI landing page.

Notes:

1. Manual and offline interaction action (e.g., login) may be required.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-quality-st.yaml-->`1.17.` Overall Data Quality {#sec:meta.metadata-data-quality-st label="|General Metadata: Overall Data Quality"}

Identifier: `meta.metadata-data-quality-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata includes details of the quality of the product based on quantitative assessment of the product with respect to high quality reference data with full traceability of the uncertainties. Validation and intercomparison statistics can provide the necessary quantification.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`2.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-per-pixel-optical.yaml-->`2.1.` Metadata Machine Readability {#sec:pxl.metadata-machine-readability-per-pixel-optical label="|Per-Pixel Metadata: Metadata Machine Readability"}

Identifier: `pxl.metadata-machine-readability-per-pixel-optical`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/nodata.yaml-->`2.2.` No Data {#sec:pxl.per-pixel-nodata label="|Per-Pixel Metadata: No Data"}

Identifier: `pxl.per-pixel-nodata`



##### Threshold requirements:

Pixels that do not correspond to an observation (‘empty pixels’) are flagged.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/incomplete-testing.yaml-->`2.3.` Incomplete Testing {#sec:pxl.per-pixel-incomplete-testing label="|Per-Pixel Metadata: Incomplete Testing"}

Identifier: `pxl.per-pixel-incomplete-testing`



##### Threshold requirements:

The metadata identifies pixels for which the per-pixel tests (below) have not all been successfully completed.

Notes:

1. This may be the result of missing ancillary data for a subset of the pixels.


##### Goal requirements:

The metadata identifies which tests have, and have not, been successfully completed for each pixel.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/saturation.yaml-->`2.4.` Saturation {#sec:pxl.per-pixel-saturation label="|Per-Pixel Metadata: Saturation"}

Identifier: `pxl.per-pixel-saturation`



##### Threshold requirements:

Metadata indicates where one or more pixel in the input spectral bands are saturated.


##### Goal requirements:

Metadata indicates which pixels are saturated for each spectral band.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud.yaml-->`2.5.` Cloud {#sec:pxl.per-pixel-cloud label="|Per-Pixel Metadata: Cloud"}

Identifier: `pxl.per-pixel-cloud`



##### Threshold requirements:

Metadata indicates whether a pixel is assessed as being cloud.


##### Goal requirements:

As threshold, but information on cloud detection should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud-shadow.yaml-->`2.6.` Cloud Shadow {#sec:pxl.per-pixel-cloud-shadow label="|Per-Pixel Metadata: Cloud Shadow"}

Identifier: `pxl.per-pixel-cloud-shadow`



##### Threshold requirements:

Metadata indicates whether a pixel is assessed as being cloud shadow.


##### Goal requirements:

As threshold, but information on cloud shadow detection should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/snow-ice-sr.yaml-->`2.7.` Snow/Ice Mask {#sec:pxl.per-pixel-snow-ice-sr label="|Per-Pixel Metadata: Snow/Ice Mask"}

Identifier: `pxl.per-pixel-snow-ice-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata indicates whether a pixel is assessed as being snow/ice or not. Information on snow/ice mask should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/view-angles-solar.yaml-->`2.8.` Solar and Viewing Geometry {#sec:pxl.per-pixel-view-angles-solar label="|Per-Pixel Metadata: Solar and Viewing Geometry"}

Identifier: `pxl.per-pixel-view-angles-solar`



##### Threshold requirements:

Provide average solar and sensor viewing azimuth and zenith angles.


##### Goal requirements:

Provide per-pixel solar and sensor viewing azimuth and zenith angles.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometric-atmospheric-corrections.yaml-->`3.` Radiometric and Atmospheric Corrections {#sec:rac label="|Radiometric and Atmospheric Corrections"}

The following requirements must be met for all pixels in a collection.
The requirements indicate both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes. Radiometric corrections must lead to a valid measurement.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/measurement-st.yaml-->`3.1.` Measurement {#sec:rac.measurements-measurement-st label="|Radiometric and Atmospheric Corrections: Measurement"}

Identifier: `rac.measurements-measurement-st`



##### Threshold requirements:

Pixel values are expressed as a measurement of the Surface Temperature of the land, expressed as Kelvin


##### Goal requirements:

Surface temperature measurements are SI traceable (see also [@sec:meta.metadata-traceability-st]).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/atmosphere-emissivity.yaml-->`3.2.` Corrections for Atmosphere and Emissivity {#sec:rac.corrections-atmosphere-emissivity label="|Radiometric and Atmospheric Corrections: Corrections for Atmosphere and Emissivity"}

Identifier: `rac.corrections-atmosphere-emissivity`



##### Threshold requirements:

Retrieval methods for estimating surface temperature are provided.

Notes:

1. The metadata references (may be through a single DOI landing page) a citable peer-reviewed algorithm.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/uncertainty-st.yaml-->`3.3.` Measurement Uncertainty {#sec:rac.measurements-uncertainty-st label="|Radiometric and Atmospheric Corrections: Measurement Uncertainty"}

Identifier: `rac.measurements-uncertainty-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Uncertainty, in Kelvin, of the surface temperature measurement for each pixel is provided.

Notes:

1. Some of the intent of the initial wording (below), which refers to atmospheric windows, may have been lost: Uncertainty, in units Kelvin, of the surface temperature for each pixel is also accompanied by distance from cloud (above) and atmospheric transmission (intervals, i.e., 0.4 - 0.55, 0.55 - 0.7, etc.).

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`4.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-st.yaml-->`4.1.` Geometric Correction {#sec:gcor.corrections-geometric-st label="|Geometric Corrections: Geometric Correction"}

Identifier: `gcor.corrections-geometric-st`



##### Threshold requirements:

Sub-pixel accuracy is achieved in **relative** geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.

Sub-pixel accuracy is taken to be less than or equal to 0.5 pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.

A consistent gridding/sampling frame is necessary to meet this requirement.

Relevant metadata must be provided under [@sec:meta.metadata-geometric-accuracy-st] and [@sec:meta.metadata-instrument-optical].

Notes:

1. The threshold level will not necessarily enable interoperability between data from **different** sources as the geometric corrections for each of the sources may differ. 


##### Goal requirements:

Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).

A consistent gridding/sampling frame is necessary to meet this requirement.

Relevant metadata must be provided under [@sec:meta.metadata-geometric-accuracy-st] and [@sec:meta.metadata-instrument-optical].

Notes:

1. This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction, and with non-image spatial data such as GIS layers and terrain models.

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

&#12;

## Annexes


### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/st-metadata-examples.yaml-->CEOS-ARD Requirement Examples (Surface Temperature) {#sec:annex-st-metadata-examples label="|CEOS-ARD Requirement Examples (Surface Temperature)"}

### General Metadata

#### Traceability

Example of measurement traceability in metadata:

```xml
<band add_offset="0.000000" category="image" data_type="INT16" fill_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale_factor="0.100000">
    <short_name>LC08ST</short_name>
    <long_name>Surface Temperature</long_name>
    <file_name>ST</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="3730.000000" min="1500.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

Example of measurement uncertainty in metadata:

```xml
<band category="qa" data_type="INT16" fill_value="-9999" name="STQA" nlines="5000" nsamps="5000" product="st_qa" scale_factor="0.010000" source="toa_refl">
    <short_name>LC08STQA</short_name>
    <long_name>Surface temperature quality band</long_name>
    <file_name>STQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="32767.000000" min="0.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

#### Data Collection Time

Example of scene center time (UTC):

```xml
<scene_center_time>17:23:57.201686Z</scene_center_time>
```

The granule start and end times are contained in the XML metadata:

```xml
<metadataObject ID="acquisitionPeriod" classification="DESCRIPTION" category="DMD">
    <metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Acquisition Period">
    <xmlData>
        <sentinel-safe:acquisitionPeriod>
            <sentinel-safe:startTime>2018-10-07T05:04:50.425838Z</sentinel-safe:startTime>
            <sentinel-safe:stopTime>2018-10-07T05:07:50.425838Z</sentinel-safe:stopTime>
        </sentinel-safe:acquisitionPeriod>
    </xmlData>
    </metadataWrap>
</metadataObject>
```

Per pixel times are derived using information from the "time_in.nc" and “indices_in.nc” datafiles following a prescribed recipe.

#### Geographical Area

Example of the bounding coordinates in decimal degrees (WGS84):

```xml
<bounding_coordinates>
    <west>-99.9109607425</west>
    <east>-98.0134952569</east>
    <north>43.3609828699</north>
    <south>41.9778528562</south>
</bounding_coordinates>
```

Example of the corner points in the map projection system (Albers):

```xml
<corner_point location="UL" x="-315585.000000" y="2264805.000000"/>
<corner_point location="LR" x="-165585.000000" y="2114805.000000"/>
```

#### Map Projection

```xml
<projection_information datum="WGS84" projection="AEA" units="meters">
    <corner_point location="UL" x="-315585.000000" y="2264805.000000"/>
    <corner_point location="LR" x="-165585.000000" y="2114805.000000"/>
    <grid_origin>UL</grid_origin>
    <albers_proj_params>
        <standard_parallel1>29.500000</standard_parallel1>
        <standard_parallel2>45.500000</standard_parallel2>
        <central_meridian>-96.000000</central_meridian>
        <origin_latitude>23.000000</origin_latitude>
        <false_easting>0.000000</false_easting>
        <false_northing>0.000000</false_northing>
    </albers_proj_params>
</projection_information>
```

#### Geometric Correction Source

Example of elevation source:

```xml
<elevation_source>GLS2000</elevation_source>
```

The XML wrapper provides the source of the geometric calibration:

```xml
<sentinel-safe:resource name="S3A_SL_1_GEC_AX_20160216T000000_20991231T235959_20180202T120000___________________MPC_O_AL_007.SEN3" role="SLSTR Geometric Calibration Data File">
  <sentinel-safe:processing name="AdfProcessing">
    <sentinel-safe:facility name="ESA Mission Performance Coordinating Centre (MPC)" organisation="ESA Mission Performance Coordinating Centre" site="Sophia Antipolis" country="France">
      <sentinel-safe:hardware name="OPE"/>
        <sentinel-safe:software name="ADC" version="1.0"/>
      </sentinel-safe:facility>
  </sentinel-safe:processing>
</sentinel-safe:resource>
```

#### Geometric Accuracy of the Data

```xml
<geometric_rmse_model>9.021</geometric_rmse_model>
<geometric_rmse_model_x>6.864</geometric_rmse_model_x>
<geometric_rmse_model_y>5.854</geometric_rmse_model_y>
```

#### Instrument

```xml
<satellite>LANDSAT_8</satellite>
<instrument>OLI/TIRS_Combined</instrument>
```

The XML wrapper provides the instrument details:

```xml
<metadataObject ID="platform" classification="DESCRIPTION" category="DMD">
    <metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Platform Description">
      <xmlData>
          <sentinel-safe:platform>
            <sentinel-safe:nssdcIdentifier>2016-011A</sentinel-safe:nssdcIdentifier>
            <sentinel-safe:familyName>Sentinel-3</sentinel-safe:familyName>
            <sentinel-safe:number>A</sentinel-safe:number>
            <sentinel-safe:instrument>
                <sentinel-safe:familyName abbreviation="SLSTR">Sea and Land Surface Temperature Radiometer</sentinel-safe:familyName>
                <sentinel-safe:mode identifier="EO">Earth Observation</sentinel-safe:mode>
            </sentinel-safe:instrument>
          </sentinel-safe:platform>
      </xmlData>
    </metadataWrap>
</metadataObject>
```

#### Sensor Calibration

```xml
<cpf_name>LC08CPF_20180101_20180331_01.02</cpf_name>
```

#### Algorithms

Example for Surface Temperature algorithm version:

```xml
<app_version>st_1.3.0</app_version>
```

#### Auxiliary Data

All Auxiliary Datafiles (ADFs) are listed in the XML wrapper:

```xml
<sentinel-safe:resource name="S3__SL_2_LSTBAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST biome data file" version="06.16">
<sentinel-safe:resource name="S3__SL_2_LSTVAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST vegetation fraction data file" version="06.16">
<sentinel-safe:resource name="S3__SL_2_LSTWAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST water vapour data file" version="06.16">
```

#### Processing Chain Provenance

Processing chain provenance information is stored in the XML wrapper under the following tag:

```xml
<metadataObject ID="processing" classification="PROVENANCE" category="PDI">
```

#### Overall Data Quality

Overall data quality information is stored in the XML wrapper under the following tag:

```xml
<metadataObject ID="measurementQualityInformation" classification="DESCRIPTION" category="DMD">
```

### Per-Pixel Metadata

#### No Data

Example of the fill_value specified for each band in metadata:

```xml
<band add_offset="0.000000" category="image" data_type="INT16" fill_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale_factor="0.100000">
    <short_name>LC08ST</short_name>
    <long_name>Surface Temperature</long_name>
    <file_name>ST</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="3730.000000" min="1500.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
  confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
  confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing" ;
```

#### Incomplete Testing

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
  confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
  confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing”;
```

#### Saturation

Example of RADSATQA band showing the saturation information for the thermal bands used for Surface Temperature calculation:

```xml
<band category="qa" data_type="UINT16" fill_value="1" name="RADSATQA" nlines="5000" nsamps="5000" product="toa_refl" source="level1">
    <short_name>LC08RADSAT</short_name>
    <long_name>saturation mask</long_name>
    <file_name>RADSATQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>bitmap</data_units>
    <bitmap_description>
        <bit num="0">Data Fill Flag (0 = valid data, 1 = invalid data)</bit>
        <bit num="1">Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="2">Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="3">Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="4">Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="5">Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="6">Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="7">Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="8">N/A</bit>
        <bit num="9">Band 9 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="10">Band 10 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="11">Band 11 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
    </bitmap_description>
    <app_version>LaSRC_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
  confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
  confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing" ;
```

#### Cloud

Example of PIXELQA showing the bit value for cloud pixels (as well as cloud and cirrus confidence):

```xml
<band category="qa" data_type="UINT16" fill_value="1" name="PIXELQA" nlines="5000" nsamps="5000" product="level2_qa" source="level1">
    <short_name>LC08PQA</short_name>
    <long_name>level-2 pixel quality band</long_name>
    <file_name>PIXELQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>quality/feature classification</data_units>
    <bitmap_description>
        <bit num="0">fill</bit>
        <bit num="1">clear</bit>
        <bit num="2">water</bit>
        <bit num="3">cloud shadow</bit>
        <bit num="4">snow</bit>
        <bit num="5">cloud</bit>
        <bit num="6">cloud confidence</bit>
        <bit num="7">cloud confidence</bit>
        <bit num="8">cirrus confidence</bit>
        <bit num="9">cirrus confidence</bit>
        <bit num="10">terrain occlusion</bit>
        <bit num="11">unused</bit>
        <bit num="12">unused</bit>
        <bit num="13">unused</bit>
        <bit num="14">unused</bit>
        <bit num="15">unused</bit>
    </bitmap_description>
    <app_version>generate_pixel_qa_1.6.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains all the cloud masking flags. Three fields are relevant:

1. cloud_in
2. confidence_in
3. bayes_in

The "cloud_in" field contains all the individual threshold-based mask:

```xml
flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
cloud_in:flag_meanings = "visible 1.37_threshold 1.6_small_histogram 1.6_large_histogram 2.25_small_histogram 2.25_large_histogram 11_spatial_coherence gross_cloud thin_cirrus medium_high fog_low_stratus 11_12_view_difference 3.7_11_view_difference thermal_histogram spare spare"
```

The "confidence_in" field contains the "summary_cloud_mask" from the most appropriate cloud_in flags; the value of the bit is 16384US.
The "bayes_in" field contains the "single_moderate" probabilistic cloud flag; the value of the bit is 2UB.

#### Cloud Shadow

Please see the cloud shadow part in the example provided in requirement 2.5

#### Snow/Ice Mask

Please see the snow part in the example provided in requirement 2.5

### Radiometric and Atmospheric Corrections

No examples provided

### Geometric Corrections

No examples provided


