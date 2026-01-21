---
title: >-
  CEOS-ARD - Synthetic Aperture Radar - Ocean Radar Backscatter - Version 1.2-draft
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

# CEOS-ARD - Synthetic Aperture Radar - Ocean Radar Backscatter

&nbsp;

## Document Status

Product Family Specification, Synthetic Aperture Radar, Ocean Radar Backscatter

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

Not available yet

## <!-- edit:pfs/SAR-ORB/authors.yaml -->Contributing Authors

- François Charbonneau, Natural Resources Canada, Canada
- Ake Rosenqvist, soloEO / Japan Aerospace Exploration Agency (JAXA), Japan
- John Truckenbrodt, German Aerospace Centre (DLR), Germany
- Clément Albinet, European Space Agency (ESA), Italy
- David Small, University of Zurich, Switzerland
- Bruce Chapman, Jet Propulsion Laboratory, USA
- Howard Zebker, Stanford University, USA
- Zheng-Shu Zhou, CSIRO, Australia
- Virginia Brancato, Jet Propulsion Laboratory, USA
- Danilo Dadamia, CONAE, Argentina
- Benjamin Deschamps, Environment and Climate Change, Canada
- Guillaume Hajduch, Collecte Localisation Satellites, France
- Josef Kellndorfer, Earth Big Data, USA
- Marco Lavalle, Jet Propulsion Laboratory, USA
- Adam Lewis, Geoscience Australia, Australia
- Thomas Logan, Alaska Satellite Facility, USA
- Franz Meyer, Alaska Satellite Facility, USA
- Nuno Miranda, European Space Agency (ESA), Italy
- Muriel Pinheiro, European Space Agency (ESA), Italy
- Marko Repse, Sinergise, Slovenia
- HariPriya Sakethapuram, ISRO, India
- Andreia Siqueira, Geoscience Australia, Australia
- Gustavo Shiroma, Jet Propulsion Laboratory, USA
- Takeo Tadono, Japan Aerospace Exploration Agency, Japan
- Medhavy Thankappan, Geoscience Australia, Australia
- Antonio Valentino, RHEA for European Space Agency (ESA), Italy
- Anna Wendleder, German Aerospace Centre (DLR), Germany
- Fang Yuan, Digital Earth Africa, Australia

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

<!-- edit:pfs/SAR-ORB/document.yaml -->
**Product Family Specification:**
Synthetic Aperture Radar, Ocean Radar Backscatter (SAR-ORB)

**Version:**
1.2-draft

**Applies to:**
Data collected by Synthetic Aperture Radar sensors

## Background

This PFS is specifically aimed at users interested in exploring the potential of SAR but who may lack the expertise or facilities for SAR processing.

The CEOS-ARD Ocean Radar Backscatter (ORB) product specification describes products that have been projected on a geoid and are provided in the Sigma-Nought ($\sigma^0$) backscatter convention, which is recommended for most ocean applications.
Backscatter may be calibrated to the ellipsoid ($\sigma^0_E$) or radiometrically terrain corrected ($\sigma^0_T$) prior to geometric terrain correction.
As the basic ORB product contains backscatter values only, it _cannot_ be directly used for SAR polarimetry or interferometric applications that require local phase estimates.
Nonetheless, an advanced ORB product could include the upper diagonal of the polarimetric $\sigma^0$ covariance matrix for enabling advanced polarimetric analysis (similar to the POL product).

&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ale.yaml -->
ALE
:   Absolute Geolocation Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/atbd.yaml -->
ATBD
:   Algorithm Theoretical Basis Document

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/auxiliary-data.yaml -->
Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ceos-ard.yaml -->
CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/covmat.yaml -->
CovMat
:   Normalised Radar Covariance Matrix

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/crs.yaml -->
CRS
:   Coordinate Reference System

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/dem.yaml -->
DEM
:   Digital Elevation Model

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/doi.yaml -->
DOI
:   Digital Object Identifier

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/dsm.yaml -->
DSM
:   Digital Surface Model

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/egm.yaml -->
EGM
:   Earth Gravitational Model

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/enl.yaml -->
ENL
:   Equivalent Number of Looks

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/epsg-code.yaml -->
EPSG Code
:   An EPSG code is a unique identifier assigned to e.g. a specific coordinate reference system (CRS) by the European Petroleum Survey Group (EPSG).

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gslc.yaml -->
GSLC
:   Geocoded Single-Look Complex

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/islr.yaml -->
ISLR
:   Intensity Signal-to-Noise Level Ratio

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/lut.yaml -->
LUT
:   Look-Up Table

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/nrb.yaml -->
NRB
:   Normalised Radar Backscatter

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/orb.yaml -->
ORB
:   Ocean Radar Backscatter

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/pol.yaml -->
POL
:   Polarimetric Radar

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/pslr.yaml -->
PSLR
:   Polarimetric Signal-to-Noise Level Ratio

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rrmse.yaml -->
rRMSE
:   Radial Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rtc.yaml -->
RTC
:   Radiometrically Terrain Corrected

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/sar.yaml -->
SAR
:   Synthetic Aperture Radar

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/si.yaml -->
SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/slc.yaml -->
SLC
:   Single-Look Complex

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/stac.yaml -->
STAC
:   SpatioTemporal Asset Catalog

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ups.yaml -->
UPS
:   Universal Polar Stereographic

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/url.yaml -->
URL
:   Uniform Resource Locator, a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/utc.yaml -->
UTC
:   Coordinated Universal Time

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/utm.yaml -->
UTM
:   Universal Transverse Mercator

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/wgs84.yaml -->
WGS84
:   World Geodetic System 1984

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/wkt.yaml -->
WKT
:   Well-Known Text (WKT) is a text markup language for representing vector geometry objects on a map, spatial reference systems of spatial objects, and transformations between spatial reference systems.
The formats were originally defined by the Open Geospatial Consortium (OGC) and described in their Simple Feature Access and Coordinate Transformation Service specifications.

&#12;

## <!-- edit:pfs/SAR-ORB/requirements.yaml -->Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-sar.yaml-->`1.1.` Traceability {#sec:meta.metadata-traceability-sar label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard.

Notes:

1. Relationship to [@sec:rcm.metadata-radiometric-accuracy-sar]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-sar.yaml-->`1.2.` Metadata Machine Readability {#sec:meta.metadata-machine-readability-sar label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta.metadata-machine-readability-sar`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable/layer for further use.


##### Goal requirements:

As threshold, but metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.1, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention, the Attribute Convention for Data Discovery (ACDD), etc.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/product-type-sar.yaml-->`1.3.` Product Type {#sec:meta.metadata-product-type-sar label="|General Metadata: Product Type"}

Identifier: `meta.metadata-product-type-sar`



##### Threshold requirements:

CEOS-ARD product type name – or names in case of compliance with more than one product type – and, if required by the data provider, copyright.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/pfs-url.yaml-->`1.4.` Document Identifier {#sec:meta.metadata-pfs-url label="|General Metadata: Document Identifier"}

Identifier: `meta.metadata-pfs-url`



##### Threshold requirements:

Reference to CEOS-ARD PFS document as URL.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-sar.yaml-->`1.5.` Data Collection Time {#sec:meta.metadata-time-sar label="|General Metadata: Data Collection Time"}

Identifier: `meta.metadata-time-sar`



##### Threshold requirements:

Number of source data acquisitions of the data collection is identified.
The start and stop UTC time of data collection is identified in the metadata, expressed in date/time.
In case of composite products, the dates/times of the first and last data takes and the per-pixel metadata [@sec:pxl.per-pixel-acquisition-id] is provided with the product.


##### Goal requirements:


As threshold.
<!-- *None* -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/source-metadata.yaml-->`2.` Source Metadata {#sec:src label="|Source Metadata"}

These are metadata records describing (detailing) **each** acquisition (source data) used to generate the ARD product.
This may be one or mutliple acquisitions.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/acquisition-id.yaml-->`2.1.` Acquisition ID {#sec:src.metadata-acquisition-id label="|Source Metadata: Acquisition ID"}

Identifier: `src.metadata-acquisition-id`



##### Threshold requirements:

Each acquisition is identified through a sequential identifier in the metadata, e.g. acqID = 1, 2, 3.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access-source.yaml-->`2.2.` Source Data Access {#sec:src.metadata-data-access-source label="|Source Metadata: Source Data Access"}

Identifier: `src.metadata-data-access-source`



##### Threshold requirements:

The metadata identifies the location from where the source data can be retrieved, expressed as a URL or DOI.


##### Goal requirements:

The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/instrument-sar.yaml-->`2.3.` Instrument {#sec:src.metadata-instrument-sar label="|Source Metadata: Instrument"}

Identifier: `src.metadata-instrument-sar`



##### Threshold requirements:

The instrument used to collect the data is identified in the metadata:

- Satellite name
- Instrument name


##### Goal requirements:

As threshold, but including a reference to the relevant [CEOS Missions, Instruments and Measurements Database](https://ceos.org/mim-database/) record.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-source.yaml-->`2.4.` Source Data Acquisition Time {#sec:src.metadata-time-source label="|Source Metadata: Source Data Acquisition Time"}

Identifier: `src.metadata-time-source`



##### Threshold requirements:

The start date and time of source data is identified in the metadata, expressed in UTC in date and time, at least to the second.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/acquisition-parameters-sar.yaml-->`2.5.` Source Data Acquisition Parameters {#sec:src.metadata-acquisition-parameters-sar label="|Source Metadata: Source Data Acquisition Parameters"}

Identifier: `src.metadata-acquisition-parameters-sar`



##### Threshold requirements:

Acquisition parameters related to the SAR antenna:

- Radar band
- Centre frequency
- Observation mode (i.e., beam mode name)
- Polarization(s) (listed as in original product)
- Antenna pointing (right/left)
- Beam ID (i.e., beam mode mnemonic)


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/orbit.yaml-->`2.6.` Source Data Orbit Information {#sec:src.metadata-orbit label="|Source Metadata: Source Data Orbit Information"}

Identifier: `src.metadata-orbit`



##### Threshold requirements:

Information related to the platform orbit used for data processing:

- Pass direction (asc/desc)[^orbit-pass-direction]
- Orbit data source (e.g., predicted, definite, precise, downlinked, etc.)

[^orbit-pass-direction]: For data crossing the North or South Pole, it is recommended to produce two distinct products and to use the appropriate “Pass direction” in each.


##### Goal requirements:

As threshold, including also:

- Platform heading angle expressed in degrees (0-360) from North 
- Orbit data file containing state vectors (minimum of 5 state vectors, from 10% of scene length before start time to 10% of scene length after stop time) 
- Platform (mean) altitude

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-parameters.yaml-->`2.7.` Source Data Processing Parameters {#sec:src.metadata-processing-parameters label="|Source Metadata: Source Data Processing Parameters"}

Identifier: `src.metadata-processing-parameters`



##### Threshold requirements:

Processing parameters details of the source data:

- Processing facility
- Processing date
- Software version
- Product level
- Product ID (file name)
- Azimuth number of looks
- Range number of looks (separate values for each beam, as necessary)


##### Goal requirements:

As threshold, plus additional relevant processing parameters, e.g., range- and azimuth look bandwidth and LUT applied.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/image-attributes-sar.yaml-->`2.8.` Source Data Image Attributes {#sec:src.metadata-image-attributes-sar label="|Source Metadata: Source Data Image Attributes"}

Identifier: `src.metadata-image-attributes-sar`



##### Threshold requirements:

Image attributes related to the source data:

- Source Data geometry (slant range/ground range)
- Azimuth pixel spacing \[m] (alternatively, Azimuth pixel spacing can be provided in second \[s], equivalent to the azimuth time sample interval) 
- Range pixel spacing 
- Azimuth resolution 
- Range resolution 
- Near range incident angle 
- Far range incident angle


##### Goal requirements:

Geometry of the image footprint expressed in WGS84 in a standardised format (e.g., WKT).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sensor-calibration-sar.yaml-->`2.9.` Sensor Calibration {#sec:src.metadata-sensor-calibration-sar label="|Source Metadata: Sensor Calibration"}

Identifier: `src.metadata-sensor-calibration-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata.
Ideally this would support machine-to-machine access.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/performance-indicators.yaml-->`2.10.` Performance Indicators {#sec:src.metadata-performance-indicators label="|Source Metadata: Performance Indicators"}

Identifier: `src.metadata-performance-indicators`



##### Threshold requirements:

Provide performance indicators on data intensity noise level ($\text{NE}\sigma^0$ and/or $\text{NE}\beta^0$ and/or $\text{NE}\gamma^0$, i.e., noise equivalent Sigma- and/or Beta- and/or Gamma-Nought).
Provided for each polarization channel when available.

Parameter may be expressed as the mean and/or minimum and maximum noise equivalent values of the source data.

Values do not need to be estimated individually for each product, but may be estimated once for each acquisition mode, and annotated on all products.


##### Goal requirements:

Provide additional relevant performance indicators (e.g., ENL, PSLR, ISLR, and performance reference DOI or URL).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/polarimetric-calibration-matrices.yaml-->`2.11.` Polarimetric Calibration Matrices {#sec:src.metadata-polarimetric-calibration-matrices label="|Source Metadata: Polarimetric Calibration Matrices"}

Identifier: `src.metadata-polarimetric-calibration-matrices`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The complex-valued polarimetric distortion matrices with the channel imbalance and the cross-talk applied for the polarimetric calibration.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/mean-faraday-rotation-angle.yaml-->`2.12.` Mean Faraday Rotation Angle {#sec:src.metadata-mean-faraday-rotation-angle label="|Source Metadata: Mean Faraday Rotation Angle"}

Identifier: `src.metadata-mean-faraday-rotation-angle`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The mean Faraday rotation angle estimated from the polarimetric data and/or from models with reference to the method or paper used to derive the estimate.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/ionosphere-indicator.yaml-->`2.13.` Ionosphere Indicator {#sec:src.metadata-ionosphere-indicator label="|Source Metadata: Ionosphere Indicator"}

Identifier: `src.metadata-ionosphere-indicator`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Flag indicating whether the backscatter imagery is “significantly impacted” by the ionosphere (0 – false, 1 – true).
Significant impact would imply that the ionospheric impact on the backscatter exceeds the radiometric calibration requirement or goal for the imagery.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/product-metadata.yaml-->`3.` Product Metadata {#sec:prd label="|Product Metadata"}

Information related to the CEOS-ARD product generation procedure and geographic parameters.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access-product.yaml-->`3.1.` Product Data Access {#sec:prd.metadata-data-access-product label="|Product Metadata: Product Data Access"}

Identifier: `prd.metadata-data-access-product`



##### Threshold requirements:

Processing parameters details of the CEOS-ARD product:

- Processing facility
- Processing date
- Software version
- Location from where CEOS-ARD product can be retrieved, expressed as a URL or DOI.


##### Goal requirements:

The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/auxiliary-data.yaml-->`3.2.` Auxiliary Data {#sec:prd.metadata-auxiliary-data label="|Product Metadata: Auxiliary Data"}

Identifier: `prd.metadata-auxiliary-data`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as DOIs.

Notes:

1. Auxiliary data includes DEMs, etc., and any additional data sources used in the generation of the product.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sample-spacing.yaml-->`3.3.` Product Sample Spacing {#sec:prd.metadata-sample-spacing label="|Product Metadata: Product Sample Spacing"}

Identifier: `prd.metadata-sample-spacing`



##### Threshold requirements:

CEOS-ARD product processing parameters details:

- Pixel (column) spacing
- Line (row) spacing


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/enl.yaml-->`3.4.` Product Equivalent Number of Looks {#sec:prd.metadata-enl label="|Product Metadata: Product Equivalent Number of Looks"}

Identifier: `prd.metadata-enl`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Equivalent Number of Looks (ENL)

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/resolution.yaml-->`3.5.` Product Resolution {#sec:prd.metadata-resolution label="|Product Metadata: Product Resolution"}

Identifier: `prd.metadata-resolution`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Average spatial resolution of the CEOS-ARD product along:

- Columns
- Rows

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/speckle-filtering.yaml-->`3.6.` Product Filtering {#sec:prd.metadata-speckle-filtering label="|Product Metadata: Product Filtering"}

Identifier: `prd.metadata-speckle-filtering`



##### Threshold requirements:

Flag if speckle filter has been applied (True/False).

Metadata should include:

- Reference to algorithm as DOI or URL
- Input filtering parameters
  - Type
  - Window size in pixel units
  - Any other parameters defining the speckle filter used


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-bbox.yaml-->`3.7.` Product Bounding Box {#sec:prd.metadata-geo-bbox label="|Product Metadata: Product Bounding Box"}

Identifier: `prd.metadata-geo-bbox`



##### Threshold requirements:

Two opposite corners of the product file (bounding box, including any zero-fill values) are identified,
expressed in the coordinate reference system defined in [@sec:prd.metadata-crs].

Notes:

1. Four corners of the product file are recommended for scenes crossing the Antemeridian, or the North or the South Pole.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-area.yaml-->`3.8.` Product Geographical Extent {#sec:prd.metadata-geo-area label="|Product Metadata: Product Geographical Extent"}

Identifier: `prd.metadata-geo-area`



##### Threshold requirements:

The geometry of the SAR image footprint expressed in WGS84, in a standardised format (e.g., WKT Polygon).


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/image-size.yaml-->`3.9.` Product Image Size {#sec:prd.metadata-image-size label="|Product Metadata: Product Image Size"}

Identifier: `prd.metadata-image-size`



##### Threshold requirements:

Image attributes of the CEOS-ARD product:

- Number of lines
- Number of pixels per line
- File header size (if applicable)
- Number of no-data border pixels (if applicable)


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/pixel-coordinate-convention.yaml-->`3.10.` Product Pixel Coordinate Convention {#sec:prd.metadata-pixel-coordinate-convention label="|Product Metadata: Product Pixel Coordinate Convention"}

Identifier: `prd.metadata-pixel-coordinate-convention`



##### Threshold requirements:

Coordinate referring to the centre, the upper left corner, or the lower left corner of a pixel.
Values are [pixel centre, pixel ULC or pixel LLC].


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/crs.yaml-->`3.11.` Product Coordinate Reference System {#sec:prd.metadata-crs label="|Product Metadata: Product Coordinate Reference System"}

Identifier: `prd.metadata-crs`



##### Threshold requirements:

The metadata lists the map projection (or geographical coordinates, if applicable) that was used and any relevant parameters required to geolocate data in that map projection, expressed in a standardised format (e.g., WKT).  
Indicate EPSG code, if defined for the CRS.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/look-direction-polynomials.yaml-->`3.12.` Look Direction Polynomials {#sec:prd.metadata-look-direction-polynomials label="|Product Metadata: Look Direction Polynomials"}

Identifier: `prd.metadata-look-direction-polynomials`



##### Threshold requirements:

In case the Look Direction Image (see [@sec:pxl.per-pixel-look-direction]) is **not** provided, then a list of the polynomial coefficients are necessary to reconstruct the look direction angle[^look-direction-angle], together with an estimate of the added error from use of polynomial vs. per-pixel more accurate values, shall be provided.

Example polynomial:

$$
\text{LookDir} = a_{1}\text{Lat}^2 + a_{2}\text{Lon}^2 + a_{3}\text{LatLon} + a_{4}\text{Lat} + a_{5}\text{Lon} + a_6
$$

where:

- $a_i$ = polynomial coefficients 
- $\text{Lat}$ = latitude  
- $\text{Lon}$ = longitude

Lat and Lon are the related coordinates in the product map units (m, deg, arcsec).

[^look-direction-angle]: The look direction angle represents the planar angle between north and each range direction. It is not constant in range, especially close to the poles.


##### Goal requirements:


As threshold.
<!-- *None* -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`4.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.

*Cloud optimized file formats are recommended.*


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/cloud-optimized-formats.yaml-->`4.1.` Cloud Optimized Formats {#sec:pxl.cloud-optimized-formats label="|Per-Pixel Metadata: Cloud Optimized Formats"}

Identifier: `pxl.cloud-optimized-formats`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

All files are provided using cloud-optimized file formats.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-sar.yaml-->`4.2.` Metadata Machine Readability {#sec:pxl.metadata-machine-readability-sar label="|Per-Pixel Metadata: Metadata Machine Readability"}

Identifier: `pxl.metadata-machine-readability-sar`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable/layer for further use.


##### Goal requirements:

As threshold, but metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.1, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention, the Attribute Convention for Data Discovery (ACDD), etc.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/data-mask.yaml-->`4.3.` Data Mask Image {#sec:pxl.per-pixel-data-mask label="|Per-Pixel Metadata: Data Mask Image"}

Identifier: `pxl.per-pixel-data-mask`



##### Threshold requirements:

Mask image indicating:

- Valid data
- Invalid data
- No data

File format specifications/contents provided in metadata:

- Sample Type (Mask)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, …)
- Bits per Sample
- Byte Order
- Bit Value Representation


##### Goal requirements:

As threshold, including additional bit value representations, e.g.:

- Layover (masked as invalid data in threshold)
- Radar shadow (masked as invalid data in threshold)
- Ocean water
- Land (recommended for ORB)
- RTC applied (e.g., for maritime scenes with land samples for which RTC has been applied)
- DEM gap filling (i.e., interpolated DEM over gaps)

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/scattering-area.yaml-->`4.4.` Scattering Area Image {#sec:pxl.per-pixel-scattering-area label="|Per-Pixel Metadata: Scattering Area Image"}

Identifier: `pxl.per-pixel-scattering-area`



**Usage: Recommended for scenes that include land areas.**

##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

DEM-based scattering area image used for Gamma-Nought terrain normalisation is provided.
This quantifies the local scattering area used to normalise for radiometric distortions induced by terrain to the measured $\beta^0$ backscatter.
The terrain-flattened $\gamma^0_T$ is best understood as $\beta^0$ divided by the local scattering area.

File format specifications/contents provided in metadata:

- Sample Type (Scattering Area)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/local-incident-angle.yaml-->`4.5.` Local Incident Angle Image {#sec:pxl.per-pixel-local-incident-angle label="|Per-Pixel Metadata: Local Incident Angle Image"}

Identifier: `pxl.per-pixel-local-incident-angle`



##### Threshold requirements:

DEM-based Local Incident angle image is provided.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Notes:

1. For maritime ORB scenes when no land areas are covered, a geoid model could be used for the calculation of the local incident angle.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/ellipsoidal-incident-angle.yaml-->`4.6.` Ellipsoidal Incident Angle Image {#sec:pxl.per-pixel-ellipsoidal-incident-angle label="|Per-Pixel Metadata: Ellipsoidal Incident Angle Image"}

Identifier: `pxl.per-pixel-ellipsoidal-incident-angle`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Ellipsoidal incident angle is provided.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
- Reference Ellipsoid Name

Notes:

1. For maritime ORB scenes when no land areas are covered, the ellipsoidal incident angle is nearly identical to the geoid based local incident angle.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/noise-power.yaml-->`4.7.` Noise Power Image {#sec:pxl.per-pixel-noise-power label="|Per-Pixel Metadata: Noise Power Image"}

Identifier: `pxl.per-pixel-noise-power`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Estimated Noise Equivalent $\sigma^0$ (or $\beta^0$ or $\gamma^0$, as applicable) used for noise removal, if applied, for each channel.
$\text{NE}\sigma^0$ and $\text{NE}\gamma^0$ are both based on a simplified ellipsoid Earth model.

File format specifications/contents provided in metadata:

- Sample Type (Gamma-Nought, Sigma-Nought, Beta-Nought)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/acquisition-id.yaml-->`4.8.` Acquisition ID Image {#sec:pxl.per-pixel-acquisition-id label="|Per-Pixel Metadata: Acquisition ID Image"}

Identifier: `pxl.per-pixel-acquisition-id`



##### Threshold requirements:

**Required for multi-source product only.**

Acquisition ID, or acquisition date, for each pixel is identified.

In case of multi-temporal image stacks, use a source acquisition ID (i.e., [@sec:src.metadata-acquisition-id]) to list contributing images.

In case of date, data represent (integer or fractional) day offset to reference observation date (in UTC). Date used as reference (“Day 0”) is provided in the metadata.

Pixels not representing a unique date (e.g., pixels averaged in image overlap zones) are flagged with a pre-set pixel value that is provided in the metadata.

File format specifications/contents provided in metadata:

- Sample type (Day, Time, ID)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per sample
- Byte Order


##### Goal requirements:

In case of image composites, the sources for each pixel are uniquely identified.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/geoid.yaml-->`4.9.` Per-Pixel Geoid {#sec:pxl.per-pixel-geoid label="|Per-Pixel Metadata: Per-Pixel Geoid"}

Identifier: `pxl.per-pixel-geoid`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Provide Geoid as used during the geometric and radiometric processing of the SAR data, resampled to an exact geometric match in extent and resolution with the image product.

File format specifications/contents provided in metadata:

- Sample Type (Height)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
- Ground Sampling Distance

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/look-direction.yaml-->`4.10.` Look Direction Image {#sec:pxl.per-pixel-look-direction label="|Per-Pixel Metadata: Look Direction Image"}

Identifier: `pxl.per-pixel-look-direction`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Look Direction Image is provided.
It represents the planar angle between north and each range direction. 

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometrically-corrected-measurements.yaml-->`5.` Radiometrically Corrected Measurements {#sec:rcm label="|Radiometrically Corrected Measurements"}

The requirements indicate the necessary outcomes and, to some degree, the minimum steps necessary to be deemed to have achieved those outcomes.
Radiometric corrections must lead to normalised measurement(s) of backscatter intensity and/or decomposed polarimetric parameters.
As for the per-pixel metadata, information regarding data format specification needs to be provided for each record.
The requirements below must be met for all pixels/samples/observations in a collection.

*Cloud optimized file formats are recommended.*


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/cloud-optimized-formats.yaml-->`5.1.` Cloud Optimized Formats {#sec:rcm.cloud-optimized-formats label="|Radiometrically Corrected Measurements: Cloud Optimized Formats"}

Identifier: `rcm.cloud-optimized-formats`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

All files are provided using cloud-optimized file formats.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/backscatter-orb.yaml-->`5.2.` Backscatter Measurements (ORB) {#sec:rcm.measurements-backscatter-orb label="|Radiometrically Corrected Measurements: Backscatter Measurements (ORB)"}

Identifier: `rcm.measurements-backscatter-orb`



##### Threshold requirements:

Geoid-corrected Sigma-Nought backscatter coefficient ($\sigma^0$) is provided for each polarization. 

File format specifications/contents provided in metadata:

- Measurement Type (Sigma-Nought)
- Backscatter Expression Convention (linear amplitude, linear power\*)
- Backscatter Conversion Equation
- Polarization (HH, HV, VV, VH)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Notes:

1. Transformation to the logarithm decibel scale is not required or desired as this step can be easily completed by the user if necessary.


##### Goal requirements:

Radiometrically Terrain-corrected Sigma-Nought backscatter coefficient ($\sigma^0_T$) is provided for each polarization.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/scaling-conversion.yaml-->`5.3.` Scaling Conversion {#sec:rcm.metadata-scaling-conversion label="|Radiometrically Corrected Measurements: Scaling Conversion"}

Identifier: `rcm.metadata-scaling-conversion`



##### Threshold requirements:

If applicable, indicate the equation to convert pixel linear amplitude/power to logarithmic decibel scale, including, if applicable, the associated calibration (dB offset) factor, and/or the equation used to convert compressed data (int8/int16/float16) to float32.


##### Goal requirements:

As threshold, but use of float32.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/noise-removal.yaml-->`5.4.` Noise Removal {#sec:rcm.metadata-noise-removal label="|Radiometrically Corrected Measurements: Noise Removal"}

Identifier: `rcm.metadata-noise-removal`



##### Threshold requirements:

Flag if noise removal has been applied (Y/N).
Metadata should include the noise removal algorithm and reference to the algorithm as URL or DOI.

Notes:

1. Thermal noise removal and image border noise removal to remove overall scene noise and scene edge artefacts, respectively.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-accuracy-sar.yaml-->`5.5.` Radiometric Accuracy {#sec:rcm.metadata-radiometric-accuracy-sar label="|Radiometrically Corrected Measurements: Radiometric Accuracy"}

Identifier: `rcm.metadata-radiometric-accuracy-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Uncertainty (e.g., bounds on $\gamma^0$ or $\sigma^0$) information is provided as document referenced as URL or DOI.
SI traceability is achieved.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/mean-wind-normalised-backscatter.yaml-->`5.6.` Mean Wind-Normalised Backscatter Measurements {#sec:rcm.measurements-mean-wind-normalised-backscatter label="|Radiometrically Corrected Measurements: Mean Wind-Normalised Backscatter Measurements"}

Identifier: `rcm.measurements-mean-wind-normalised-backscatter`



**Usage:** Only for Maritime scenes.

##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Mean wind-normalised (over ocean) backscatter coefficient is provided for each available polarization.
It is calculated as the ratio between the backscatter intensity and a simulated backscatter intensity image generated using an ocean surface wind model such as, e.g., [@quilfen1998] or [@vachon2000] for VV and HH polarization respectively.

File format specifications/contents provided in metadata:

- Measurement Type (Wind-Normalised Backscatter)
- Backscatter Expression Convention (intensity ratio)
- Polarization (HH, HV, VV, VH)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Notes:

1. Reference wind model, wind speed and direction used for reference backscattering coefficient should be provided.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`6.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-algorithm.yaml-->`6.1.` Geometric Correction Algorithm {#sec:gcor.metadata-geometric-correction-algorithm label="|Geometric Corrections: Geometric Correction Algorithm"}

Identifier: `gcor.metadata-geometric-correction-algorithm`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Metadata references, e.g.:

- A metadata citable peer-reviewed algorithm
- Technical documentation regarding the implementation of that algorithm expressed as URLs or DOIs
- The sources of auxiliary data used to make corrections
- Resampling method used for geometric processing of the source data

Notes:

1. Examples of technical documentation can include e.g., an Algorithm Theoretical Basis Document (ATBD) or a product user guide.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/dem.yaml-->`6.2.` Digital Elevation Model {#sec:gcor.corrections-dem label="|Geometric Corrections: Digital Elevation Model"}

Identifier: `gcor.corrections-dem`



**Usage: For products including land areas.**

##### Threshold requirements:

- During ortho-rectification, the data provider shall use the same DEM that was used for the radiometric terrain flattening to ensure consistency of the data stack.
- Provide reference to Digital Elevation Model used for geometric terrain correction.
- Provide reference to Earth Gravitational Model (EGM) used for geometric correction.


##### Goal requirements:

- A DEM with comparable or better resolution to the resolution of the output CEOS-ARD product shall be used if available.
  Else, the upsampled DEM is identified.
- Resampling method used for preparation of the DEM.
- Method used for resampling the EGM.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-accuracy-radar.yaml-->`6.3.` Geometric Accuracy {#sec:gcor.corrections-geometric-accuracy-radar label="|Geometric Corrections: Geometric Accuracy"}

Identifier: `gcor.corrections-geometric-accuracy-radar`



##### Threshold requirements:

Accurate geolocation is a prerequisite to radar processing to correct for terrain and to enable interoperability between radar sensors.

The absolute geolocation error (ALE) for a sensor is typically assessed through analysis of Single Look Complex (SLC) imagery and measured along the slant range and azimuth directions (case A: SLC ALE).

The end-to-end “ARD” ALE of the final CEOS-ARD product could be measured directly in the final image product in the chosen map projection, i.e., in the map coordinate directions: e.g., Northing and Easting (case B: ARD ALE).

Providing accuracy estimates based on measurements following at least one scheme (A or B or both) meets the threshold requirement.

Estimates of the ALE is provided as a bias and a standard deviation, with (Case A) SLC ALE expressed in slant range and azimuth, and (Case B) ARD ALE expressed in map projection dimensions.

Notes:

1. This assessment is often made through comparison of measured corner reflector positions with their projected location in the imagery. In some cases, other mission calibration/validation results may be used.
2. The ALE is not typically assessed for every processed image, but through an ALE assessment by the data processing team characterizing all or (usually a subset) of the generated products.


##### Goal requirements:

Output product sub-sample accuracy should be less than or equal to 0.1 (slant range) pixel radial root mean square error (rRMSE).

Provide documentation of estimates of ALE as DOI or URL.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-refined-accuracy.yaml-->`6.4.` Geometric Refined Accuracy {#sec:gcor.corrections-geometric-refined-accuracy label="|Geometric Corrections: Geometric Refined Accuracy"}

Identifier: `gcor.corrections-geometric-refined-accuracy`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Values provided under [@sec:gcor.corrections-geometric-accuracy-radar] are provided by the SAR mission Cal/Val team.

CEOS-ARD processing steps could include method refining the geometric accuracy, such as cross-correlation of the SAR data in slant range with a SAR scene simulated from a DSM or DEM.

Methodology used (name and reference), quality flag, geometric standard deviation values should be provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/gridding-convention.yaml-->`6.5.` Gridding Convention {#sec:gcor.corrections-gridding-convention label="|Geometric Corrections: Gridding Convention"}

Identifier: `gcor.corrections-gridding-convention`



##### Threshold requirements:

A consistent gridding/sampling frame is used. The origin is chosen to minimise any need for subsequent resampling between multiple products (be they from the same or different providers).
This is typically accomplished via a “snap to grid” in relation to the most proximate grid tile in a global system.

Notes:

1. If a product hierarchy of resolutions exists (or is planned), the multiple resolutions should nest within each other (e.g., 12.5m, 25m, 50m, 100m, etc.), and not be disjoint.


##### Goal requirements:

Provide DOI or URL to gridding convention used.

When multiple providers share a common map projection, providers are encouraged to standardise the origins of their products among each other.

In the case of UTM/UPS coordinates, the upper left corner coordinates should be set to an integer multiple of sample intervals from a 100 km by 100 km grid tile of the Military Grid Reference System's 100k coordinates (“snap to grid”).

For products presented in geographic coordinates (latitude and longitude), the origin should be set to an integer multiple of samples in relation to the closest integer degree.

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


### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/sar-general-processing-roadmap.yaml-->General Processing Map {#sec:annex-sar-general-processing-roadmap label="|General Processing Map"}

The radiometric interoperability of CEOS-ARD SAR products is ensured by a common processing chain during production. The recommended processing roadmap involves the following steps:

- Apply the best possible orbit parameters to give the most accurate product possible. These will have been projected to an ellipsoidal model such as WGS84. To achieve the level of geometric accuracy required for the DEM-based correction, precise orbit determination will be required.
- Apply instrument calibration to produce Beta-Nought values with high fidelity.
- Convert Single-Look-Complex (SLC) radiometric channel(s) to intensity NRB, ORB and POL and in addition for POL, the cross-product element(s) of the covariance as shown in [@sec:annex-sar-pol-covmat].
- Perform radiometric terrain correction (gamma backscatter convention terrain-flattening) on the covariance matrix by applying the local surface normalisation factor to each backscatter measurement element [@small2011; @shiroma2022].
- Perform polarimetric speckle filtering (optional for NRB and ORB), before geocoding, to optimally preserve the polarimetric information. Most popular polarimetric decomposition methodologies are incoherent in nature, which requires averaging the covariance matrix for stationarity. Depending on the application, a polarimetric filter that preserves local point targets and locally average extended targets may be used, e.g., Sigma Lee filter with 7x7 window and 3-point target [@lee2009]. Multi-looking could be performed to meet optimal output sample spacing before the geometric correction step. No speckle filtering or multi-looking is performed for GSLC products.
- For GSLC products, the topographic phase is estimated relative to a reference orbit and removed from the SLC data [@zebker2010; @zebker2017] (see [@sec:annex-sar-topographic-phase-removal])
- Geometric terrain correction (relative to geoid for ORB) is applied to the normalized backscatter measurement data. For POL, the resampling methodology should be nearest-neighbour, bilinear or average in order to preserve integrity of the covariance matrix as other resampling functions can introduce artefacts due to the mix of intensity and complex number elements in the matrix. Geocoding to a common grid structure with specified pixel spacings for true data cube format.
- Generate CEOS format metadata to accompany product layers.
- Optionally, a SpatioTemporal Asset Catalog (STAC) file is added to the product.

[@tbl:sar-general-processing-roadmap-tbl1] lists possible sequential steps and existing software tools (e.g., Gamma software (GAMMA, 2018)) and scripting tasks that can be used to form the CEOS-ARD SAR processing roadmap.

| Step                                                         | Implementation option                                        |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1. Orbital data refinement                                   | Check xml date and delivered format. RADARSAT-2, pre EDOT (July 2015) replace. Post July 2015, check if ‘DEF’, otherwise replace. (Gamma - RSAT2\_vec) |
| 2. Apply radiometric scaling Look-Up Table (LUT) to Beta-Nought | Specification of LUT on ingest.&#10;(Gamma - par_RSAT2_SLC/SG) |
| 3. Generate covariance matrix elements                       | Gamma – COV_MATRIX                                           |
| 4. Radiometric terrain normalisation                         | Gamma - geo_radcal2                                          |
| 5. Speckle filtering (Boxcar or Sigma Lee)                   | Custom scripting                                             |
| 6. Geometric terrain correction/Geocoding                    | Gamma – gc_map and geocode_back                              |
| 7. Create metadata                                           | Custom scripting                                             |

: SAR ARD processing roadmap and software options. RADARSAT-2 Example {#tbl:sar-general-processing-roadmap-tbl1}


### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/sar-topographic-phase-removal.yaml-->Topographic phase removal {#sec:annex-sar-topographic-phase-removal label="|Topographic phase removal"}

InSAR analysis capabilities from CEOS-ARD SAR products are enabled with GSLC products, which is also the case when the Flattened Phase per-pixel data ([@sec:rcm.measurements-flattened-phase]) are included in the NRB or POL products. This is made possible since the simulated topographic phase relative to a given reference orbit has been subtracted.

From classical approach with SLC data, interferometric phase $\Delta \varphi_{1-2}$ between two SAR acquisitions is composed of a topographic phase $\Delta \varphi_{\text{Topo}\_1-2}$, a surface displacement phase $\Delta \varphi_{\text{Disp}\_1-2}$ and other noise terms $\Delta \varphi_{\text{Noise}\_1-2}$ ([@eq:sar-topographic-phase-removal-eq1]). The topographic phase consists to the difference in geometrical path length from each of the two antenna positions to the point on the SAR image ($\varphi_{\text{DEM}\_\text{SLC}}$) and is a function of their orbital baseline distance ([@eq:sar-topographic-phase-removal-eq2]). The surface displacement phase is related to the displacement of the surface that occurred in between the two acquisitions. The noise term is the function of the radar signal interaction with the atmosphere and the ionosphere during each acquisition and function of the system noise.

$$
\Delta \varphi_{1-2} = \Delta \varphi_{\text{Topo}\_1-2} + \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq1}

Where

$$
\Delta \varphi_{\text{Topo}\_1-2} = \varphi_{\text{DEM}\_\text{SLC}\_1} = \varphi_{\text{DEM}\_\text{SLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq2}

Since CEOS-ARD products are already geocoded, it is important to remove the wrapped simulated topographic phase $\varphi_{\text{SimDEM}\_\text{SLC}}$ from the data in slant range ([@eq:sar-topographic-phase-removal-eq3]) during their production, before the geocoding step. The key here is to simulate the topographic phase relatively to a constant reference orbit, as done in a regular InSAR processing. There are two different ways to simulate the topographic phase:

1. The use of a virtual circular orbit above a nonrotating planet [@zebker2010]
2. The use of a specific orbit cycle or a simulated orbit of the SAR mission

In both cases, the InSAR topographic phase $\Delta \varphi_{\text{Topo}\_\text{OrbRef}-2}$ is simulated against the position of a virtual sensor $\Delta \varphi_{\text{Topo}\_\text{OrbRef}}$ lying on a reference orbit, instead of being simulated relatively to an existing reference SAR acquisition ($\varphi_{\text{DEM}\_\text{SLC}\_1}$). The use of a virtual circular orbit is a more robust approach since the reference orbit is defined at a fixed height above scene nadir and assuming the reference orbital height constant for all CEOS-ARD products. While with the second approach, the CEOS-ARD data producer must select a specific archived orbit cycle of the SAR mission or define a simulated one, from which the relative orbit, matching the one of the SAR acquisitions to be processed (to be converted to CEOS-ARD), is defined as the reference orbit. With this second approach, it is important to always use the same orbit cycle (or simulated orbit) for all the CEOS-ARD produced for a mission, in order to preserve the relevant compensated phase in between them. Providing absolute reference orbit number information in the metadata (item 1.7.15) allows users to validate the InSAR feasibility in between CEOS-ARD products.

$$
\varphi_{\text{Flattended}\_\text{SLC}\_2} = \varphi_{\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-2}
$$ {#eq:sar-topographic-phase-removal-eq3}

This procedure is equivalent to bring the position of the sensor platform of all the SAR acquisitions at the same orbital position (i.e., zeros baseline distance in between), which results in a Flattened phase  $\varphi_{\text{Flattended}\_\text{SLC}}$, independent of the local topography.

The phase subtraction could be performed by using a motion compensation approach [@zebker2010] or directly on the SLC data. Then the geometrical correction is performed on the Flattened SLC, which results in a GSLC product.

GSLC can also be saved as a NRB product by including the Flattened Phase per-pixel data ([@sec:rcm.measurements-flattened-phase]) as follows:

$$\text{NRB:} \quad \gamma_T^0 = |GSLC|^2 $$

$$\text{Flattended Phase:} \quad \varphi_{\text{Flattended}} = \arg (GSLC) $$

For POL product, the Flattened phase needs also to be subtracted from the complex number phase of the off-diagonal elements of the covariance matrix.

Demonstration:

From CEOS-ARD flattened SAR products, InSAR processing can be easily performed without dealing with topographic features and orbital sensor position, as for example with two GSLC products

$$
\varphi_{\text{Flattened}\_\text{GSLC}\_1} = \varphi_{\text{SLC}\_1} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-1} = \varphi_{\text{SLC}\_1} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_1}
$$ {#eq:sar-topographic-phase-removal-eq4}

$$
\varphi_{\text{Flattened}\_\text{GSLC}\_2} = \varphi_{\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-2} = \varphi_{\text{SLC}\_2} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq5}

The differential phase is

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} =  \varphi_{\text{Flattened}\_\text{GSLC}\_1} - \varphi_{\text{Flattened}\_\text{GSLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq6}

Which can be expanded using ([@eq:sar-topographic-phase-removal-eq3])

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\varphi_{\text{SLC}\_1} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_1}) - (\varphi_{\text{SLC}\_2} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_2})
$$ {#eq:sar-topographic-phase-removal-eq7}

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\varphi_{\text{SLC}\_1} - \varphi_{\text{SLC}\_2}) - (\varphi_{\text{DEM}\_\text{SLC}\_1}) - \varphi_{\text{DEM}\_\text{SLC}\_2})
$$ {#eq:sar-topographic-phase-removal-eq8}

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = \Delta\varphi_{\text{SLC}\_1-\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq9}

Where $\Delta\varphi_{\text{SLC}\_1-\text{SLC}\_2}$ can be express as [@eq:sar-topographic-phase-removal-eq1], which gives

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\Delta \varphi_{\text{Topo}\_1-2} + \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2}) - \Delta\varphi_{\text{Topo}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq10}

Consequently, the differential phase of two CEOS-ARD products doesn’t contain a topographic phase and is already unwrapped (at least over stable areas). It is only function of the surface displacement and of the noise term. Depending on the reference DEM and the satellite orbital state vector accuracies, some residual topographic phase could be present. Atmospheric (item 2.15) and ionospheric (item 2.16) phase corrections could be performed during the production of CEOS-ARD products, which reduces the differential phase noise in an InSAR analysis.

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2})
$$ {#eq:sar-topographic-phase-removal-eq11}


### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/sar-pol-covmat.yaml-->Normalised Covariance Matrices (CovMat) {#sec:annex-sar-pol-covmat label="|Normalised Covariance Matrices (CovMat)"}

In order to preserve the inter-channel polarimetric phase and thus the full information content of coherent dual-pol and fully polarimetric data, the covariance matrix is proposed as the data storage format. Covariance matrices are generated from the complex cross product of polarimetric channels, as shown in [@eq:sar-pol-covmat-eq1] for fully polarimetric data (C3) and in [@eq:sar-pol-covmat-eq3] for dual polarization data (C2). Since these matrices are complex symmetrical, only the upper diagonal elements (bold elements) need to be stored in the ARD database.

**Fully polarimetric**

$$
C3 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* & \mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \\
\sqrt{2} \cdot HV \cdot HH^* & 2 \cdot |\mathbf{H}\mathbf{V}|^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{V} \cdot \mathbf{H}\mathbf{V}^* \\
VV \cdot HH^* & \sqrt{2} \cdot VV \cdot HV^* & |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq1}

Where HV = VH, under the reciprocity assumption. \| \| and \* mean respectively complex modulus and the complex conjugate.

**Dual polarization**

$$
\text{HH-HV:} \quad C2 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \\
HV \cdot HH^* &  |\mathbf{H}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq2}

$$
\text{VV-VH:} \quad C2 = \begin{bmatrix}
| \mathbf{V} \mathbf{H} |^2 & \mathbf{V}\mathbf{H} \cdot \mathbf{V}\mathbf{H}^* \\
VH \cdot VH^* &  |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq3}

$$
\text{CH-CV:} \quad C2 = \begin{bmatrix}
| \mathbf{C} \mathbf{H} |^2 & \mathbf{C}\mathbf{H} \cdot \mathbf{C}\mathbf{V}^* \\
CV \cdot CH^* &  |\mathbf{C}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:eq:sar-pol-covmat-eq4}

Where CH and CV refer to dual polarization transmitting a circular polarized signal. \[CH, CV] can be replaced by \[LH, LV] or \[RH, RV] for left (L) or right (R) hand circular transmission respectively, although RCM will offer only right-hand circular transmission. The coherent HH-VV configuration available on TerraSAR-X could also be represented as C2 format.

Polarimetric decomposition methods like [@yamaguchi2011] for fully polarimetric, or m-chi [@raney2012] for compact polarimetric data, can be applied directly on averaged (speckle filtered) C3 and C2 matrices respectively. These decompositions enhance scattering information, bring it to a more comprehensible level to end-users, and raise the performance of thematic classification methodologies. For SAR products that were acquired with single polarization the use of the covariance matrix does not result in superfluous storage requirements, since only the matrix elements that are populated are retained and the diagonal matrix elements are the backscatter intensities. Thus, a single channel intensity product would yield only one matrix element and the storage needs would not change.

In order to ease the data structure and the metadata in between C3 and C2, [@eq:sar-pol-covmat-eq1] should be redefined as [@eq:sar-pol-covmat-eq5]. Users will have to take care of this non-standard representation when applying their polarimetric analytic tools. “\< \>” means that ARD matrix elements are speckle filtered. [@eq:sar-pol-covmat-eq5] is valid both for dual-linear and quad polarization.

$$
\text{C3 modified:} \quad C3_m = \begin{bmatrix}
| \langle \mathbf{H} \mathbf{H} |^2 \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \rangle\\
\langle HV \cdot HH^* \rangle & \langle|\mathbf{H}\mathbf{V}|^2 \rangle & \langle\mathbf{H}\mathbf{V} \cdot \mathbf{V}\mathbf{V}^* \rangle \\
\langle VV \cdot HH^* \rangle& \langle VV \cdot HV^* \rangle & \langle|\mathbf{V}\mathbf{V}|^2 \rangle
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq5}

Furthermore, for compact polarimetric data, it is recommended to store them, by simple transformation, under the circular-circular basis, since RR and RL polarizations ([@eq:sar-pol-covmat-eq6]) permit faster and more intuitive RGB visualizations (R=RR, G=RR/(RR+RL), B= RL).

$$
\text{CH-CV (C2 circular):} \quad C2_c = \begin{bmatrix}
\langle | \mathbf{R} \mathbf{R} |^2 \rangle & \langle\mathbf{R}\mathbf{R} \cdot \mathbf{R}\mathbf{¬}^* \rangle \\
\langle RL \cdot RR^* \rangle &  \langle|\mathbf{R}\mathbf{L}|^2\rangle
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq6}


### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/sar-orb-example.yaml-->Ocean Radar Backscatter example {#sec:annex-sar-orb-example label="|Ocean Radar Backscatter example"}

In contrast to NRB and POL, CEOS-ARD Ocean Radar Backscatter ORB products are geoid corrected and are provided in the Sigma-Nought (σE0) backscatter convention ([@fig:sar-orb-example-fig1a]), which is recommended for most ocean applications. In addition, availability of the “Local (or Ellipsoidal) Incidence Angle Image” ([@fig:sar-orb-example-fig1d]) and “Look Direction Image” per-pixel metadata are highly recommended (otherwise the general metadata “Look Direction Polynomials”) since they required for operational applications like ocean wind field estimates.

The following figures show Sentinel-1 ORB products of the Tropical Cyclone Harold passing Vanuatu on April 6, 2020:

![VV intensity; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-VV.png){#fig:sar-orb-example-fig1a}

![VH intensity; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-VH.png){#fig:sar-orb-example-fig1b}

![Data mask image; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-data-mask.png){#fig:sar-orb-example-fig1c}

![Local incident angle; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-local-indicident-angle.png){#fig:sar-orb-example-fig1d}

Another useful file is the “Mean Wind-Normalised Backscatter Measurements” ([@fig:sar-orb-example-fig2b]) which efficiently attenuates intensity variation along range and visually enhances oceanic features. This file is calculated as the ratio between the backscatter intensity and a simulated backscatter intensity image generated using an ocean surface wind model, like CMOD\_IRF2 [@quilfen1998] for VV polarization or CMOD\_IRF2K [@vachon2000] for HH polarization, and the SAR local incidence angle and the look direction information.

The following figures show Sentinel-1 EW ORB products:

![ORB intensity (Sigma-Nought); Processing: G. Hajduch (CLS)](assets/sar-orb-examples/S1-ORB-sigma-nought.png){#fig:sar-orb-example-fig2a}

![Intensity compensated with the “Mean Wind-Normalised Backscatter Measurement” (i.e., not Sigma-Nought) and geocoded; Processing: G. Hajduch (CLS)](assets/sar-orb-examples/S1-ORB-intesity-compensated.png){#fig:sar-orb-example-fig2b}


