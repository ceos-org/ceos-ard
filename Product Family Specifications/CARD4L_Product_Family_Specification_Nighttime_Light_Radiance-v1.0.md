|![](Aspose.Words.b8384b8a-2471-4f90-bd7d-d8c24c69c8ea.001.png)|<p>**Analysis Ready Data**</p><p>***For Land***</p>|<p>**Product Family**</p><p>**Specification**</p><p>**Nighttime Light Surface Radiance (CARD4L-NLSR)**</p>|
| :-: | :-: | :-: |

# **Document Status**
**For Adoption as:	Product Family Specification, Nighttime Light Surface Radiance**

This Specification should next be reviewed on: 	TBD

<a name="_gjdgxs"></a>Proposed revisions may be provided to:			<lsi@lists.ceos.org>
# **Document History**

|**Version**|**Date**|**Description of Change**|**Author**|
| :- | :- | :- | :- |
|0\.0.1|11\.12.2020|Zero Draft translating previous materials to this format. With many thanks to all CEOS contributors.|Wang, Román|
|0\.0.2|12\.09.2020|Removed references to Black Marble to keep specification focused on the general measurement. Suggested acronym of Nighttime Light Surface Radiance (NLSR).|Killough|
|0\.1.0|23\.06.2022|Corrected references and author affiliation.|<p>Ramachandran</p><p></p>|

# **Contributing Authors (in alphabetical order)**
**	Brian Killough, NASA Langley Research Center, CEOS Systems Engineering Office, USA

`	`Bhaskar Ramachandran, NASA Goddard Space Flight Center, USA

`	`Miguel Román, Leidos Inc., Civil Group, USA

`	`Zhuosen Wang, University of Maryland/GSFC, USA

# **Description**
**Product Family Title:** 		**Nighttime Light Surface Radiance (CARD4L-NLSR)**

<a name="_30j0zll"></a>**Applies to:***	Data collected with nighttime light sensors operating in the VIS/NIR wavelengths. These typically operate with ground sample distance and resolution in the order of 10-1000m; however, the Specification is not inherently limited to this resolution.
# **Definitions**

|NLSR|Nighttime Light Surface Radiance|
| :-: | :- |
|Ancillary Data|Data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information, and data from other instruments.|
|Auxiliary Data|The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources.|
|Metadata|Structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content.|
|MTF|Modulation Transfer Function|
|Spectral Resolution|Defines the narrowest spectral feature that can be resolved by a spectrometer.|
|Spatial Resolution|The highest magnification of the sensor at the ground surface.|
|Spectral Sampling Distance|Spectral sampling is the interval, in wavelength units, between discrete data points in the measured spectrum.|
|Spatial Sampling Distance|Spatial sampling distance is the barycentre-to-barycentre distance between adjacent spatial samples on the Earth's surface.|
#
# **Requirements**
## **General Metadata**
*These are metadata records describing a distributed collection of pixels. The collection of pixels referred to must be contiguous in space and time. General metadata should allow the user to assess the overall suitability of the dataset, and must meet the following requirements:*

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**1.1**|**Traceability**|Not required.|<p>Data must be traceable to SI reference standard. <br>*Note 1: Relationship to 3.2. Traceability requires an estimate of measurement uncertainty.*</p><p>*Note 2: Information on traceability should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.2**|**Metadata Machine Readability**|Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use.|As threshold, but metadata should be provided in a community endorsed standard that facilitates <br>machine-readability, such as ISO 19115-2.|||||
|**1.3**|**Data Collection Time**|<p>The data collection time is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified.</p><p></p>|Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second.|||||
|**1.4**|**Geographical<br>Area**|The surface location to which the data relates is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84).|The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) with the projection system (if any) and reference datum provided. |||||
|**1.5**|**Coordinate Reference System**|The metadata lists the coordinate reference system that has been used.|As threshold.|||||
|**1.6**|**Map Projection**|<a name="_1fob9te"></a>The metadata lists the map projection that has been used and any relevant parameters required in relation to use of data in that map projection.|As threshold.|||||
|**1.7**|**Geometric Correction Methods**|<p>Not required. </p><p>The user is not explicitly advised of the geometric correction source and methods.</p>|Information on geometric correction methods should be available in the metadata as a single DOI landing page, including reference database and auxiliary data such as elevation model(s) and reference chip-sets.|||||
|**1.8**|**Geometric<br>Accuracy of the Data**|<p>Not required. </p><p>The user is not provided with results of geometric accuracy assessments pertaining to the dataset.</p>|<p>The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data. Accuracy is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed quantitatively, for example, as root mean square error (RMSE) or Circular Error Probability (CEP90, CEP95), etc. </p><p>*Note 1: Information on geometric accuracy of the data should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.9**|**Instrument**|The instrument used to collect the data is identified in the metadata.|As threshold, but information should be available in the metadata as a single DOI landing page with references to the relevant CEOS Missions, Instruments, and Measurements Database record.|||||
|**1.10**|**Spectral Bands**|<p>The central wavelength for each band for which data is included is identified in the metadata, expressed in SI units.</p><p></p>|<p>As threshold, with instrument spectral response details (e.g., full spectral response function) also included or directly accessible using details in the metadata. <br>Central wavelength and bandwidth at full-width half maximum value of the relative spectral response function are provided at least.</p><p>*Note 1: Information on spectral bands should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.11**|**Sensor Calibration**|<p>Not required.</p><p>The general metadata does not include sensor calibration details.</p>|<p>Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata. Ideally this would support machine-to-machine access. </p><p>*Note 1: Information on sensor calibration should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.12**|**Radiometric Accuracy**|<p>Not required.</p><p>The general metadata does not include information on the radiometric accuracy of the data.</p>|<p>The metadata includes metrics describing the assessed absolute radiometric uncertainty of the version of the data or product, expressed as absolute radiometric uncertainty relative to appropriate, known reference sites and standards (for example, pseudo-invariant calibration sites, rigorously collected field spectra, Rayleigh, DCC, etc.)</p><p>*Note 1: Information on radiometric accuracy should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.13**|**Algorithms**|<p>All algorithms, and the sequence in which they were applied in the generation process, are identified in the metadata. For example, these may be available through Algorithm Theoretical Basis documents. </p><p>*Note 1: Information on algorithms should be available in the metadata as a single DOI landing page.*</p>|<p>As threshold, but only algorithms that have been published in a peer-reviewed journal.</p><p>*Note 1: It is possible that high quality corrections are applied through non-disclosed processes*. *CARD4L does not per-se require full and open data and methods.* </p><p>*Note 2: Information on algorithms should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.14**|**Auxiliary Data**|<p>The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as a single DOI landing page. </p><p>*Note 1: Auxiliary data includes DEMs, aerosols, etc. data sources.* </p>|<p>As threshold, but information on auxiliary data should be available in the metadata as a single DOI landing page and is also available for free online download, contemporaneously with the product or through a link to the source.</p><p></p>|||||
|**1.15**|<p>**Processing Chain Provenance**</p><p></p>|Not required.|<p>Information on processing chain provenance should be available in the metadata as a single DOI landing page containing detailed description of the processing steps used to generate the product, the organization that performed the processing, and the versions of software used, giving full transparency to the users.</p><p></p>|||||
|**1.16**|<p>**Data Access**</p><p></p>|<p>Information on data access should be available in the metadata as a single DOI landing page.</p><p>*Note 1: Manual and offline interaction action (e.g., login) may be required.*</p>|As threshold.|||||
|**1.17**|**Overall Data Quality**|Not applicable.|<p>Machine-readable metrics describing the overall quality of the data are included in the metadata, at minimum the cloud cover extent, i.e.:</p><p>- Proportion of observations over land (c.f. ocean) affected by non-target phenomena, e.g., cloud and cloud shadows</p>|||||


## **Per-Pixel Metadata**
*The following minimum metadata specifications apply to each pixel. Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider. Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for application.*

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**2.1**|**Metadata Machine Readability**|Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.|As threshold.|||||
|**2.2**|**No Data**|Pixels that do not correspond to an observation (‘empty pixels’) are flagged.|As threshold.|||||
|**2.3**|<p>**Incomplete<br>Testing**</p><p></p>|<p>The metadata identifies pixels for which the per-pixel tests (below) have not all been successfully completed.</p><p>*Note 1: This may be the result of missing ancillary data for a subset of the pixels.*</p>|The metadata identifies which tests have, and have not, been successfully completed for each pixel.|||||
|**2.4**|**Saturation**|Metadata indicates where one or more spectral bands are saturated.|Metadata indicates which pixels are saturated for each spectral band.|||||
|**2.5**|**Cloud**|Metadata indicates whether a pixel is assessed as being cloud.|As threshold, information on cloud detection should be available in the metadata as a single DOI landing page.|||||
|**2.6**|**Cloud Shadow**|Not required.|Metadata indicates whether a pixel is assessed as being cloud shadow. Information on cloud shadow detection should be available in the metadata as a single DOI landing page.|||||
|**2.7**|**Land/Water<br>Mask**|Metadata indicates whether a pixel is land or water.|As threshold, information on land/water mask should be available in the metadata as a single DOI landing page.|||||
|**2.8**|**Snow/Ice Mask**|Metadata indicates whether a pixel is snow/ice.|As threshold, information on snow/ice mask should be available in the metadata as a single DOI landing page.|||||
|**2.9**|**Terrain Shadow Mask**|Not required.|The metadata indicates pixels that are not directly illuminated due to terrain shadowing.|||||
|**2.10**|**Terrain Occlusion**|Not required.|The metadata indicates pixels that are not visible to the sensor due to terrain occlusion during off-nadir viewing.|||||
|**2.11**|**Lunar and Viewing Geometry**|Provide average lunar and sensor viewing azimuth and zenith angles.|Provide per-pixel lunar and sensor viewing azimuth and zenith angles.|||||
|**2.12**|**Terrain Illumination Correction**|Not required.|Coefficients used for terrain illumination correction are provided for each pixel.|||||
|**2.13**|**Aerosol Optical Depth Parameters**|Not required.|To be determined.|||||
|**2.14**|**Moon Illumination Fraction**|Provide average moon illumination fraction.|Provide per-pixel moon illumination fraction|||||
|**2.15**|**Brightness Temperature**|Provide brightness temperature from thermal bands.  |As threshold.|||||
|**2.16**|**Solar Zenith Angle**|Provide solar zenith angle to support stray-light corrections (see also 3.6).|As threshold.|||||

## **Radiometric and Atmospheric Corrections**
*The following requirements must be met for all pixels in a collection. The requirements indicate both the necessary outcomes (3.1-3.3) and the minimum steps necessary to be deemed to have achieved those outcomes (3.4 onward). Radiometric corrections must lead to a valid measurement of surface reflectance.*

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**3.1**|**Measurement**|Pixel values that are expressed as a measurement of the nighttime light radiance. |Nighttime light radiance measurements are SI traceable (see also 1.1).|||||
|**3.2**|**Measurement Uncertainty**|<p>Not required.</p><p>*Note 1: In current practice, users determine fitness for purpose based on knowledge of the lineage of the data, rather than on a specific estimate of measurement uncertainty.*</p>|<p>An estimate of the certainty of the values is provided in measurement units. </p><p>*Note 1: This is a requirement for SI traceability. See also 1.1.*</p><p>*Note 2: Information on measurement uncertainty should be available in the metadata as a single DOI landing page.*</p>|||||
|**3.3**|**Measurement Normalisation**|Not required.|<p>Measurements are normalised for viewing conditions (i.e., nadir view angle). This may include radiative transfer modelling.</p><p></p><p>*Note 1: Information on measurement normalisation should be available in the metadata as single DOI landing page.*</p>|||||
|**3.4**|**Atmospheric Corrections**|<p>Corrections are applied for atmospheric scattering.</p><p></p><p>Metadata contains a single DOI landing page with references to:</p><p>- a citable peer-reviewed algorithm </p><p>- technical documentation regarding the implementation of that algorithm </p><p>- the sources of ancillary data used to make corrections</p><p></p><p>*Note 1: Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.*</p>|As threshold.|||||
|<a name="_3znysh7"></a>**3.5**|**Lunar Radiance Corrections**|<p>Corrections are applied for lunar radiance.</p><p></p><p>Metadata contains a single DOI landing page with references to:</p><p>- a citable peer-reviewed algorithm </p><p>- technical documentation regarding the implementation of that algorithm and the lunar model used.</p><p></p><p>*Note 1: Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.*</p>|As threshold.|||||
|**3.6**|**Stray Light Corrections**|<p>Corrections are applied for stray light.</p><p></p><p>Metadata contains a single DOI landing page with references to:</p><p>- a citable peer-reviewed algorithm </p><p>- technical documentation regarding the implementation of that algorithm and any models used.</p><p></p><p>*Note 1: Examples of technical documentation include an Algorithm Theoretical Basis Document, product user guide, etc.*</p>|As threshold.|||||

## **Geometric Corrections**
*Geometric corrections must place the measurement accurately on the surface of the Earth (that is, geolocate the measurement) allowing measurements taken through time to be compared.* 

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**4.1**|**Geometric<br>Correction**|<p>Sub-pixel accuracy is achieved in relative geolocation, that is, the pixels from the same instrument and platform are consistently located, and are thus comparable, through time.</p><p></p><p>Sub-pixel accuracy is taken to be less than or equal to 0.5-pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.</p><p></p><p>A consistent gridding/sampling frame is used, including common cell size, origin, and nominal sample point location within the cell (centre, ll, ur).</p><p></p><p>Relevant metadata must be provided under 1.8 and 1.9.</p><p>*Note 1: The threshold level will not necessarily enable interoperability between data from* different *sources as the geometric corrections for each of the sources may differ.*</p>|<p>Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid). </p><p></p><p>A consistent gridding/sampling frame is necessary to meet this requirement.</p><p></p><p>Relevant metadata must be provided under 1.8 and 1.9.</p><p>*Note 1: This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction and with non-image spatial data such as GIS layers and terrain models.*</p>|||||


# **Summary Self-Assessment Table**

||**Threshold**|**Target**|
| :-: | :-: | :-: |
|**1. General Metadata**|||
|1\.1 Traceability|||
|1\.2 Metadata Machine Readability|||
|1\.3 Data Collection Time|||
|1\.4 Geographical Area|||
|1\.5 Coordinate Reference System|||
|1\.6 Map Projection|||
|1\.7 Geometric Correction Methods|||
|1\.8 Geometric Accuracy of the Data|||
|1\.9 Instrument|||
|1\.10 Spectral Bands|||
|1\.11 Sensor Calibration|||
|1\.12 Radiometric Accuracy|||
|1\.13 Algorithms|||
|1\.14 Auxiliary Data|||
|1\.15 Processing Chain Provenance|||
|1\.16 Data Access|||
|1\.17 Overall Data Quality|||
|**2. Per-Pixel Metadata**|||
|2\.1 Metadata Machine Readability|||
|2\.2 No Data|||
|2\.3 Incomplete Testing|||
|2\.4 Saturation|||
|2\.5 Cloud|||
|2\.6 Cloud Shadow|||
|2\.7 Land/Water Mask|||
|2\.8 Snow/Ice Mask|||
|2\.9 Terrain Shadow Mask|||
|2\.10 Terrain Occlusion|||
|2\.11 Lunar and Viewing Geometry|||
|2\.12 Terrain Illumination Correction|||
|2\.13 Aerosol Optical Depth Parameters|||
|2\.14 Moon Illumination Fraction |||
|2\.15 Brightness Temperature |||
|2\.16 Solar Zenith Angle|||
|**3. Radiometric and Atmospheric Corrections**|||
|3\.1 Measurement|||
|3\.2 Measurement Uncertainty|||
|3\.3 Measurement Normalisation|||
|3\.4 Atmospheric Corrections|||
|3\.5 Lunar Radiance Corrections|||
|3\.6 Stray Light Corrections|||
|**4. Geometric Corrections**|||
|4\.1 Geometric Correction|||

# **Guidance**
This section aims to provide background and specific information on the processing steps that can be used to achieve analysis ready data. This Guidance material does not replace or override the specifications. 
# **Introduction to CARD4L**
**What is CEOS Analysis Ready Data for Land (CARD4L) products?**

CARD4L products have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort. These products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets. 

CARD4L products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development. They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures. They may not be suitable for all purposes and are not intended as a ‘replacement’ for other types of satellite products.

**When can a product be called CARD4L?**

The CARD4L branding is applied to a particular product once:

- the product has been assessed as meeting CARD4L requirements by the agency responsible for production and distribution of the product, and
- the assessment has been peer reviewed by the CEOS Land Surface Imaging Virtual Constellation in consultation with other CEOS working groups as appropriate, including the CEOS Working Group on Calibration and Validation.

Agencies or other entities considering undertaking an assessment process should contact the [Land Surface Imaging Virtual Constellation](http://ceos.org/ourwork/virtual-constellations/lsi/).

A product can continue to use CARD4L branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

**What is the difference between Threshold and Target?**

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making. 

Products that meet target requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the *threshold* level. 

Target requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, *target* specifications may (and subject to due process) become accepted as *threshold* requirements.
# **Procedural Examples**
**Processes to produce Threshold Nighttime Light Surface Radiance (NLSR) CARD4L:**

The following correction processes would typically be applied to produce CARD4L-NLSR Threshold:

- *No example processes are provided at this time.*

The following additional processes could be applied to produce CARD4L-NLSR Target:

- *No example processes are provided at this time.*
# **Specific Examples**
**Processes to produce Threshold Nighttime Light Surface Radiance CARD4L:**

- *No example processes are provided at this time.*
# **Reference Papers**
The following papers provide scientific and technical guidance:

<a name="_2et92p0"></a>Román, M.O., Wang, Z., Sun, Q., Kalb, V., Miller, S.D., Molthan, A., Schultz, L., Bell, J., Stokes, E.C., Pandey, B., Seto, K.C., Hall, D., Oda, T., Wolfe, R.E., Lin, G., Golpayegani, N., Devadiga, S., Davidson, C., Sarkar, S., Praderas, C., Schmaltz, J., Boller, R., Stevens, J., Ramos González, O.M., Padilla, E., Alonso, J., Detrés, Y., Armstrong, R., Miranda, I., Conte, Y., Marrero, N., MacManus, K., Esch, T., Masuoka, E.J., 2018. NASA's Black Marble nighttime lights product suite. Remote Sens. Environ. <doi:10.1016/j.rse.2018.03.017>

Wang, Z., Román, M.O., Kalb, V.L., Miller, S.D., Zhang, J., Shrestha, R.M., 2021. Quantifying uncertainties in nighttime light retrievals from Suomi-NPP and NOAA-20 VIIRS Day/Night Band data. Remote Sens. Environ. 263. <doi:10.1016/j.rse.2021.112557>

Mills, S., & Miller, S.D., 2014, October. VIIRS Day-Night Band (DNB) calibration methods for improved uniformity. In Earth Observing Systems XIX (Vol. 9218, p. 921809). International Society for Optics and Photonics.

Ryan, R.E. et al., 2019. The Terra Vega Active Light Source: A First Step in a New Approach to Perform Nighttime Absolute Radiometric Calibrations and Early Results Calibrating the VIIRS DNB. *Remote Sens.* 2019, *11*, 710. [https://doi.org/10.3390/rs11060710](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdoi.org%2F10.3390%2Frs11060710&data=04%7C01%7Cbrian.d.killough%40nasa.gov%7C790d52640470420063cf08d9098258f1%7C7005d45845be48ae8140d43da96dd17b%7C0%7C0%7C637551277751607761%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=uJ870BxZ4SB4RdRDihH1q2aT0N52XxlxLru%2BcA0DdSY%3D&reserved=0)

