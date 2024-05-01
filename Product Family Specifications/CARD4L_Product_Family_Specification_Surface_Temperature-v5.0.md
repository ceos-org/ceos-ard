|![](Aspose.Words.9df1c7b0-11bb-4842-ae0a-0c5bdacc8202.001.png)|<p><a name="_hlk2093829"></a>**Analysis Ready Data**</p><p>***For Land***</p>|<p>**Product Family**</p><p>**Specification**</p><p>**Surface Temperature** </p>|
| :-: | :-: | :-: |

# **Document Status**
**Product Family Specification, Surface Temperature**

This Specification should next be reviewed on: 	March 2021, or no later than 2 weeks before LSI-VC-11 meeting.

Proposed revisions may be provided to:			<lsi@lists.ceos.org> 
# **Document History**

|**Version**|**Date**|**Description of change**|**Author**|
| :- | :- | :- | :- |
|0\.0.2|23\.03.2017|Zero Draft based on materials provided by Geoscience Australia and the USGS in particular.|Ross |
||16\.04.2017|Included document history; ||
|1\.0.0|18\.04.2017|<p>Revised to:</p><p>- Formatting and structure</p><p>- <a name="_gjdgxs"></a>Included guidance section</p>|Lewis|
|1\.0.1|18\.04.2017|Merged ‘geometric source’ and ‘geometric method’ elements.|Lewis|
|2\.0|25\.08.2017|Incorporated first round of revisions following feedback from the UK and others.|Lewis|
|2\.1|06\.09.2017|Feedback from ESA; removed reference to bands (1.10) as these are not relevant to ST; Feedback on 1.13 included to the effect that ST algorithm may not be supplied at Threshold level. Added qualifying notes to 2.7,2.8.|Lewis|
|3\.0|05\.12.2017|Feedback during the teleconference.|Lewis|
|3\.1|22\.12.2017|Feedback during and after (emails) the teleconference (05/12/2017) included.|Siqueira|
|3\.2|01\.08.2018|Outcome from LSI-VC-6 meeting addressed: *Surface Brightness Temperature (SBT) is not needed as a CARD4L product – there is no clear user base. The Surface Temperature (ST) PFS will be retained, with references to SBT removed in the next update cycle."* Therefore, ST became the minimum requirement (threshold) for CARD4L ST PFS.|Siqueira|
|3\.3|21\.01.2019|Feedback from ESA and USGS self-assessment included. Added Annex 1 containing examples (provided by USGS and ESA) on selected requirements.|Siqueira|
|3\.3.1|06\.02.2019|Final draft shared with LSI-VC list and LSI-VC-7 meeting participants seeking support for document endorsement at the LSI-VC-7 meeting.|Siqueira|
|3\.3.1|20\.02.2019|Comments and suggestions from LSI-VC-7 meeting (minutes) and feedback from USGS incorporated.|Siqueira|
|3\.3.2|28\.02.2019|Formatting and verbiage updates for consistency.|Metzger|
|4\.0|02\.03.2019|Version endorsed at LSI-VC7 meeting (14Feb 2019)|LSI-VC|
|4\.1|26\.06.2019|Added self-assessment columns|Bontje|
|4\.2|04\.09.2019|Requirement 3.2 (Corrections for Atmosphere and Emissivity) rewording - agreed at LSI-VC8 meeting.|Siqueira|
|<p>4\.3</p><p></p><p></p><p></p><p></p><p></p><p>4\.4</p><p>5\.0</p>|<p>08\.05.2020</p><p></p><p></p><p></p><p></p><p></p><p>25\.05.2020</p><p>08\.06.2020</p>|<p>This review cycle considers feedback received from USGS and ESA after the formal self-assessment for Surface Temperature products (Landsat and Sentinel-2). Minor editorial changes were done throughout the document. Requirements 1.2, 1.14, 1.16 and 2.1 have been updated.</p><p>Feedback from USGS added (email: 21/05/2020).</p><p>Tech edit.</p>|<p>Siqueira</p><p></p><p></p><p></p><p></p><p></p><p>Siqueira</p><p>Bontje, Labahn</p>|

<a name="_hlk42517514"></a>Adam Lewis, Geoscience Australia, Australia

Jonathon Ross, Geoscience Australia, Australia

Andreia Siqueira, Geoscience Australia, Australia

Darcie Bontje, USGS, USA

Steve Labahn, USGS, USA

Mary Metzger, USGS, USA

# **Description**
**Product Family Title:** 		**Surface Temperature (CARD4L-ST)**

**Applies to:*** 	Data collected with multispectral sensors operating in the thermal infrared (TIR) wavelengths. These typically operate with ground sample distance and resolution in the order of 10-100m; however, the Specification is not inherently limited to this resolution.

At present, surface temperature measurements tend to be provided as either surface brightness temperature (SBT) or as land surface temperatures (LST) requiring the SBT to be modified according to the emissivity of the target. This specification identifies the Surface Temperature (ST) as being the minimum or Threshold requirement for analysis ready land surface data. Nevertheless, both SBT and LST are *land* measurements, requiring atmospheric corrections.
# **Definitions**

|LST|Land Surface Temperature|
| :-: | :- |
|ST|Surface Temperature|
|SBT|Surface Brightness Temperature|
|Ancillary Data|Ancillary data is data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information and data from other instruments.|
|Auxiliary Data|Auxiliary data is the data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources.|
|Metadata|Metadata is structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data, without the need to have knowledge about its entire content.|
|MTF|Modulation Transfer Function|
|Spectral Resolution|Spectral resolution defines the narrowest spectral feature that can be resolved by a spectrometer.|
|Spatial Resolution|The highest magnification of the sensor at the ground surface.|
|Spectral Sampling Distance|Spectral sampling is the interval, in wavelength units, between discrete data points in the measured spectrum.|
|Spatial Sampling Distance|Spatial sampling distance is the barycentre-to-barycentre distance between adjacent spatial samples on the Earth's surface.|

#
# **Requirements**
## **General Metadata**
<a name="_1fob9te"></a>*These are metadata records describing a distributed collection of pixels. The collection of pixels referred to must be contiguous in space and time. General Metadata should allow the user to assess the overall suitability of the dataset, and must meet the following requirements:*

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|<p>**Target (Desired)**</p><p>**Requirements**</p>|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**1.1**|**Traceability**|Not required.|<p>Data must be traceable to SI reference standard. Information on traceability should be available in the metadata as a single DOI landing page.</p><p></p><p>Policy on measurement traceability: <https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6536></p><p></p><p>Guidance on measurement traceability: <https://anab.qualtraxcloud.com/ShowDocument.aspx?ID=6532></p><p>*Note 1: SI Traceability requires an estimate of measurement uncertainty.*</p>|||||
|**1.2**|**Metadata Machine Readability**|Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use.|As threshold, but metadata should be provided in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2.|||||
|**1.3**|**Data Collection Time**|The start and stop time of data collection is identified in the metadata, expressed in date/time, to the second, with the time offset from UTC unambiguously identified.|<a name="_3znysh7"></a>Acquisition time for each pixel is identified (or can be reliably determined) in the metadata, expressed in date/time at UTC, to the second.|||||
|**1.4**|**Geographical Area**|The surface location to which the data relate is identified, typically as a series of four corner points, expressed in an accepted coordinate reference system (e.g., WGS84 coordinates).|The geographic area covered by the observations is identified specifically, such as through a set of coordinates of a closely bounding polygon. The location to which each pixel refers is identified (or can be reliably determined) expressed in projection coordinates with reference datum. |||||
|**1.5**|**Coordinate Reference System**|The metadata lists the coordinate reference system that has been used.|As threshold.|||||
|**1.6**|**Map Projection**|Not required. |The metadata lists the map projection that has been used, if any, and any relevant parameters required in relation to use of data in that map projection.|||||
|**1.7**|**Geometric Correction Methods**|<p>Not required. </p><p></p><p>The user is not explicitly advised of the geometric correction source and methods.</p>|Information on geometric correction methods should be available in the metadata as a single DOI landing page containing information on geodetic correction methods used, including reference database and auxiliary data such as elevation model(s) and reference chip-sets.  |||||
|**1.8**|**Geometric Accuracy of the Data**|<p>Not required. </p><p>The user is not provided with results of geometric correction processes pertaining to the dataset.</p>|<p>The metadata includes metrics describing the assessed geodetic accuracy of the data, expressed units of the coordinate system of the data. Accuracy is assessed by independent verification (as well as internal model-fit where applicable). Uncertainties are expressed as root mean square error (RMSE) or Circular Error 90% Probability (CEP90).</p><p>*Note 1: Information on geometric accuracy of the data should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.9**|**Instrument**|The instrument used to collect the data is identified in the metadata.|As threshold, but information on instrument should be available in the metadata as a single DOI landing page with references to the relevant CEOS Missions, Instruments and Measurements Database record.|||||
|**1.10**|**Spectral Bands**|The central wavelength for each band for which data is included is identified in the metadata, expressed in SI units.|<p>As threshold, with instrument spectral response details (e.g., full spectral response function) also included or directly accessible using details in the metadata. <br>Central wavelength and bandwidth at full-width half maximum value of the relative spectral response function are provided at least.</p><p>*Note 1: Information on spectral bands should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.11**|**Sensor Calibration**|Not required.|<p>Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata. Ideally this would support machine-to-machine access. </p><p>*Note 1: Information on sensory calibration should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.12**|**Radiometric Accuracy**|<p>Not required. </p><p>The general metadata does not include information on the radiometric accuracy of the data.</p>|<p>Information on radiometric accuracy should be available in the metadata as a single DOI landing page providing information on metrics describing the assessed absolute radiometric accuracy of the data, expressed as absolute radiometric uncertainty relative to a known reference standard.</p><p>*Note 1: For example, this may come from comparison with routine and rigorously collected in situ measurements.* </p>|||||
|**1.13**|**Algorithms**|All algorithms and versions, and the sequence in which they were applied in the generation process, are identified in the metadata.|<p>As threshold, but only algorithms that have been published in a peer-reviewed journal.</p><p>*Note 1: It is possible that high-quality corrections are applied through non-disclosed processes*. *CARD4L does not per-se require full and open data and methods.*</p><p>*Note 2: Information on algorithms should be available in the metadata as a single DOI landing page.*</p>|||||
|**1.14**|**Auxiliary Data**|<p>The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as a single DOI landing page. </p><p>*Note 1: Auxiliary data includes DEMs, aerosols, etc. data sources.*</p>|<p>As threshold, but information on auxiliary data should be available in the metadata as a single DOI landing page and is also available for free online download, contemporaneously with the product or through a link to the source.</p><p></p>|||||
|**1.15**|**Processing Chain Provenance**|<p>Not required.</p><p></p>|Information on processing chain provenance should be available in the metadata as a single DOI landing page containing description of the processing chain used to generate the product, including the versions of the software used and information on the data collection baseline, giving full transparency to the users.|||||
|**1.16**|**Data Access**|<p>Information on data access should be available in the metadata as a single DOI landing page.</p><p>*Note 1: Manual and offline interaction action (e.g., login) may be required.*</p>|<p>As threshold.</p><p></p>|||||
|**1.17**|**Overall Data Quality**|Not applicable.|The metadata includes details of the quality of the product based on quantitative assessment of the product with respect to high quality reference data with full traceability of the uncertainties. Validation and intercomparison statistics can provide the necessary quantification. |||||


## **Per-Pixel Metadata**
*Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for application and includes ‘quality flags’. The following minimum metadata specifications apply to each pixel. Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider. Similarly, the mechanism or form of the per-pixel metadata (additional data bands, mask layers, etc.) is open to the provider.* 

|**#**|**Item**|**Threshold (Minimum) Requirements**|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**2.1**|**Metadata Machine Readability**|Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component part for further use.|As threshold.|||||
|**2.2**|**No Data**|Pixels that do not correspond to an observation (‘empty pixels’) are flagged.|As threshold.|||||
|**2.3**|**Incomplete Testing**|<p>The metadata identifies pixels for which the per-pixel tests (below) have not all been successfully completed.</p><p>*Note 1: e.g., due to missing ancillary data for some pixels.*</p>|<p>The metadata identifies which tests have, and have not, been successfully completed for each pixel.</p><p></p>|||||
|**2.4**|**Saturation**|Metadata indicates where one or more pixel in the input spectral bands are saturated.|Metadata indicates which pixels are saturated for each spectral band.|||||
|**2.5**|**Cloud**|Metadata indicates whether a pixel is assessed as being cloud.|As threshold, but information on cloud detection should be available in the metadata as a single DOI landing page.|||||
|**2.6**|**Cloud Shadow**|Metadata indicates whether a pixel is assessed as being cloud shadow.|As threshold, but information on cloud shadow detection should be available in the metadata as a single DOI landing page.|||||
|**2.7**|**Snow/ <br>Ice mask**|Not required.|The metadata indicates whether a pixel is assessed as being snow/ice or not. Information on snow/ice mask should be available in the metadata as a single DOI landing page.|||||
|**2.8**|**Solar and Viewing Geometry**|Provide average solar and sensor viewing azimuth and zenith angles.|Provide per-pixel solar and sensor viewing azimuth and zenith angles.|||||


## **Radiometric and Atmospheric Corrections**
*The following requirements must be met for all pixels in a collection. Radiometric corrections must lead to a valid measurement of surface temperature.*

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**3.1**|**Measurement**|Pixel values are expressed as a measurement of the Surface Temperature of the land, expressed as Kelvin.|Surface temperature measurements are SI traceable (see also 1.1).|||||
|**3.2**|**Corrections for Atmosphere and Emissivity**|<p>Retrieval methods for estimating surface temperature are provided.</p><p>*Note 1: The metadata references (may be through a single DOI landing page) a citable peer-reviewed algorithm.*</p>|As threshold.|||||
|**3.3**|<p>**Measurement Uncertainty**</p><p></p>|<p>Not required.</p><p></p>|<p>Uncertainty, in Kelvin, of the surface temperature measurement for each pixel is provided.</p><p>*Note 1: Some of the intent of the initial wording (below), which refers to atmospheric windows, may have been lost:*</p><p>*Uncertainty, in units Kelvin, of the surface temperature for each pixel is also accompanied by distance from cloud (above) and atmospheric transmission (intervals, i.e., 0.4 - 0.55, 0.55 - 0.7, etc.).*</p>|||||


## **Geometric Corrections**
*Geometric corrections must place the measurement accurately on the surface of the Earth (that is, geolocate the measurement) allowing measurements taken through time to be compared.* 

|**#**|**Item**|<p>**Threshold (Minimum)**</p><p>**Requirements**</p>|**Target (Desired)<br>Requirements**|**Threshold<br>Self-Assessment**|**Target<br>Self-Assessment**|**Self-Assessment<br>Explanation/ Justification**|**Recommended<br>Requirement<br>Modification**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|**4.1**|**Geometric Correction**|<p>Sub-pixel accuracy is achieved in relative geolocation, that is, the pixels from the same instrument and platform are consistently located, and in thus comparable, through time.</p><p></p><p>Sub-pixel accuracy is taken to be less than or equal to 0.5 pixel radial root mean square error (rRMSE) or equivalent in Circular Error Probability (CEP) relative to a defined reference image.</p><p></p><p>A consistent gridding/sampling frame is necessary to meet this requirement.</p><p></p><p>Relevant metadata must be provided under 1.8 and 1.9.</p><p>*Note 1: The threshold level will not necessarily enable interoperability between data from* different *sources as the geometric corrections for each of the sources may differ.* </p>|<p>Sub-pixel accuracy is achieved relative to an identified absolute independent terrestrial referencing system (such as a national map grid). </p><p></p><p>A consistent gridding/sampling frame is necessary to meet this requirement.</p><p></p><p>Relevant metadata must be provided under 1.8 and 1.9.</p><p>*Note 1: This requirement is intended to enable interoperability between imagery from different platforms that meet this level of correction, and with non-image spatial data such as GIS layers and terrain models.*</p><p></p>|||||

#
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
||||
|**2. Per-Pixel Metadata**|||
|2\.1 Metadata Machine Readability|||
|2\.2 No Data|||
|2\.3 Incomplete Testing|||
|2\.4 Saturation|||
|2\.5 Cloud|||
|2\.6 Cloud Shadow|||
|2\.7 Snow/Ice Mask|||
|2\.8 Solar and Viewing Geometry|||
||||
|**3. Radiometric and Atmospheric Corrections**|||
|3\.1 Measurement|||
|3\.2 Corrections for Atmosphere and Emissivity|||
|3\.3 Measurement Uncertainty|||
||||
|**4. Geometric Corrections**|||
|4\.1 Geometric Correction|||



# **Guidance**
This section aims to provide background and specific information on the processing steps that can be used to achieve analysis ready data. This Guidance material does not replace or over-ride the specifications. 
# **Introduction to CARD4L**
**What is CEOS Analysis Ready Data for Land (CARD4L) products?**

CARD4L products have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort. These products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets.

CARD4L products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development. They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures. They may not be suitable for all purposes and are not intended as a ‘replacement’ for other types of satellite products.

**When can a product be called CARD4L?**

The CARD4L branding is applied to a particular product once:

- that product has been assessed as meeting CARD4L requirements by the agency responsible for production and distribution of the product, and
- that assessment has been peer reviewed by the CEOS Land Surface Imaging Virtual Constellation in consultation with the CEOS Working Group on Calibration and Validation.

Agencies or other entities considering undertaking an assessment process should contact the co-leads of the [Land Surface Imaging Virtual Constellation](http://ceos.org/ourwork/virtual-constellations/lsi/). 

A product can continue to use CARD4L branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

**What is the difference between Threshold and Target?**

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making. 

Products that meet target requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the *threshold* level. 

Target requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, *target* specifications may (and subject to due process) become accepted as *threshold* requirements.
# **Procedural Examples**
**Processes to produce Threshold Surface Temperature CARD4L-ST:**

The following correction processes would typically be applied to produce CARD4L-ST Threshold:

- *No example processes are provided at this time.*
# **Specific Examples**
**Processes to produce Threshold Surface Temperature CARD4L-ST:**

- *No example processes are provided at this time.*
# **Reference papers**
The following papers provide scientific and technical guidance:

Cook, M., Schott, J.R, Mandel, J., Raqueno, M. (2014). Development of an Operational Calibration Methodology for the Landsat Thermal Data Archive and Initial Testing of the Atmospheric Compensation Component of a Land Surface Temperature (LST) Product from the Archive. ***Remote Sensing*** 6 (11244-11266). doi:10.3390/rs61111244 ISSN 2072-4292. [www.mdpi.com/journal/remotesensing](http://www.mdpi.com/journal/remotesensing)

Li et al., (2013) Satellite-derived land surface temperature: Current status and perspectives. ***Remote Sensing of Environment*** 131 14–37. <https://doi.org/10.1016/j.rse.2012.12.008>.



# **Annex 1 – CARD4L Requirement Examples (Surface Temperature)**
## **General Metadata**

|**#**|**Item**|**Example 1**|**Example 2**|
| :-: | :-: | :-: | :-: |
|**1.1**|**Traceability**|<p>Example of measurement traceability in metadata: </p><p><band add\_offset="0.000000" category="image" data\_type="INT16" fill\_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale\_factor="0.100000"</p><p>`    `<short\_name>LC08ST</short\_name></p><p>`    `<long\_name>Surface Temperature</long\_name></p><p>`    `<file\_name>ST</file\_name></p><p>`    `<pixel\_size units="meters" x="30" y="30"/></p><p>`    `<resample\_method>none</resample\_method></p><p>`    `<data\_units>temperature (kelvin)</data\_units></p><p>`    `<valid\_range max="3730.000000" min="1500.000000"/></p><p>`    `<app\_version>st\_1.3.0</app\_version></p><p>`    `<production\_date>2018-11-30T04:47:38Z</production\_date></p><p></band></p><p></p><p>Example of measurement uncertainty in metadata:</p><p><band category="qa" data\_type="INT16" fill\_value="-9999" name="STQA" nlines="5000" nsamps="5000" product="st\_qa" scale\_factor="0.010000" source="toa\_refl"></p><p>`    `<short\_name>LC08STQA</short\_name></p><p>`    `<long\_name>Surface temperature quality band</long\_name></p><p>`    `<file\_name>STQA</file\_name></p><p>`    `<pixel\_size units="meters" x="30" y="30"/></p><p>`    `<resample\_method>none</resample\_method></p><p>`    `<data\_units>temperature (kelvin)</data\_units></p><p>`    `<valid\_range max="32767.000000" min="0.000000"/></p><p>`    `<app\_version>st\_1.3.0</app\_version></p><p>`    `<production\_date>2018-11-30T04:47:38Z</production\_date></p><p></band></p>|NA|
|**1.2**|**Metadata Machine Readability**|NA|NA|
|**1.3**|**Data Collection Time**|<p>Example of scene center time (UTC):</p><p><scene\_center\_time>17:23:57.201686Z</scene\_center\_time></p>|The granule start and end times are contained in the XML metadata:<br>`     	`<metadataObject ID="acquisitionPeriod" classification="DESCRIPTION" category="DMD"><br>`        	`<metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Acquisition Period"><br>`           	`<xmlData><br>`              	`<sentinel-safe:acquisitionPeriod><br>`                 	`<sentinel-safe:startTime>2018-10-07T05:04:50.425838Z</sentinel-safe:startTime><br>`                 	`<sentinel-safe:stopTime>2018-10-07T05:07:50.425838Z</sentinel-safe:stopTime><br>`              	`</sentinel-safe:acquisitionPeriod><br>`           	`</xmlData><br>`        	`</metadataWrap><br>`     	`</metadataObject><br><br>Per pixel times are derived using information from the "time\_in.nc" and “indices\_in.nc” datafiles following a prescribed recipe|
|**1.4**|**Geographical Area**|<p>Example of the bounding coordinates in decimal degrees (WGS84):</p><p><bounding\_coordinates></p><p>`    `<west>-99.9109607425</west></p><p>`    `<east>-98.0134952569</east></p><p>`    `<north>43.3609828699</north></p><p>`    `<south>41.9778528562</south></p><p></bounding\_coordinates></p><p></p><p>Example of the corner points in the map projection system (Albers):</p><p><corner\_point location="UL" x="-315585.000000" y="2264805.000000"/></p><p><corner\_point location="LR" x="-165585.000000" y="2114805.000000"/></p>|NA|
|**1.5**|**Coordinate Reference System**|<p>Example of the projected coordinate system info:</p><p></p><p><projection\_information datum="WGS84" projection="AEA" units="meters"></p>|NA|
|**1.6**|**Map Projection**|<p>Example: </p><p><projection\_information datum="WGS84" projection="AEA" units="meters"></p><p>`    `<corner\_point location="UL" x="-315585.000000" y="2264805.000000"/></p><p>`    `<corner\_point location="LR" x="-165585.000000" y="2114805.000000"/></p><p>`    `<grid\_origin>UL</grid\_origin></p><p>`    `<albers\_proj\_params></p><p>`        `<standard\_parallel1>29.500000</standard\_parallel1></p><p>`        `<standard\_parallel2>45.500000</standard\_parallel2></p><p>`        `<central\_meridian>-96.000000</central\_meridian></p><p>`        `<origin\_latitude>23.000000</origin\_latitude></p><p>`        `<false\_easting>0.000000</false\_easting></p><p>`        `<false\_northing>0.000000</false\_northing></p><p>`    `</albers\_proj\_params></p><p></projection\_information></p>|NA|
|**1.7**|**Geometric Correction Source**|<p>Example of elevation source:</p><p><elevation\_source>GLS2000</elevation\_source></p>|The XML wrapper provides the source of the geometric calibration:<br><br><sentinel-safe:resource name="S3A\_SL\_1\_GEC\_AX\_20160216T000000\_20991231T235959\_20180202T120000\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_MPC\_O\_AL\_007.SEN3" role="SLSTR Geometric Calibration Data File"><br>`   `<sentinel-safe:processing name="AdfProcessing"><br>`  	`<sentinel-safe:facility name="ESA Mission Performance Coordinating Centre (MPC)" organisation="ESA Mission Performance Coordinating Centre" site="Sophia Antipolis" country="France"><br>`     	`<sentinel-safe:hardware name="OPE"/><br>`         `<sentinel-safe:software name="ADC" version="1.0"/><br>`      `</sentinel-safe:facility><br>`   `</sentinel-safe:processing><br></sentinel-safe:resource><br> |
|**1.8**|**Geometric Accuracy of the Data**|<p>Example:</p><p><geometric\_rmse\_model>9.021</geometric\_rmse\_model></p><p><geometric\_rmse\_model\_x>6.864</geometric\_rmse\_model\_x></p><p><geometric\_rmse\_model\_y>5.854</geometric\_rmse\_model\_y></p>|NA|
|**1.9**|**Instrument**|<p>Example:</p><p><satellite>LANDSAT\_8</satellite></p><p><instrument>OLI/TIRS\_Combined</instrument></p>|<p>The XML wrapper provides the instrument details:</p><p></p><p>`         `<metadataObject ID="platform" classification="DESCRIPTION" category="DMD"></p><p>`            `<metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Platform Description"></p><p>`               `<xmlData></p><p>`                  `<sentinel-safe:platform></p><p>`                     `<sentinel-safe:nssdcIdentifier>2016-011A</sentinel-safe:nssdcIdentifier></p><p>`                     `<sentinel-safe:familyName>Sentinel-3</sentinel-safe:familyName></p><p>`                     `<sentinel-safe:number>A</sentinel-safe:number></p><p>`                     `<sentinel-safe:instrument></p><p>`                        `<sentinel-safe:familyName abbreviation="SLSTR">Sea and Land Surface Temperature Radiometer</sentinel-safe:familyName></p><p>`                        `<sentinel-safe:mode identifier="EO">Earth Observation</sentinel-safe:mode></p><p>`                     `</sentinel-safe:instrument></p><p>`                  `</sentinel-safe:platform></p><p>`               `</xmlData></p><p>`            `</metadataWrap></p><p>`         `</metadataObject></p>|
|**1.10**|**Spectral Bands**|NA|NA|
|**1.11**|**Sensor Calibration**|<p>Example:</p><p><cpf\_name>LC08CPF\_20180101\_20180331\_01.02</cpf\_name></p>|NA|
|**1.12**|**Radiometric Accuracy**|NA|NA|
|**1.13**|**Algorithms**|<p>Example for Surface Temperature algorithm version:</p><p><app\_version>st\_1.3.0</app\_version></p>|NA|
|**1.14**|**Auxiliary Data**|NA|All Auxiliary Datafiles (ADFs) are listed in the XML wrapper:<br>`                       	`<sentinel-safe:resource name="S3\_\_SL\_2\_LSTBAX\_20000101T000000\_20991231T235959\_20151214T120000\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_MPC\_O\_AL\_001.SEN3" role="SLSTR LST biome data file" version="06.16"><br>`                       	`<sentinel-safe:resource name="S3\_\_SL\_2\_LSTVAX\_20000101T000000\_20991231T235959\_20151214T120000\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_MPC\_O\_AL\_001.SEN3" role="SLSTR LST vegetation fraction data file" version="06.16"><br>`                       	`<sentinel-safe:resource name="S3\_\_SL\_2\_LSTWAX\_20000101T000000\_20991231T235959\_20151214T120000\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_MPC\_O\_AL\_001.SEN3" role="SLSTR LST water vapour data file" version="06.16">|
|**1.15**|**Processing Chain Provenance**|NA|Processing chain provenance information is stored in the XML wrapper under the following tag:<br>`     	`<metadataObject ID="processing" classification="PROVENANCE" category="PDI">|
|**1.16**|**Data Access**|NA|NA|
|**1.17**|**Overall Data Quality**|NA|Overall data quality information is stored in the XML wrapper under the following tag:<br>`     	`<metadataObject ID="measurementQualityInformation" classification="DESCRIPTION" category="DMD">|


## **Per-Pixel Metadata**

|**#**|**Item**|**Example 1**|**Example 2**|
| :-: | :-: | :-: | :-: |
|**2.1**|**Metadata Machine Readability**|NA|NA|
|**2.2**|**No Data**|<p>Example of the fill\_value specified for each band in metadata:</p><p><band add\_offset="0.000000" category="image" data\_type="INT16" fill\_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale\_factor="0.100000"</p><p>`    `<short\_name>LC08ST</short\_name></p><p>`    `<long\_name>Surface Temperature</long\_name></p><p>`    `<file\_name>ST</file\_name></p><p>`    `<pixel\_size units="meters" x="30" y="30"/></p><p>`    `<resample\_method>none</resample\_method></p><p>`    `<data\_units>temperature (kelvin)</data\_units></p><p>`    `<valid\_range max="3730.000000" min="1500.000000"/></p><p>`    `<app\_version>st\_1.3.0</app\_version></p><p>`    `<production\_date>2018-11-30T04:47:38Z</production\_date></p><p></band></p>|<p>The "flags\_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:<br><br>`    	`ushort confidence\_in(rows, columns) ;<br>`            	`confidence\_in:flag\_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;<br>`            	`confidence\_in:flag\_meanings = "coastline ocean tidal land inland\_water unfilled spare spare cosmetic duplicate day twilight sun\_glint snow summary\_cloud summary\_pointing" ;</p><p></p><p></p>|
|**2.3**|**Incomplete Testing**|NA|The "flags\_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:<br><br>`        `ushort confidence\_in(rows, columns) ;<br>`                `confidence\_in:flag\_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;<br>`                `confidence\_in:flag\_meanings = "coastline ocean tidal land inland\_water unfilled spare spare cosmetic duplicate day twilight sun\_glint snow summary\_cloud summary\_pointing”;|
|**2.4**|**Saturation**|<p>Example of RADSATQA band showing the saturation information for the thermal bands used for Surface Temperature calculation:</p><p><band category="qa" data\_type="UINT16" fill\_value="1" name="RADSATQA" nlines="5000" nsamps="5000" product="toa\_refl" source="level1"></p><p>`    `<short\_name>LC08RADSAT</short\_name></p><p>`    `<long\_name>saturation mask</long\_name></p><p>`    `<file\_name>RADSATQA</file\_name></p><p>`    `<pixel\_size units="meters" x="30" y="30"/></p><p>`    `<resample\_method>none</resample\_method></p><p>`    `<data\_units>bitmap</data\_units></p><p>`    `<bitmap\_description></p><p>`        `<bit num="0">Data Fill Flag (0 = valid data, 1 = invalid data)</bit></p><p>`        `<bit num="1">Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="2">Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="3">Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="4">Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="5">Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="6">Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="7">Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="8">N/A</bit></p><p>`        `<bit num="9">Band 9 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="10">Band 10 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`        `<bit num="11">Band 11 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit></p><p>`    `</bitmap\_description></p><p>`    `<app\_version>LaSRC\_1.3.0</app\_version></p><p>`    `<production\_date>2018-11-30T04:47:38Z</production\_date></p><p></band></p>|The "flags\_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:<br><br>`        `ushort confidence\_in(rows, columns) ;<br>`                `confidence\_in:flag\_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;<br>`                `confidence\_in:flag\_meanings = "coastline ocean tidal land inland\_water unfilled spare spare cosmetic duplicate day twilight sun\_glint snow summary\_cloud summary\_pointing" ;|
|**2.5**|**Cloud**|<p>Example of PIXELQA showing the bit value for cloud pixels (as well as cloud and cirrus confidence):</p><p><band category="qa" data\_type="UINT16" fill\_value="1" name="PIXELQA" nlines="5000" nsamps="5000" product="level2\_qa" source="level1"></p><p>`    `<short\_name>LC08PQA</short\_name></p><p>`    `<long\_name>level-2 pixel quality band</long\_name></p><p>`    `<file\_name>PIXELQA</file\_name></p><p>`    `<pixel\_size units="meters" x="30" y="30"/></p><p>`    `<resample\_method>none</resample\_method></p><p>`    `<data\_units>quality/feature classification</data\_units></p><p>`    `<bitmap\_description></p><p>`        `<bit num="0">fill</bit></p><p>`        `<bit num="1">clear</bit></p><p>`        `<bit num="2">water</bit></p><p>`        `<bit num="3">cloud shadow</bit></p><p>`        `<bit num="4">snow</bit></p><p>`        `<bit num="5">cloud</bit></p><p>`        `<bit num="6">cloud confidence</bit></p><p>`        `<bit num="7">cloud confidence</bit></p><p>`        `<bit num="8">cirrus confidence</bit></p><p>`        `<bit num="9">cirrus confidence</bit></p><p>`        `<bit num="10">terrain occlusion</bit></p><p>`        `<bit num="11">unused</bit></p><p>`        `<bit num="12">unused</bit></p><p>`        `<bit num="13">unused</bit></p><p>`        `<bit num="14">unused</bit></p><p>`        `<bit num="15">unused</bit></p><p>`    `</bitmap\_description></p><p>`    `<app\_version>generate\_pixel\_qa\_1.6.0</app\_version></p><p>`    `<production\_date>2018-11-30T04:47:38Z</production\_date></p><p></band></p>|The "flags\_in.nc" datafile contains all the cloud masking flags<br>Three fields are relevant: i) cloud\_in; ii) confidence\_in; and iii) bayes\_in<br><br>The "cloud\_in" field contains all the individual threshold-based mask:<br>flag\_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128U 	S, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;<br>cloud\_in:flag\_meanings = "visible 1.37\_threshold 1.6\_small\_histo 	gram 1.6\_large\_histogram 2.25\_small\_histogram 2.25\_large\_histogram 11\_spatial\_co 	herence gross\_cloud thin\_cirrus medium\_high fog\_low\_stratus 11\_12\_view\_differenc 	e 3.7\_11\_view\_difference thermal\_histogram spare spare"<br><br>The "confidence\_in" field contains the "summary\_cloud\_mask" from the most appropriate cloud\_in flags; the value of the bit is 16384US<br><br>The "bayes\_in" field contains the "single\_moderate" probabilistic cloud flag; the value of the bit is 2UB|
|**2.6**|**Cloud Shadow**|Please see the cloud shadow part in the example provided in requirement 2.5|NA|
|**2.7**|**Snow/Ice Mask**|Please see the snow part in the example provided in requirement 2.5|NA|
|**2.8**|**Solar and Viewing Geometry**|NA|NA|


## **Radiometric and Atmospheric Corrections**

|**#**|**Item**|**Example 1**|**Example 2**|
| :-: | :-: | :-: | :-: |
|**3.1**|**Measurement**|NA|NA|
|**3.2**|**Corrections for Atmosphere (and Emissivity in the Case of ST)**|<p>NA</p><p></p>|NA|
|**3.3**|**Measurement Uncertainty**|NA|NA|

## **Geometric Corrections**

|**#**|**Item**|**Example 1**|**Example 2**|
| :-: | :-: | :-: | :-: |
|**4.1**|**Geometric Correction**|NA|NA|


