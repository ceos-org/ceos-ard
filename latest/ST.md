---
title: CEOS-ARD - Optical - Surface Temperature
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

> CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.

&nbsp;

**Product Family Specification:**
Optical, Surface Temperature (ST)

**Applies to:**
Data collected with multispectral sensors operating in the thermal infrared (TIR) wavelengths.
These typically operate with ground sample distance and resolution in the order of 10-100m;
however, the Specification is not inherently limited to this resolution.

At present, surface temperature measurements tend to be provided as either surface brightness temperature (SBT) or as land surface temperatures (LST) requiring the SBT to be modified according to the emissivity of the target.
This specification identifies the Surface Temperature (ST) as being the minimum or Threshold requirement for analysis ready land surface data. Nevertheless, both SBT and LST are land measurements, requiring atmospheric corrections.

&#12;

## Document History

Not available yet

## Contributing Authors

- Geoscience Australia, Australia
  - Adam Lewis
  - Jonathon Ross
  - Andreia Siqueira
- USGS, USA
  - Darcie Bontje
  - Steve Labahn
  - Mary Metzger

&#12;

## Glossary

CEOS-ARD
:   Committee on Earth Observation Satellites - Analysis Ready Data

DOI
:   Digital Object Identifier

LST
:   Land Surface Temperature

SBT
:   Surface Brightness Temperature

SI
:   International System of Units, internationally known by the abbreviation SI (from French Système international d'unités)

ST
:   Surface Temperature

TIR
:   Thermal Infrared

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


#### `1.1.` General Metadata: Traceability {#sec:meta.metadata-traceability-st label="|General Metadata: Traceability"}

Identifier: `meta.metadata-traceability-st`


##### Threshold requirements:


*None*


##### Goal requirements:

Data must be traceable to SI reference standard.
- [Policy on measurement traceability](https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6536) - [Guidance on measurement traceability](https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6532)

Notes:

1. Relationship to [@sec:rac.measurements-uncertainty-st]. Traceability requires an estimate of measurement uncertainty.
2. Information on traceability should be available in the metadata as a single DOI landing page.

### `2.` Source Metadata {#sec:src label="|Source Metadata"}

These are metadata records describing (detailing) **each** acquisition (source data) used to generate the ARD product.
This may be one or mutliple acquisitions.


#### `2.1.` Source Metadata: Example Requirement {#sec:src.example label="|Source Metadata: Example Requirement"}

Identifier: `src.example`


This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### `3.` Product Metadata {#sec:prd label="|Product Metadata"}

Information related to the CEOS-ARD product generation procedure and geographic parameters.


#### `3.1.` Product Metadata: Example Requirement {#sec:prd.example label="|Product Metadata: Example Requirement"}

Identifier: `prd.example`


This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### `4.` Per-Pixel Metadata {#sec:pxl label="|Per-Pixel Metadata"}

The following minimum metadata specifications apply to each pixel.
Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider.
Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications.


#### `4.1.` Per-Pixel Metadata: Example Requirement {#sec:pxl.example label="|Per-Pixel Metadata: Example Requirement"}

Identifier: `pxl.example`


This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

### `5.` Radiometric and Atmospheric Corrections {#sec:rac label="|Radiometric and Atmospheric Corrections"}

The following requirements must be met for all pixels in a collection.
The requirements indicate both the necessary outcomes and the minimum steps necessary to be deemed to have achieved those outcomes. Radiometric corrections must lead to a valid measurement of surface reflectance.


#### `5.1.` Radiometric and Atmospheric Corrections: Measurement Uncertainty {#sec:rac.measurements-uncertainty-st label="|Radiometric and Atmospheric Corrections: Measurement Uncertainty"}

Identifier: `rac.measurements-uncertainty-st`


Note: In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.

##### Threshold requirements:


*None*


##### Goal requirements:

Uncertainty, in Kelvin, of the surface temperature measurement for each pixel is provided.

Notes:

1. Some of the intent of the initial wording (below), which refers to atmospheric windows, may have been lost: Uncertainty, in units Kelvin, of the surface temperature for each pixel is also accompanied by distance from cloud (above) and atmospheric transmission (intervals, i.e., 0.4 - 0.55, 0.55 - 0.7, etc.).

### `6.` Geometric Corrections {#sec:gcor label="|Geometric Corrections"}

The geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared.
This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready.


#### `6.1.` Geometric Corrections: Example Requirement {#sec:gcor.example label="|Geometric Corrections: Example Requirement"}

Identifier: `gcor.example`


This is an example requirement.

##### Threshold requirements:

This is a threshold requirement.


##### Goal requirements:

This is a goal requirement.

Notes:

1. This is a note.

&#12;


## References

::: {#refs}
:::

&#12;

## Annexes

### CEOS-ARD ST Requirement Examples {#sec:annex-st-metadata-examples label="|CEOS-ARD ST Requirement Examples"}

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


