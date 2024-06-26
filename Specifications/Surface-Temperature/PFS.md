---
title: CEOS-ARD Product Family Specification
subtitle: Surface Temperature
---

![CEOS Analysis Ready Data](../../Logo/CEOS_ARD_Logo_for_PFS.png)

## Document History

| Version                | Date                                        | Description of Change                                        | Author                                   |
| :--------------------- | :------------------------------------------ | :----------------------------------------------------------- | :--------------------------------------- |
| 0.0.2                 | 23.03.2017                                 | Zero Draft based on materials provided by Geoscience Australia and the USGS in particular. | Ross                                     |
|                        | 16.04.2017                                 | Included document history;                                   |                                          |
| 1.0.0                 | 18.04.2017                                 | Revised to:&#10;- Formatting and structure&#10;- Included guidance section | Lewis                                    |
| 1.0.1                 | 18.04.2017                                 | Merged ‘geometric source’ and ‘geometric method’ elements.   | Lewis                                    |
| 2.0                   | 25.08.2017                                 | Incorporated first round of revisions following feedback from the UK and others. | Lewis                                    |
| 2.1                   | 06.09.2017                                 | Feedback from ESA; removed reference to bands (1.10) as these are not relevant to ST; Feedback on 1.13 included to the effect that ST algorithm may not be supplied at Threshold level. Added qualifying notes to 2.7,2.8. | Lewis                                    |
| 3.0                   | 05.12.2017                                 | Feedback during the teleconference.                          | Lewis                                    |
| 3.1                   | 22.12.2017                                 | Feedback during and after (emails) the teleconference (05/12/2017) included. | Siqueira                                 |
| 3.2                   | 01.08.2018                                 | Outcome from LSI-VC-6 meeting addressed: *Surface Brightness Temperature (SBT) is not needed as a CARD4L product – there is no clear user base. The Surface Temperature (ST) PFS will be retained, with references to SBT removed in the next update cycle."* Therefore, ST became the minimum requirement (threshold) for CARD4L ST PFS. | Siqueira                                 |
| 3.3                   | 21.01.2019                                 | Feedback from ESA and USGS self-assessment included. Added Annex 1 containing examples (provided by USGS and ESA) on selected requirements. | Siqueira                                 |
| 3.3.1                 | 06.02.2019                                 | Final draft shared with LSI-VC list and LSI-VC-7 meeting participants seeking support for document endorsement at the LSI-VC-7 meeting. | Siqueira                                 |
| 3.3.1                 | 20.02.2019                                 | Comments and suggestions from LSI-VC-7 meeting (minutes) and feedback from USGS incorporated. | Siqueira                                 |
| 3.3.2                 | 28.02.2019                                 | Formatting and verbiage updates for consistency.             | Metzger                                  |
| 4.0                   | 02.03.2019                                 | Version endorsed at LSI-VC7 meeting (14Feb 2019)             | LSI-VC                                   |
| 4.1                   | 26.06.2019                                 | Added self-assessment columns                                | Bontje                                   |
| 4.2                   | 04.09.2019                                 | Requirement 3.2 (Corrections for Atmosphere and Emissivity) rewording - agreed at LSI-VC8 meeting. | Siqueira                                 |
| 4.3&#10;4.4&#10;5.0 | 08.05.2020&#10;25.05.2020&#10;08.06.2020 | This review cycle considers feedback received from USGS and ESA after the formal self-assessment for Surface Temperature products (Landsat and Sentinel-2). Minor editorial changes were done throughout the document. Requirements 1.2, 1.14, 1.16 and 2.1 have been updated.&#10;Feedback from USGS added (email: 21/05/2020).&#10;Tech edit. | Siqueira&#10;Siqueira&#10;Bontje, Labahn |

## Contributing Authors

- Adam Lewis, Geoscience Australia, Australia
- Jonathon Ross, Geoscience Australia, Australia
- Andreia Siqueira, Geoscience Australia, Australia
- Darcie Bontje, USGS, USA
- Steve Labahn, USGS, USA
- Mary Metzger, USGS, USA

## Description

**Product Family Title: Surface Temperature (CARD4L-ST)**

**Applies to:** Data collected with multispectral sensors operating in the thermal infrared (TIR) wavelengths. These typically operate with ground sample distance and resolution in the order of 10-100m; however, the Specification is not inherently limited to this resolution.

At present, surface temperature measurements tend to be provided as either surface brightness temperature (SBT) or as land surface temperatures (LST) requiring the SBT to be modified according to the emissivity of the target. This specification identifies the Surface Temperature (ST) as being the minimum or Threshold requirement for analysis ready land surface data. Nevertheless, both SBT and LST are *land* measurements, requiring atmospheric corrections.

&#12;

## Definitions

|            Term            | Description                                                  |
| :------------------------: | :----------------------------------------------------------- |
|            LST             | Land Surface Temperature                                     |
|             ST             | Surface Temperature                                          |
|            SBT             | Surface Brightness Temperature                               |
|       Ancillary Data       | Ancillary data is data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information and data from other instruments. |
|       Auxiliary Data       | Auxiliary data is the data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources. |
|          Metadata          | Metadata is structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content. |
|            MTF             | Modulation Transfer Function                                 |
|    Spectral Resolution     | Spectral resolution defines the narrowest spectral feature that can be resolved by a spectrometer. |
|     Spatial Resolution     | The highest magnification of the sensor at the ground surface. |
| Spectral Sampling Distance | Spectral sampling is the interval, in wavelength units, between discrete data points in the measured spectrum. |
| Spatial Sampling Distance  | Spatial sampling distance is the barycentre-to-barycentre distance between adjacent spatial samples on the Earth's surface. |

&#12;

## Requirements

### General Metadata

*These are metadata records describing a distributed collection of pixels. The collection of pixels referred to must be contiguous in space and time. General Metadata should allow the user to assess the overall suitability of the dataset, and must meet the following requirements:*

|    #     |                Item                | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :------: | :--------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **1.1**  |          **Traceability**          | Not required.                                                | Data must be traceable to SI reference standard. Information on traceability should be available in the metadata as a single DOI landing page.&#10;Policy on measurement traceability: <https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6536>&#10;Guidance on measurement traceability: <https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6532>&#10;*Note 1: SI Traceability requires an estimate of measurement uncertainty.* |                           |                        |                                            |                                      |
| **1.2**  |  **Metadata Machine Readability**  | Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use. | As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2. |                           |                        |                                            |                                      |
| **1.3**  |      **Data Collection Time**      | The start and stop time of data collection is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified. | Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second. |                           |                        |                                            |                                      |
| **1.4**  |       **Geographical Area**        | The surface location to which the data relate is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84 coordinates). | The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) expressed in projection coordinates with reference datum. |                           |                        |                                            |                                      |
| **1.5**  |  **Coordinate Reference System**   | The metadata lists the coordinate reference system that has been used. | As threshold.                                                |                           |                        |                                            |                                      |
| **1.6**  |         **Map Projection**         | Not required.                                                | The metadata lists the map projection that has been used, if any, and any relevant parameters required in relation to use of data in that map projection. |                           |                        |                                            |                                      |
| **1.7**  |  **Geometric Correction Methods**  | Not required.&#10;The user is not explicitly advised of the geometric correction source and methods. | Information on geometric correction methods should be available in the metadata as a single DOI landing page containing information on geodetic correction methods used, including reference database and auxiliary data such as elevation model(s) and reference chip-sets. |                           |                        |                                            |                                      |
| **1.8**  | **Geometric Accuracy of the Data** | Not required.&#10;The user is not provided with results of geometric correction processes pertaining to the dataset. | The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data. Accuracy is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed as root mean square error (RMSE) or Circular Error 90% Probability (CEP90).&#10;*Note 1: Information on geometric accuracy of the data should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.9**  |           **Instrument**           | The instrument used to collect the data is identified in the metadata. | As threshold, but information on instrument should be available in the metadata as a single DOI landing page with references to the relevant CEOS Missions, Instruments and Measurements Database record. |                           |                        |                                            |                                      |
| **1.10** |         **Spectral Bands**         | The central wavelength for each band for which data is included is identified in the metadata, expressed in SI units. | As threshold, with instrument spectral response details (e.g., full spectral response function) also included or directly accessible using details in the metadata.&#10;Central wavelength and bandwidth at full-width half maximum value of the relative spectral response function are provided at least.&#10;*Note 1: Information on spectral bands should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.11** |       **Sensor Calibration**       | Not required.                                                | Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata. Ideally this would support machine-to-machine access.&#10;*Note 1: Information on sensory calibration should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.12** |      **Radiometric Accuracy**      | Not required.&#10;The general metadata does not include information on the radiometric accuracy of the data. | Information on radiometric accuracy should be available in the metadata as a single DOI landing page providing information on metrics describing the assessed absolute radiometric accuracy of the data, expressed as absolute radiometric uncertainty relative to a known reference standard.&#10;*Note 1: For example, this may come from comparison with routine and rigorously collected in situ measurements.* |                           |                        |                                            |                                      |
| **1.13** |           **Algorithms**           | All algorithms and versions, and the sequence in which they were applied in the generation process, are identified in the metadata. | As threshold, but only algorithms that have been published in a peer-reviewed journal.&#10;*Note 1: It is possible that high-quality corrections are applied through non-disclosed processes*. *CARD4L does not per-se require full and open data and methods.*&#10;*Note 2: Information on algorithms should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.14** |         **Auxiliary Data**         | The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as a single DOI landing page.&#10;*Note 1: Auxiliary data includes DEMs, aerosols, etc. data sources.* | As threshold, but information on auxiliary data should be available in the metadata as a single DOI landing page and is also available for free online download, contemporaneously with the product or through a link to the source. |                           |                        |                                            |                                      |
| **1.15** |  **Processing Chain Provenance**   | Not required.                                                | Information on processing chain provenance should be available in the metadata as a single DOI landing page containing description of the processing chain used to generate the product, including the versions of the software used and information on the data collection baseline, giving full transparency to the users. |                           |                        |                                            |                                      |
| **1.16** |          **Data Access**           | Information on data access should be available in the metadata as a single DOI landing page.&#10;*Note 1: Manual and offline interaction action (e.g., login) may be required.* | As threshold.                                                |                           |                        |                                            |                                      |
| **1.17** |      **Overall Data Quality**      | Not applicable.                                              | The metadata includes details of the quality of the product based on quantitative assessment of the product with respect to high quality reference data with full traceability of the uncertainties. Validation and intercomparison statistics can provide the necessary quantification. |                           |                        |                                            |                                      |

### Per-Pixel Metadata

*Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for application and includes ‘quality flags’. The following minimum metadata specifications apply to each pixel. Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider. Similarly, the mechanism or form of the per-pixel metadata (additional data bands, mask layers, etc.) is open to the provider.* 

|    #    |               Item               | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :-----: | :------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **2.1** | **Metadata Machine Readability** | Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.2** |           **No Data**            | Pixels that do not correspond to an observation (‘empty pixels’) are flagged. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.3** |      **Incomplete Testing**      | The metadata identifies pixels for which the per-pixel tests (below) have not all been successfully completed.&#10;*Note 1: e.g., due to missing ancillary data for some pixels.* | The metadata identifies which tests have, and have not, been successfully completed for each pixel. |                           |                        |                                            |                                      |
| **2.4** |          **Saturation**          | Metadata indicates where one or more pixel in the input spectral bands are saturated. | Metadata indicates which pixels are saturated for each spectral band. |                           |                        |                                            |                                      |
| **2.5** |            **Cloud**             | Metadata indicates whether a pixel is assessed as being cloud. | As threshold, but information on cloud detection should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **2.6** |         **Cloud Shadow**         | Metadata indicates whether a pixel is assessed as being cloud shadow. | As threshold, but information on cloud shadow detection should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **2.7** |       **Snow/  Ice mask**        | Not required.                                                | The metadata indicates whether a pixel is assessed as being snow/ice or not. Information on snow/ice mask should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **2.8** |  **Solar and Viewing Geometry**  | Provide average solar and sensor viewing azimuth and zenith angles. | Provide per-pixel solar and sensor viewing azimuth and zenith angles. |                           |                        |                                            |                                      |


### Radiometric and Atmospheric Corrections

*The following requirements must be met for all pixels in a collection. Radiometric corrections must lead to a valid measurement of surface temperature.*

|    #    |                     Item                      | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :-----: | :-------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **3.1** |                **Measurement**                | Pixel values are expressed as a measurement of the Surface Temperature of the land, expressed as Kelvin. | Surface temperature measurements are SI traceable (see also 1.1). |                           |                        |                                            |                                      |
| **3.2** | **Corrections for Atmosphere and Emissivity** | Retrieval methods for estimating surface temperature are provided.&#10;*Note 1: The metadata references (may be through a single DOI landing page) a citable peer-reviewed algorithm.* | As threshold.                                                |                           |                        |                                            |                                      |
| **3.3** |          **Measurement Uncertainty**          | Not required.                                                | Uncertainty, in Kelvin, of the surface temperature measurement for each pixel is provided.&#10;*Note 1: Some of the intent of the initial wording (below), which refers to atmospheric windows, may have been lost:*&#10;*Uncertainty, in units Kelvin, of the surface temperature for each pixel is also accompanied by distance from cloud (above) and atmospheric transmission (intervals, i.e., 0.4 - 0.55, 0.55 - 0.7, etc.).* |                           |                        |                                            |                                      |

### Geometric Corrections
*Geometric corrections must place the measurement accurately on the surface of the Earth (that is, geolocate the measurement) allowing measurements taken through time to be compared.* 

|    #    |           Item           | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :-----: | :----------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **4.1** | **Geometric Correction** | Sub-pixel accuracy is achieved in relative geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.&#10;Sub-pixel accuracy is taken to be less than or equal to 0.5 pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.&#10;A consistent gridding/sampling frame is necessary to meet this requirement.&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;*Note 1: The threshold level will not necessarily enable interoperability between data from* different *sources as the geometric corrections for each of the sources may differ.* | Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).&#10;A consistent gridding/sampling frame is necessary to meet this requirement.&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;*Note 1: This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction, and with non-image spatial data such as GIS layers and terrain models.* |                           |                        |                                            |                                      |

## Summary Self-Assessment Table

### 1. General Metadata

|                                    | Threshold | Target |
| :--------------------------------- | :-------: | :----: |
| 1.1 Traceability                   |           |        |
| 1.2 Metadata Machine Readability   |           |        |
| 1.3 Data Collection Time           |           |        |
| 1.4 Geographical Area              |           |        |
| 1.5 Coordinate Reference System    |           |        |
| 1.6 Map Projection                 |           |        |
| 1.7 Geometric Correction Methods   |           |        |
| 1.8 Geometric Accuracy of the Data |           |        |
| 1.9 Instrument                     |           |        |
| 1.10 Spectral Bands                |           |        |
| 1.11 Sensor Calibration            |           |        |
| 1.12 Radiometric Accuracy          |           |        |
| 1.13 Algorithms                    |           |        |
| 1.14 Auxiliary Data                |           |        |
| 1.15 Processing Chain Provenance   |           |        |
| 1.16 Data Access                   |           |        |
| 1.17 Overall Data Quality          |           |        |

### 2. Per-Pixel Metadata

|                                  | Threshold | Target |
| :------------------------------- | :-------: | :----: |
| 2.1 Metadata Machine Readability |           |        |
| 2.2 No Data                      |           |        |
| 2.3 Incomplete Testing           |           |        |
| 2.4 Saturation                   |           |        |
| 2.5 Cloud                        |           |        |
| 2.6 Cloud Shadow                 |           |        |
| 2.7 Snow/Ice Mask                |           |        |
| 2.8 Solar and Viewing Geometry   |           |        |

### 3. Radiometric and Atmospheric Corrections

|                                               | Threshold | Target |
| :-------------------------------------------- | :-------: | :----: |
| 3.1 Measurement                               |           |        |
| 3.2 Corrections for Atmosphere and Emissivity |           |        |
| 3.3 Measurement Uncertainty                   |           |        |

### 4. Geometric Corrections

|                          | Threshold | Target |
| :----------------------- | :-------: | :----: |
| 4.1 Geometric Correction |           |        |

&#12;

## Guidance

This section aims to provide background and specific information on the processing steps that can be used to achieve analysis ready data. This Guidance material does not replace or override the specifications.

## Introduction to CARD4L

### What is CEOS Analysis Ready Data for Land (CARD4L) products?

CARD4L products have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort. These products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets.

CARD4L products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development. They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures. They may not be suitable for all purposes and are not intended as a ‘replacement’ for other types of satellite products.

### When can a product be called CARD4L?

The CARD4L branding is applied to a particular product once:

- that product has been assessed as meeting CARD4L requirements by the agency responsible for production and distribution of the product, and
- that assessment has been peer reviewed by the CEOS Land Surface Imaging Virtual Constellation in consultation with the CEOS Working Group on Calibration and Validation.

Agencies or other entities considering undertaking an assessment process should contact the co-leads of the [Land Surface Imaging Virtual Constellation](http://ceos.org/ourwork/virtual-constellations/lsi/). 

A product can continue to use CARD4L branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

### What is the difference between Threshold and Target?

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making. 

Products that meet target requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the *threshold* level. 

Target requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, *target* specifications may (and subject to due process) become accepted as *threshold* requirements.

## Procedural Examples

Processes to produce Threshold Surface Temperature CARD4L-ST.

The following correction processes would typically be applied to produce CARD4L-ST Threshold:

- *No example processes are provided at this time.*

## Specific Examples

Processes to produce Threshold Surface Temperature CARD4L-ST:

- *No example processes are provided at this time.*

## Reference papers

The following papers provide scientific and technical guidance:

1. Cook, M., Schott, J.R, Mandel, J., Raqueno, M. (2014). Development of an Operational Calibration Methodology for the Landsat Thermal Data Archive and Initial Testing of the Atmospheric Compensation Component of a Land Surface Temperature (LST) Product from the Archive. ***Remote Sensing*** 6 (11244-11266). doi:10.3390/rs61111244 ISSN 2072-4292. [www.mdpi.com/journal/remotesensing](http://www.mdpi.com/journal/remotesensing)
2. Li et al., (2013) Satellite-derived land surface temperature: Current status and perspectives. ***Remote Sensing of Environment*** 131 14–37. <https://doi.org/10.1016/j.rse.2012.12.008>.
