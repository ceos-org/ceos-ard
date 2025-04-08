---
title: CEOS-ARD - Synthetic Aperture Radar - Polarimetric Radar
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

# CEOS-ARD - Synthetic Aperture Radar - Polarimetric Radar

&nbsp;

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

&nbsp;

**Product Family Specification:**
Synthetic Aperture Radar, Polarimetric Radar (SAR-POL)

**Applies to:**
This PFS is specifically aimed at users interested in exploring the potential of SAR but who may lack the expertise or facilities for SAR processing.

The CEOS-ARD Polarimetric Radar (POL) product format is an extension of the CEOS-ARD Normalised Radar Backscatter (NRB) format.
This extension is required in order to better support Level-1 SLC polarimetric data, including full-polarimetric modes (e.g., RADARSAT-2, ALOS-2/4, SAOCOM-1 and future missions), and hybrid or linear dual-polarimetric modes (i.e., Compact Polarimetric mode available on RCM, SAOCOM and the upcoming NISAR mission).

&#12;

## Document History

Not available yet

## Contributing Authors

- Alaska Satellite Facility, USA
  - Franz Meyer
  - Thomas Logan
- Collecte Localisation Satellites, France
  - Guillaume Hajduch
- CONAE, Argentina
  - Danilo Dadamia
- CSIRO, Australia
  - Zheng-Shu Zhou
- Digital Earth Africa, Australia
  - Fang Yuan
- Earth Big Data, USA
  - Josef Kellndorfer
- Environment and Climate Change, Canada
  - Benjamin Deschamps
- European Space Agency (ESA), Italy
  - Clément Albinet
  - Muriel Pinheiro
  - Nuno Miranda
- Geoscience Australia, Australia
  - Adam Lewis
  - Andreia Siqueira
  - Medhavy Thankappan
- German Aerospace Centre (DLR), Germany
  - Anna Wendleder
  - John Truckenbrodt
- ISRO, India
  - HariPriya Sakethapuram
- Japan Aerospace Exploration Agency, Japan
  - Takeo Tadono
- Jet Propulsion Laboratory, USA
  - Bruce Chapman
  - Gustavo Shiroma
  - Marco Lavalle
  - Virginia Brancato
- Natural Resources Canada, Canada
  - François Charbonneau
- RHEA, Italy
  - Antonio Valentino
- Sinergise, Slovenia
  - Marko Repse
- soloEO, Japan
  - Ake Rosenqvist
- Stanford University, USA
  - Howard Zebker
- University of Zurich, Switzerland
  - David Small

&#12;

## Glossary

ALE
:   Absolute geolocation error

ATBD
:   Algorithm Theoretical Basis Document

Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

CovMat
:   Normalised Radar Covariance Matrix

CRS
:   Coordinate Reference System

DEM
:   Digital Elevation Model

DOI
:   Digital Object Identifier

DSM
:   Digital Surface Model

EGM
:   Earth Gravitational Model

ENL
:   Equivalent Number of Looks

EPSG Code
:   An EPSG code is a unique identifier assigned to e.g. a specific coordinate reference system (CRS) by the European Petroleum Survey Group (EPSG).

GSLC
:   Geocoded Single-Look Complex

ISLR
:   Intensity Signal-to-Noise Level Ratio

LUT
:   Look-Up Table

Metadata
:   Structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content.

NRB
:   Normalised Radar Backscatter

ORB
:   Ocean Radar Backscatter

POL
:   Polarimetric Radar

PRD
:   Polarimetric Radar Decomposition

PSLR
:   Polarimetric Signal-to-Noise Level Ratio

RTC
:   Radiometrically Terrain Corrected

SAR
:   Synthetic Aperture Radar

SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

SLC
:   Single-Look Complex

STAC
:   SpatioTemporal Asset Catalog

UPS
:   Universal Polar Stereographic

URL
:   Uniform Resource Locator, a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.

UTC
:   Coordinated Universal Time

UTM
:   Universal Transverse Mercator

WGS84
:   World Geodetic System 1984

WKT
:   Well-Known Text (WKT) is a text markup language for representing vector geometry objects on a map, spatial reference systems of spatial objects, and transformations between spatial reference systems.
The formats were originally defined by the Open Geospatial Consortium (OGC) and described in their Simple Feature Access and Coordinate Transformation Service specifications.

&#12;

## Introduction

### What are CEOS Analysis Ready Data (CEOS-ARD) products? {#sec:intro-what-are-ceos-ard-products label="|What are CEOS Analysis Ready Data (CEOS-ARD) products?"}

CEOS-ARD products have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort.
These products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets.

CEOS-ARD are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, particularly time series analysis and multi-sensor application development.
They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures.
They may not be suitable for all purposes and are not intended as a _replacement_ for other types of satellite products.

### When can a product be called CEOS-ARD? {#sec:intro-when-is-a-product-ceos-ard label="|When can a product be called CEOS-ARD?"}

The CEOS-ARD branding is applied to a particular product once:

- that product has been assessed as meeting CEOS-ARD requirements by the agency or other entities responsible for production and distribution of the product, and
- that the assessment has been peer reviewed by the relevant CEOS team(s).

Agencies or other entities considering undertaking an assessment process should consult the [CEOS-ARD Governance Framework](https://ceos.org/ard/files/CEOS_ARD_Governance_Framework_18-October-2021.pdf) or contact <ard-contact@lists.ceos.org>.

A product can continue to use CEOS-ARD branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

### What is the difference between Threshold and Goal? {#sec:intro-difference-threshold-goal label="|What is the difference between Threshold and Goal?"}

**Threshold** (or: minimum) requirements are the **minimum** that is needed for the data to be analysis ready.
This must be practical and accepted by the data producers.

**Goal** (or: desired) requirements (previously referred to as “Target”) are the ideal; where we would like to be.
Some providers may already meet these.

Products that meet all _threshold_ requirements should be immediately useful for scientific analysis or decision-making.

Products that meet _goal_ requirements will reduce the overall product uncertainties and enhance broad-scale applications.
For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the _threshold_ level.

Goal requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field.
Over time, _goal_ specifications may (and subject to due process) become accepted as _threshold_ requirements.

### Which processing levels are defined in the CEOS-ARD Polarimetric Radar PFS? {#sec:intro-sar-pol-processing-levels label="|Which processing levels are defined in the CEOS-ARD Polarimetric Radar PFS?"}

The POL product can be defined in two processing levels:

The **normalised covariance matrix (CovMat)** representation (C2 or C3) which preserves the inter-channel polarimetric phase(s) and maximizes the available information for users.
Interoperability within current CEOS-ARD SAR backscatter definition is preserved, since diagonal elements of the covariance matrix are backscatter intensities.
Scattering information enhancement can be achieved by applying incoherent polarimetric decomposition techniques (e.g., Freeman-Durden, van Zyl, Cloude-Pottier, Yamaguchi-based) directly on the C2 or C3 matrix.

**Polarimetric Radar Decomposition (PRD)** refers to ARD products where polarimetric information is broken down into simplified parameters to facilitate user interpretation of the data.
They are derived from coherent or incoherent polarimetric decomposition techniques.

### Which limitations apply to CEOS-ARD Polarimetric Radar? {#sec:intro-sar-pol-limitations label="|Which limitations apply to CEOS-ARD Polarimetric Radar?"}

For Polarimetric Radar (POL) products, optimal incoherent Polarimetric Radar Decomposition (PRD) should be performed under the slant range projection [@gens2013; @toutin2013].
In order to minimise bias in the CEOS-ARD SAR Level-2A covariance matrix product, speckle filtering and averaging of the covariance matrix should be applied in the slant range projection, and geocoding should be performed using nearest-neighbour resampling.
Specifically, nearest-neighbour resampling ensures that the averaged covariance matrix elements in slant range and in geocoded ground projection are exactly the same.
Consequently, the polarimetrically derived parameters are exactly equal in both approaches (assuming that no further averaging is performed on the ARD product for decomposing the polarimetric information).
Bilinear and average resampling methods are also suitable for resampling the covariance matrix, but some differences with polarimetric parameters generated in slant range and then resampled (bilinear) might be observed on sloped terrains.
Even if Sinc interpolation may be more robust for spatial resampling, it does not preserve covariance matrix integrity, and should consequently not be used for this ARD product.

It is recommended that ARD providers who desire to distribute PRD products decompose the polarimetric information starting from Level-1 SLC data and then geocode the derived parameters rather than use the CovMat ARD product.
Resampling can be performed using any of the supported methods (nearest-neighbour, bilinear, average, bi-cubic spline or Lanczos are recommended), which need to be indicated in the product metadata.
Note that coherent decomposition techniques cannot be performed on CovMat ARD products.

Covariance matrix products contain a variable number of layers (or bands) with different data types depending on the polarimetric mode (full or dual) and decomposition technique.
The CovMat products for the C2 matrix have 3 layers (2 real-valued diagonal elements and 1 complex-valued off-diagonal element).
CovMat products for the C3 matrix have 6 layers (3 real-valued diagonal elements and 3 complex-valued off-diagonal elements).
Layers that can be obtained via a complex conjugation of other layers are not provided within the product.
Polarimetric Decomposition products contain typically 2 to 4 (or more) real-valued layers depending on the particular decomposition algorithm.
Within the CovMat product files, ARD layers are organized in order to reduce access delays and maximize efficiency in extracting the desired information.
In CovMat products, geographically contiguous samples for each layer may be stored next to each other and organized “layer by layer”.
Alternatively, samples belonging to the same covariance matrix might be stored next to each other and organized “matrix by matrix”.
PRD products are organized “layer by layer”, i.e., with bands corresponding to the output of the polarimetric decomposition stored next to each other.

&#12;

## Requirements

**WARNING:** The requirement numbers below are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided in brackets directly after the title.

<!-- todo: remove requirement numbers -->

### `1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### `1.1.` General Metadata: Traceability {#sec:meta.metadata-traceability-sar label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability-sar`


##### Threshold requirements:


*None*


##### Goal requirements:

Data must be traceable to SI reference standard.

Notes:

1. Relationship to [@sec:rcm.metadata-radiometric-accuracy]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

---

#### `1.2.` General Metadata: Metadata Machine Readability {#sec:meta.metadata-machine-readability label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta.metadata-machine-readability`


##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use.


##### Goal requirements:

Metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.1, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention, the Attribute Convention for Data Discovery (ACDD), etc.

---

#### `1.3.` General Metadata: Product Type {#sec:meta.metadata-product-type-sar label="|General Metadata: Product Type"}

Identifier: `meta.metadata-product-type-sar`


##### Threshold requirements:

CEOS-ARD product type name – or names in case of compliance with more than one product type – and, if required by the data provider, copyright.


##### Goal requirements:


*None*

---

#### `1.4.` General Metadata: Document Identifier {#sec:meta.metadata-pfs-url label="|General Metadata: Document Identifier"}

Identifier: `meta.metadata-pfs-url`


##### Threshold requirements:

Reference to CEOS-ARD PFS document as URL.


##### Goal requirements:


*None*

---

#### `1.5.` General Metadata: Data Collection Time {#sec:meta.metadata-time label="|General Metadata: Data Collection Time"}

Identifier: `meta.metadata-time`


##### Threshold requirements:

Number of source data acquisitions of the data collection is identified.
The start and stop UTC time of data collection is identified in the metadata, expressed in date/time.
In case of composite products, the dates/times of the first and last data takes and the per-pixel metadata [@sec:pxl.per-pixel-acquisition-id] is provided with the product.


##### Goal requirements:


*None*

### `2.` Source Metadata {#sec:src label="|Source Metadata"}

These are metadata records describing (detailing) **each** acquisition (source data) used to generate the ARD product.
This may be one or mutliple acquisitions.


#### `2.1.` Source Metadata: Sequential ID {#sec:src.metadata-sequential-id label="|Source Metadata: Sequential ID"}

Identifier: `src.metadata-sequential-id`


##### Threshold requirements:

Each acquisition is identified through a sequential identifier in the metadata, e.g. 1, 2, 3.


##### Goal requirements:


*None*

---

#### `2.2.` Source Metadata: Source Data Access {#sec:src.metadata-data-access-source label="|Source Metadata: Source Data Access"}

Identifier: `src.metadata-data-access-source`


##### Threshold requirements:

The metadata identifies the location from where the source data can be retrieved, expressed as a URL or DOI.


##### Goal requirements:

The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### `2.3.` Source Metadata: Instrument {#sec:src.metadata-instrument label="|Source Metadata: Instrument"}

Identifier: `src.metadata-instrument`


##### Threshold requirements:

The instrument used to collect the data is identified in the metadata:

- Satellite name
- Instrument name


##### Goal requirements:

A reference to the relevant [CEOS Missions, Instruments and Measurements Database](https://ceos.org/mim-database/) record.

---

#### `2.4.` Source Metadata: Source Data Acquisition Time {#sec:src.metadata-time-source label="|Source Metadata: Source Data Acquisition Time"}

Identifier: `src.metadata-time-source`


##### Threshold requirements:

The start date and time of source data is identified in the metadata, expressed in UTC in date and time, at least to the second.


##### Goal requirements:


*None*

---

#### `2.5.` Source Metadata: Source Data Acquisition Parameters {#sec:src.metadata-acquisition-parameters-sar label="|Source Metadata: Source Data Acquisition Parameters"}

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


*None*

---

#### `2.6.` Source Metadata: Orbit Information {#sec:src.metadata-orbit label="|Source Metadata: Orbit Information"}

Identifier: `src.metadata-orbit`


##### Threshold requirements:

Information related to the platform orbit used for data processing:

- Pass direction (asc/desc)[^orbit-pass-direction]
- Orbit data source (e.g., predicted, definite, precise, downlinked, etc.)

[^orbit-pass-direction]: For data crossing the North or South Pole, it is recommended to produce two distinct products and to use the appropriate “Pass direction” in each.


##### Goal requirements:

- Platform heading angle expressed in degrees (0-360) from North 
- Orbit data file containing state vectors (minimum of 5 state vectors, from 10% of scene length before start time to 10% of scene length after stop time) 
- Platform (mean) altitude

---

#### `2.7.` Source Metadata: Processing Parameters {#sec:src.metadata-processing-parameters label="|Source Metadata: Processing Parameters"}

Identifier: `src.metadata-processing-parameters`


##### Threshold requirements:

Processing parameters details of the data:

- Processing facility
- Processing date
- Software version
- Product level
- Product ID (file name)
- Azimuth number of looks
- Range number of looks (separate values for each beam, as necessary)


##### Goal requirements:

Additional relevant processing parameters, e.g., range- and azimuth look bandwidth and LUT applied.

---

#### `2.8.` Source Metadata: Source Data Image Attributes {#sec:src.metadata-image-attributes-sar label="|Source Metadata: Source Data Image Attributes"}

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

#### `2.9.` Source Metadata: Sensor Calibration {#sec:src.metadata-sensor-calibration label="|Source Metadata: Sensor Calibration"}

Identifier: `src.metadata-sensor-calibration`


##### Threshold requirements:


*None*


##### Goal requirements:

Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata.
Ideally this would support machine-to-machine access.

---

#### `2.10.` Source Metadata: Performance Indicators {#sec:src.metadata-performance-indicators label="|Source Metadata: Performance Indicators"}

Identifier: `src.metadata-performance-indicators`


##### Threshold requirements:

Provide performance indicators on data intensity noise level ($\text{NE}\sigma^0$ and/or $\text{NE}\beta^0$ and/or $\text{NE}\gamma^0$, i.e., noise equivalent Sigma- and/or Beta- and/or Gamma-Nought).
Provided for each polarization channel when available.
Parameter may be expressed as the mean and/or minimum and maximum noise equivalent values of the data. 
Values do not need to be estimated individually for each product, but may be estimated once for each acquisition mode, and annotated on all products.


##### Goal requirements:

Provide additional relevant performance indicators (e.g., ENL, PSLR, ISLR, and performance reference DOI or URL).

---

#### `2.11.` Source Metadata: Polarimetric Calibration Matrices {#sec:src.metadata-polarimetric-calibration-matrices label="|Source Metadata: Polarimetric Calibration Matrices"}

Identifier: `src.metadata-polarimetric-calibration-matrices`


##### Threshold requirements:


*None*


##### Goal requirements:

The complex-valued polarimetric distortion matrices with the channel imbalance and the cross-talk applied for the polarimetric calibration.

---

#### `2.12.` Source Metadata: Mean Faraday Rotation Angle {#sec:src.metadata-mean-faraday-rotation-angle label="|Source Metadata: Mean Faraday Rotation Angle"}

Identifier: `src.metadata-mean-faraday-rotation-angle`


##### Threshold requirements:


*None*


##### Goal requirements:

The mean Faraday rotation angle estimated from the polarimetric data and/or from models with reference to the method or paper used to derive the estimate.

---

#### `2.13.` Source Metadata: Ionosphere Indicator {#sec:src.metadata-ionosphere-indicator label="|Source Metadata: Ionosphere Indicator"}

Identifier: `src.metadata-ionosphere-indicator`


##### Threshold requirements:


*None*


##### Goal requirements:

Flag indicating whether the backscatter imagery is “significantly impacted” by the ionosphere (0 – false, 1 – true).
Significant impact would imply that the ionospheric impact on the backscatter exceeds the radiometric calibration requirement or goal for the imagery.

### `3.` Product Metadata {#sec:prd label="|Product Metadata"}

Information related to the CEOS-ARD product generation procedure and geographic parameters.


#### `3.1.` Product Metadata: Product Data Access {#sec:prd.metadata-data-access-product label="|Product Metadata: Product Data Access"}

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

#### `3.2.` Product Metadata: Auxiliary Data {#sec:prd.metadata-auxiliary-data label="|Product Metadata: Auxiliary Data"}

Identifier: `prd.metadata-auxiliary-data`


##### Threshold requirements:


*None*


##### Goal requirements:

The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as DOIs.

Notes:

1. Auxiliary data includes DEMs, etc., and any additional data sources used in the generation of the product.

---

#### `3.3.` Product Metadata: Sample Spacing {#sec:prd.metadata-sample-spacing label="|Product Metadata: Sample Spacing"}

Identifier: `prd.metadata-sample-spacing`


##### Threshold requirements:

Product processing parameters details:

- Pixel (column) spacing
- Line (row) spacing


##### Goal requirements:


*None*

---

#### `3.4.` Product Metadata: Equivalent Number of Looks {#sec:prd.metadata-enl label="|Product Metadata: Equivalent Number of Looks"}

Identifier: `prd.metadata-enl`


##### Threshold requirements:


*None*


##### Goal requirements:

Equivalent Number of Looks (ENL)

---

#### `3.5.` Product Metadata: Resolution {#sec:prd.metadata-resolution label="|Product Metadata: Resolution"}

Identifier: `prd.metadata-resolution`


##### Threshold requirements:


*None*


##### Goal requirements:

Average spatial resolution along:

- Columns
- Rows

---

#### `3.6.` Product Metadata: Speckle Filtering {#sec:prd.metadata-speckle-filtering label="|Product Metadata: Speckle Filtering"}

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


*None*

---

#### `3.7.` Product Metadata: Polarimetric Filtering {#sec:prd.metadata-pol-filtering label="|Product Metadata: Polarimetric Filtering"}

Identifier: `prd.metadata-pol-filtering`


##### Threshold requirements:

Advanced polarimetric filter preserving covariance matrix properties should be applied.


##### Goal requirements:


*None*

---

#### `3.8.` Product Metadata: Bounding Box {#sec:prd.metadata-bounding-box label="|Product Metadata: Bounding Box"}

Identifier: `prd.metadata-bounding-box`


##### Threshold requirements:

Two opposite corners of the measurement file (bounding box, including any zero-fill values) are identified,
expressed in the coordinate reference system defined in [@sec:prd.metadata-crs].

Notes:

1. Four corners of the measurement file are recommended for scenes crossing the Antemeridian, or the North or the South Pole.


##### Goal requirements:


*None*

---

#### `3.9.` Product Metadata: Geographical Extent {#sec:prd.metadata-footprint label="|Product Metadata: Geographical Extent"}

Identifier: `prd.metadata-footprint`


##### Threshold requirements:

The geometry of the image footprint expressed in WGS84, in a standardised format (e.g., WKT Polygon).


##### Goal requirements:


*None*

---

#### `3.10.` Product Metadata: Image Size {#sec:prd.metadata-image-size label="|Product Metadata: Image Size"}

Identifier: `prd.metadata-image-size`


##### Threshold requirements:

Image attributes:

- Number of lines
- Number of pixels per line
- File header size (if applicable)
- Number of no-data border pixels (if applicable)


##### Goal requirements:


*None*

---

#### `3.11.` Product Metadata: Pixel Coordinate Convention {#sec:prd.metadata-pixel-coordinate-convention label="|Product Metadata: Pixel Coordinate Convention"}

Identifier: `prd.metadata-pixel-coordinate-convention`


##### Threshold requirements:

Coordinate referring to the centre, the upper left corner, or the lower left corner of a pixel.
Values are [pixel centre, pixel ULC or pixel LLC].


##### Goal requirements:


*None*

---

#### `3.12.` Product Metadata: Coordinate Reference System {#sec:prd.metadata-crs label="|Product Metadata: Coordinate Reference System"}

Identifier: `prd.metadata-crs`


##### Threshold requirements:

The metadata lists the map projection (or geographical coordinates, if applicable) that was used and any relevant parameters required to geolocate data in that map projection, expressed in a standardised format (e.g., WKT).  
Indicate EPSG code, if defined for the CRS.


##### Goal requirements:


*None*

### `4.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.


#### `4.1.` Per-Pixel Metadata: Cloud Optimized Formats {#sec:pxl.cloud-optimized-formats label="|Per-Pixel Metadata: Cloud Optimized Formats"}

Identifier: `pxl.cloud-optimized-formats`


##### Threshold requirements:


*None*


##### Goal requirements:

All files are provided using cloud-optimized file formats.

---

#### `4.2.` Per-Pixel Metadata: Metadata Machine Readability {#sec:pxl.metadata-machine-readability label="|Per-Pixel Metadata: Metadata Machine Readability"}

Identifier: `pxl.metadata-machine-readability`


##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use.


##### Goal requirements:

Metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.1, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention, the Attribute Convention for Data Discovery (ACDD), etc.

---

#### `4.3.` Per-Pixel Metadata: Data Mask Image {#sec:pxl.per-pixel-data-mask label="|Per-Pixel Metadata: Data Mask Image"}

Identifier: `pxl.per-pixel-data-mask`


##### Threshold requirements:

Mask image indicating:

- Valid data
- Invalid data
- No data

File format specifications/contents provided in metadata:

- Sample Type (Mask)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
- Bit Value Representation


##### Goal requirements:

Additional bit value representations, e.g.:

- Layover (masked as invalid data in threshold)
- Radar shadow (masked as invalid data in threshold)
- Ocean water
- Land (recommended for ORB)
- RTC applied (e.g., for maritime scenes with land samples for which RTC has been applied)
- DEM gap filling (i.e., interpolated DEM over gaps)

---

#### `4.4.` Per-Pixel Metadata: Scattering Area Image {#sec:pxl.per-pixel-scattering-area label="|Per-Pixel Metadata: Scattering Area Image"}

Identifier: `pxl.per-pixel-scattering-area`


**Usage: Recommended for scenes that include land areas.**

##### Threshold requirements:


*None*


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

#### `4.5.` Per-Pixel Metadata: Local Incident Angle Image {#sec:pxl.per-pixel-local-incident-angle label="|Per-Pixel Metadata: Local Incident Angle Image"}

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

1. For maritime ORB scenes when no land areas are covered, a geoid model could be used for the calculation of the local incident angle


##### Goal requirements:


*None*

---

#### `4.6.` Per-Pixel Metadata: Ellipsoidal Incident Angle Image {#sec:pxl.per-pixel-ellipsoidal-incident-angle label="|Per-Pixel Metadata: Ellipsoidal Incident Angle Image"}

Identifier: `pxl.per-pixel-ellipsoidal-incident-angle`


##### Threshold requirements:

Ellipsoidal incident angle is provided.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
- Reference Ellipsoid Name

Notes:

1. For maritime ORB scenes when no land areas are covered, a geoid model could be used for the calculation of the local incident angle


##### Goal requirements:


*None*

---

#### `4.7.` Per-Pixel Metadata: Noise Power Image {#sec:pxl.per-pixel-noise-power label="|Per-Pixel Metadata: Noise Power Image"}

Identifier: `pxl.per-pixel-noise-power`


##### Threshold requirements:


*None*


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

#### `4.8.` Per-Pixel Metadata: Gamma-to-Sigma Ratio Image {#sec:pxl.per-pixel-gamma-sigma-ratio label="|Per-Pixel Metadata: Gamma-to-Sigma Ratio Image"}

Identifier: `pxl.per-pixel-gamma-sigma-ratio`


##### Threshold requirements:


*None*


##### Goal requirements:

Ratio of the integrated area in the Gamma projection over the integrated area 
in the Sigma projection (ground). Multiplying RTC $\gamma^0_T$ by this ratio results in an 
estimate of RTC $\sigma^0_T$.

File format specifications/contents provided in metadata:

- Sample Type (Ratio)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### `4.9.` Per-Pixel Metadata: Acquisition ID Image {#sec:pxl.per-pixel-acquisition-id label="|Per-Pixel Metadata: Acquisition ID Image"}

Identifier: `pxl.per-pixel-acquisition-id`


##### Threshold requirements:

**Required for multi-source product only.**

Acquisition ID, or acquisition date, for each pixel is identified.

In case of multi-temporal image stacks, use source acquisition ID (i.e., [@sec:src.metadata-sequential-id]) to list contributing images.

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

#### `4.10.` Per-Pixel Metadata: DEM {#sec:pxl.per-pixel-dem label="|Per-Pixel Metadata: DEM"}

Identifier: `pxl.per-pixel-dem`


##### Threshold requirements:


*None*


##### Goal requirements:

Provide DEM or DSM as used during the geometric and radiometric processing of the SAR data, resampled to an exact geometric match in extent and resolution with the image product.

Can also be provided with ORB products containing land areas.

File format specifications/contents provided in metadata:

- Sample Type (Height)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

### `5.` Radiometrically Corrected Measurements {#sec:rcm label="|Radiometrically Corrected Measurements"}

The requirements indicate the necessary outcomes and, to some degree, the minimum steps necessary to be deemed to have achieved those outcomes.
Radiometric corrections must lead to normalised measurement(s) of backscatter intensity and/or decomposed polarimetric parameters.
As for the per-pixel metadata, information regarding data format specification needs to be provided for each record.
The requirements below must be met for all pixels/samples/observations in a collection.


#### `5.1.` Radiometrically Corrected Measurements: Cloud Optimized Formats {#sec:rcm.cloud-optimized-formats label="|Radiometrically Corrected Measurements: Cloud Optimized Formats"}

Identifier: `rcm.cloud-optimized-formats`


##### Threshold requirements:


*None*


##### Goal requirements:

All files are provided using cloud-optimized file formats.

---

#### `5.2.` Radiometrically Corrected Measurements: Backscatter Measurements \[POL] {#sec:rcm.measurements-backscatter-pol label="|Radiometrically Corrected Measurements: Backscatter Measurements \[POL]"}

Identifier: `rcm.measurements-backscatter-pol`


##### Threshold requirements:

Measurements can be one of the following types or both: 
  
- **Normalised Radar Covariance Matrix (CovMat)**
  Diagonal (equivalent to NRB) and upper diagonal elements of the terrain-flattened Gamma-Nought ($\gamma^0_T$) Covariance Matrix are provided for coherent dual (e.g., HH-HV, VV-VH, or …) and fully polarimetric (e.g., HH-HV-VH-VV) acquisitions.
- **Polarimetric Radar Decomposition (PRD)**
  The individual components of the polarimetric decomposition obtained from the terrain-flattened (Gamma-Nought, $\gamma^0_T$) covariance matrix.

File format specifications/contents provided in metadata:

- Measurement Type (CovMat, PRD)
- Measurement convention unit (linear amplitude, linear power, angle)
- Individual covariance matrix element or/and Individual component of the decomposition (C3m11, C3m12, … or H, A, alpha, or …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Notes:

1. It is recommended to keep CovMat or PRD measurement files separated.
Otherwise, specify the multi-channel format order (BIP, BIL, BSQ).


##### Goal requirements:


*None*

---

#### `5.3.` Radiometrically Corrected Measurements: Scaling Conversion {#sec:rcm.metadata-scaling-conversion label="|Radiometrically Corrected Measurements: Scaling Conversion"}

Identifier: `rcm.metadata-scaling-conversion`


##### Threshold requirements:

If applicable, indicate the equation to convert pixel linear amplitude/power to logarithmic decibel scale, including, if applicable, the associated calibration (dB offset) factor, and/or the equation used to convert compressed data (int8/int16/float16) to float32.


##### Goal requirements:

Use of float32.

---

#### `5.4.` Radiometrically Corrected Measurements: Noise Removal {#sec:rcm.metadata-noise-removal label="|Radiometrically Corrected Measurements: Noise Removal"}

Identifier: `rcm.metadata-noise-removal`


##### Threshold requirements:

Flag if noise removal has been applied (Y/N).
Metadata should include the noise removal algorithm and reference to the algorithm as URL or DOI.

Notes:

1. Thermal noise removal and image border noise removal to remove overall scene noise and scene edge artefacts, respectively.


##### Goal requirements:


*None*

---

#### `5.5.` Radiometrically Corrected Measurements: Radiometric Terrain Correction Algorithm {#sec:rcm.corrections-radiometric-terrain-correction label="|Radiometrically Corrected Measurements: Radiometric Terrain Correction Algorithm"}

Identifier: `rcm.corrections-radiometric-terrain-correction`


##### Threshold requirements:

Adjustments were made for terrain by modelling the local contributing scattering area using the preferred choice of a published peer-reviewed algorithm to produce radiometrically terrain corrected (RTC) $\gamma^0_T$ backscatter estimates.  

Metadata references, e.g.

- a citable peer-reviewed algorithm
- technical documentation regarding the algorithm used to generate the backscatter estimates is expressed as URLs or DOIs 
- the sources of auxiliary data used to make corrections

Notes:

1. Examples of technical documentation include an Algorithm, Theoretical Basis Document, product user guide, etc.


##### Goal requirements:


*None*

---

#### `5.6.` Radiometrically Corrected Measurements: Radiometric Accuracy {#sec:rcm.metadata-radiometric-accuracy label="|Radiometrically Corrected Measurements: Radiometric Accuracy"}

Identifier: `rcm.metadata-radiometric-accuracy`


##### Threshold requirements:


*None*


##### Goal requirements:

Uncertainty (e.g., bounds on $\gamma^0$ or $\sigma^0$) information is provided as document referenced as URL or DOI.
SI traceability is achieved.

---

#### `5.7.` Radiometrically Corrected Measurements: Flattened Phase {#sec:rcm.measurements-flattened-phase label="|Radiometrically Corrected Measurements: Flattened Phase"}

Identifier: `rcm.measurements-flattened-phase`


**Usage: Alternative to GSLC product for NRB and POL products**

##### Threshold requirements:


*None*


##### Goal requirements:

The Flattened Phase is the interferometric phase for which the topographic phase contribution is removed.
It is derived from the range-Doppler SLC product using a DEM and the orbital state vectors with respect to a reference orbit (see [@sec:annex-sar-topographic-phase-removal]).
The use of the Flattened Phase with the NRB or POL intensity ([@sec:rcm]) provides the GSLC equivalent, as follows:  

$$
\text{GSLC} = \sqrt{NRB} \times \exp(j \cdot \text{FlattenPhase})
$$

File format specifications/contents provided in metadata:

- Measurement Type (Flattened Phase)
- Reference Polarization (HH/HV/VV/VH)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

In case of polarimetric data, indicate the reference polarization.

### `6.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### `6.1.` Geometric Corrections: Geometric Correction Algorithm {#sec:gcor.metadata-geometric-correction-algorithm label="|Geometric Corrections: Geometric Correction Algorithm"}

Identifier: `gcor.metadata-geometric-correction-algorithm`


##### Threshold requirements:


*None*


##### Goal requirements:

Metadata references, e.g.: 
- A metadata citable peer-reviewed algorithm
- Technical documentation regarding the implementation of that algorithm expressed as URLs or DOIs
- The sources of auxiliary data used to make corrections
- Resampling method used for geometric processing of the source data

Notes:

1. Examples of technical documentation can include e.g., an Algorithm Theoretical Basis Document (ATBD) or a product user guide.

---

#### `6.2.` Geometric Corrections: Digital Elevation Model {#sec:gcor.corrections-dem label="|Geometric Corrections: Digital Elevation Model"}

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

#### `6.3.` Geometric Corrections: Geometric Accuracy {#sec:gcor.corrections-geometric-accuracy-radar label="|Geometric Corrections: Geometric Accuracy"}

Identifier: `gcor.corrections-geometric-accuracy-radar`


##### Threshold requirements:

Accurate geolocation is a prerequisite to radar processing to correct for terrain and to enable interoperability between radar sensors.

The absolute geolocation error (ALE) for a sensor is typically assessed through analysis of Single Look Complex (SLC) imagery and measured along the slant range and azimuth directions (case A: SLC ALE).

The end-to-end “ARD” ALE of the final product could be measured directly in the final image product in the chosen map projection, i.e., in the map coordinate directions: e.g., Northing and Easting (case B: ARD ALE).

Providing accuracy estimates based on measurements following at least one scheme (A or B or both) meets the threshold requirement.

Estimates of the ALE is provided as a bias and a standard deviation, with (Case A) SLC ALE expressed in slant range and azimuth, and (Case B) ARD ALE expressed in map projection dimensions.

Notes:

1. This assessment is often made through comparison of measured corner reflector positions with their projected location in the imagery. In some cases, other mission calibration/validation results may be used.
2. The ALE is not typically assessed for every processed image, but through an ALE assessment by the data processing team characterizing all or (usually a subset) of the generated products.


##### Goal requirements:

Output product sub-sample accuracy should be less than or equal to 0.1 (slant range) pixel radial root mean square error (rRMSE). 
Provide documentation of estimates of ALE as DOI or URL.

---

#### `6.4.` Geometric Corrections: Geometric Refined Accuracy {#sec:gcor.corrections-geometric-refined-accuracy label="|Geometric Corrections: Geometric Refined Accuracy"}

Identifier: `gcor.corrections-geometric-refined-accuracy`


##### Threshold requirements:


*None*


##### Goal requirements:

Values provided under [@sec:gcor.corrections-geometric-accuracy-radar] are provided by the SAR mission Cal/Val team.

CEOS-ARD processing steps could include method refining the geometric accuracy, such as cross-correlation of the SAR data in slant range with a SAR scene simulated from a DSM or DEM.

Methodology used (name and reference), quality flag, geometric standard deviation values should be provided.

---

#### `6.5.` Geometric Corrections: Gridding Convention {#sec:gcor.corrections-gridding-convention label="|Geometric Corrections: Gridding Convention"}

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


## References

::: {#refs}
:::

&#12;

## Annexes

### General Processing Roadmap {#sec:annex-sar-general-processing-roadmap label="|General Processing Roadmap"}

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

### Topographic phase removal {#sec:annex-sar-topographic-phase-removal label="|Topographic phase removal"}

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

### Normalised Covariance Matrices (CovMat) {#sec:annex-sar-pol-covmat label="|Normalised Covariance Matrices (CovMat)"}

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

### Polarimetric Radar Decomposition (PRD) {#sec:annex-sar-pol-prd label="|Polarimetric Radar Decomposition (PRD)"}

Different methodologies allow decomposition of coherent dual-polarization data or fully polarimetric data to meaningful components summarizing the scattering processing with the interacting media. Decomposition techniques are divided in two categories: Coherent and incoherent.

#### Coherent decompositions

Coherent decompositions express the scattering matrix by the summation of elementary objects of known signature (ex.: a sphere, a diplane, a cylinder, a helix, …). They are used mainly to describe point targets which are coherent. As for examples, coherent PRD could be (but not limited to):

1. Pauli decomposition (3 layers)
   - $|\alpha|^2$: sphere (odd-bounce interaction) \[Intensity]
   - $|\beta|^2$: 0° diplane (even-bounce interaction) \[Intensity]
   - $|\gamma|^2$: 45° diplane (volumetric interaction) \[Intensity]
2. Krogager decomposition (5 layers) [@krogager1993]
   - $|\kappa_\sigma|^2$ : sphere (odd-bounce interaction) \[Intensity]
   - $|\kappa_\delta|^2$ : diplane (odd-bounce interaction) \[Intensity]
   - $|\kappa_\eta|^2$ : helix \[Intensity]
   - $\theta$: orientation angle \[degrees]
   - $\Phi_s$: sphere to diplane angle \[degrees]
3. Cameron (nine classes) – non-dimensional layers [@cameron1996]
   
   | Classes         |  ID  |
   | :-------------- | :--: |
   | Trihedral       |  1   |
   | Dihedral        |  2   |
   | Narrow Dihedral |  3   |
   | Dipole          |  4   |
   | Cylinder        |  5   |
   | ¼ wave          |  6   |
   | Right Helix     |  7   |
   | Left Helix      |  8   |
   | Asymmetrical    |  9   |

   : Classification of Non-Dimensional Layers {#tbl:sar-pol-prd-tbl1}

#### Incoherent decompositions

Incoherent decompositions describe distributed targets in terms of scattering mechanisms and their diversity. They are generated from averaged Covariance, Coherence or Kennaugh matrices. As for examples, incoherent PRD could be (but not limited to):

1. Based and saved on intensity of scattering mechanisms can be [@freeman1998; @yamaguchi2011; @raney2012]
   
   | Level 2b - Layers [Intensity]  | Freeman-Durden | Yamaguchi | m-chi |
   | :----------------------------- | :------------: | :-------: | :---: |
   | Odd-bounce (surface/trihedral) |       X        |     X     |   X   |
   | Even-bounce (dihedral)         |       X        |     X     |   X   |
   | Random (volumetric)            |       X        |     X     |   X   |
   | Helix                          |                |     X     |       |

   : Incoherent Decompositions: Freeman-Durden, Yamaguchi, m-chi {#tbl:sar-pol-prd-tbl2}
   
2. Based on eigenvector-eigenvalue decomposition expressing the diversity of scattering mechanisms [@cloude1996] and types:
   
   - $H$ : Entropy \[ \]  is the polarization diversity
   - $A$ : Anisotropy \[ \]  is weighted difference between the 2ⁿᵈ and 3ʳᵈ eigenvalues
   - $\alpha$ : Odd-even bounce angle \[Degrees]
   - $\beta$ : orientation angle \[Degrees]

### Polarimetric Radar Decomposition Product Examples {#sec:annex-sar-pol-examples label="|Polarimetric Radar Decomposition Product Examples"}

From fully polarimetric covariance matrix ARD format POL (Level-2a), it is possible to apply any version of the popular Yamaguchi methodology, which decomposes the polarimetric information under relative intensities of 4 scattering types: Odd bounce, Even bounce, Random (volume) and helix. [@fig:sar-pol-examples-fig1]b shows HH intensity of a RADARSAT fully polarimetric acquired over a Spanish area. Decomposition using Yamaguchi methodology [@yamaguchi2011] can be expressed in RGB colour composite ([@fig:sar-pol-examples-fig1]c) where Red channel refers to even bounce scattering like urban area; Green channel is random scattering like vegetation; and Blue channel is odd bounce scattering like bare soil. [@fig:sar-pol-examples-fig1]d is equivalent to c) where radiometric normalisation (terrain flattening) has been applied with the help of the DEM of the scene ([@fig:sar-pol-examples-fig1]a).

![Example of polarimetric decomposition generated from ARD covariance format. a) Shaded DEM of the area; b) RADARSAT-2 HH intensity; c) Yamaguchi decomposition colour composite (Red: even bounce, Green: random, Blue: odd bounce); d) Same as c) with terrain flattening option. Generated from Radarsat-2 FQ18W acquired over Murcia, Spain on 18 June 2014 - ©MDA 2014](assets/sar-pol-examples/pol-decomposition.jpeg){#fig:sar-pol-examples-fig1}

[@fig:sar-pol-examples-fig2] is a PRD compact polarimetric m-chi decomposition [@raney2012] simulated from two Canadian prairies Radarsat-2 fully polarimetric scenes acquired in May and June 2012. In May, before the growing season [@fig:sar-pol-examples-fig2]a, m-chi shows mainly surface scattering from bare soil (blue channel) and vegetation interaction from forested areas (green channel), while in June [@fig:sar-pol-examples-fig2]b growth of vegetation modifies the radar signal with interacting media function of the vegetation density and geometry which increase the amount of even bounce (red channel) and random scattering.

![m-chi decomposition colour composite of simulated compact polarimetry from Radarsat-2 over an agriculture area. RGB representation: Red: even bounce, Green: random, Blue: odd bounce. a) 3 May 2012; and b) 18 June 2012. Generated from Radarsat-2 FQ6W acquired over SMAPVEX12 campaign Manitoba, Canada on 3 May and 20 June 2012 - ©MDA 2012](assets/sar-pol-examples/m-chi-decomposition.jpeg){#fig:sar-pol-examples-fig2}


