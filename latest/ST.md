---
title: >-
  CEOS-ARD - Optical - Surface Temperature - Version 6.0.0-draft
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
secPrefixTemplate: $$i$$
# we want to include all citations regardless of usage, see https://pandoc.org/MANUAL.html#including-uncited-items-in-the-bibliography
nocite: |
  @*
---

![](assets/CEOS_logo_colour_black_text_right.png)

# CEOS-ARD - Optical - Surface Temperature

&nbsp;

## Draft Version

This is a draft version.
Please visit the [CEOS-ARD website](https://ceos.org/ard) for the latest endorsed version of this document.

## Document Status

Product Family Specification, Optical, Surface Temperature

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

### 2026-08-14 (MAJOR)

**This is a breaking change!**

- Created separate requirements for 'Corrections for Atmosphere' and 'Adjustments for Emissivity and Anisotropy'. Per-pixel emissivity information is now required at Threshold. 
- Introduced a Threshold requirement for 'Measurement Uncertainty'.
- Renamed 'Measurement' to 'Measurand'
- Removed threshold requirement for 'Algorithms'.
- Introduced Per-pixel Goal requirement for 'Terrain Occlusion'.
- Replaced 'Snow/Ice' mask with 'Surface', covering Land/Water at Threshold and Snow/Ice at Goal.
- Updated 'Cloud' and 'Cloud Shadow' requirements to align more closely with the AR PFS v2.0 and the suitability of cloud shadow for non-reflectance methods.
- Updated 'No Data' requirement to address https://github.com/ceos-org/ceos-ard/issues/4.
- Updated 'Incomplete Testing' requirement to aid machine readability / automated assessment.
- Removed redundant 'Metadata Machine Readability' requirement from Per-pixel Metadata.
- Replaced General Metadata Percentage of Valid Observations requirement with Valid Pixels
- Introduced a new Processing Chain Provenance requirement, where Threshold = Reconstructibility, Goal = Reproducibility. 
- Removed 'Radiometric Accuracy' requirement.
- Adopted AR PFS v2.0 requirements for 'Auxiliary Data', 'Measurand Uncertainty', 'Encoding', 'Sensor Calibration', 'Spectral Bands', 'Instrument', 'Geometric Uncertainty of the Data', 'Geometric Correction Methods', 'Map Projection', and 'Data Collection Time'.
- Aligned with other optical PFS where the ST PFS had minor editorial differences.

**Justification:**
Update to address evolving landscape of thermal missions, including capabilities of the commercial sector and user needs. Closer alignment with more recently updated PFS. Changes also reflect recent CEOS-ARD Oversight Group discussions, swapping strict threshold requirements for algorithms in favour of uncertainty information.

**Editor:** Harvey Jones

### 2026-03-26 (PATCH)

- Renamed CARD4L to CEOS-ARD
- Restructured the document; removed empty or unused parts
- Split "Applies to" section into "Applies to" and "Background" sections
- Document history has been reset. Check the previous versions for details
- Numerical identifiers were rotated and are deprecated; new textual identifiers have been added
- The requirement "Radiometric corrections must lead to a valid measurement [...]" has been moved from the category description to the measurement requirement.
- If no threshold requirement applies, the wording has been made consistent (e.g. former req. 1.7 and 1.8).
- Former req. 1.9: Removed "on instrument" from "As threshold, but information on instrument should be available".
- Former req. 2.3: Replaced the wording "e.g., due to missing ancillary data for some pixels." with "This may be the result of missing ancillary data for a subset of the pixels."
- Annex has been reformatted and updated

**Justification:**
Migration to building blocks.

**Editor:** Matthias Mohr


## Contributing Authors

- Mathias Gergely (Aistech Space)
- Harvey Jones (CEOS-ARD Secretariat)
- Emilie Delogu (CNES)
- Andreas Brunn (Constellr)
- Andreas Dietz (DLR)
- Philipp Reiners (DLR)
- Fraser Parlane (EarthDaily)
- Peter Strobl (EC)
- Silvia Scifoni (ESA/Serco)
- Adam Lewis (Geoscience Australia)
- Jonathon Ross (Geoscience Australia)
- Andreia Siqueira (Geoscience Australia)
- Siri Jodha Khalsa (IEEE)
- Jean-Francois Piolle (IFREMER)
- Misako Kachi (JAXA)
- Matthias Mohr (MoreGeo)
- Edward M. Armstrong (NASA/JPL/CalTech)
- Mark de Jong (NRCan)
- Anastasia Sarelli (OroraTech)
- Josephine Wong (OroraTech)
- Daniel Evans (SatVu)
- Jamie McMillan (SatVu)
- Darren Ghent (University of Leicester)
- Chase Mueller (USGS)
- Chris Barnes (USGS)
- Darcie Bontje (USGS)
- Mary Metzger (USGS)
- Steve Labahn (USGS)

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

**Product Family Specification:**
Optical, Surface Temperature (ST)

**Version:**
6.0.0-draft

**Applies to:**
Data collected with satellite sensors operating in the thermal infrared (TIR and MWIR) and microwave wavelengths. These typically operate with ground sample distance and resolution in the order 1 dm - 50 km however the specification is not inherently limited to these resolutions.


## Background

Remotely sensed surface temperature measurements tend to be provided as surface brightness temperature (SBT), land surface temperature (LST), water surface temperature (WST), or ice surface temperature (IST), where LST, WST, and IST are derived from SBT accounting for the emissivity of the target. This specification identifies Surface Temperature (ST), including but not limited to LST, WST, and IST, as the minimum or threshold requirement for analysis ready surface data.

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

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/doi.yaml -->
DOI
:   Digital Object Identifier

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gis.yaml -->
GIS
:   Geographic Information System

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/lst.yaml -->
LST
:   Land Surface Temperature

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

## Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/ceos-ard-pfs-version.yaml-->`1.1.` CEOS-ARD PFS Compliance Version {#sec:meta-ardver label="|General Metadata: CEOS-ARD PFS Compliance Version"}

Identifier: `meta-ardver`



##### Threshold requirements:

Version of the CEOS-ARD PFS with which the product is complying is identified.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-st.yaml-->`1.2.` Metrological Traceability of the Measurand to SI {#sec:meta-trace-st label="|General Metadata: Metrological Traceability of the Measurand to SI"}

Identifier: `meta-trace-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard, documented by URL or DOI.

Note:

1. SI Traceability requires an estimate of measurement uncertainty (see [@sec:rac-muncer-st]).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-st.yaml-->`1.3.` Metadata Machine Readability {#sec:meta-memare-st label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta-memare-st`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable for further use.


##### Goal requirements:

As threshold, but metadata is provided in a community endorsed standard that facilitates machine-readability, such as CEOS-ARD Metadata Specifications, ISO 19115-2, STAC, the Climate and Forecast (CF) convention, or the Attribute Convention for Data Discovery (ACDD).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-st.yaml-->`1.4.` Data Collection Time {#sec:meta-time-st label="|General Metadata: Data Collection Time"}

Identifier: `meta-time-st`



##### Threshold requirements:

The beginning and end of the data collection time is expressed in date/time and identified in the metadata consistent with ISO 8601. The time is expressed with the time offset from UTC unambiguously identified.

In the case of composite or mosaic products, the dates/times of the first and last data takes are provided with the product.


##### Goal requirements:

As threshold, but information required to determine, within a stated uncertainty, when the individual observations were taken is available.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-area-optical.yaml-->`1.5.` Geographical Area {#sec:meta-geoarea-optical label="|General Metadata: Geographical Area"}

Identifier: `meta-geoarea-optical`



##### Threshold requirements:

The surface location to which the data relates is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84).


##### Goal requirements:

The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) with the projection system (if any) and reference datum provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/crs-ar.yaml-->`1.6.` Coordinate Reference System {#sec:meta-crs-ar label="|General Metadata: Coordinate Reference System"}

Identifier: `meta-crs-ar`



##### Threshold requirements:

The coordinate reference system that has been used is detailed.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/map-projection-ar.yaml-->`1.7.` Map Projection {#sec:meta-mapproj-ar label="|General Metadata: Map Projection"}

Identifier: `meta-mapproj-ar`



##### Threshold requirements:

The map projection that has been used and any relevant parameters required in relation to use of data in that map projection is detailed.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-methods-st.yaml-->`1.8.` Geometric Correction Methods {#sec:meta-geocorm-st label="|General Metadata: Geometric Correction Methods"}

Identifier: `meta-geocorm-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on geometric correction source and methods are provided, including reference database and auxiliary data such as elevation model(s) and reference chip-sets, documented by URL or DOI.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-uncertainty-st.yaml-->`1.9.` Geometric Uncertainty of the Data {#sec:meta-geounc-st label="|General Metadata: Geometric Uncertainty of the Data"}

Identifier: `meta-geounc-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Inclusion of metrics describing the assessed geodetic uncertainty of the data, expressed in units of the coordinate system of the data. Uncertainty is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed quantitatively and documented by URL or DOI.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/instrument-st.yaml-->`1.10.` Instrument {#sec:meta-instru-st label="|General Metadata: Instrument"}

Identifier: `meta-instru-st`



##### Threshold requirements:

The instrument used to collect the data is identified.

- Satellite name
- Instrument name


##### Goal requirements:

As threshold, with references to the relevant "CEOS Missions, Instruments and Measurements" (MIM) database record ([database.eohandbook.com](https://database.eohandbook.com)).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/spectral-bands-st.yaml-->`1.11.` Spectral Bands {#sec:meta-specband-st label="|General Metadata: Spectral Bands"}

Identifier: `meta-specband-st`



##### Threshold requirements:

Spectral response function and method of assessment is provided.


##### Goal requirements:

As threshold, but information on spectral bands is documented by URL or DOI.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sensor-calibration-st.yaml-->`1.12.` Sensor Calibration {#sec:meta-sencal-st label="|General Metadata: Sensor Calibration"}

Identifier: `meta-sencal-st`



##### Threshold requirements:

Binary description of calibrated/not calibrated only.


##### Goal requirements:

Sensor calibration parameters are identified or can be accessed using details included in the metadata, documented by URL or DOI. 

Ideally this would support machine-to-machine access.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/measurand-uncertainty.yaml-->`1.13.` Measurand Uncertainty {#sec:meta-measurunc label="|General Metadata: Measurand Uncertainty"}

Identifier: `meta-measurunc`



##### Threshold requirements:

Methods of determining the assessed measurand uncertainty of the version of the data are specified, documented by URL or DOI.


##### Goal requirements:

As threshold, but the absolute measurand uncertainty of the data is provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/measurand-encoding.yaml-->`1.14.` Measurand Encoding {#sec:meta-measurenc label="|General Metadata: Measurand Encoding"}

Identifier: `meta-measurenc`



##### Threshold requirements:

Range and bit depth are provided.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/algorithms-st.yaml-->`1.15.` Algorithms {#sec:meta-malgos-st label="|General Metadata: Algorithms"}

Identifier: `meta-malgos-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

All algorithms and the sequence in which they were applied in the generation process are identified and documented by URL or DOI.

Algorithms must be published and validated, and a description of the validation process is included.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/auxiliary-data-st.yaml-->`1.16.` Auxiliary Data {#sec:meta-auxdat-st label="|General Metadata: Auxiliary Data"}

Identifier: `meta-auxdat-st`



##### Threshold requirements:

Lists the sources of auxiliary data used in the generation process, documented by URL or DOI.

Note:

1. Auxiliary data includes DEMs, aerosols, water vapor, Climate Modeling Grids, and any other data sources used in product generation.


##### Goal requirements:

As threshold, but information on auxiliary data should be available for free online download, contemporaneously with the product or through a link to the source.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-chain-prov-st.yaml-->`1.17.` Processing Chain Provenance {#sec:meta-proprov-st label="|General Metadata: Processing Chain Provenance"}

Identifier: `meta-proprov-st`



##### Threshold requirements:

The provider attaches to each delivered dataset (delivery unit) information which allows the provider to reconstruct the exact processing environment (software versions, calibration files, parameter settings) in which this particular output was produced.


##### Goal requirements:

As threshold, but the provider is required to reproduce the exact same output.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access-st.yaml-->`1.18.` Data Access {#sec:meta-daccess-st label="|General Metadata: Data Access"}

Identifier: `meta-daccess-st`



##### Threshold requirements:

The location from where the data can be retrieved is identified, expressed as a URL or DOI.

Note:

1. Manual and offline interaction action (e.g., login) may be required.


##### Goal requirements:

An online location is identified from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/valid-pixels.yaml-->`1.19.` Valid Pixels {#sec:meta-valpix label="|General Metadata: Valid Pixels"}

Identifier: `meta-valpix`



##### Threshold requirements:

Percentage of valid pixels in a specified area based on the applied flags from [@sec:pxl].


##### Goal requirements:


As threshold.
<!-- *None* -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`2.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata is provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to **discriminate between** (choose) observations on the basis of their individual suitability for application.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/nodata-st.yaml-->`2.1.` No Data {#sec:pxl-pinodat-st label="|Per-Pixel Metadata: No Data"}

Identifier: `pxl-pinodat-st`



##### Threshold requirements:

Pixels that do not correspond to an observation (No Data / Invalid / Falsified / Valid / Modelled) are flagged.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/incomplete-testing-st.yaml-->`2.2.` Incomplete Testing {#sec:pxl-pincot-st label="|Per-Pixel Metadata: Incomplete Testing"}

Identifier: `pxl-pincot-st`



##### Threshold requirements:

Identifies pixels for which the per-pixel tests ([@sec:pxl-pisatur-ar], [@sec:pxl-picloud-st], [@sec:pxl-picloudsh-st], [@sec:pxl-surf-st], [@sec:pxl-terrain-st]) have not all been successfully completed.

Note:

1. This may be the result of missing ancillary data for a subset of the pixels.


##### Goal requirements:

Identifies which tests ([@sec:pxl-pisatur-ar], [@sec:pxl-picloud-st], [@sec:pxl-picloudsh-st], [@sec:pxl-surf-st], [@sec:pxl-terrain-st]) have and have not been successfully completed for each pixel.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/saturation-ar.yaml-->`2.3.` Saturation {#sec:pxl-pisatur-ar label="|Per-Pixel Metadata: Saturation"}

Identifier: `pxl-pisatur-ar`



##### Threshold requirements:

Specification of whether there is pixel radiometric saturation at Level 1 in one or more spectral bands.


##### Goal requirements:

As threshold, with specification of which pixels are radiometrically saturated for each spectral band.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud-st.yaml-->`2.4.` Cloud {#sec:pxl-picloud-st label="|Per-Pixel Metadata: Cloud"}

Identifier: `pxl-picloud-st`



##### Threshold requirements:

Specification of whether a pixel is cloud-affected.


##### Goal requirements:

As threshold, but information on cloud type or confidence is included, documented by URL or DOI.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud-shadow-st.yaml-->`2.5.` Cloud Shadow {#sec:pxl-picloudsh-st label="|Per-Pixel Metadata: Cloud Shadow"}

Identifier: `pxl-picloudsh-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Specification of whether a pixel is cloud shadow-affected. Information on cloud shadow detection is documented by URL or DOI.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/surface-st.yaml-->`2.6.` Surface {#sec:pxl-surf-st label="|Per-Pixel Metadata: Surface"}

Identifier: `pxl-surf-st`



##### Threshold requirements:

Specification of whether a pixel is assessed as being land or water, including the information source and other relevant surface characteristic information.

Note:

1. External data sources are listed in [@sec:meta-auxdat-st].


##### Goal requirements:

As threshold, but pixels are identified as being snow or ice.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/view-angles-solar-ar.yaml-->`2.7.` Solar and Viewing Geometry {#sec:pxl-vigeso-ar label="|Per-Pixel Metadata: Solar and Viewing Geometry"}

Identifier: `pxl-vigeso-ar`



##### Threshold requirements:

Specification of the solar and sensor viewing azimuth and zenith angles.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/terrain-occlusion-st.yaml-->`2.8.` Terrain Occlusion {#sec:pxl-terrain-st label="|Per-Pixel Metadata: Terrain Occlusion"}

Identifier: `pxl-terrain-st`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Specification of whether pixels are not visible to the sensor due to terrain occlusion during off-nadir viewing.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometric-atmospheric-corrections.yaml-->`3.` Radiometric and Atmospheric Corrections {#sec:rac label="|Radiometric and Atmospheric Corrections"}

The following requirements must be met for all pixels in a collection.
The requirements indicate both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/measurand-st.yaml-->`3.1.` Measurand {#sec:rac-measur-st label="|Radiometric and Atmospheric Corrections: Measurand"}

Identifier: `rac-measur-st`



##### Threshold requirements:

Pixel values are a measurement of the Surface Temperature expressed in kelvin.

Note:

1. See [@sec:meta-specband-st]


##### Goal requirements:

Surface temperature measurements are SI traceable (see also [@sec:meta-trace-st]).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/atmosphere.yaml-->`3.2.` Corrections for Atmosphere {#sec:rac-catmos label="|Radiometric and Atmospheric Corrections: Corrections for Atmosphere"}

Identifier: `rac-catmos`



##### Threshold requirements:

Retrieval methods for estimating surface temperature are provided.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/emissivity-st.yaml-->`3.3.` Adjustments for Emissivity and Anisotropy {#sec:rac-emiani label="|Radiometric and Atmospheric Corrections: Adjustments for Emissivity and Anisotropy"}

Identifier: `rac-emiani`



##### Threshold requirements:

Retrieval methods for estimating surface emissivity per channel are provided.


##### Goal requirements:

As threshold, but the retrieval method for estimating the total directional emissivity is provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/uncertainty-st.yaml-->`3.4.` Measurand Uncertainty {#sec:rac-muncer-st label="|Radiometric and Atmospheric Corrections: Measurand Uncertainty"}

Identifier: `rac-muncer-st`



##### Threshold requirements:

A self-assessed declaration of per-pixel measurement uncertainty, following Section 3.2.4 (Uncertainty Characterization) of the Joint Earth Observation Mission Quality Assessment Framework - Optical Guidelines is provided, meeting the Basic or Good criteria.


##### Goal requirements:

A self-assessed declaration of per-pixel measurement uncertainty, following Section 3.2.4 (Uncertainty Characterization) of the Joint Earth Observation Mission Quality Assessment Framework - Optical Guidelines is provided, meeting the Excellent or Ideal criteria.

Note:

1. https://science.nasa.gov/wp-content/uploads/2026/05/joint-optical-guidelines-jul2025-signed.pdf

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`4.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

Geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-st.yaml-->`4.1.` Geometric Correction {#sec:gcor-geocorr-st label="|Geometric Corrections: Geometric Correction"}

Identifier: `gcor-geocorr-st`



##### Threshold requirements:

Sub-pixel uncertainty is achieved in relative geolocation, that is, the pixels from the same instrument and platform are consistently located, and in thus comparable, through time.

Sub-pixel uncertainty is taken to be less than or equal to 0.5 pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.

A consistent gridding/sampling frame is used, including common cell size, origin, and nominal sample point location within the cell (centre, ll, ur).

Relevant metadata must be provided under [@sec:meta-geounc-st] and [@sec:meta-instru-st].

Notes:

1. The threshold level will not necessarily enable interoperability between data from different sources as the geometric corrections for each of the sources may differ.
2. It is useful to note if the sensor is used at its native resolution before geometric correction or that some resampling must be done.


##### Goal requirements:

Sub-pixel uncertainty is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).

Relevant metadata must be provided under [@sec:meta-geounc-st] and [@sec:meta-instru-st].

Note:

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

