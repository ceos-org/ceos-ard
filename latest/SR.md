---
title: >-
  CEOS-ARD - Optical - Surface Reflectance - Version 5.0.1-draft
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
5.0.1-draft

**Applies to:**
Data collected by Optical sensors

## Background

Data collected with multispectral optical sensors operating in the VIS/NIR/SWIR wavelengths at all ground sample distances and resolutions.

&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/atbd.yaml -->
ATBD
:   Algorithm Theoretical Basis Document

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/auxiliary-data.yaml -->
Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/brdf.yaml -->
BRDF
:   Bi-Directional Reflectance Function

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

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/nir.yaml -->
NIR
:   Near Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rmse.yaml -->
RMSE
:   Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rrmse.yaml -->
rRMSE
:   Radial Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/si.yaml -->
SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/sr.yaml -->
SR
:   Surface Reflectance

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/swir.yaml -->
SWIR
:   Shortwave Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/utc.yaml -->
UTC
:   Coordinated Universal Time

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/vis.yaml -->
VIS
:   Visible

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/wgs84.yaml -->
WGS84
:   World Geodetic System 1984

&#12;

## <!-- edit:pfs/SR/requirements.yaml -->Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-sr.yaml-->`1.1.` Traceability {#sec:meta.metadata-traceability-sr label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard.

Notes:

1. Relationship to [@sec:rac.measurements-uncertainty-sr]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-optical.yaml-->`1.2.` Metadata Machine Readability {#sec:meta.metadata-machine-readability-optical label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta.metadata-machine-readability-optical`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.


##### Goal requirements:

As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-sr.yaml-->`1.3.` Data Collection Time {#sec:meta.metadata-time-sr label="|General Metadata: Data Collection Time"}

Identifier: `meta.metadata-time-sr`



##### Threshold requirements:

The data collection time is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified.


##### Goal requirements:

Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-area-sr.yaml-->`1.4.` Geographical Area {#sec:meta.metadata-geo-area-sr label="|General Metadata: Geographical Area"}

Identifier: `meta.metadata-geo-area-sr`



##### Threshold requirements:

The surface location to which the data relate is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84).


##### Goal requirements:

The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) with the projection system (if any) and reference datum provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/crs-optical.yaml-->`1.5.` Coordinate Reference System {#sec:meta.metadata-crs-optical label="|General Metadata: Coordinate Reference System"}

Identifier: `meta.metadata-crs-optical`



##### Threshold requirements:

The metadata lists the coordinate reference system that has been used.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/map-projection-sr.yaml-->`1.6.` Map Projection {#sec:meta.metadata-map-projection-sr label="|General Metadata: Map Projection"}

Identifier: `meta.metadata-map-projection-sr`



##### Threshold requirements:

The metadata lists the map projection that has been used (or geographical coordinates, if applicable) and any relevant parameters required in relation to use of data in that map projection.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-methods-sr.yaml-->`1.7.` Geometric Correction Methods {#sec:meta.metadata-geometric-correction-methods-sr label="|General Metadata: Geometric Correction Methods"}

Identifier: `meta.metadata-geometric-correction-methods-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on geometric correction methods should be available in the metadata as a single DOI landing page, including reference database and auxiliary data such as elevation model(s) and reference chip-sets.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-accuracy-sr.yaml-->`1.8.` Geometric Accuracy of the Data {#sec:meta.metadata-geometric-accuracy-sr label="|General Metadata: Geometric Accuracy of the Data"}

Identifier: `meta.metadata-geometric-accuracy-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data.
Accuracy is assessed by independent verification (as well as internal model-fit where applicable).
Uncertainties are expressed quantitatively, for example, as root mean square error (RMSE) or Circular Error Probability (CEP90, CEP95), etc.

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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-accuracy-sr.yaml-->`1.12.` Radiometric Accuracy {#sec:meta.metadata-radiometric-accuracy-sr label="|General Metadata: Radiometric Accuracy"}

Identifier: `meta.metadata-radiometric-accuracy-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata includes metrics describing the assessed absolute radiometric uncertainty of the version of the data or product, expressed as absolute radiometric uncertainty relative to appropriate, known reference sites and standards (for example, pseudo-invariant calibration sites, rigorously collected field spectra, Rayleigh, DCC, etc.)

Notes:

1. Information on radiometric accuracy should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/algorithms-sr.yaml-->`1.13.` Algorithms {#sec:meta.metadata-algorithms-sr label="|General Metadata: Algorithms"}

Identifier: `meta.metadata-algorithms-sr`



##### Threshold requirements:

All algorithms, and the sequence in which they were applied in the generation process, are identified in the metadata.
For example, these may be available through Algorithm Theoretical Basis documents.

Notes:

1. Information on algorithms should be available in the metadata as a single DOI landing page.


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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-chain-prov-sr.yaml-->`1.15.` Processing Chain Provenance {#sec:meta.metadata-processing-chain-prov-sr label="|General Metadata: Processing Chain Provenance"}

Identifier: `meta.metadata-processing-chain-prov-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on processing chain provenance should be available in the metadata as a single DOI landing page containing detailed description of the processing steps used to generate the product, including the versions of software used, giving full transparency to the users.

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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-quality-sr.yaml-->`1.17.` Overall Data Quality {#sec:meta.metadata-data-quality-sr label="|General Metadata: Overall Data Quality"}

Identifier: `meta.metadata-data-quality-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Machine-readable metrics describing the overall quality of the data are included in the metadata, at minimum the cloud cover extent, i.e.:

- Proportion of observations over land (c.f. ocean) affected by non-target phenomena, e.g., cloud and cloud shadows

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`2.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.

*Cloud optimized file formats are recommended.*


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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/land-water-sr.yaml-->`2.7.` Land/Water Mask {#sec:pxl.per-pixel-land-water-sr label="|Per-Pixel Metadata: Land/Water Mask"}

Identifier: `pxl.per-pixel-land-water-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata indicates whether a pixel is assessed as being land or water. Information on land/water mask should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/snow-ice-sr.yaml-->`2.8.` Snow/Ice Mask {#sec:pxl.per-pixel-snow-ice-sr label="|Per-Pixel Metadata: Snow/Ice Mask"}

Identifier: `pxl.per-pixel-snow-ice-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata indicates whether a pixel is assessed as being snow/ice or not. Information on snow/ice mask should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/terrain-shadow.yaml-->`2.9.` Terrain Shadow Mask {#sec:pxl.per-pixel-terrain-shadow label="|Per-Pixel Metadata: Terrain Shadow Mask"}

Identifier: `pxl.per-pixel-terrain-shadow`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata indicates pixels that are not directly illuminated due to terrain shadowing.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/terrain-occlusion.yaml-->`2.10.` Terrain Occlusion {#sec:pxl.per-pixel-terrain-occlusion label="|Per-Pixel Metadata: Terrain Occlusion"}

Identifier: `pxl.per-pixel-terrain-occlusion`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata indicates pixels that are not visible to the sensor due to terrain occlusion during off-nadir viewing.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/view-angles-solar.yaml-->`2.11.` Solar and Viewing Geometry {#sec:pxl.per-pixel-view-angles-solar label="|Per-Pixel Metadata: Solar and Viewing Geometry"}

Identifier: `pxl.per-pixel-view-angles-solar`



##### Threshold requirements:

Provide average solar and sensor viewing azimuth and zenith angles.


##### Goal requirements:

Provide per-pixel solar and sensor viewing azimuth and zenith angles.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/terrain-illumination.yaml-->`2.12.` Terrain Illumination Correction {#sec:pxl.per-pixel-terrain-illumination label="|Per-Pixel Metadata: Terrain Illumination Correction"}

Identifier: `pxl.per-pixel-terrain-illumination`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Coefficients used for terrain illumination correction are provided for each pixel.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometric-atmospheric-corrections.yaml-->`3.` Radiometric and Atmospheric Corrections {#sec:rac label="|Radiometric and Atmospheric Corrections"}

The following requirements must be met for all pixels in a collection.
The requirements indicate both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes. Radiometric corrections must lead to a valid measurement.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/measurement-sr.yaml-->`3.1.` Measurement {#sec:rac.measurements-measurement-sr label="|Radiometric and Atmospheric Corrections: Measurement"}

Identifier: `rac.measurements-measurement-sr`



##### Threshold requirements:

Pixel values are expressed as a measurement of the Surface Reflectance of the land. This is a dimensionless value.


##### Goal requirements:

Surface Reflectance measurements are SI traceable (see also [@sec:meta.metadata-traceability-sr]).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/uncertainty-sr.yaml-->`3.2.` Measurement Uncertainty {#sec:rac.measurements-uncertainty-sr label="|Radiometric and Atmospheric Corrections: Measurement Uncertainty"}

Identifier: `rac.measurements-uncertainty-sr`



Note: In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.

##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

An estimate of the certainty of the values is provided in measurement units.

Notes:

1. This is a requirement for SI traceability. See also [@sec:meta.metadata-traceability-sr].
2. Information on measurement uncertainty should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/normalisation-sr.yaml-->`3.3.` Measurement Normalisation {#sec:rac.measurements-normalisation-sr label="|Radiometric and Atmospheric Corrections: Measurement Normalisation"}

Identifier: `rac.measurements-normalisation-sr`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Measurements are normalised for solar and viewing conditions (i.e., nadir view angle and average solar angles). This may include terrain illumination and/or Bi-Directional Reflectance Function (BRDF) correction.

Notes:

1. Information on measurement normalisation should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/directional-atmospheric-scattering.yaml-->`3.4.` Directional Atmospheric Scattering {#sec:rac.measurements-directional-atmospheric-scattering label="|Radiometric and Atmospheric Corrections: Directional Atmospheric Scattering"}

Identifier: `rac.measurements-directional-atmospheric-scattering`



##### Threshold requirements:

Corrections are applied for aerosols and molecular (Rayleigh) scattering.

Metadata contains a single DOI landing page with references to:

- a citable peer-reviewed algorithm
- technical documentation regarding the implementation of that algorithm
- the sources of ancillary data used to make corrections

Notes:

1. Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/water-vapour.yaml-->`3.5.` Water Vapour Corrections {#sec:rac.corrections-water-vapour label="|Radiometric and Atmospheric Corrections: Water Vapour Corrections"}

Identifier: `rac.corrections-water-vapour`



##### Threshold requirements:

Corrections are applied for water vapour. Metadata contains a single DOI landing page with references to:

- a citable peer-reviewed algorithm
- technical documentation regarding the implementation of that algorithm

Notes:

1. Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/ozone.yaml-->`3.6.` Ozone Corrections {#sec:rac.corrections-ozone label="|Radiometric and Atmospheric Corrections: Ozone Corrections"}

Identifier: `rac.corrections-ozone`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data is corrected for ozone.

Relevant metadata must be provided under [@sec:meta.metadata-geometric-accuracy-sr] and [@sec:meta.metadata-instrument-optical].

Metadata contains a single DOI landing page with references to:

- a citable peer-reviewed algorithm
- technical documentation regarding the implementation of that algorithm

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`4.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-sr.yaml-->`4.1.` Geometric Correction {#sec:gcor.corrections-geometric-sr label="|Geometric Corrections: Geometric Correction"}

Identifier: `gcor.corrections-geometric-sr`



##### Threshold requirements:

Sub-pixel accuracy is achieved in **relative** geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.

Sub-pixel accuracy is taken to be less than or equal to 0.5 pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.

A consistent gridding/sampling frame is used, including common cell size, origin, and nominal sample point location within the cell (centre, ll, ur).

Relevant metadata must be provided under [@sec:meta.metadata-geometric-accuracy-sr] and [@sec:meta.metadata-instrument-optical].

Notes:

1. The threshold level will not necessarily enable interoperability between data from **different** sources as the geometric corrections for each of the sources may differ. 


##### Goal requirements:

Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).

A consistent gridding/sampling frame is necessary to meet this requirement.

Relevant metadata must be provided under [@sec:meta.metadata-geometric-accuracy-sr] and [@sec:meta.metadata-instrument-optical].

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

