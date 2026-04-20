---
title: >-
  CEOS-ARD - Optical - Aquatic Reflectance - Version 2.0.0-draft
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
# we want to include all citations regardless of usage, see https://pandoc.org/MANUAL.html#including-uncited-items-in-the-bibliography
nocite: |
  @*
---

![](assets/CEOS_logo_colour_black_text_right.png)

# CEOS-ARD - Optical - Aquatic Reflectance

&nbsp;

## Document Status

Product Family Specification, Optical, Aquatic Reflectance

Proposed revisions may be provided to: [ard-contact@lists.ceos.org](mailto:ard-contact@lists.ceos.org)

## Document History

### 2026-04-13 (PATCH)

- Restructured the document; removed empty or unused parts
- Document history has been reset. Check the previous versions for details
- Numerical identifiers were rotated and are deprecated; new textual identifiers have been added
- The definitions are included in the document instead of referring to the CEOS Terms and Defintions Wiki
- The references are not grouped by requirements and threshold/goal any longer. Instead, they are listed in the requirements as a note.
- The requirement "Radiometric corrections must lead to a valid measurement [...]" has been moved from the category description to the measurement requirement.
- The requirement references (i.e. "3.1-3.3" and "3.4 onwards") were removed from the category description of "Products and Algorithms".
- If no threshold requirement applies, the wording has been made consistent (e.g. former req. 1.7 and 1.8).

**Justification:**
Migration to building blocks.

**Editor:** Matthias Mohr


## Contributing Authors

### Technical Leads

- Arnold Dekker (CSIRO) 
- Daniela Gurlin (Independent Consultant)

### Organisational Leads

- Matt Steventon (CEOS-ARD Oversight Group Secretariat)
- Harvey Jones (CEOS-ARD Oversight Group Secretariat)

### Contributors

- Carsten Brockmann (Brockmann Consult)
- Vittorio Brando (CNR) 
- Claudia Giardino (CNR) 
- Nicole Pinnel (DLR) 
- Peter Gege (DLR) 
- Barbara Bulgarelli (EC) 
- Peter Strobl (EC)
- Frédéric Mélin (EC) 
- Ewa Kwiatkowska (EUMETSAT) 
- Hayley Evers-King (EUMETSAT) 
- Andreia Siqueira (GA) 
- Medhavy Thankappan (GA) 
- Peter Harrison (GA) 
- Igor Ogashawara (IGB Berlin)
- Raisha Lovindeer (IOCCG)
- Hiroshi Murakami (JAXA)
- Joseph D. Ortiz (Kent State)
- Sean Bailey (NASA)
- Nima Pahlevan (NASA) 
- Anthony Vodacek (RIT)
- Heidi Dierssen (University of Connecticut) 
- Maycira Costa (University of Victoria) 
- Ben Page (USGS) 
- Chris Barnes (USGS)
- Liesbeth de Keukelare (VITO) 

&#12;

## CEOS Analysis Ready Data Definition

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

## Description

**Product Family Specification:**
Optical, Aquatic Reflectance (AR)

**Version:**
2.0.0-draft

**Applies to:**
Data collected with multispectral and hyperspectral imaging sensors operating in the VIS/NIR/SWIR wavelengths over water bodies (including oceans, seas, coastal zones, and inland waters). These typically operate with ground sample distance and resolution in the order of 1-4000 metres however the specification is not inherently limited to these resolutions.


&#12;

## Definitions and Abbreviations

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ancillary-data.yaml -->
Ancillary Data
:   Data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information, and data from other instruments.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/aod.yaml -->
AOD
:   Aerosol Optical Depth

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/ar.yaml -->
AR
:   Aquatic Reflectance

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/atbd.yaml -->
ATBD
:   Algorithm Theoretical Basis Document

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/auxiliary-data.yaml -->
Auxiliary Data
:   The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources, e.g., DEM, aerosols.

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/bipm.yaml -->
BIPM
:   Bureau International des Poids et Mesures (International Bureau of Weights and Measures)

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

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gsd.yaml -->
GSD
:   Ground Sample Distance

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/gum.yaml -->
GUM
:   Guide to the Expression of Uncertainty in Measurement

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/nir.yaml -->
NIR
:   Near Infrared

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/rrmse.yaml -->
rRMSE
:   Radial Root Mean Square Error

<!-- edit:/home/runner/work/ceos-ard/ceos-ard/glossary/si.yaml -->
SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

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

## Requirements

**WARNING:** The section numbers in front of the title (e.g. 1.1) are not stable and may change or may be removed at any time.
Do **not** use the numbers to refer back to specific requirements!
Instead, use the textual identifier that is provided below the title.

<!-- todo: remove requirement numbers -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/general-metadata.yaml-->`1.` General Metadata {#sec:meta label="|General Metadata"}

These are metadata records describing a distributed collection of pixels.
The collection of pixels referred to must be contiguous in space and time.
General metadata should allow the user to assess the _overall_ suitability of the dataset, and must meet the requirements listed below.

Information should be available in the metadata as a single DOI landing page, which may include links to further detailed documents and references to citable peer-reviewed algorithms or technical documentation.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/ceos-ard-pfs-version.yaml-->`1.1.` CEOS-ARD PFS Compliance Version {#sec:meta-ardver label="|General Metadata: CEOS-ARD PFS Compliance Version"}

Identifier: `meta-ardver`



##### Threshold requirements:

Version of the CEOS-ARD PFS with which the product is complying is identified.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/traceability-ar.yaml-->`1.2.` Traceability {#sec:meta-trace-ar label="|General Metadata: Traceability"}

Identifier: `meta-trace-ar`



##### Threshold requirements:

Aquatic Reflectance (dimensionless) or the Remote Sensing Reflectance ($sr^{-1}$) of the water bodies ($AR = \pi \cdot R_{rs}$) is given.


##### Goal requirements:

Data must be traceable to SI reference standard.

Note:

1. Relationship to [@sec:pral-muncer-ar]. Traceability requires an estimate of measurement uncertainty.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/machine-readability-optical.yaml-->`1.3.` Metadata Machine Readability {#sec:meta-memare-optical label="|General Metadata: Metadata Machine Readability"}

Identifier: `meta-memare-optical`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.


##### Goal requirements:

As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/time-ar.yaml-->`1.4.` Data Collection Time {#sec:meta-time-ar label="|General Metadata: Data Collection Time"}

Identifier: `meta-time-ar`



##### Threshold requirements:

The beginning and end of the data collection time is expressed in date/time and identified in the metadata consistent with ISO 8601. The time is expressed with the time offset from UTC unambiguously identified.


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

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-correction-methods-ar.yaml-->`1.8.` Geometric Correction Methods {#sec:meta-geocorm-ar label="|General Metadata: Geometric Correction Methods"}

Identifier: `meta-geocorm-ar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on geometric correction source and methods are provided, including reference database and auxiliary data such as elevation model(s) and reference chip-sets.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/geometric-uncertainty.yaml-->`1.9.` Geometric Uncertainty of the Data {#sec:meta-geounc label="|General Metadata: Geometric Uncertainty of the Data"}

Identifier: `meta-geounc`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Inclusion of metrics describing the assessed geodetic uncertainty of the data, expressed in units of the coordinate system of the data. Uncertainty is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed quantitatively.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/instrument-ar.yaml-->`1.10.` Instrument {#sec:meta-instru-ar label="|General Metadata: Instrument"}

Identifier: `meta-instru-ar`



##### Threshold requirements:

The instrument used to collect the data is identified.


##### Goal requirements:

As threshold, with references to the relevant “CEOS Missions, Instruments, and Measurements Database” record ([database.eohandbook.com](https://database.eohandbook.com)).

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/spectral-bands-ar.yaml-->`1.11.` Spectral Bands {#sec:meta-specband-ar label="|General Metadata: Spectral Bands"}

Identifier: `meta-specband-ar`



##### Threshold requirements:

Full spectral response function is provided.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/sensor-calibration-ar.yaml-->`1.12.` Sensor Calibration {#sec:meta-sencal-ar label="|General Metadata: Sensor Calibration"}

Identifier: `meta-sencal-ar`



##### Threshold requirements:

Binary description of calibrated/not calibrated only.


##### Goal requirements:

Specification of sensor calibration parameters including history of onboard calibrations where available.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-uncertainty.yaml-->`1.13.` Measurand Radiometric Uncertainty {#sec:meta-radunc label="|General Metadata: Measurand Radiometric Uncertainty"}

Identifier: `meta-radunc`



##### Threshold requirements:

Metrics describing the assessed radiometric uncertainty of the version of the data or product are provided. Method of determination of radiometric uncertainty is specified.


##### Goal requirements:

As threshold, but the absolute radiometric uncertainty of the data is provided.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/radiometric-encoding.yaml-->`1.14.` Radiometric Encoding {#sec:meta-radenc label="|General Metadata: Radiometric Encoding"}

Identifier: `meta-radenc`



##### Threshold requirements:

Range and bit depth are provided.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/algorithms-ar.yaml-->`1.15.` Algorithms {#sec:meta-malgos-ar label="|General Metadata: Algorithms"}

Identifier: `meta-malgos-ar`



##### Threshold requirements:

All algorithms and the sequence in which they were applied in the generation process are identified.

Algorithms must be published and validated, and a description of the validation process is included.

Note:

1. It is possible that corrections are applied through non-disclosed processes. CEOS-ARD does not require full and open data and methods.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/auxiliary-data-ar.yaml-->`1.16.` Auxiliary Data {#sec:meta-auxdat-ar label="|General Metadata: Auxiliary Data"}

Identifier: `meta-auxdat-ar`



##### Threshold requirements:

Lists the sources of auxiliary data used in the generation process.


##### Goal requirements:

As threshold, but information on auxiliary data should be available for free online download, contemporaneously with the product or through a link to the source.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/processing-chain-prov-ar.yaml-->`1.17.` Processing Chain Provenance {#sec:meta-proprov-ar label="|General Metadata: Processing Chain Provenance"}

Identifier: `meta-proprov-ar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Information on processing chain provenance should be available with a detailed description of the processing steps used to generate the product, including the versions of software used, giving full transparency to the users.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/metadata/data-access.yaml-->`1.18.` Data Access {#sec:meta-daccess label="|General Metadata: Data Access"}

Identifier: `meta-daccess`



##### Threshold requirements:

Information on data access should be available in the metadata as a single DOI landing page.

Note:

1. Manual and offline interaction action (e.g., login) may be required.


##### Goal requirements:


As threshold.
<!-- *None* -->

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
Whether the metadata is provided in a single record relevant to all pixels, or separately for each pixel, is at the discretion of the data provider.
Per-pixel metadata should allow users to **discriminate between** (choose) observations on the basis of their individual suitability for application.

Information should be available in the metadata as a single DOI landing page, which may include links to further detailed documents and references to citable peer-reviewed algorithms or technical documentation.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/machine-readability.yaml-->`2.1.` Metadata Machine Readability {#sec:pxl-pimemare label="|Per-Pixel Metadata: Metadata Machine Readability"}

Identifier: `pxl-pimemare`



##### Threshold requirements:

Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/nodata-ar.yaml-->`2.2.` No Data {#sec:pxl-pinodat-ar label="|Per-Pixel Metadata: No Data"}

Identifier: `pxl-pinodat-ar`



##### Threshold requirements:

Pixels that do not correspond to an observation (e.g., empty pixels / invalid observations / below noise floor) are masked.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/incomplete-testing-ar.yaml-->`2.3.` Per-pixel Assessment {#sec:pxl-pixass label="|Per-Pixel Metadata: Per-pixel Assessment"}

Identifier: `pxl-pixass`



##### Threshold requirements:

Identifies pixels for which the per-pixel tests (below) have not all been successfully completed.

Note:

1. This may be the result of missing ancillary data for a subset of the pixels.


##### Goal requirements:

Identifies which tests have and have not been successfully completed for each pixel.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/saturation-ar.yaml-->`2.4.` Saturation {#sec:pxl-pisatur-ar label="|Per-Pixel Metadata: Saturation"}

Identifier: `pxl-pisatur-ar`



##### Threshold requirements:

Specification of whether there is pixel radiometric saturation at Level 1 in one or more spectral bands.


##### Goal requirements:

As threshold, with specification of which pixels are radiometrically saturated for each spectral band.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud-ar.yaml-->`2.5.` Cloud {#sec:pxl-picloud-ar label="|Per-Pixel Metadata: Cloud"}

Identifier: `pxl-picloud-ar`



##### Threshold requirements:

Specification of whether a pixel is cloud or cloud-affected.


##### Goal requirements:

As threshold, but clouds and cirrus clouds are differentiated.

Note:

1. See @foga2017, @skakun2022, @zhu2012, and @zhu2015.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/cloud-shadow-ar.yaml-->`2.6.` Cloud Shadow {#sec:pxl-picloudsh-ar label="|Per-Pixel Metadata: Cloud Shadow"}

Identifier: `pxl-picloudsh-ar`



##### Threshold requirements:

Specification of whether a pixel is cloud shadow or cloud shadow-affected.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/land-water-ar.yaml-->`2.7.` Land {#sec:pxl-lawama-ar label="|Per-Pixel Metadata: Land"}

Identifier: `pxl-lawama-ar`



##### Threshold requirements:

Specification of whether a pixel is less than 100% water covered due to land.

Note:

1. See @jones2019, @mikelsons2021, and @pekel2016.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/ice.yaml-->`2.8.` Ice {#sec:pxl-pice label="|Per-Pixel Metadata: Ice"}

Identifier: `pxl-pice`



##### Threshold requirements:

Specification of whether a pixel is ice or ice-affected.

Note:

1. See @dworak2021, @liu2019, @liu2016, @robinson2003, @bourg2014, and @heinila2018.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/sun-glint.yaml-->`2.9.` Sun Glint {#sec:pxl-pisungli label="|Per-Pixel Metadata: Sun Glint"}

Identifier: `pxl-pisungli`



##### Threshold requirements:

Specification of whether sun glint in a pixel is negligible, correctable (moderate), or uncorrectable (severe).

Notes:

1. Sun glint is deemed uncorrectable if the upper limit of the dynamic range of a sensor's spectral band is reached (i.e., radiometric saturation occurs).
2. See @botha2016, @kay2013, and @bourg2014.


##### Goal requirements:

Specification of the amount of sun glint for each pixel and spectral band.

Notes:

1. An additional product must be provided to specify the amount.
2. See [@sec:pral-cosungli] and @fink2014.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/sky-glint.yaml-->`2.10.` Sky Glint {#sec:pxl-piskygli label="|Per-Pixel Metadata: Sky Glint"}

Identifier: `pxl-piskygli`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Specification of the amount of sky glint for each pixel and spectral band.

Notes:

1. An additional product must be provided to specify the amount.
2. Sky glint is the at-water-surface reflected component of the diffuse downwelling irradiance.
3. See [@sec:pral-coskygli], @reusen2023, and @fink2014.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/view-angles-solar-ar.yaml-->`2.11.` Solar and Viewing Geometry {#sec:pxl-vigeso-ar label="|Per-Pixel Metadata: Solar and Viewing Geometry"}

Identifier: `pxl-vigeso-ar`



##### Threshold requirements:

Specification of the solar and sensor viewing azimuth and zenith angles.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/whitecap-foam.yaml-->`2.12.` Whitecap / Foam {#sec:pxl-piwhifo label="|Per-Pixel Metadata: Whitecap / Foam"}

Identifier: `pxl-piwhifo`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Specification of whether a pixel is affected by whitecaps or foam.
If affected, detail the method applied.

Note:

1. See [@sec:pral-cowhifo], @dierssen2019, @dierssen2021, @frouin2019, @koepke1984, @moore2000, @wang2017, and @eumetsat2021.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/aod-parameters.yaml-->`2.13.` Aerosol Optical Depth Parameters {#sec:pxl-paodpara label="|Per-Pixel Metadata: Aerosol Optical Depth Parameters"}

Identifier: `pxl-paodpara`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Either per-pixel spectral AOD or per-pixel AOD (550 nm) and Angstrom exponent are provided.

Note:

1. This might be an input or an output parameter.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/adjacency-effects.yaml-->`2.14.` Adjacency Effects {#sec:pxl-pajdeff label="|Per-Pixel Metadata: Adjacency Effects"}

Identifier: `pxl-pajdeff`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Depending on the adjacency effects correction method (embedded in the atmospheric correction or separate from the atmospheric correction) the metadata specifies the amount of per-pixel adjacency effect contamination.

Notes:

1. An additional product must be provided to specify the amount.
2. See @botha2016, @bulgarelli2014, @bulgarelli2018, @sei2015, and @wu2023.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/floating-vegetation.yaml-->`2.15.` Floating Vegetation / Surface Scum {#sec:pxl-floatveg label="|Per-Pixel Metadata: Floating Vegetation / Surface Scum"}

Identifier: `pxl-floatveg`



##### Threshold requirements:

Specification of whether a pixel is affected by floating vegetation/surface scum.

Note:

1. See @bell2023, @bresciani2014, @gendall2023, @hu2009, @matthews2012, and @matthews2015.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/bathymetry.yaml-->`2.16.` Bathymetry {#sec:pxl-pibathy label="|Per-Pixel Metadata: Bathymetry"}

Identifier: `pxl-pibathy`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Water surface to bottom substratum depth (i.e., water column depth) at the specific pixel location is specified.

Notes:

1. Specify whether a recalculation to a mean sea level has taken place for oceanic waters.
2. Specify whether a recalculation to a mean water surface level has taken place for any non-oceanic waters.
3. See @hartmann2022, @khazaei2022, @kim2024, @weatherall2015, @gebco2024, and @iho2024.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/optically-deep-shallow-assessment.yaml-->`2.17.` Optically Deep or Optically Shallow Assessment {#sec:pxl-podosas label="|Per-Pixel Metadata: Optically Deep or Optically Shallow Assessment"}

Identifier: `pxl-podosas`



##### Threshold requirements:

Information regarding whether pixels are optically deep or shallow is provided if there is an assumption during the processing that a pixel is optically deep or optically shallow.

Note:

1. See @kutser2020.


##### Goal requirements:

A flag that indicates optically deep and shallow waters is provided.

Note:

1. See @brando2009, @dekker2011, and @richardson2024.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/optical-water-type.yaml-->`2.18.` Optical Water Type {#sec:pxl-powaty label="|Per-Pixel Metadata: Optical Water Type"}

Identifier: `pxl-powaty`



##### Threshold requirements:

Specification of optical water type, when applicable (for optically deep waters).

Note:

1. See @hieronymi2024.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/turbid-water.yaml-->`2.19.` Turbid Water {#sec:pxl-pituwa label="|Per-Pixel Metadata: Turbid Water"}

Identifier: `pxl-pituwa`



##### Threshold requirements:

Specification of whether a pixel is assessed as being turbid.

Notes:

1. See @morel2006, @morel2008, and @hooker2003.
2. References for the corresponding flag algorithms are @hudson2016 and @shi2007, respectively.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/per-pixel/elevation-water.yaml-->`2.20.` Elevation {#sec:pxl-piwaele label="|Per-Pixel Metadata: Elevation"}

Identifier: `pxl-piwaele`



##### Threshold requirements:

Specification of approximate elevation (above mean sea level) of the surface of the water body pixels is required for atmospheric correction (range = -430 m to approx. 6500 m)

Note:

1. See @guth2021.


##### Goal requirements:


As threshold.
<!-- *None* -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/products-algorithms.yaml-->`3.` Products and Algorithms {#sec:pral label="|Products and Algorithms"}

The following requirements must be met for all pixels in a collection. The requirements specify both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes.

Metadata must contain a single DOI landing page with relevant information to support each requirement. For corrections, references to a citable peer-reviewed algorithm or technical documentation regarding the implementation of that algorithm and the sources of ancillary data used to make corrections/provision of parameterisation data are required. Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/measurement-ar.yaml-->`3.1.` Measurement {#sec:pral-measur-ar label="|Products and Algorithms: Measurement"}

Identifier: `pral-measur-ar`



##### Threshold requirements:

Pixel values that are expressed as a measurement of the Aquatic Reflectance (dimensionless) or the Remote Sensing Reflectance ($sr^{-1}$) of the water bodies ($AR = \pi \cdot R_{rs}$).

Note:

1. Radiometric corrections must lead to a valid measurement of aquatic reflectance.


##### Goal requirements:

As threshold.

Note:

1. See also [@sec:meta-trace-ar] and [@sec:pral-mnormal-ar]

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/uncertainty-ar.yaml-->`3.2.` Measurement Uncertainty {#sec:pral-muncer-ar label="|Products and Algorithms: Measurement Uncertainty"}

Identifier: `pral-muncer-ar`



##### Threshold requirements:

An estimate of the uncertainty of the values is provided in measurement units, following the BIPM Guide to the Expression of Uncertainty in Measurement (GUM).

Notes:

1. In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.
2. See @gum_6_2020 and @vabson2024.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/measurements/normalisation-ar.yaml-->`3.3.` Measurement Normalisation {#sec:pral-mnormal-ar label="|Products and Algorithms: Measurement Normalisation"}

Identifier: `pral-mnormal-ar`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Measurements are normalised (to nadir) to remove the effect of bidirectional dependence of the upwelling radiance on observation and solar-illumination geometries.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/directional-atmospheric-scattering-ar.yaml-->`3.4.` Directional Atmospheric Scattering {#sec:pral-dirats-ar label="|Products and Algorithms: Directional Atmospheric Scattering"}

Identifier: `pral-dirats-ar`



##### Threshold requirements:

Specification of corrections applied for molecular (Rayleigh) scattering and for aerosol scattering and absorption..

Note:

1. See @mobley2016.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/water-vapour-ar.yaml-->`3.5.` Water Vapour Corrections {#sec:pral-wavap-ar label="|Products and Algorithms: Water Vapour Corrections"}

Identifier: `pral-wavap-ar`



##### Threshold requirements:

Corrections are applied for water vapour if spectral bands are affected.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/ozone-ar.yaml-->`3.6.` Ozone Corrections {#sec:pral-cozone label="|Products and Algorithms: Ozone Corrections"}

Identifier: `pral-cozone`



##### Threshold requirements:

Data is corrected for ozone if spectral bands are affected.

Notes:

1. Relevant metadata must be provided in [@sec:meta-geounc] and [@sec:meta-instru-ar].
2. See @dekeukelaere2018, @harmel2018, @mobley2016, @pahlevan2017, @pahlevan2021, and @vanhellemont2019.


##### Goal requirements:


As threshold.
<!-- *None* -->

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/gaseous-absorption.yaml-->`3.7.` Other Gaseous Absorption Corrections {#sec:pral-ogasab label="|Products and Algorithms: Other Gaseous Absorption Corrections"}

Identifier: `pral-ogasab`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Data is corrected for other trace gaseous absorption for affected spectral bands.

Notes:

1. Relevant metadata must be provided in [@sec:meta-geounc] and [@sec:meta-instru-ar].
2. See @dekeukelaere2018, @harmel2018, @mobley2016, @pahlevan2017, and @pahlevan2021.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/sun-glint.yaml-->`3.8.` Sun Glint Correction {#sec:pral-cosungli label="|Products and Algorithms: Sun Glint Correction"}

Identifier: `pral-cosungli`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

Sun glint is removed from the data if a pixel is of correctable (i.e., not radiometrically saturating) sun glint.

Notes:

1. Sun glint removal methods can only partially remove sun glint from a pixel. Over or under correction may occur.
2. See [@sec:pxl-pisungli], @botha2016, @groetsch2020, @harmel2018, @kay2009, @kutser2009, and @lavender2010glint.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/sky-glint.yaml-->`3.9.` Sky Glint Correction {#sec:pral-coskygli label="|Products and Algorithms: Sky Glint Correction"}

Identifier: `pral-coskygli`



##### Threshold requirements:

Specification of whether or not sky glint is implicitly corrected for in the atmospheric correction procedure

Notes:

1. Sky glint is often modelled in forward models explicitly. It is also often measured with above surface spectroradiometers. However, sky glint is seldom corrected for separately in atmospheric and air-water interface correction methods.
2. See [@sec:pxl-piskygli], @gege2016, @groetsch2020, and @zhang2017.


##### Goal requirements:

Sky glint is separately assessed and corrected for in the data processing. The metadata indicates the surface contributions from sky glint removed from the data.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/whitecap-foam.yaml-->`3.10.` Whitecap / Foam Correction {#sec:pral-cowhifo label="|Products and Algorithms: Whitecap / Foam Correction"}

Identifier: `pral-cowhifo`



##### Threshold requirements:

Specification of whether the water leaving reflectance or radiance is corrected for the contribution from surface whitecaps and foam.

Note:

1. See @dierssen2019, @dierssen2021, @frouin2019, @koepke1984, @moore2000, @wang2017, @eumetsat2021, and @lavender2010whitecaps.


##### Goal requirements:

The data are corrected for the contribution from surface whitecaps and foam and reported on a per-pixel basis.

Note:

1. See [@sec:pxl-piwhifo].

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/adjacency-effects.yaml-->`3.11.` Adjacency Effects Correction {#sec:pral-cajdeff label="|Products and Algorithms: Adjacency Effects Correction"}

Identifier: `pral-cajdeff`



##### Threshold requirements:


Not required.
<!-- *None* -->


##### Goal requirements:

The data are corrected for adjacency effects.

Note:

1. See @castagna2025, @kiselev2015, @pan2025, @sterckx2015, and @wu2024.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/turbid-water.yaml-->`3.12.` Turbid Water Reflectance Correction {#sec:pral-cotuwa label="|Products and Algorithms: Turbid Water Reflectance Correction"}

Identifier: `pral-cotuwa`



##### Threshold requirements:

Specification of whether the atmospheric correction accounted for a pixel being turbid or not.

Note:

1. See @gossn2019, @moore1999, and @stumpf2003.


##### Goal requirements:


As threshold.
<!-- *None* -->

### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/sections/requirement-categories/geometric-corrections-metadata.yaml-->`4.` Geometric Corrections Metadata (Co-Registration and Ortho-Rectification) {#sec:gcom label="|Geometric Corrections Metadata (Co-Registration and Ortho-Rectification)"}

Geometric corrections must place the measurement accurately on the surface of the Earth (that is, geolocate the measurement) allowing measurements taken through time to be compared. Ocean and coastal imagery do not have an independent terrestrial referencing system and therefore [@sec:gcom-corore] applies to that imagery.


#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/geometric-ar.yaml-->`4.1.` Geometric Correction {#sec:gcom-geocorr-ar label="|Geometric Corrections Metadata (Co-Registration and Ortho-Rectification): Geometric Correction"}

Identifier: `gcom-geocorr-ar`



Applies for:

1. land 
2. inland waters where an independent terrestrial referencing system is available

##### Threshold requirements:

Sub-pixel uncertainty is achieved in **relative** geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.

Sub-pixel uncertainty is taken to be less than or equal to 0.5-pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.

A consistent gridding/sampling frame is used, including common cell size, origin, and nominal sample point location within the cell (centre, ll, ur).

Relevant metadata must be provided under [@sec:meta-geounc] and [@sec:meta-instru-ar].

Notes:

1. The threshold level will not necessarily enable interoperability between data from **different** sources as the geometric corrections for each of the sources may differ.
2. It is useful to note if the sensor is used at its native resolution before geometric correction or that some resampling must be done.


##### Goal requirements:

Sub-pixel uncertainty is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).

Relevant metadata must be provided under [@sec:meta-geounc] and [@sec:meta-instru-ar].

Note:

1. This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction and with non-image spatial data such as GIS layers and terrain models.

---

#### <!-- edit:/home/runner/work/ceos-ard/ceos-ard/requirements/corrections/coregistration-orthorectification.yaml-->`4.2.` Co-Registration and Ortho-Rectification {#sec:gcom-corore label="|Geometric Corrections Metadata (Co-Registration and Ortho-Rectification): Co-Registration and Ortho-Rectification"}

Identifier: `gcom-corore`



##### Threshold requirements:

Co-registration is performed to ensure consistency of pixel location in each spectral band of one image at 0.5 GSD.

Ortho rectification specifies the pointing accuracy related to a geographic reference grid. The associated uncertainty is pixel size dependent and therefore cannot be given an a priori measure of uncertainty.

The specifications of the co-registration and ortho-rectification processing (including parameterisation data) must be provided, including the estimated uncertainty of each processing, in publicly available documentation.

Note:

1. Including but not limited to ocean-to-sea to coastal, estuarine, deltaic, lagoonal waters and inland water bodies such as canals, rivers, lakes and reservoirs.


##### Goal requirements:

Co-registration is performed to ensure consistency of pixel location in each spectral band of one image at 0.2 GSD.

Ortho rectification specifies the pointing accuracy related to a geographic reference grid. The associated uncertainty is pixel size dependent and therefore cannot be given an a priori measure of uncertainty.

The specifications of the co-registration and ortho-rectification processing (including parameterisation data) must be provided, including the estimated uncertainty of each processing, in publicly available documentation.

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

