---
title: >-
  CEOS-ARD - Synthetic Aperture Radar - Interferometric SAR - Version 2.0.0-draft
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

# CEOS-ARD - Synthetic Aperture Radar - Interferometric SAR

&nbsp;

## Draft Version

This is a draft version.
Please visit the [CEOS-ARD website](https://ceos.org/ard) for the latest endorsed version of this document.

## Document Status

Product Family Specification, Synthetic Aperture Radar, Interferometric SAR

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

### 2026-07-20 (MINOR)

- The Combined SAR PFS has been split into separate PFS per product type
- Restructured the document; various minor editorial changes; removed empty, irrelevant, or unused parts - many of the changes resulted from the split
- Numerical identifiers were rotated and are deprecated; new textual identifiers have been added
- Moved the Background paragraph about the commonalities and differences in the SAR PFSes to the Introduction
- Requirement "Document identifier": Removed the trailing “for Synthetic Aperture Radar”
- Requirement "Radar Unit Look Vector Grid Image" and "Slant Range Sensor to Surface Image": Integrated the conditional "In the case of \[InSAR] product, \[...] of the reference acquisition." directly into the first paragraph with the addition of "of the reference acquisition".
- Requirement "InSAR Phase Uncertainty Image" and following: The order of the "File format specifications/contents" has changed in some cases; Removed “(for [InSAR] product only)” from "insarID number" entry; Added a reference back to “InSAR Pair” requirement.
- Requirement category "CEOS-ARD Product Data Attributes" renamed to “Product Metadata”; Requirement "Source Data Attributes" renamed to “Source Metadata”. Adapted descriptions accordingly.
- Requirement category "Source Data Attributes": Moved the information about sequential acquisition identifiers to a new threshold requirement “Acquisition ID”. Adapted category description accordingly.
- The subcategories for Source and Product metadata have been flattened into top-level categories
- Annex has been reformatted and updated as required by the split
- Document history has been reset. Check the previous versions for details

**Note:** This document is the successor of the former [CEOS-ARD for SAR PFS v1.3.1](https://ceos.org/ard/files/PFS/SAR/v1.3.1/CEOS-ARD_PFS_SAR_v1.3.1.pdf) for product type **Interferometric SAR (InSAR)**.

**Justification:**
Migration to building blocks.

**Editor:** Matthias Mohr


## Contributing Authors

- François Charbonneau, Natural Resources Canada, Canada
- Ake Rosenqvist, soloEO / Japan Aerospace Exploration Agency, Japan
- John Truckenbrodt, German Aerospace Centre (DLR), Germany
- Clément Albinet, European Space Agency (ESA), Italy
- David Small, University of Zurich, Switzerland
- Bruce Chapman, Jet Propulsion Laboratory, USA
- Howard Zebker, Stanford University, USA
- Zheng-Shu Zhou, CSIRO, Australia
- Kimberlee Baldry, Geoscience Australia, Australia
- David Bekaert, Jet Propulsion Laboratory, USA
- Virginia Brancato, Jet Propulsion Laboratory, USA
- Danilo Dadamia, CONAE, Argentina
- Benjamin Deschamps, Environment and Climate Change, Canada
- Matt Garthwaite, CSIRO, Australia
- Guillaume Hajduch, Collecte Localisation Satellites, France
- Jayasri Poludasu, ISRO, India
- Josef Kellndorfer, Earth Big Data, USA
- Joseph Kennedy, Alaska Satellite Facility, USA
- Marco Lavalle, Jet Propulsion Laboratory, USA
- Thomas Logan, Alaska Satellite Facility, USA
- Franz Meyer, Alaska Satellite Facility, USA
- Nuno Miranda, European Space Agency (ESA), Italy
- Matthias Mohr, moreGeo GmbH, Germany
- Muriel Pinheiro, European Space Agency (ESA), Italy
- Marko Repse, Sinergise, Slovenia
- HariPriya Sakethapuram, ISRO, India
- Gustavo H. X. Shiroma, Jet Propulsion Laboratory, USA
- Usha Sundari, ISRO, India
- Andreia Siqueira, Geoscience Australia, Australia
- Scott Staniewicz, Jet Propulsion Laboratory, USA
- Takeo Tadono, Japan Aerospace Exploration Agency, Japan
- Medhavy Thankappan, Geoscience Australia, Australia
- Antonio Valentino, Starion for European Space Agency (ESA), Italy
- Anna Wendleder, German Aerospace Centre (DLR), Germany
- Fang Yuan, Digital Earth Africa, Australia
- Francesco De Zan, Delta-Phi Remote Sensing GmbH, Germany

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

**Product Family Specification:**
Synthetic Aperture Radar, Interferometric SAR (INSAR)

**Version:**
2.0.0-draft

**Applies to:**
Data collected by Synthetic Aperture Radar sensors


## Background

This PFS is specifically aimed at users interested in exploring the potential of SAR but who may lack the expertise or facilities for SAR processing.

The CEOS-ARD Interferometric SAR (InSAR) product format specification describes products resulting from InSAR processing steps.
Two levels of product categories are supported:
1) The first level includes InSAR coherence and wrapped interferogram images derived from a pair (or several pairs) of SLC or GSLC source data listed in the product metadata file. The product metadata file reports the processing information (parameters and methods) used to produce them. The PFS also supports unwrapped interferograms, but their inclusion is not a threshold requirement for this product level. An InSAR pair identification label allows support of InSAR time series products derived from several repeated pass SAR source combinations. A Boolean flag is used to indicate whether the interferometric phases due to Earth curvature and to the surface topography are removed from interferograms. This InSAR product level can then serve as input in temporal coherence analysis techniques or as input in production of time series displacement products by distributed target approaches like Small BAseline Subset (SBAS) technique [@lanari2004].
2) InSAR displacement belongs to the second level of InSAR products. Displacement products can be expressed as InSAR displacement from a pair of SAR acquisitions and/or from a time series of SAR acquisitions, as a displacement and/or as displacement rate products over a time period. Since several different InSAR displacement approaches exist in the literature for which, each have their own criteria and parameters, it is not possible to prescribe specific metadata details. Nonetheless, it is required that main processing steps (with reference to methodologies), with their chosen parameters (criteria like statistical thresholds and estimation window sizes) are well defined in the displacement product metadata, in order to preserve traceability for the end users. For InSAR displacement products generated from first level CEOS-ARD InSAR, listed “source” products in the metadata can refer to those first level CEOS-ARD InSAR described above. In accordance with other CEOS-ARD products, per-pixel metadata and data are terrain geocoded products.

&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/acdd.yaml -->
ACDD
:   Attribute Convention for Data Discovery as defined by Earth Science Information Partners (ESIP)

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ale.yaml -->
ALE
:   Absolute Geolocation Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/atbd.yaml -->
ATBD
:   Algorithm Theoretical Basis Document

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/auxiliary-data.yaml -->
Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/cb.yaml -->
CB
:   Composite Backscatter

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ceos-ard.yaml -->
CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/composite-product.yaml -->
Composite Product
:   Product where samples (or pixels) are generated from more than one input data source, e.g. by local resolution weighting or by backscatter averaging.

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

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ecef.yaml -->
ECEF
:   Earth-Centred Earth-Fixed

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ecr.yaml -->
ECR
:   Earth-Centred Rotating

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/egm.yaml -->
EGM
:   Earth Gravitational Model

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/enl.yaml -->
ENL
:   Equivalent Number of Looks

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/epsg-code.yaml -->
EPSG Code
:   An EPSG code is a unique identifier assigned to e.g. a specific coordinate reference system (CRS) by the European Petroleum Survey Group (EPSG).

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/fft.yaml -->
FFT
:   Fast Fourier Transform

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gcp.yaml -->
GCP
:   Ground Control Point

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gslc.yaml -->
GSLC
:   Geocoded Single-Look Complex

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/insar.yaml -->
InSAR
:   Interferometric Radar

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/islr.yaml -->
ISLR
:   Intensity Signal-to-Noise Level Ratio

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/lut.yaml -->
LUT
:   Look-Up Table

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/metadata.yaml -->
Metadata
:   Structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/mosaic-product.yaml -->
Mosaic Product
:   Product generated from more than one input data source and where a pixel value in the product uniquely corresponds to the pixel value of one of its input data sources.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/nrb.yaml -->
NRB
:   Normalised Radar Backscatter

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/orb.yaml -->
ORB
:   Ocean Radar Backscatter

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/pfs.yaml -->
PFS
:   Product Family Specification

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/pol.yaml -->
POL
:   Polarimetric Radar

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/pslr.yaml -->
PSLR
:   Polarimetric Signal-to-Noise Level Ratio

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rmse.yaml -->
RMSE
:   Root Mean Square Error

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

## Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-sar.yaml-->`1.1.` Traceability {#sec:meta-trace-sar label="|General Metadata: Traceability"}

Identifier: `meta-trace-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data must be traceable to SI reference standard.

Notes:

1. Relationship to [@sec:rcm-radacc-sar]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-sar.yaml-->`1.2.` Metadata Machine Readability {#sec:meta-memare-sar label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta-memare-sar`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable for further use.


##### Goal requirements:

As threshold, but metadata is formatted in accordance with the latest corresponding CEOS-ARD SAR Metadata Specifications, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention and the Attribute Convention for Data Discovery (ACDD), etc.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/product-type.yaml-->`1.3.` Product Type {#sec:meta-protype label="|General Metadata: Product Type"}

Identifier: `meta-protype`



##### Threshold requirements:

CEOS-ARD product type name – or names in case of compliance with more than one product type – and, if required by the data provider, copyright.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/pfs-url.yaml-->`1.4.` Document Identifier {#sec:meta-pfsurl label="|General Metadata: Document Identifier"}

Identifier: `meta-pfsurl`



##### Threshold requirements:

Reference to CEOS-ARD PFS document as URL.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-sar.yaml-->`1.5.` Data Collection Time {#sec:meta-time-sar label="|General Metadata: Data Collection Time"}

Identifier: `meta-time-sar`



##### Threshold requirements:

Number of source data acquisitions of the data collection is identified.
The start and stop UTC time of data collection is identified in the metadata, expressed in date/time.
In the case of composite or mosaic products, the dates/times of the first and last data takes is provided with the product.


##### Goal requirements:

As threshold, but using ISO 8601 time format.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/source-metadata.yaml-->`2.` Source Metadata {#sec:src label="|Source Metadata"}

Metadata describing (detailing) **each** acquisition used to generate the ARD product.

Source data attribute information can refer to other products for higher level ARD derived from those, under the condition of their availability (@sec:src-daccess-src).


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/acquisition-id.yaml-->`2.1.` Acquisition ID {#sec:src-macqid label="|Source Metadata: Acquisition ID"}

Identifier: `src-macqid`



##### Threshold requirements:

Source data attribute information are described for each acquisition and sequentially identified e.g. as acqID = 1, 2, 3, …


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access-source.yaml-->`2.2.` Source Data Access {#sec:src-daccess-src label="|Source Metadata: Source Data Access"}

Identifier: `src-daccess-src`



##### Threshold requirements:

The metadata identifies the location from where the source data can be retrieved, expressed as a URL or DOI.


##### Goal requirements:

The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/instrument-sar.yaml-->`2.3.` Instrument {#sec:src-instru-sar label="|Source Metadata: Instrument"}

Identifier: `src-instru-sar`



##### Threshold requirements:

The instrument used to collect the data is identified in the metadata:

- Satellite name
- Instrument name


##### Goal requirements:

As threshold, but using [CEOS Mission-Instruments-Measurements (MIM) database](https://ceos.org/mim-database) as reference.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-source.yaml-->`2.4.` Source Data Acquisition Time {#sec:src-time-src label="|Source Metadata: Source Data Acquisition Time"}

Identifier: `src-time-src`



##### Threshold requirements:

The start date and time of source data is identified in the metadata, expressed in UTC in date and time, at least to the second.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/acquisition-parameters-sar.yaml-->`2.5.` Source Data Acquisition Parameters {#sec:src-acqpar label="|Source Metadata: Source Data Acquisition Parameters"}

Identifier: `src-acqpar`



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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/orbit-insar.yaml-->`2.6.` Source Data Orbit Information {#sec:src-orbit-insar label="|Source Metadata: Source Data Orbit Information"}

Identifier: `src-orbit-insar`



##### Threshold requirements:

Information related to the platform orbit used for data processing:

- Relative orbit number, if defined


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-parameters.yaml-->`2.7.` Source Data Processing Parameters {#sec:src-propar label="|Source Metadata: Source Data Processing Parameters"}

Identifier: `src-propar`



##### Threshold requirements:

Processing parameters details of the source data:

- Processing facility
- Processing date
- Software version
- Product level
- Product ID (file name)
- Azimuth number of looks
- Range number of looks (separate values for each beam, as necessary)

Note:

1. Azimuth and Range number of looks are not required when sources are CEOS-ARD or any other geocoded products


##### Goal requirements:

As threshold, plus additional relevant processing parameters, e.g., range- and azimuth look bandwidth and LUT applied.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/image-attributes-sar.yaml-->`2.8.` Source Data Image Attributes {#sec:src-imgatt-sar label="|Source Metadata: Source Data Image Attributes"}

Identifier: `src-imgatt-sar`



##### Threshold requirements:

Image attributes related to the source data:

- Source data geometry (slant range/ground range/geocoded)
- Azimuth pixel spacing \[m] (alternatively, azimuth pixel spacing can be provided in second \[s], equivalent to the azimuth time sample interval)
- Range pixel spacing
- Azimuth resolution
- Range resolution 
- Near range incident angle
- Far range incident angle

Note:

1. For geocoded sources such as GSLC and InSAR, Azimuth and Range pixel spacing are replaced by line (row) and pixel (column) spacing information. Spatial resolution information is not required for geocoded sources.


##### Goal requirements:

Geometry of the image footprint expressed in WGS84 in a standardised format (e.g., WKT).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sensor-calibration-sar.yaml-->`2.9.` Sensor Calibration {#sec:src-sencal-sar label="|Source Metadata: Sensor Calibration"}

Identifier: `src-sencal-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata.
Ideally this would support machine-to-machine access.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/performance-indicators.yaml-->`2.10.` Performance Indicators {#sec:src-perfind label="|Source Metadata: Performance Indicators"}

Identifier: `src-perfind`



##### Threshold requirements:

Provide performance indicators on data intensity noise level ($\text{NE}\sigma^0$ and/or $\text{NE}\beta^0$ and/or $\text{NE}\gamma^0$, i.e., noise equivalent Sigma- and/or Beta- and/or Gamma-Nought).
Provided for each polarization channel when available.

Parameter may be expressed as the mean and/or minimum and maximum noise equivalent values of the source data.

Values do not need to be estimated individually for each product, but may be estimated once for each acquisition mode, and annotated on all products.


##### Goal requirements:

Provide additional relevant performance indicators (e.g., ENL, PSLR, ISLR, and performance reference DOI or URL).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/polarimetric-calibration-matrices.yaml-->`2.11.` Polarimetric Calibration Matrices {#sec:src-polcalm label="|Source Metadata: Polarimetric Calibration Matrices"}

Identifier: `src-polcalm`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The complex-valued polarimetric distortion matrices with the channel imbalance and the cross-talk applied for the polarimetric calibration.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/mean-faraday-rotation-angle.yaml-->`2.12.` Mean Faraday Rotation Angle {#sec:src-farotan label="|Source Metadata: Mean Faraday Rotation Angle"}

Identifier: `src-farotan`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The mean Faraday rotation angle estimated from the polarimetric data and/or from models with reference to the method or paper used to derive the estimate.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/ionosphere-indicator.yaml-->`2.13.` Ionosphere Indicator {#sec:src-ionind label="|Source Metadata: Ionosphere Indicator"}

Identifier: `src-ionind`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Flag indicating whether the backscatter imagery is “significantly impacted” by the ionosphere (0 – false, 1 – true).
Significant impact would imply that the ionospheric impact on the backscatter exceeds the radiometric calibration requirement or goal for the imagery.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/product-metadata.yaml-->`3.` Product Metadata {#sec:prd label="|Product Metadata"}

Information related to the CEOS-ARD product generation procedure and geographic parameters.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access-product.yaml-->`3.1.` Product Data Access {#sec:prd-daccess-prod label="|Product Metadata: Product Data Access"}

Identifier: `prd-daccess-prod`



##### Threshold requirements:

Processing parameters details of the CEOS-ARD product:

- Processing facility
- Processing date
- Software version
- Location from where CEOS-ARD product can be retrieved, expressed as a URL or DOI.


##### Goal requirements:

The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/auxiliary-data-sar.yaml-->`3.2.` Auxiliary Data {#sec:prd-auxdat-sar label="|Product Metadata: Auxiliary Data"}

Identifier: `prd-auxdat-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as DOIs.

Note:

1. Auxiliary data includes DEMs, etc., and any additional data sources used in the generation of the product.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sample-spacing.yaml-->`3.3.` Product Sample Spacing {#sec:prd-samspa label="|Product Metadata: Product Sample Spacing"}

Identifier: `prd-samspa`



##### Threshold requirements:

CEOS-ARD product processing parameters details:

- Pixel (column) spacing
- Line (row) spacing


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/enl.yaml-->`3.4.` Product Equivalent Number of Looks {#sec:prd-enl label="|Product Metadata: Product Equivalent Number of Looks"}

Identifier: `prd-enl`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Equivalent Number of Looks (ENL)

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/resolution.yaml-->`3.5.` Product Resolution {#sec:prd-resol label="|Product Metadata: Product Resolution"}

Identifier: `prd-resol`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Average spatial resolution of the CEOS-ARD product along:

- Columns
- Rows

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-bbox.yaml-->`3.6.` Product Bounding Box {#sec:prd-geobbox label="|Product Metadata: Product Bounding Box"}

Identifier: `prd-geobbox`



##### Threshold requirements:

Two opposite corners of the product file (bounding box, including any zero-fill values) are identified,
expressed in the coordinate reference system defined in [@sec:prd-crs-sar].

Four corners of the product file are recommended for scenes crossing the Antemeridian, or the North or the South Pole.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geo-area-sar.yaml-->`3.7.` Product Geographical Extent {#sec:prd-geoarea-sar label="|Product Metadata: Product Geographical Extent"}

Identifier: `prd-geoarea-sar`



##### Threshold requirements:

The geometry of the SAR image footprint expressed in longitude/latitude based on WGS84 (EPSG 4326), in a standardised format (e.g., WKT Polygon).


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/image-size.yaml-->`3.8.` Product Image Size {#sec:prd-imgsize label="|Product Metadata: Product Image Size"}

Identifier: `prd-imgsize`



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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/pixel-coordinate-convention.yaml-->`3.9.` Product Pixel Coordinate Convention {#sec:prd-pixcoco label="|Product Metadata: Product Pixel Coordinate Convention"}

Identifier: `prd-pixcoco`



##### Threshold requirements:

Coordinate referring to the centre, the upper left corner, or the lower left corner of a pixel.
Values are pixel centre, pixel ULC or pixel LLC.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/crs-sar.yaml-->`3.10.` Product Coordinate Reference System {#sec:prd-crs-sar label="|Product Metadata: Product Coordinate Reference System"}

Identifier: `prd-crs-sar`



##### Threshold requirements:

The metadata lists the map projection (or geographical coordinates, if applicable) that was used and any relevant parameters required to geolocate data in that map projection, expressed in a standardised format (e.g., WKT).

Indicate EPSG code, if defined for the CRS.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radar-unit-look-vector.yaml-->`3.11.` Radar Unit Look Vector {#sec:prd-rulvec label="|Product Metadata: Radar Unit Look Vector"}

Identifier: `prd-rulvec`



##### Threshold requirements:

3-D components radar unit look vector, specified at centre of scene, in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating - ECR) is provided.
It consists of unit vectors from antenna to surface pixel (i.e., positive Z component).

Only required if the corresponding per-pixel metadata [@sec:pxl-radulov-insar] is **not** provided.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/insar-pair.yaml-->`3.12.` InSAR Pair {#sec:prd-inspair label="|Product Metadata: InSAR Pair"}

Identifier: `prd-inspair`



##### Threshold requirements:

InSAR baseline criteria information

- Baseline type: Single Reference, Multi-baseline or All
- Minimal and maximal perpendicular baselines (not required when type = "All")
- Minimal and maximal temporal baselines (not required when type = "All")

When InSAR product contains image data derived from InSAR pairs, as defined in @sec:rcm-coheri, @sec:rcm-interfi, and @sec:rcm-unwinterfi, provide list of source acquisition ID (e.g. as per @sec:src-macqid) for the InSAR pair (primary and secondary acquisitions).
Repeat for multiple InSAR pair products and assign/specify InSAR pair ID number (e.g., insarID = 1, 2, 3 …).
For multi-polarisation source acquisition, specify the polarisation used for the InSAR pair.
      
Provide Perpendicular and Parallel orbit baseline information estimated at scene centre.
In addition, orbital baseline information can be provided as per pixel metadata via @sec:pxl-iperba and @sec:pxl-iparba.

Flag if orbital baseline refinement has been applied (true/false).
If true, specify refinement method (e.g., GCPs, FFT, …).

Azimuth common band filtering and range spectral shift filtering flags.


##### Goal requirements:

Source type format with value "GSLC" should be provided when InSAR analysis is performed from GSLC products generated from SLC source acquisitions listed in @sec:src.
If GSLC data aren't provided with the InSAR product, provide the GSLC URL link(s) if it is available.
If source acquisitions listed in @sec:src are GSLC, discard this note.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/insar-pair-coregistration.yaml-->`3.13.` InSAR Pair Co-registration {#sec:prd-inspacr label="|Product Metadata: InSAR Pair Co-registration"}

Identifier: `prd-inspacr`



##### Threshold requirements:

Co-registration information of source acquisitions with a reference source.
Provide reference source ID (or filename if different from source list) and for each co-registered source, report the azimuth and range standard deviation error in metre or sample fraction.

**Not required when the InSAR product is generated from GSLC products (see product level in @sec:src-propar).**


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/insar-phase-quality.yaml-->`3.14.` Local InSAR Phase Quality {#sec:prd-inpqual label="|Product Metadata: Local InSAR Phase Quality"}

Identifier: `prd-inpqual`



##### Threshold requirements:

Local InSAR phase quality estimation information

- Methodology name (e.g., Coherence, DespecKS, Persistent Scatterers \[Temporal variability of intensity and/or Spectral diversity correlation], …)
- Reference to methodology (text or DOI)
- Estimation parameters and selection criteria used, as for examples:

    1. For coherence

        - Window size
        - Weighting shape
        - Coherence threshold for selection
    
    2.	For DespecKS [@ferretti2011] or similar statistical approach

        - Window size
        - Statistical test function (Kolmogorov-Smirnov, Anderson-Darling, …)
        - Number of statistically homogeneous pixels (SHP) threshold for selection
        - Phase triangulation coherence ($\gamma_{PTA}$) threshold
    
    3.	For Persistent Scatterers

        - Temporal variability of intensity

            -	Intensity mean/std ratio threshold
            -	Relative intensity threshold
            -	Spectral diversity correlation
            -	Line and column spectral looks
            -	Intensity minimal threshold
            -	Spectral correlation threshold
            -	Intensity mean/std ratio threshold

All phase quality estimation techniques used shall be listed.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/filtering-interferogram.yaml-->`3.15.` Interferogram Filtering {#sec:prd-intfil label="|Product Metadata: Interferogram Filtering"}

Identifier: `prd-intfil`



##### Threshold requirements:

If applied, interferogram filtering information

-	Methodology name
-	Reference to methodology (text or DOI)
-	Filtering parameters used


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/phase-unwrapping.yaml-->`3.16.` Phase Unwrapping {#sec:prd-phasun label="|Product Metadata: Phase Unwrapping"}

Identifier: `prd-phasun`



##### Threshold requirements:

If an Unwrapped Interferogram Image (see [@sec:rcm-unwinterfi]) is provided, technique used for InSAR phase unwrapping

- Methodology name
- Reference to methodology (text or DOI)
- Unwrapping parameters

    1. Coherence threshold
    2. Number of iterations
    3. Stable reference point coordinates or multi-point approach information


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/atmospheric-phase.yaml-->`3.17.` Atmospheric Phase Correction {#sec:prd-catpha label="|Product Metadata: Atmospheric Phase Correction"}

Identifier: `prd-catpha`



##### Threshold requirements:

If applied, reference to atmospheric phase correction technique and parameters used.

- Methodology name
- Reference to methodology (text or DOI)


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/ionospheric-phase.yaml-->`3.18.` Ionospheric Phase Correction {#sec:prd-ionpha label="|Product Metadata: Ionospheric Phase Correction"}

Identifier: `prd-ionpha`



##### Threshold requirements:

If applied, reference to ionospheric phase correction technique and parameters used.

- Methodology name
- Reference to methodology (text or DOI)


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/displacement-modelling.yaml-->`3.19.` Displacement Modelling {#sec:prd-dismod label="|Product Metadata: Displacement Modelling"}

Identifier: `prd-dismod`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Reference to displacement modelling technique used

- Methodology name
- Reference to methodology (text or DOI)
- Specific input parameters used

If a temperature refinement model is used, indicate model and temperature data source.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/per-pixel-metadata.yaml-->`4.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata is provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to **discriminate between** (choose) observations on the basis of their individual suitability for application.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-sar.yaml-->`4.1.` Metadata Machine Readability {#sec:pxl-memare-sar label="|Per-Pixel Metadata: Metadata Machine Readability"}

Identifier: `pxl-memare-sar`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable for further use.


##### Goal requirements:

As threshold, but metadata is formatted in accordance with the latest corresponding CEOS-ARD SAR Metadata Specifications, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention and the Attribute Convention for Data Discovery (ACDD), etc.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/data-mask.yaml-->`4.2.` Data Mask Image {#sec:pxl-damaski label="|Per-Pixel Metadata: Data Mask Image"}

Identifier: `pxl-damaski`



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

Notes:

1. All bit value representations included in the Data Mask Image should be indicated in the metadata.
2. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.


##### Goal requirements:

As threshold, including additional bit value representations, e.g.:

- Layover (masked as invalid data in threshold)
- Radar shadow (masked as invalid data in threshold)
- Ocean water
- Land (recommended for ORB)
- RTC applied (e.g., for maritime scenes with land samples for which RTC has been applied)
- DEM gap filling (i.e., interpolated DEM over gaps)
- Unwrapped interferogram phase quality flag/score

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/scattering-area.yaml-->`4.3.` Scattering Area Image {#sec:pxl-piscata label="|Per-Pixel Metadata: Scattering Area Image"}

Identifier: `pxl-piscata`



**Usage:** Recommended for scenes that include land areas.

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

Notes:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file could be provided as a URL address of that unique metadata file.
2. Required for products such as NRB and POL if they are to be used as an input to production of composite backscatter (CB) when weighted averages based on the areas are used to generate composite backscatter.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/ellipsoidal-incident-angle.yaml-->`4.4.` Ellipsoidal Incident Angle Image {#sec:pxl-pelinca label="|Per-Pixel Metadata: Ellipsoidal Incident Angle Image"}

Identifier: `pxl-pelinca`



##### Threshold requirements:

Ellipsoidal incident angle is provided.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
- Reference Ellipsoid Name

Required when a Radar Unit Look Vector Grid Image (see @sec:pxl-radulov-insar) is not provided.

Note:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/noise-power.yaml-->`4.5.` Noise Power Image {#sec:pxl-pinopow label="|Per-Pixel Metadata: Noise Power Image"}

Identifier: `pxl-pinopow`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Estimated Noise Equivalent $\sigma^0$ (or $\beta^0$ or $\gamma^0$, as applicable) used for noise removal, if applied, for each channel.
$\text{NE}\sigma^0$ and $\text{NE}\gamma^0$ are both based on either an ellipsoid Earth model or the local topography.

File format specifications/contents provided in metadata:

- Sample Type (Gamma-Nought, Sigma-Nought, Beta-Nought)
- Correction model type (Ellipsoid, Topography)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/gamma-sigma-ratio.yaml-->`4.6.` Gamma-to-Sigma Ratio Image {#sec:pxl-gasiri label="|Per-Pixel Metadata: Gamma-to-Sigma Ratio Image"}

Identifier: `pxl-gasiri`



##### Threshold requirements:


Not required.
<!-- *None* -->


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

Note:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/dem.yaml-->`4.7.` Per-Pixel DEM {#sec:pxl-pidem label="|Per-Pixel Metadata: Per-Pixel DEM"}

Identifier: `pxl-pidem`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Provide DEM or DSM as used during the geometric and radiometric processing of the SAR data, resampled to an exact geometric match in extent and resolution with the CEOS-ARD SAR image product.

File format specifications/contents provided in metadata:

- Sample Type (Height)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Note:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/radar-unit-look-vector-grid-insar.yaml-->`4.8.` Radar Unit Look Vector Grid Image {#sec:pxl-radulov-insar label="|Per-Pixel Metadata: Radar Unit Look Vector Grid Image"}

Identifier: `pxl-radulov-insar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

3-D components radar unit look vector of the reference acquisition, specified at each pixel in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating – ECR), is provided.
It consists of unit vectors from the antenna to the surface pixel (i.e., positive Z component).

File format specifications/contents provided in metadata:

- Sample Type (3D unit vector)
- Source acquisition ID (e.g. acqID)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Double Float, …)
- Bits per Sample
- Byte Order

Note:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/slant-range-insar.yaml-->`4.9.` Slant Range Sensor to Surface Image {#sec:pxl-slarassi-insar label="|Per-Pixel Metadata: Slant Range Sensor to Surface Image"}

Identifier: `pxl-slarassi-insar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Slant range distance from the sensor to the surface of the reference acquisition, specified at each pixel in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating – ECR) is provided.

File format specifications/contents provided in metadata:

- Sample Type (Length)
- Source acquisition ID (e.g. acqID)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order

Note:

1. For CEOS-ARD products created from repeat-pass acquisitions, with narrow orbital tube radius, a single static per pixel metadata file can be provided as a URL address of that unique metadata file.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/insar-phase-uncertainty.yaml-->`4.10.` InSAR Phase Uncertainty Image {#sec:pxl-pinphun label="|Per-Pixel Metadata: InSAR Phase Uncertainty Image"}

Identifier: `pxl-pinphun`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Estimates of uncertainty in InSAR phase is provided, such as finite signal to noise ratio, quantization noise, platform state vector accuracy, or DEM error.
Identification of which error sources are included will be provided as DOI/URL reference or brief description.
It represents statistical variation from known noise sources only.
In case both the wrapped and unwrapped interferograms are supplied, specify which interferogram the uncertainty image corresponds to. 

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order
-	insarID number (see [@sec:prd-inspair])
-	Corresponding interferogram

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/atmospheric-phase-correction.yaml-->`4.11.` Atmospheric Phase Correction Image {#sec:pxl-atphaci label="|Per-Pixel Metadata: Atmospheric Phase Correction Image"}

Identifier: `pxl-atphaci`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Phase correction value at each pixel, if applied.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order
-	insarID number (see [@sec:prd-inspair])

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/ionospheric-phase-correction.yaml-->`4.12.` Ionospheric Phase Correction Image {#sec:pxl-piopha label="|Per-Pixel Metadata: Ionospheric Phase Correction Image"}

Identifier: `pxl-piopha`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Phase correction value at each pixel, if applied.

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order
-	insarID number (see [@sec:prd-inspair])

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/simulated-topographic-phase.yaml-->`4.13.` Simulated Topographic Phase Image {#sec:pxl-sitophi label="|Per-Pixel Metadata: Simulated Topographic Phase Image"}

Identifier: `pxl-sitophi`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Simulated topographic phase image(s) used to remove topographic contribution to interferogram(s).

File format specifications/contents provided in metadata:

- Sample Type (Angle)
- insarID number (see [@sec:prd-inspair])
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/insar-perpendicular-baseline.yaml-->`4.14.` InSAR Perpendicular Baseline Image {#sec:pxl-iperba label="|Per-Pixel Metadata: InSAR Perpendicular Baseline Image"}

Identifier: `pxl-iperba`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Perpendicular orbital baseline between primary and secondary source acquisitions.

File format specifications/contents provided in metadata:

- Sample Type (Length)
- insarID number (see [@sec:prd-inspair])
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/insar-parallel-baseline.yaml-->`4.15.` InSAR Parallel Baseline Image {#sec:pxl-iparba label="|Per-Pixel Metadata: InSAR Parallel Baseline Image"}

Identifier: `pxl-iparba`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Parallel orbital baseline between primary and secondary source acquisitions.

File format specifications/contents provided in metadata:

- Sample Type (Length)
- insarID number (see [@sec:prd-inspair])
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/insar-displacement-model-point.yaml-->`4.16.` InSAR Displacement Model Point Image {#sec:pxl-idimopo label="|Per-Pixel Metadata: InSAR Displacement Model Point Image"}

Identifier: `pxl-idimopo`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data file(s) identifying pixels used for InSAR displacement modeling (requirements [@sec:rcm-indispi; @sec:rcm-indisrei; @sec:rcm-indisrai; @sec:rcm-indisramfi]).
As a suggestion, this information can be provided as a single multi-layer file, where each 1-bit layer, containing 0 (not used) and 1 (used) flags, refers to an insarID pair (for SBAS type InSAR) or Source ID (when insarIDs are not listed).
Instead, a list of Dates identifying layers can be provided under this item.  

File format specifications/contents provided in metadata:

- Sample Type (Model Points)
-	Source ID or insarID number or Dates
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (1bit, 8bit, …)
- Bits per Sample
- Byte Order

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/radiometrically-corrected-measurements.yaml-->`5.` Radiometrically Corrected Measurements {#sec:rcm label="|Radiometrically Corrected Measurements"}

The requirements indicate the necessary outcomes and, to some degree, the minimum steps necessary to be deemed to have achieved those outcomes.
Radiometric corrections must lead to normalised measurement(s) of backscatter intensity and/or decomposed polarimetric parameters.
As for the per-pixel metadata, information regarding data format specification needs to be provided for each record.
The requirements below must be met for all pixels/samples/observations in a collection.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/backscatter-insar.yaml-->`5.1.` Backscatter Measurements (InSAR) {#sec:rcm-backsca-insar label="|Radiometrically Corrected Measurements: Backscatter Measurements (InSAR)"}

Identifier: `rcm-backsca-insar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Terrain-flattened Radiometrically Terrain Corrected (RTC) Gamma-Nought backscatter coefficient ($\gamma^0_T$) is provided for each polarization.

File format specifications/contents provided in metadata:

- Measurement Type (Gamma-Nought)
- Source ID (e.g. see [@sec:src-macqid])
- Backscatter Expression Convention (linear amplitude, or linear power \[see note])
- Polarization (HH, HV, VV, VH, …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

Note:

1. Transformation to the logarithm decibel scale is not required or desired as this step can be completed by the user if necessary.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/scaling-conversion.yaml-->`5.2.` Scaling Conversion {#sec:rcm-scaconv label="|Radiometrically Corrected Measurements: Scaling Conversion"}

Identifier: `rcm-scaconv`



##### Threshold requirements:

If applicable, indicate the equation to convert pixel linear amplitude/power to logarithmic decibel scale, including, if applicable, the associated calibration (dB offset) factor, and/or the equation used to convert compressed data (int8/int16/float16) to float32.


##### Goal requirements:

As threshold, but use of float32.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/noise-removal.yaml-->`5.3.` Noise Removal {#sec:rcm-noiser label="|Radiometrically Corrected Measurements: Noise Removal"}

Identifier: `rcm-noiser`



##### Threshold requirements:

Flag if noise removal (see note) has been applied (Y/N).
Metadata should include the noise removal algorithm and reference to the algorithm as URL or DOI.

Note:

1. Thermal noise removal and image border noise removal to remove overall scene noise and scene edge artefacts, respectively.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/radiometric-terrain-algorithm-minimal.yaml-->`5.4.` Radiometric Terrain Correction Algorithm {#sec:rcm-radtalg-min label="|Radiometrically Corrected Measurements: Radiometric Terrain Correction Algorithm"}

Identifier: `rcm-radtalg-min`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Require resolution of DEM better than the output product resolution when applying terrain corrections.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-accuracy-sar.yaml-->`5.5.` Radiometric Accuracy {#sec:rcm-radacc-sar label="|Radiometrically Corrected Measurements: Radiometric Accuracy"}

Identifier: `rcm-radacc-sar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Uncertainty (e.g., bounds on $\gamma^0$ or $\sigma^0$) information is provided as document referenced as URL or DOI.
SI traceability is achieved.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/coherence-image.yaml-->`5.6.` Coherence Image {#sec:rcm-coheri label="|Radiometrically Corrected Measurements: Coherence Image"}

Identifier: `rcm-coheri`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

InSAR coherence image for each InSAR pair defined in [@sec:prd-inspair].

File format specifications/contents provided in metadata:

- Measurement Type (Coherence)
- insarID number
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, Complex Float, …)
- Bits per Sample
- Byte Order

Coherence image statistics:

- Average
- Standard deviation

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/interferogram-image.yaml-->`5.7.` Interferogram Image {#sec:rcm-interfi label="|Radiometrically Corrected Measurements: Interferogram Image"}

Identifier: `rcm-interfi`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Interferogram image for each InSAR pair defined in [@sec:prd-inspair].
Indicate if the InSAR simulated ellipsoid and topographic phases have been subtracted.

File format specifications/contents provided in metadata:

- Measurement Type (Interferogram)
- insarID number
- Subtracted Earth curvature phase flag (True, False)
- Subtracted topographic phase flag (True, False)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/interferogram-image-unwrapped.yaml-->`5.8.` Unwrapped Interferogram Image {#sec:rcm-unwinterfi label="|Radiometrically Corrected Measurements: Unwrapped Interferogram Image"}

Identifier: `rcm-unwinterfi`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Unwrapped interferogram image for each InSAR pair defined in [@sec:prd-inspair].

File format specifications/contents provided in metadata:

- Measurement Type (Unwrapped Interferogram)
- insarID number
- Component (Line of Sight, Vertical, East, North)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/insar-displacement-image.yaml-->`5.9.` InSAR Displacement Image {#sec:rcm-indispi label="|Radiometrically Corrected Measurements: InSAR Displacement Image"}

Identifier: `rcm-indispi`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Displacement map image(s) could be expressed as a single cumulative displacement map or a temporal series of incremental displacement maps. 

File format specifications/contents provided in metadata:

- Measurement Type (InSAR Cumulative Displacement or InSAR Incremental Displacement)
- Measurement projection (Line of Sight, Vertical, Horizontal, East, North)
- Interval start time
- Interval end time
- Reference Polarization (HH, HV, VV, VH, RH, RL, …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

In case of polarimetric data, indicate the reference polarization.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/insar-displacement-residue-image.yaml-->`5.10.` InSAR Displacement Residue Image {#sec:rcm-indisrei label="|Radiometrically Corrected Measurements: InSAR Displacement Residue Image"}

Identifier: `rcm-indisrei`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Displacement residue map images for each source acquisition generated from displacement model.

File format specifications/contents provided in metadata:

- Measurement Type (Displacement residues)
- Measurement projection (Line of Sight, Vertical, Horizontal, East, North)
- Source ID
- Reference Polarization (HH, HV, VV, VH, RH, RL, …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

In case of polarimetric data, indicate the reference polarization.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/insar-displacement-rate-image.yaml-->`5.11.` InSAR Displacement Rate Image {#sec:rcm-indisrai label="|Radiometrically Corrected Measurements: InSAR Displacement Rate Image"}

Identifier: `rcm-indisrai`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Mean linear displacement rate (velocity) estimate. 

File format specifications/contents provided in metadata:

- Measurement Type (Displacement rate)
- Measurement projection (Line of Sight, Vertical, Horizontal, East, North)
- Interval start time
- Interval end time
- Rate (velocity) units (mm/year, cm/year, mm/month, …)
- Reference Polarization (HH, HV, VV, VH, RH, RL, …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

In case of polarimetric data, indicate the reference polarization.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/insar-displacement-rate-model-fit-image.yaml-->`5.12.` InSAR Displacement Rate Model Fit Image {#sec:rcm-indisramfi label="|Radiometrically Corrected Measurements: InSAR Displacement Rate Model Fit Image"}

Identifier: `rcm-indisramfi`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Goodness of fit for model defined in [@sec:rcm-indisrai].

File format specifications/contents provided in metadata:

- Measurement Type (Model standard deviation, R-squared, RMSE …)
- Measurement projection (Line of Sight, Vertical, Horizontal, East, North)
- Interval start time
- Interval end time
- Reference Polarization (HH, HV, VV, VH, RH, RL, …)
- Data Format (GeoTIFF, HDF5, NetCDF, …)
- Data Type (Int, Float, …)
- Bits per Sample
- Byte Order

In case of polarimetric data, indicate the reference polarization.

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections.yaml-->`6.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

Geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-algorithm.yaml-->`6.1.` Geometric Correction Algorithm {#sec:gcor-geocalg label="|Geometric Corrections: Geometric Correction Algorithm"}

Identifier: `gcor-geocalg`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Metadata references, e.g.:

- A metadata citable peer-reviewed algorithm
- Technical documentation regarding the implementation of that algorithm expressed as URLs or DOIs
- The sources of auxiliary data used to make corrections
- Resampling method used for geometric processing of the source data

Note:

1. Examples of technical documentation can include e.g., an Algorithm Theoretical Basis Document (ATBD), or a product user guide.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/dem.yaml-->`6.2.` Digital Elevation Model {#sec:gcor-cdem label="|Geometric Corrections: Digital Elevation Model"}

Identifier: `gcor-cdem`



**Usage:** For products including land areas.

##### Threshold requirements:

a. During ortho-rectification, the data provider shall use the same DEM that was used for the radiometric terrain flattening to ensure consistency of the data stack.
b. Provide reference to the Digital Elevation Model used for geometric terrain correction. For mosaic or composite products, specify the DEM used for each input data source, if different.
c. Provide reference to Earth Gravitational Model (EGM) if used for geometric correction. For mosaic or composite products, specify the EGM used for each input data source, if different.


##### Goal requirements:

a. A DEM with comparable or better resolution to the resolution of the output CEOS-ARD product shall be used if available. Else, the upsampled DEM is identified.
b. Resampling method used for preparation of the DEM.
c. Method used for resampling the EGM.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-accuracy-sar.yaml-->`6.3.` Geometric Accuracy {#sec:gcor-geomacc-sar label="|Geometric Corrections: Geometric Accuracy"}

Identifier: `gcor-geomacc-sar`



##### Threshold requirements:

Accurate geolocation is a prerequisite to radar processing to correct for terrain and to enable interoperability between radar sensors.

The absolute geolocation error (ALE) for a sensor is typically assessed through analysis of Single Look Complex (SLC) imagery and measured along the slant range and azimuth directions (case A: SLC ALE).
The end-to-end “ARD” ALE of the final CEOS-ARD product could be measured directly in the final image product in the chosen map projection, i.e., in the map coordinate directions: e.g., Northing and Easting (case B: ARD ALE).
Providing accuracy estimates based on measurements following at least one scheme (A or B or both) meets the threshold requirement.

Estimates of the ALE is provided as a bias and a standard deviation, with (Case A) SLC ALE expressed in slant range and azimuth, and (Case B) ARD ALE expressed in map projection dimensions.

For composite products, when sources come from different SAR platforms or different beam modes, provide averaged ALE or averaged ARD ALE.

Notes:

1. This assessment is often made through comparison of measured corner reflector positions with their projected location in the imagery. In some cases, other mission calibration/validation results may be used.
2. The ALE is not typically assessed for every processed image, but through an ALE assessment by the data processing team characterizing all or (usually a suitably representative subset) of the generated products.
3. For new SAR missions, as long as calibration/validation reports are not available, values can be set to NaN and provide a DOI or URL link to pre-launch mission specification document.


##### Goal requirements:

Output product sub-sample accuracy should be less than or equal to 0.1 (slant range) pixel radial root mean square error (rRMSE).

Provide documentation of estimates of ALE as DOI or URL.

Specify the SAR acquisition used for geocoding. SAR acquisition could be different from the two source acquisitions of the product when a stack of acquisitions is processed simultaneously.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-refined-accuracy.yaml-->`6.4.` Geometric Refined Accuracy {#sec:gcor-georacc label="|Geometric Corrections: Geometric Refined Accuracy"}

Identifier: `gcor-georacc`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Values provided under [@sec:gcor-geomacc-sar] are provided by the SAR mission Cal/Val team.

CEOS-ARD processing steps could include method refining the geometric accuracy, such as cross-correlation of the SAR data in slant range with a SAR scene simulated from a DSM or DEM.

Methodology used (name and reference), quality flag, geometric standard deviation values should be provided.

For composite products, provide averaged ALE or averaged ARD ALE estimated from all sources.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/gridding-convention.yaml-->`6.5.` Gridding Convention {#sec:gcor-gridconv label="|Geometric Corrections: Gridding Convention"}

Identifier: `gcor-gridconv`



##### Threshold requirements:

A consistent gridding/sampling frame is used. The origin is chosen to minimise any need for subsequent resampling between multiple products (be they from the same or different providers).
This is typically accomplished via a “snap to grid” in relation to the most proximate grid tile in a global system.

Note:

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

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/introduction/sar-differences.yaml-->Compatibility and Interoperability of CEOS-ARD SAR Products {#sec:intro-sar-differences label="|Compatibility and Interoperability of CEOS-ARD SAR Products"}

As can be seen from the individual PFS descriptions, only a few minor details in terms of generated parameters and/or the addition of supplemental data distinguish these CEOS-ARD products.
In part, they are to a large extent all backward-compatible.
For example, POL products implicitly include NRB products, while a coastal NRB or POL product can simply be made compatible with other ORB products by applying gamma-to-sigma conversion.
Just as GSLC can be converted to NRB (given that terrain-flattening was applied, a goal-requirement for GSLC, the inverse conversion can be made true by including the optional topographically flattened phase.
In this way a NRB or POL product can be used like a GSLC for InSAR applications.
Consequently, it becomes obvious that they all can follow a common approach, in terms of content and structure, in order to optimize their interoperability.

&#12;

## References

::: {#refs}
:::

&#12;

## Annexes

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/annexes/sar-general-processing-roadmap.yaml-->General Processing Roadmap {#sec:annex-sar-general-processing-roadmap label="|General Processing Roadmap"}

The radiometric interoperability of CEOS-ARD SAR products is ensured by a common processing chain during production. The recommended processing roadmap involves the following steps:

- Apply the best possible orbit parameters to give the most accurate product possible. These will have been projected to an ellipsoidal model such as WGS84. To achieve the level of geometric accuracy required for the DEM-based correction, precise orbit determination will be required.
- Apply instrument calibration to produce Beta-Nought values with high fidelity.
- Convert Single-Look-Complex (SLC) radiometric channel(s) to intensity NRB, ORB and POL and in addition for POL, the cross-product element(s) of the covariance as shown in annex "Normalised Covariance Matrices (CovMat)" of the applicable PFS.
- Perform radiometric terrain correction (gamma backscatter convention terrain-flattening) on the covariance matrix by applying the local surface normalisation factor to each backscatter measurement element [@small2011; @shiroma2022].
- Perform polarimetric speckle filtering (optional for NRB and ORB), before geocoding, to optimally preserve the polarimetric information. Most popular polarimetric decomposition methodologies are incoherent in nature, which requires averaging the covariance matrix for stationarity. Depending on the application, a polarimetric filter that preserves local point targets and locally average extended targets may be used, e.g., Sigma Lee filter with 7x7 window and 3-point target [@lee2009]. Multi-looking could be performed to meet optimal output sample spacing before the geometric correction step. No speckle filtering or multi-looking is performed for GSLC products.
- For GSLC products, the topographic phase is estimated relative to a reference orbit and removed from the SLC data [@zebker2010; @zebker2017] (see annex "Topographic phase removal" in the applicable PFS)
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

InSAR analysis capabilities from CEOS-ARD SAR products are enabled with GSLC products, which is also the case when the Flattened Phase per-pixel data are included in the NRB or POL products. This is made possible since the simulated topographic phase relative to a given reference orbit has been subtracted.

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

In both cases, the InSAR topographic phase $\Delta \varphi_{\text{Topo}\_\text{OrbRef}-2}$ is simulated against the position of a virtual sensor $\Delta \varphi_{\text{Topo}\_\text{OrbRef}}$ lying on a reference orbit, instead of being simulated relatively to an existing reference SAR acquisition ($\varphi_{\text{DEM}\_\text{SLC}\_1}$). The use of a virtual circular orbit is a more robust approach since the reference orbit is defined at a fixed height above scene nadir and assuming the reference orbital height constant for all CEOS-ARD products. While with the second approach, the CEOS-ARD data producer must select a specific archived orbit cycle of the SAR mission or define a simulated one, from which the relative orbit, matching the one of the SAR acquisitions to be processed (to be converted to CEOS-ARD), is defined as the reference orbit. With this second approach, it is important to always use the same orbit cycle (or simulated orbit) for all the CEOS-ARD produced for a mission, in order to preserve the relevant compensated phase in between them. Providing absolute reference orbit number information in the metadata (see requirement "Reference Orbit" in the applicable PFS) allows users to validate the InSAR feasibility in between CEOS-ARD products.

$$
\varphi_{\text{Flattended}\_\text{SLC}\_2} = \varphi_{\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-2}
$$ {#eq:sar-topographic-phase-removal-eq3}

This procedure is equivalent to bring the position of the sensor platform of all the SAR acquisitions at the same orbital position (i.e., zeros baseline distance in between), which results in a Flattened phase  $\varphi_{\text{Flattended}\_\text{SLC}}$, independent of the local topography.

The phase subtraction could be performed by using a motion compensation approach [@zebker2010] or directly on the SLC data. Then the geometrical correction is performed on the Flattened SLC, which results in a GSLC product.

GSLC can also be saved as a NRB product by including the Flattened Phase per-pixel data as follows:

$$\text{NRB:} \quad \gamma_T^0 = |GSLC|^2 $$

$$\text{Flattended Phase:} \quad \varphi_{\text{Flattended}} = \arg (GSLC) $$

For the POL product, the Flattened Phase is defined for a specific polarisation. Since off-diagonal elements of the covariance matrix contain the relative phase between two polarizations, other polarization(s) Flattened Phase can be estimated by subtracting the complex number phase of the off-diagonal elements from reference polarization Flattened phase. As for example, if the reference Flattened Phase is for HH polarization ($\phi_{HH}$), then the Flattened Phase for VV polarization is $\phi_{VV} = \phi_{HH} - \arg\!\left(HH \, VV^{*}\right)$. Nonetheless, since the elements of the covariance matrix have been averaged, providing individual polarization Flattened Phase images under requirement "Flattened Phase" in the applicable PFS is more accurate.

InSAR from [GSLC] Demonstration:

From CEOS-ARD flattened SAR products, InSAR processing can be easily performed without dealing with topographic features and orbital sensor position, as for example with two [GSLC] products 

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

Where $\Delta\varphi_{\text{SLC}\_1-\text{SLC}\_2}$ can be expressed as [@eq:sar-topographic-phase-removal-eq1], which gives

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\Delta \varphi_{\text{Topo}\_1-2} + \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2}) - \Delta\varphi_{\text{Topo}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq10}

Consequently, the differential phase of two CEOS-ARD products doesn’t contain a topographic phase and is already unwrapped (at least over stable areas). It is only function of the surface displacement and of the noise term. Depending on the reference DEM and the satellite orbital state vector accuracies, some residual topographic phase could be present. Atmospheric (see [@sec:pxl-atphaci]) and ionospheric (see [@sec:pxl-piopha]) phase corrections could be performed during the production of CEOS-ARD products, which reduces the differential phase noise in an InSAR analysis.

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2})
$$ {#eq:sar-topographic-phase-removal-eq11}


