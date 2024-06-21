![CEOS Analysis Ready Data](../../Logo/CEOS_ARD_Logo_blue_lowres.png)
# CEOS-ARD Product Family Specification: Aquatic Surface Reflectance

## Document History

| Version | Date       | Description of Change | Author                                                       |
| :------ | :--------- | :-------------------- | :----------------------------------------------------------- |
| 1.0     | 2 Feb 2022 | Initial version.      | Andreia Siqueira (GA), Christopher Barnes (USGS/KBR), Steve Labahn, (USGS) Arnold Dekker (SatDek), Barbara Bulgarelli (JRC-EC), Carsten Brockmann (Brockmann Consulting), Daniela Gurlin (Wisconsin DNR), Joseph D. Ortiz (Kent State), Igor Ogashawara (IGB Berlin), Anthony Vodacek (RIT), Nima Pahlevan (NASA), Liesbeth de Keukelare (VITO), Ils Reusen (VITO), Steef Peters (WaterInsight), Claudia Giardino (CNR), Tiit Kutser (WaterForCE), Steve Greb (UW-Madison), Sindy Sterckx (VITO), Vittorio E. Brando (CNR), Merrie-Beth Neely (GeoAquaWatch), Paul Digiacomo (NOAA) |

## Authors

- Andreia Siqueira, GA
- Christopher Barnes, USGS/KBR, USA
- Steve Labahn, USGS, USA
- Arnold Dekker, SatDek, Australia
- Barbara Bulgarelli, JRC-EC
- Carsten Brockmann, Brockmann Consulting, Germany
- Daniela Gurlin, Wisconsin DNR, USA
- Joseph D. Ortiz, Kent State, USA
- Igor Ogashawara, IGB Berlin, Germany
- Anthony Vodacek, RIT, USA
- Nima Pahlevan, NASA, USA
- Liesbeth de Keukelare, VITO, Belgium
- Ils Reusen, VITO, Belgium
- Sindy Sterckx, VITO, Belgium
- Steef Peters, WaterInsight,
- Claudia Giardino, CNR, Italy
- Vittorio E. Brando, CNR, Italy
- Tiit Kutser, WaterForCE
- Steve Greb, UW-Madison, USA
- Merrie-Beth Neely, GeoAquaWatch, USA
- Paul Digiacomo, NOAA, USA

## Description

**Product Family Title: Aquatic Reflectance (CARD4L-AR)**

**Applies to:** Data collected with multispectral and hyperspectral sensors operating in the VIS/NIR/SWIR wavelengths over water bodies. These typically operate with ground sample distance and resolution in the order of 10-1000 m; however, the specification is not inherently limited to this resolution.

&#12;
## Definitions

|            Term            | Description                                                  |
| :------------------------: | :----------------------------------------------------------- |
|             AR             | Aquatic Reflectance                                          |
|       Ancillary Data       | Data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information, and data from other instruments. |
|       Auxiliary Data       | The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources. |
|          Metadata          | Structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content. |
|            MTF             | Modulation Transfer Function                                 |
|    Spectral Resolution     | Defines the narrowest spectral feature that can be resolved by a spectrometer. |
|     Spatial Resolution     | The highest magnification of the sensor at the ground surface. |
| Spectral Sampling Distance | Spectral sampling is the interval, in wavelength units, between discrete data points in the measured spectrum. |
| Spatial Sampling Distance  | Spatial sampling distance is the barycentre-to-barycentre distance between adjacent spatial samples on the Earth's surface. |

&#12;
## Requirements

### General Metadata

*These are metadata records describing a distributed collection of pixels. The collection of pixels referred to must be contiguous in space and time. General metadata should allow the user to assess the **overall** suitability of the dataset, and must meet the following requirements:*

|    #     |                Item                | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :------: | :--------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **1.1**  |          **Traceability**          | Not required.                                                | Data must be traceable to SI reference standard.&#10;*Note 1: Relationship to 3.2. Traceability requires an estimate of measurement uncertainty.&#10;Note 2: Information on traceability should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.2**  |  **Metadata Machine Readability**  | Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use. | As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2. |                           |                        |                                            |                                      |
| **1.3**  |      **Data Collection Time**      | The data collection time is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified. | Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second. |                           |                        |                                            |                                      |
| **1.4**  |       **Geographical Area**        | The surface location to which the data relates is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84). | The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) with the projection system (if any) and reference datum provided. |                           |                        |                                            |                                      |
| **1.5**  |  **Coordinate Reference System**   | The metadata lists the coordinate reference system that has been used. | As threshold.                                                |                           |                        |                                            |                                      |
| **1.6**  |         **Map Projection**         | The metadata lists the map projection that has been used and any relevant parameters required in relation to use of data in that map projection. | As threshold.                                                |                           |                        |                                            |                                      |
| **1.7**  |  **Geometric Correction Methods**  | Not required.&#10;The user is not explicitly advised of the geometric correction source and methods. | Information on geometric correction methods should be available in the metadata as a single DOI landing page, including reference database and auxiliary data such as elevation model(s) and reference chip-sets. |                           |                        |                                            |                                      |
| **1.8**  | **Geometric Accuracy of the Data** | Not required.&#10;The user is not provided with results of geometric accuracy assessments pertaining to the dataset. | The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data. Accuracy is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed quantitatively, for example, as root mean square error (RMSE) or Circular Error Probability (CEP90, CEP95), etc.&#10;*Note 1: Information on geometric accuracy of the data should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.9**  |           **Instrument**           | The instrument used to collect the data is identified in the metadata. | As threshold, but information should be available in the metadata as a single DOI landing page with references to the relevant CEOS Missions, Instruments, and Measurements Database record. |                           |                        |                                            |                                      |
| **1.10** |         **Spectral Bands**         | The central wavelength and full width at half maximum for each spectral band for which data is included is identified in the metadata, expressed in SI units. | As threshold, with instrument spectral response details (e.g., full spectral response function) also included or directly accessible using details in the metadata.&#10;*Note 1: Information on spectral bands should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.11** |       **Sensor Calibration**       | Not required.  The general metadata does not include sensor calibration details. | Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata. Ideally this would support machine-to-machine access.&#10;*Note 1: Information on sensor calibration should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.12** |      **Radiometric Accuracy**      | The metadata provides the number of bits required (e.g., 8, 10, 12, 14, 16, etc.). | The metadata includes metrics describing the assessed absolute radiometric uncertainty of the version of the data or product, expressed as absolute radiometric uncertainty relative to appropriate, known reference sites and standards (for example, pseudo-invariant calibration sites, rigorously collected field spectra, PICS, Rayleigh, DCC, etc.)&#10;*Note 1: Information on radiometric accuracy should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.13** |           **Algorithms**           | All algorithms, and the sequence in which they were applied in the generation process, are identified in the metadata. For example, these may be available through Algorithm Theoretical Basis documents.&#10;*Note 1: Information on algorithms should be available in the metadata as a single DOI landing page.* | As threshold, but only algorithms that have been published in a peer-reviewed journal.&#10;*Note 1: It is possible that high-quality corrections are applied through non-disclosed processes. CARD4L does not per-se require full and open data and methods.*&#10;*Note 2: Information on algorithms should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **1.14** |         **Auxiliary Data**         | The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as a single DOI landing page.&#10;*Note 1: Auxiliary data includes DEMs, aerosols, land mask, bathymetry, NO₂, etc. data sources.* | As threshold, but information on auxiliary data should be available in the metadata as a single DOI landing page and is also available for free online download, contemporaneously with the product or through a link to the source. |                           |                        |                                            |                                      |
| **1.15** |  **Processing Chain Provenance**   | Not required.                                                | Information on processing chain provenance should be available in the metadata as a single DOI landing page containing detailed description of the processing steps used to generate the product, including the versions of software used, giving full transparency to the users. |                           |                        |                                            |                                      |
| **1.16** |          **Data Access**           | Information on data access should be available in the metadata as a single DOI landing page.&#10;*Note 1: Manual and offline interaction action (e.g., login) may be required.* | As threshold.                                                |                           |                        |                                            |                                      |
| **1.17** |      **Overall Data Quality**      | Machine-readable metrics describing the overall quality of the data are included in the metadata, at minimum the cloud cover extent, i.e.: &#10;- Proportion of observations over land and over water affected by non-target phenomena, e.g., cloud and cloud shadows. | As threshold.                                                |                           |                        |                                            |                                      |

### Per-Pixel Metadata

*The following minimum metadata specifications apply to each pixel. Whether the metadata are provided in a single record relevant to all pixels, or separately for each pixel, is at the discretion of the data provider. Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for application.*

|    #     |                            Item                             | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :------: | :---------------------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **2.1**  |              **Metadata Machine Readability**               | Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.2**  |                         **No Data**                         | Pixels that do not correspond to an observation (e.g., ‘empty pixels/invalid observation/below noise floor’) are flagged. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.3**  |                  **Per-pixel Assessment**                   | The metadata identifies pixels for which the per-pixel tests (below) have not all been successfully completed.&#10;*Note 1: This may be the result of missing ancillary data for a subset of the pixels.* | The metadata identifies which tests have, and have not, been successfully completed for each pixel. |                           |                        |                                            |                                      |
| **2.4**  |                       **Saturation**                        | Metadata indicates where one or more spectral bands are saturated. | Metadata indicates which pixels are saturated for each spectral band. |                           |                        |                                            |                                      |
| **2.5**  |                          **Cloud**                          | Metadata indicates whether a pixel is assessed as being cloud. | As threshold, information on cloud detection should be available in the metadata as a single DOI landing page along with the confidence in this assessment. Clouds and cirrus clouds are differentiated. |                           |                        |                                            |                                      |
| **2.6**  |                      **Cloud Shadow**                       | Metadata indicates whether a pixel is assessed as being cloud shadow. | As threshold, but information on cloud shadow detection should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **2.7**  |                     **Land/Water Mask**                     | The metadata indicates whether a pixel is assessed as being land or water. Information on land/water mask should be available in the metadata as a single DOI landing page. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.8**  |                **Sea/Lake/ River Ice Mask**                 | The metadata indicates whether a pixel is assessed as being sea/lake/river ice or not. Information on sea/lake/river ice mask should be available in the metadata as a single DOI landing page. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.9**  |                        **Sun Glint**                        | The metadata indicates whether a pixel is assessed as absent or correctable (moderate), or uncorrectable (severe) Sun glint.&#10;*Note 1: Sun glint is deemed uncorrectable if the upper limit of the dynamic range of a sensor is reached (i.e., saturation occurs).* | The metadata indicates the amount of Sun glint for each pixel and band. |                           |                        |                                            |                                      |
| **2.10** |                        **Sky Glint**                        | Not required.                                                | The metadata indicates the amount of sky glint for each pixel and band. |                           |                        |                                            |                                      |
| **2.11** |                   **Whitecap/ Foam Mask**                   | The metadata indicates whether a pixel is assessed as affected by whitecaps or foam as a function of the wind speed or other. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.12** |               **Solar and Viewing Geometry**                | The metadata provides average solar and sensor viewing azimuth and zenith angles. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.13** |                    **Adjacency Effects**                    | Not required.                                                | The metadata provides the risk of per-pixel adjacency effects contamination, through flagging to denote per-pixel minimum, medium or high adjacency effects contamination.&#10;*Note 1: This effect often occurs in increased turbid or optically shallow waters near shorelines that may confuse this assessment*. |                           |                        |                                            |                                      |
| **2.14** |          **Floating Vegetation/Surface Scum Mask**          | The metadata indicates whether a pixel is assessed as affected by floating vegetation/surface scum. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.15** |            **Aerosol Optical Depth Parameters**             | The metadata indicates either per-pixel spectral Aerosol Optical Depth (AOD), or per-pixel AOD (550nm) and Angstrom exponent. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.16** |                   **Deep/ Shallow Water**                   | Not required.                                                | The metadata indicates where available: the bottom depth referenced to the mean sea level for the oceans and referenced to mean levels for lakes. Information on bathymetry should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **2.17** |     **Optically Deep or Optically Shallow Assessment**      | The metadata indicates, based on likelihood (bathymetry maps and average $`K_d`$ (preferred) or based on turbidity or Secchi disk transparency), whether water pixels may be optically deep or optically shallow. This will most likely be bathymetry map contour based. | Based on an assessment from an inversion algorithm that estimates the optically deep or optically shallow per-pixel status. |                           |                        |                                            |                                      |
| **2.18** |                    **Turbid Water Flag**                    | The metadata indicates whether a pixel is assessed as being turbid or not. Information on turbid water mask should be available in the metadata as a single DOI landing page. | As threshold.                                                |                           |                        |                                            |                                      |
| **2.19** | **Bidirectional Reflectance Distribution Function Applied** | Not required.                                                | Metadata indicates which pixels are corrected for BRDF effects. |                           |                        |                                            |                                      |
| **2.20** |                     **Altitude (ASL)**                      | The metadata indicates approximate altitude (ASL) of water body pixels is required for atmospheric correction (range = -430 to \~6500m) | As threshold.                                                |                           |                        |                                            |                                      |

### Radiometric and Atmospheric Corrections

*The following requirements must be met for all pixels in a collection. The requirements indicate both the necessary outcomes (3.1-3.3) and the minimum steps necessary to be deemed to have achieved those outcomes (3.4 onwards). Radiometric corrections must lead to a valid measurement of aquatic reflectance.*

|    #     |                             Item                             | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **3.1**  |                       **Measurement**                        | Pixel values are expressed as a measurement of the Aquatic Reflectance ($`AR = \pi \cdot R_{rs}`$) or the Remote Sensing Reflectance ($`sr^{-1}`$) of the water bodies. This is a dimensionless value. | Aquatic Reflectance or Remote Sensing Reflectance measurements are SI traceable (see also 1.1). |                           |                        |                                            |                                      |
| **3.2**  |                 **Measurement Uncertainty**                  | Not required.&#10;*Note 1: In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.* | An estimate of the uncertainty of the values is provided in measurement units. Following Guide to the Expression of Uncertainty in Measurement (GUM).&#10;*Note 1: This is a requirement for SI traceability. See also 1.1.*&#10;*Note 2: Information on measurement uncertainty should be available in the metadata as a single DOI landing page.* |                           |                        |                                            |                                      |
| **3.3**  |                **Measurement Normalisation**                 | Not required.                                                | Measurements are normalised for solar and viewing conditions, including BRDF correction (see also 3.14).&#10;*Note 1: Information on measurement normalisation should be available in the metadata as single DOI landing page.* |                           |                        |                                            |                                      |
| **3.4**  |            **Atmospheric Reflectance Correction**            | Metadata indicates corrections are applied for molecular (Rayleigh) scattering and aerosol scattering and absorption.&#10;Metadata contains a single DOI landing page with references to a citable peer-reviewed algorithm, technical documentation regarding the implementation of that algorithm and the sources of ancillary data used to make corrections.&#10;*Note 1: Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.* | As threshold.                                                |                           |                        |                                            |                                      |
| **3.5**  |                 **Water Vapour Corrections**                 | Corrections are applied for water vapour if spectral bands are affected. Metadata contains a single DOI landing page with references to a citable peer-reviewed algorithm, technical documentation regarding the implementation of that algorithm.&#10;*Note 1: Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.* | As threshold.                                                |                           |                        |                                            |                                      |
| **3.6**  |                    **Ozone Corrections**                     | Data is corrected for ozone if spectral bands are affected.&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;Metadata contains a single DOI landing page with references to a citable peer-reviewed algorithm, technical documentation regarding the implementation of the ozone correction algorithm. | As threshold.                                                |                           |                        |                                            |                                      |
| **3.7**  |        **Other Trace Gaseous Absorption Corrections**        | Data is corrected for other trace gaseous absorption if spectral bands are affected.&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;Metadata contains a single DOI landing page with references to a citable peer-reviewed algorithm, technical documentation regarding the implementation of the other trace gaseous absorption correction algorithm. | As threshold.                                                |                           |                        |                                            |                                      |
| **3.8**  |                   **Sun Glint Correction**                   | Not required.                                                | The metadata indicates the surface contributions from Sun glint removed from the data if a pixel is assessed as being of correctable (moderate) Sun glint. |                           |                        |                                            |                                      |
| **3.9**  |                   **Sky Glint Correction**                   | Sky glint is implicitly corrected for in the atmospheric correction procedure. | Sky glint is separately assessed and corrected for in the data processing. The metadata indicates the surface contributions from sky glint are removed from the data. |                           |                        |                                            |                                      |
| **3.10** |                 **Whitecap/Foam Correction**                 | The water-leaving reflectance or radiance is corrected for the contribution from surface whitecaps and foam if a pixel is assessed as affected by whitecaps or foam. | As threshold.                                                |                           |                        |                                            |                                      |
| **3.11** |               **Adjacency Effects Correction**               | Not required.                                                | Information on adjacency effects correction (for example, citable peer-reviewed algorithm approach, technical documentation of the implementation, sources of ancillary data) should be available in the metadata as a single DOI landing page. |                           |                        |                                            |                                      |
| **3.12** |       **Floating Vegetation/Surface Scum Correction**        | The metadata indicates whether a pixel has been corrected for floating vegetation/surface scum or not. In that case information on floating vegetation/surface scum water mask should be available in the metadata as a single DOI landing page. | As threshold.                                                |                           |                        |                                            |                                      |
| **3.13** |                 **Turbid Water Correction**                  | The metadata indicates whether the atmospheric correction accounted for a pixel being turbid or not. In that case information on turbid water mask should be available in the metadata as a single DOI landing page. | As threshold.                                                |                           |                        |                                            |                                      |
| **3.14** | **Bidirectional Reflectance Distribution Function Correction** | Not required.                                                | Data is corrected for BRDF effects (see also 3.3.).          |                           |                        |                                            |                                      |

### Geometric Corrections

*Geometric corrections must place the measurement accurately on the surface of the Earth (that is, geolocate the measurement) allowing measurements taken through time to be compared.*

|    #    |           Item           | Threshold (Minimum) Requirements                             | Target (Desired) Requirements                                | Threshold Self-Assessment | Target Self-Assessment | Self-Assessment Explanation/ Justification | Recommended Requirement Modification |
| :-----: | :----------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :-----------------------: | :--------------------: | :----------------------------------------: | :----------------------------------: |
| **4.1** | **Geometric Correction** | Sub-pixel accuracy is achieved in relative geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.&#10;&#10;Sub-pixel accuracy is taken to be less than or equal to 0.5-pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.&#10;&#10;A consistent gridding/sampling frame is used, including common cell size, origin, and nominal sample point location within the cell (centre, ll, ur).&#10;&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;*Note 1: The threshold level will not necessarily enable interoperability between data from* different *sources as the geometric corrections for each of the sources may differ.* | Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid).&#10;&#10;A consistent gridding/sampling frame is necessary to meet this requirement.&#10;&#10;Relevant metadata must be provided under 1.8 and 1.9.&#10;*Note 1: This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction and with non-image spatial data such as GIS layers and terrain models.* |                           |                        |                                            |                                      |

## Summary Self-Assessment Table

### 1. General Metadata

|                                                              |  Threshold   | Target |
| :----------------------------------------------------------- | :----------: | :----: |
| 1.1 Traceability                                             | Not Required |        |
| 1.2 Metadata Machine Readability                             |              |        |
| 1.3 Data Collection Time                                     |              |        |
| 1.4 Geographical Area                                        |              |        |
| 1.5 Coordinate Reference System                              |              |        |
| 1.6 Map Projection                                           |              |        |
| 1.7 Geometric Correction Methods                             | Not Required |        |
| 1.8 Geometric Accuracy of the Data                           | Not Required |        |
| 1.9 Instrument                                               |              |        |
| 1.10 Spectral Bands                                          |              |        |
| 1.11 Sensor Calibration                                      | Not Required |        |
| 1.12 Radiometric Accuracy                                    |              |        |
| 1.13 Algorithms                                              |              |        |
| 1.14 Auxiliary Data                                          |              |        |
| 1.15 Processing Chain Provenance                             | Not Required |        |
| 1.16 Data Access                                             |              |        |
| 1.17 Overall Data Quality                                    |              |        |

### 2. Per-Pixel Metadata

|                                                              |  Threshold   | Target |
| :----------------------------------------------------------- | :----------: | :----: |
| 2.1 Metadata Machine Readability                             |              |        |
| 2.2 No Data                                                  |              |        |
| 2.3 Per-pixel Assessment                                     |              |        |
| 2.4 Saturation                                               |              |        |
| 2.5 Cloud                                                    |              |        |
| 2.6 Cloud Shadow                                             |              |        |
| 2.7 Land/Water Mask                                          |              |        |
| 2.8 Sea/Lake/River Ice Mask                                  |              |        |
| 2.9 Sun Glint                                                |              |        |
| 2.10 Sky Glint                                               | Not Required |        |
| 2.11 Whitecap/Foam Mask                                      |              |        |
| 2.12 Solar and Viewing Geometry                              |              |        |
| 2.13 Adjacency Effects                                       | Not Required |        |
| 2.14 Floating Vegetation/Surface Scum Mask                   |              |        |
| 2.15 Aerosol Optical Depth Parameters                        |              |        |
| 2.16 Deep/Shallow Water                                      | Not Required |        |
| 2.17 Optically Deep or Optically Shallow Assessment          |              |        |
| 2.18 Turbid Water Flag                                       |              |        |
| 2.19 Bidirectional Reflectance Distribution Function Applied | Not Required |        |
| 2.20 Altitude (ASL)                                          |              |        |

### 3. Radiometric and Atmospheric Corrections

|                                                              |  Threshold   | Target |
| :----------------------------------------------------------- | :----------: | :----: |
| 3.1 Measurement                                              |              |        |
| 3.2 Measurement Uncertainty                                  | Not Required |        |
| 3.3 Measurement Normalisation                                | Not Required |        |
| 3.4 Atmospheric Reflectance Correction                       |              |        |
| 3.5 Water Vapour Corrections                                 |              |        |
| 3.6 Ozone Corrections                                        |              |        |
| 3.7 Other Trace Gaseous Absorption Corrections               |              |        |
| 3.8 Sun Glint Correction                                     | Not Required |        |
| 3.9 Sky Glint Correction                                     |              |        |
| 3.10 Whitecap/Foam Correction                                |              |        |
| 3.11 Adjacency Effects Correction                            | Not Required |        |
| 3.12 Floating Vegetation/Surface Scum Correction             |              |        |
| 3.13 Turbid Water Correction                                 |              |        |
| 3.14 Bidirectional Reflectance Distribution Function Correction | Not Required |        |

### Geometric Corrections

|                                                              |  Threshold   | Target |
| :----------------------------------------------------------- | :----------: | :----: |
| 4.1 Geometric Correction                                     |              |        |

&#12;
## Guidance

This section aims to provide background and specific information on the processing steps that can be used to achieve analysis ready data. This Guidance material does not replace or over-ride the specifications.

## Introduction to CARD4L

### What is CEOS Analysis Ready Data for Land (CARD4L) products?

CARD4L products have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort. These products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets.

CARD4L products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development. They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures. They may not be suitable for all purposes and are not intended as a ‘replacement’ for other types of satellite products.

### When can a product be called CARD4L?

The CARD4L branding is applied to a particular product once:

- that product has been assessed as meeting CARD4L requirements by the agency responsible for production and distribution of the product, and
- that assessment has been peer reviewed by the CEOS Land Surface Imaging Virtual Constellation in consultation with other CEOS working groups as appropriate, including the CEOS Working Group on Calibration and Validation.

Agencies or other entities considering undertaking an assessment process should contact the [Land Surface Imaging Virtual Constellation](http://ceos.org/ourwork/virtual-constellations/lsi/).

A product can continue to use CARD4L branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

### What is the difference between Threshold and Target?

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making.

Products that meet target requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the *threshold* level.

Target requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, *target* specifications may (and subject to due process) become accepted as *threshold* requirements.

## Procedural Examples

**Processes to produce Threshold Aquatic Reflectance CARD4L:**

The following correction processes would typically be applied to produce CARD4L-AR Threshold:

- *No example processes are provided at this time.*

The following additional processes could be applied to produce CARD4L-AR Target:

- *No example processes are provided at this time.*

## Specific Examples

**Processes to produce Threshold Aquatic Reflectance CARD4L.**

- *No example processes are provided at this time.*

## Reference Papers

The following papers provide scientific and technical guidance:

1. Botha, E.J., Brando, V.E., & Dekker, A.G., 2016. Effects of per-pixel variability on uncertainties in bathymetric retrievals from high-resolution satellite images. Remote Sens. 8(6), 459, <https://doi.org/10.3390/rs8060459>. (*Supports requirements* *2.9, 2.13, 3.8 & 3.11*)
2. Bourg, L., 2014. Sentinel-3 OLCI Level-0 and Level-1B ATBD. Algorithm Theoretical Basis Document S3-ACR-TN-007, Issue 5.0, ACRI, 10 December 2014. (*Supports requirement 2.9*)
3. Brando, V.E., Anstee, J.M., Wettle, M., Dekker, A.G., Phinn, S.R., & Roelfsema, C., 2009. A physics based retrieval and quality assessment of bathymetry from suboptimal hyperspectral data. Remote Sens. Environ. 113(4), 755-770, <https://doi.org/10.1016/j.rse.2008.12.003>. (*Supports requirement 2.17*)
4. Bresciani, M., Adamo, M., De Carolis, G., Matta, E., Pasquariello, G., Vaičiūtė, D., & Giardino, C., 2014. Monitoring blooms and surface accumulation of cyanobacteria in the Curonian Lagoon by combining MERIS and ASAR data. Remote Sens. Environ. 146, 124-135, <https://doi.org/10.1016/j.rse.2013.07.040>. (*Supports requirements 2.14 & 3.12*)
5. Brockmann, C., Kirches, G., Militzer, J., & Stelzer, K., 2015. SENTINEL 3 – LAND-WATER MASK, Version 1.2. Technical Note S3\_LandWaterMask\_v1\_2.docx, Brockmann Consult GmbH, 14.08.2015. (*Supports requirement* \*2.\*7)
6. Bulgarelli, B. & Zibordi, G., 2018a. On the detectability of adjacency effects in ocean color remote sensing of mid-latitude coastal environments by SeaWiFS, MODIS-A, MERIS, OLCI, OLI and MSI. Remote Sens. Environ. 209, 423-438, <https://doi.org/10.1016/j.rse.2017.12.021>. (*Supports requirement 2.13*)
7. Bulgarelli, B. & Zibordi, G., 2018b. Seasonal impact of adjacency effects in ocean color radiometry at the AAOT validation site. IEEE Geosci. Remote. Sens. Lett. 15(4), 488-492, <https://doi.org/10.1109/LGRS.2017.2781900>. (*Supports requirement* *2.13*)
8. Bulgarelli, B. & Zibordi, G., 2020. Adjacency radiance around a small island: implications for system vicarious calibration. Appl. Opt. 59(10), C63-C69, <https://doi.org/10.1364/AO.378512>. (*Supports requirement* *2.13*)
9. C-GLOPS-2, 2018. Lake Ice Extent (LIE) collection 250m Baltic Sea region, Version 1.0.1. Algorithm Theoretical Basis Document CGLOPS2\_QAR\_LIE-250m-V1.0.1, I1.03, Copernicus Global Land Service, 09.11.2018. (*Supports requirement 2.8*)
10. Colin F.M., 2014. Glint Avoidance and Removal in the Maritime Environment. Thesis. Rochester Institute of Technology, accessed from <https://scholarworks.rit.edu/theses/8301/> on 27. September 2021. (*Supports requirements 2.9 & 2.10*)
11. De Keukelaere, L., Sterckx, S., Adriaensen, S., Knaeps, E., Reusen, I., Giardino, C., Bresciani, M., Hunter, P., Neil, C., Van der Zande, D., & Vaiciute, D., 2018. Atmospheric correction of Landsat-8/OLI and Sentinel-2/MSI data using iCOR algorithm: validation for coastal and inland waters. Eur. J. Remote Sens. 51(1), 525-542, <https://doi.org/10.1080/22797254.2018.1457937>. (*Supports requirements 2.15, 3.6, 3.7 & 3.11*)
12. Dekker A.G., Phinn S.R., Anstee J.M., Bissett P., Brando, V.E., Casey, B., Fearns, P., Hedley, J., Klonowski, W., Lee, Z.P., Lynch, M., Lyons, M., Mobley, C. & Roelfsema, C., 2011. Intercomparison of shallow water bathymetry, hydro-optics and benthos mapping techniques in Australian and Caribbean coastal environments. Limnol. Oceanogr. Methods 9(9), 396-425, <https://doi.org/10.4319/lom.2011.9.396>. (*Supports requirement 2.17*)
13. Dierssen, H.M., 2019. Hyperspectral measurements, parameterizations, and atmospheric correction of whitecaps and foam from visible to shortwave infrared for ocean color remote sensing. Front. Earth Sci. 7(14), <https://doi.org/10.3389/feart.2019.00014>. (*Supports requirements* *2.11 & 3.10*)
14. Dierssen, H.M., 2021. Corrigendum: Hyperspectral measurements, parameterizations, and atmospheric correction of whitecaps and foam from visible to shortwave infrared for ocean color remote sensing. Front. Earth Sci. 9(683136), <https://doi.org/10.3389/feart.2021.683136>. (*Supports requirement 3.10*)
15. Dworak, R., Liu, Y., Key, J., & Meier, W\.N., 2021. A blended sea ice concentration product from AMSR2 and VIIRS. Remote Sens. 13(15), 2982, <https://doi.org/10.3390/rs13152982>. (*Supports requirement 2.8*)
16. Fan, Y., Li, W., Voss, K.J., Gatebe, C.K., & Stamnes, K., 2016. Neural network method to correct bidirectional effects in water-leaving radiance. Appl. Opt. 55(1), 10-21. <https://doi.org/10.1364/AO.55.000010>. (*Supports requirements 2.19, 3.3, 3.14*)
17. Foga, S., Scaramuzza, P.L., Guo, S., Zhu, Z., Dilley, R.D., Beckmann, T., Schmidt, G.L., Dwyer, J.L., Hughes, M.J., & Laue, B., 2017. Cloud detection algorithm comparison and validation for operational Landsat data products. Remote Sens. Environ. 194, 379-390, <https://doi.org/10.1016/j.rse.2017.03.026>. (*Supports requirement* 2.5)
18. Frouin, R.J., Franz, B.A., Ibrahim, A., Knobelspiesse, K., Ahmad, Z., ..., & Zhai, P.-W., 2019. Atmospheric correction of satellite ocean-color imagery during the PACE era. Front. Earth Sci. 7(145), <https://doi.org/10.3389/feart.2019.00145>. (*Supports requirements 2.11 & 3.10*)
19. Gege, P. & Groetsch, P., 2016. A spectral model for correcting sun glint and sky glint. Conference paper: Ocean Optics XXIII, Oct. 23-28, 2016, Victoria, Canada. (*Supports requirement 3.9*)
20. Gossn, J.I., Ruddick, K.G., & Dogliotti, A.I., 2019. Atmospheric correction of OLCI imagery over extremely turbid waters based on the red, NIR and 1016 nm bands and a new baseline residual technique. Remote Sens. 11(3), 220, <https://doi.org/10.3390/rs11030220>. (Supports requirement 3.13)
21. Groetsch, P.M.M., Foster R., & Gilerson, A., 2020. Exploring the limits for sky and sun glint correction of hyperspectral above-surface reflectance observations. Appl. Opt. 59(9), 2942-2954, <https://doi.org/10.1364/AO.385853>. (*Supports requirements 3.8 & 3.9*)
22. Harmel, T., Chami, M., Tormos, T., Reynaud, N., & Danis, P.-A, 2018. Sun glint correction of the Multi-Spectral Instrument (MSI)-SENTINEL-2 imagery over inland and sea waters from SWIR bands. Remote Sens. Environ. 204, 308-321, <https://doi.org/10.1016/j.rse.2017.10.022>. (*Supports requirements 3.6, 3.7 & 3.8*)
23. Ilori, C.O., Pahlevan, N., & Knudby, A., 2019. Analyzing performances of different atmospheric correction techniques for Landsat 8: Application for coastal remote sensing. Remote Sens. 11(4), 469, <https://doi.org/10.3390/rs11040469>. (*Supports requirement 2.15*)
24. JCGM, 2008. Evaluation of measurement data - Guide to the expression of uncertainty in measurement. JCGM 100:2008, GUM 1995 with minor corrections, First edition, September 2008. (*Supports requirement 3.2*)
25. Jones, J.W., 2019. Improved automated detection of subpixel-scale inundation - Revised Dynamic Surface Water Extent (DSWE) partial surface water tests. Remote Sens. 11(4), 374, <https://doi.org/10.3390/rs11040374>. (*Supports requirement* *2.7*)
26. Kay, S., Hedley, J., & Lavender, S., 2013. Sun glint estimation in marine satellite images: a comparison of results from calculation and radiative transfer modeling. Appl. Opt. 52(23), 5631-5639, <https://doi.org/10.1364/AO.52.005631>. (*Supports requirement* *2.9*)
27. Kay, S., Hedley, J.D., & Lavender, S., 2009. Sun glint correction of high and low spatial resolution images of aquatic scenes: a review of methods for visible and near-infrared wavelengths. Remote Sens. 1(4), 697-730, <https://doi.org/10.3390/rs1040697>. (Supports requirement 3.8)
28. Kiselev, V., Bulgarelli, B., & Heege, T., 2015. Sensor independent adjacency correction algorithm for coastal and inland water systems. Remote Sens. Environ. 157, 85-95, <https://doi.org/10.1016/j.rse.2014.07.025>. (*Supports requirement 3.11*)
29. Koepke, P., 1984. Effective reflectance of oceanic whitecaps. Appl. Opt. 23(11), 1816-1824, <https://doi.org/10.1364/AO.23.001816>. (*Supports requirements* *2.11 & 3.10*)
30. Kutser, T., Hedley, J., Giardino, C., Roelfsema, C., & Brando, V., 2020. Remote sensing of shallow waters - A 50 year retrospective and future directions. Remote Sens. Environ. 240, 111619, <https://doi.org/10.1016/j.rse.2019.111619>. (*Supports requirement 2.17*)
31. Kutser, T., Vahtmäe, E., & Praks, J., 2009. A sun glint correction method for hyperspectral imagery containing areas with non-negligible water leaving NIR signal. Remote Sens. Environ. 113(10), 2267-2274, <https://doi.org/10.1016/j.rse.2009.06.016>. (*Supports requirement 3.8*)
32. Lavender, S. & Kay, S., 2010.  Sentinel-3 OLCI Glint Correction ATBD. Algorithm Theoretical Basis Document S3-L2-SD-03-C09-ARG- ATBD, Issue 2.0, ARGANS, 08 April 2010. (*Supports requirement 3.8*)
33. Lee, Z., Du, K., Voss, K.J., Zibordi, G., Lubac, B., Arnone, R., & Weidemann, A., 2011. An inherent-optical-property-centered approach to correct the angular effects in water-leaving radiance. Appl. Opt. 50, 19, 3155-3167, <https://doi.org/10.1364/AO.50.003155>. (*Supports requirements 2.19, 3.3, 3.14*)
34. Liu, X., Steele, C., Simis, S., Warren, M., Tyler, A., Spyrakos, E., Selmes, N., & Hunter, P., 2021. Retrieval of Chlorophyll-a concentration and associated product uncertainty in optically diverse lakes and reservoirs. Remote Sens. Environ., 267, 112710, <https://doi.org/10.1016/j.rse.2021.112710>.
35. Liu, Y. & Key, J.R., 2019. Ice Surface Temperature, Ice Concentration, and Ice Cover, Version 1.2. Algorithm Theoretical Basis Document ATBD\_GOES-R\_IceConcentration\_v1.2\_Feb2019, NOAA NESDIS Center for Satellite Applications and Research, February 8, 2019. (*Supports requirement* *2.8*)
36. Liu, Y., Key, J., & Mahoney, R., 2016. Sea and freshwater ice concentration from VIIRS on Suomi NPP and the future JPSS satellites. Remote Sens. 8(6), 523, <https://doi.org/10.3390/rs8060523>. (*Supports requirement* *2.8*)
37. Matthews, M.W. & Odermatt, D., 2015. Improved algorithm for routine monitoring of cyanobacteria and eutrophication in inland and near-coastal waters. Remote Sens. Environ. 156, 374-382, <https://doi.org/10.1016/j.rse.2014.10.010>. (*Supports requirements 2.14 & 3.12*)
38. Matthews, M.W., Bernard, S., & Robertson, L., 2012. An algorithm for detecting trophic status (chlorophyll-a), cyanobacterial dominance, surface scums and floating vegetation in inland and coastal waters. Remote Sens. Environ. 124, 637-652, <https://doi.org/10.1016/j.rse.2012.05.032>. (*Supports requirements 2.14 & 3.12*)
39. Mikelsons, K., Wang, M., Wang, X.L., & Jiang, L., 2021. Global land mask for satellite ocean color remote sensing. Remote Sens. Environ. 257, 112356, <https://doi.org/10.1016/j.rse.2021.112356>. (*Supports requirement* 2.7)
40. Mobley, C.D., Werdell, J., Franz, B., Ahmad, Z., & Bailey, S., 2016. Atmospheric Correction for Satellite Ocean Color Radiometry. NASA Tech. Memo. 20160011399, NASA Goddard Space Flight Center, Greenbelt, Maryland, 06/01/2016, <https://ntrs.nasa.gov/citations/20160011399>. (*Supports requirements 2.19, 3.3 & 3.14*)
41. Moore, G.F., Aiken, J., & Lavender, S.J., 1999. The atmospheric correction of water colour and the quantitative retrieval of suspended particulate matter in Case II waters: Application to MERIS. Int. J. Remote Sens. 20(9), 1713-1733, <https://doi.org/10.1080/014311699212434>. (*Supports requirement 3.13*)
42. Moore, K.D., Voss, K.J., & Gordon, H.R., 2000. Spectral reflectance of whitecaps: Their contribution to water-leaving radiance. J. Geophys. Res. Oceans 105(C3), 6493-6499, <https://doi.org/10.1029/1999JC900334>. (*Supports requirements* *2.11 & 3.10*)
43. Morel, A. & Bélanger, S., 2006. Improved detection of turbid waters from ocean color sensors information. Remote Sens. Environ. 102(3-4), 237-249, <https://doi.org/10.1016/j.rse.2006.01.022>. (*Supports requirement 2.18*)
44. Morel, A. & Gentili, 2008. Practical application of the “turbid water” flag in ocean color imagery: Interference with sun-glint contaminated pixels in open ocean. Remote Sens. Environ. 112(3), 934-938, <https://doi.org/10.1016/j.rse.2007.07.009>. (*Supports requirement 2.18*)
45. Pahlevan, N., Mangin, A., Balasubramanian, S.V., Smith, B., Alikas, K., ..., & Warren, M., 2021. ACIX-Aqua: A global assessment of atmospheric correction methods for Landsat-8 and Sentinel-2 over lakes, rivers, and coastal waters. Remote Sens. Environ. 258, 112366, <https://doi.org/10.1016/j.rse.2021.112366>. (*Supports requirements 2.15, 3.2, 3.6 & 3.7*)
46. Pahlevan, N., Schott, J.R., Franz, B.A., Zibordi, Z., Markham, B., Bailey, S., Schaaf, C.B., Ondrusek, M., Greb, S., & Strait, C.M., 2017. Landsat 8 remote sensing reflectance (Rrs) products: Evaluations, intercomparisons, and enhancements. Remote Sens. Environ. 190, 289-301, <https://doi.org/10.1016/j.rse.2016.12.030>. (*Supports requirements 2.15, 3.6 & 3.7*)
47. Park, Y.-J. & Ruddick, K., 2005. Model of remote-sensing reflectance including bidirectional effects for case 1 and case 2 waters. Appl. Opt. 44(7), 1236-1249, <https://doi.org/10.1364/AO.44.001236>. (*Supports requirements 2.19, 3.3 & 3.14*)
48. Pekel, J.-F., Cottam, A., Gorelick, N., & Belward, A.S., 2016. High-resolution mapping of global surface water and its long-term changes. Nature 540, 418-422, <https://doi.org/10.1038/nature20584>. (*Supports requirement 2.7*)
49. Robinson, W\.D., Franz, B.A., Patt, F.S., Bailey, S.W., & Werdell, P.J., 2003. Masks and Flags Updates. Chapter 6 In: Patt, F.S., et al., 2003: Algorithm Updates for the Fourth SeaWiFS Data Reprocessing. NASA Tech. Memo. 2003--206892, Vol. 22, Hooker, S.B. & Firestone, E.R, Eds., NASA Goddard Space Flight Center, Greenbelt, Maryland. (*Supports requirements 2.8 & 2.18*)
50. Soppa, M.A., Silva, B., Steinmetz, F., Keith, D., Scheffler, D., Bohn, N., & Bracher, A., 2021. Assessment of Polymer atmospheric correction algorithm for hyperspectral remote sensing imagery over coastal waters. Sensors 21(12), 4125, <https://doi.org/10.3390/s21124125>. (*Supports requirements 2.19, 3.3 & 3.14*)
51. Sterckx, S., Knaeps, E., Kratzer, S., & Ruddick, K., 2015. SIMilarity Environment Correction (SIMEC) applied to MERIS data over inland and coastal waters. Remote Sens. Environ. 157, 96-110, <https://doi.org/10.1016/j.rse.2014.06.017>. (*Supports requirement 3.11*)
52. Stumpf, R.P., Arnone, R.A., Gould, Jr., R.W., Martinolich, P.M., & Ransibrahmanakul, V. 2003. A partially coupled ocean-atmosphere model for retrieval of water-leaving radiance from SeaWiFS in coastal waters. Chapter 9 In: Patt, F.S., et al., 2003: Algorithm Updates for the Fourth SeaWiFS Data Reprocessing. NASA Tech. Memo. 2003--206892, Vol. 22, Hooker, S.B. & Firestone, E.R., Eds., NASA Goddard Space Flight Center, Greenbelt, Maryland. (*Supports requirement 3.13*)
53. Vanhellemont, Q., 2019. Adaptation of the dark spectrum fitting atmospheric correction for aquatic applications of the Landsat and Sentinel-2 archives. Remote Sens. Environ. 225, 175-192, <https://doi.org/10.1016/j.rse.2019.03.010>. (*Supports requirements 2.15 & 3.6*)
54. Wang, M., Liu, X., Jiang, L., & Son, S.H., 2017. Visible Infrared Imaging Radiometer Suite (VIIRS) Ocean Color Products, Version 1.0. Algorithm Theoretical Basis Document ATBD\_OceanColor\_v1.0, NOAA NESDIS Center for Satellite Applications and Research, June 5, 2017. (*Supports requirements 2.11 & 3.10*)
55. Warren, M.A., Simis, S.G., & Selmes, N., 2021. Complementary water quality observations from high and medium resolution Sentinel sensors by aligning chlorophyll-a and turbidity algorithms. Remote Sens. Environ. 265, 112651, <https://doi.org/10.1016/j.rse.2021.112651>. (*Supports requirement 3.2*)
56. Zhang, X., He, S., Shabani, A., Zhai, P.-W., & Du, K., 2017. Spectral sea surface reflectance of skylight. Opt. Express 25(4), A1-A13, <https://doi.org/10.1364/OE.25.0000A1>. (*Supports requirement 3.9*)
57. Zheng, G. & DiGiacomo, P.M., 2017. Uncertainties and applications of satellite-derived coastal water quality products. Prog. Oceanogr. 159, 45-72, <https://doi.org/10.1016/j.pocean.2017.08.007>. (*Supports requirement 3.2*)
58. Zhu, Z. & Woodcock, C.E, 2012. Object‐based cloud and cloud shadow detection in Landsat imagery. Remote Sens. Environ. 118, 83‐94, <https://doi.org/10.1016/j.rse.2011.10.028>. (*Supports requirement* *2.5*)
59. Zhu, Z., Wang, S., & Woodcock, C.E., 2015. Improvement and expansion of the Fmask algorithm: cloud, cloud shadow, and snow detection for Landsats 4‐7, 8, and Sentinel 2 images. Remote Sens. Environ. 159, 269‐277, <https://doi.org/10.1016/j.rse.2014.12.014>. (*Supports requirement 2.5*)
