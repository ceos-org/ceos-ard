<!--lint disable-->
<img align="right" width="150" src="./Logo/CEOS_ARD_Logo_blue_lowres.png">

# CEOS Analysis Ready Data <br> Product Family Specification: Synethetic Aperture Radar
﻿
|<a name="_heading=h.30j0zll"></a>**Version**|**Date**|**Description of change**|**Affected CEOS-ARD product**|**Author**|
| :- | :- | :- | :- | :- |
|0\.1|14-12-2022|Zero Draft based on the CARD4L NRB PFS v5.5, POL PFS 3.5, ORB PFS v1.0 and draft GSLC v0.1 |-|<p>Charbonneau</p><p>Truckenbrodt</p>|
|0\.2|13-02-2023|<p>Reformat to CEOS-ARD PFS template. Change “CARD4L” to “CEOS-ARD”</p><p>Change “Target” to “Goal”</p>|-|Rosenqvist|
|0\.3|29-07-2023|<p>Refinement of GSLC specifications and alignment with NRB, POL and ORB parameters. </p><p></p><p>Annex reorganization and ORB and GSLC examples added</p>|[GSLC]|Charbonneau, Zebker, Rosenqvist, Albinet, Small, Truckenbrodt|
|0\.3.1|26-09-2023|New items 1.7.15 (Reference orbit) and 3.7 (Flattened Phase) added as Goal|[NRB] [POL]|Charbonneau|
|0\.4|26-09-2023|Item 4.3 (Geometric accuracy). Clarification added to indicate whether absolute location accuracy (ALE) estimates refer to source data, ARD product, or both.|[NRB] [POL] [ORB] [GSLC]|Small, Chapman, Charbonneau, Rosenqvist, Albinet, Truckenbrodt|
|0\.4.1|11-10-2023|Add product code in summary table|     |Rosenqvist|
|1\.0|11-10-2023|CEOS-ARD for SAR PFS – including Geocoded Single-Look Complex v1.0 – endorsed at LSI-VC-14     |     |LSI-VC|

<a name="_heading=h.oq5oi4r2r64e"></a>
# **Contributing Authors**
François Charbonneau, Natural Resources Canada, Canada

Ake Rosenqvist, soloEO / Japan Aerospace Exploration Agency, Japan

John Truckenbrodt, German Aerospace Centre (DLR), Germany

Clément Albinet, European Space Agency (ESA), Italy

David Small, University of Zurich, Switzerland

Bruce Chapman, Jet Propulsion Laboratory, USA

Howard Zebker, Stanford University, USA

Danilo Dadamia, CONAE, Argentina

Benjamin Deschamps, Environment and Climate Change, Canada

Guillaume Hajduch, Collecte Localisation Satellites, France

Josef Kellndorfer, Earth Big Data, USA

Marco Lavalle, Jet Propulsion Laboratory, USA

Thomas Logan, Alaska Satellite Facility, USA

Franz Meyer, Alaska Satellite Facility, USA

Nuno Miranda, European Space Agency (ESA), Italy

Muriel Pinheiro, European Space Agency (ESA), Italy

Marko Repse, Sinergise, Slovenia

HariPriya Sakethapuram, ISRO, India

Andreia Siqueira, Geoscience Australia, Australia

Takeo Tadono, Japan Aerospace Exploration Agency, Japan

Medhavy Thankappan, Geoscience Australia, Australia

Antonio Valentino, RHEA *for* European Space Agency (ESA), Italy

Anna Wendleder, German Aerospace Centre (DLR), Germany

Fang Yuan, Digital Earth Africa, Australia

Zheng-Shu Zhou, CSIRO, Australia


# **CEOS Analysis Ready Data Definition**
*“CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.”*

# **Description**
**Product Family Specification Title: 	Synthetic Aperture Radar (CEOS-ARD SAR)**

**Applies to:**  				Data collected by Synthetic Aperture Radar sensors





# **Background to CEOS-ARD for Synthetic Aperture Radar**
The CEOS Analysis Ready Data (CEOS-ARD) Product Family Specification (PFS) for Synthetic Aperture Radar (SAR) data is specifically aimed at users interested in exploring the potential of SAR but who may lack the expertise or facilities for SAR processing. 

This CEOS-ARD for Synthetic Aperture Radar PFS incorporates, into a single generic document, the following four CEOS-ARD SAR specifications endorsed by CEOS Land Surface Imaging-Virtual Constellation (CEOS LSI-VC):

- Normalised Radar Backscatter [version 5.5]
- Polarimetric Radar [version 3.5]
- Ocean Radar Backscatter [version 1.0]
- Geocoded Single-Look Complex [version 1.0]	

The **CEOS-ARD Normalised Radar Backscatter [NRB]** specification describes products that have been subject to Radiometric Terrain Correction (RTC) and are provided in the Gamma-Nought ($\gamma^0_T$) backscatter convention (Small, 2011), which mitigates the variations from diverse observation geometries and is recommended for most land applications. An additional metadata layer can be optionally provided for conversion of $\gamma^0_T$ to Sigma-Nought ($\sigma^0_T$) backscatter layer for compatibility with legacy software or numerical models. As the **[NRB]** product contains backscatter values only, it cannot be directly used for SAR polarimetry or interferometric applications that require relative polarization phase or local phase estimates respectively. However, as an option, a “flattened” phase data layer can be provided with an **[NRB]** product for enabling InSAR analysis. The flattened phase is the interferometric phase, with respect to a reference orbit and to a DEM, for which the topographic phase contribution is removed. 



The **CEOS-ARD** **Polarimetric Radar [POL]** product format is an extension of the CEOS-ARD Normalised Radar Backscatter format **[NRB]**. This extension is required in order to better support Level-1 SLC polarimetric data, including full-polarimetric modes (e.g., RADARSAT-2, ALOS-2/4, SAOCOM-1 and future missions), and hybrid or linear dual-polarimetric modes (i.e., Compact Polarimetric mode available on RCM, SAOCOM and the upcoming NISAR mission). The **[POL]** product can be defined in two processing levels:

- The normalised covariance matrix **[CovMat]** representation (C2 or C3) which preserves the inter-channel polarimetric phase(s) and maximizes the available information for users. Interoperability within current CEOS-ARD SAR backscatter definition is preserved, since diagonal elements of the covariance matrix are backscatter intensities. Scattering information enhancement can be achieved by applying incoherent polarimetric decomposition techniques (e.g., Freeman-Durden, van Zyl, Cloude-Pottier, Yamaguchi-based) directly on the C2 or C3 matrix. 

- Polarimetric Radar Decomposition **[PRD]** refers to ARD products where polarimetric information is broken down into simplified parameters to facilitate user interpretation of the data. They are derived from coherent or incoherent polarimetric decomposition techniques. 

**Notice and Limitations [POL]**

For Polarimetric Radar **[POL]** products, optimal incoherent Polarimetric Radar Decomposition **[PRD]** should be performed under the slant range projection (Gens et al., 2013, Toutin et al., 2013). In order to minimise bias in the CEOS-ARD SAR Level-2a covariance matrix product, speckle filtering and averaging of the covariance matrix should be applied in the slant range projection, and geocoding should be performed using nearest-neighbour resampling. Specifically, nearest-neighbour resampling ensures that the averaged covariance matrix elements in slant range and in geocoded ground projection are exactly the same. Consequently, the polarimetrically derived parameters are exactly equal in both approaches (assuming that no further averaging is performed on the ARD product for decomposing the polarimetric information). Bilinear and average resampling methods are also suitable for resampling the covariance matrix, but some differences with polarimetric parameters generated in slant range and then resampled (bilinear) might be observed on sloped terrains. Even if Sinc interpolation may be more robust for spatial resampling, it does not preserve covariance matrix integrity, and should consequently not be used for this ARD product.

It is recommended that ARD providers who desire to distribute **[PRD]** products decompose the polarimetric information starting from Level-1 SLC data and then geocode the derived parameters rather than use the **[CovMat]** ARD product. Resampling can be performed using any of the supported methods (nearest-neighbour, bilinear, average, bi-cubic spline or Lanczos are recommended), which need to be indicated in the product metadata. Note that coherent decomposition techniques cannot be performed on **[CovMat]** ARD products.



Covariance matrix products contain a variable number of layers (or bands) with different data types depending on the polarimetric mode (full or dual) and decomposition technique. The **[CovMat]** products for the C2 matrix have 3 layers (2 real-valued diagonal elements and            1 complex-valued off-diagonal element). **[CovMat]** products for the C3 matrix have 6 layers (3 real-valued diagonal elements and 3 complex-valued off-diagonal elements). Layers that can be obtained via a complex conjugation of other layers are not provided within the product. Polarimetric Decomposition products contain typically 2 to 4 (or more) real-valued layers depending on the particular decomposition algorithm. Within the **[CovMat]** product files, ARD layers are organized in order to reduce access delays and maximize efficiency in extracting the desired information. In **[CovMat]** products, geographically contiguous samples for each layer may be stored next to each other and organized “layer by layer”. Alternatively, samples belonging to the same covariance matrix might be stored next to each other and organized “matrix by matrix”. **[PRD]** products are organized “layer by layer”, i.e., with bands corresponding to the output of the polarimetric decomposition stored next to each other. ). 

The **CEOS-ARD Ocean Radar Backscatter [ORB]** product specification describes products that have been projected on a geoid and are provided in the Sigma-Nought ($\sigma^0$) backscatter convention, which is recommended for most ocean applications. Backscatter may be calibrated to the ellipsoid ($\sigma^0_E$) or radiometrically terrain corrected ($\sigma^0_T$) prior to geometric terrain correction. As the basic **[ORB]** product contains backscatter values only, it *cannot* be directly used for SAR polarimetry or interferometric applications that require local phase estimates. Nonetheless, an advanced **[ORB]** product could include the upper diagonal of the polarimetric $\sigma^0$ covariance matrix for enabling advanced polarimetric analysis (similar to the **[POL]** product). 

The **CEOS-ARD Geocoded Single-Look Complex (GSLC)** product is relevant to interferometric studies. The **[GSLC]** product is derived from the range-Doppler (i.e. slant range) Single-Look Complex (SLC) product using a DEM and the orbital state vectors and output in the map projected system. The phase of a geocoded SLC is “flattened” with respect to a reference orbit and to a DEM, to eliminate topographic phase contributions [Zebker et al., 2017 and Zheng and Zebker, 2017]. The sample spacing of the **[GSLC]** product in the map coordinate directions is comparable to the full resolution original SLC product. The **[GSLC]** product can be directly overlaid on a map or combined with other similar **[GSLC]** products to derive interferograms and create change maps, for example. Since the **[GSLC]** phase is flattened, the phase difference between two **[GSLC]** products** acquired on a same relative orbit produces an interferogram referring only to surface displacement and noise (i.e., no topographic fringes). The **[GSLC]** product may optionally** be radiometrically terrain corrected such that the squared amplitude yields $\gamma^0_T$.


As can be seen from the above PFS descriptions, only a few minor details in terms of generated parameters and/or the addition of supplemental data distinguish these CEOS-ARD products. In part, they are to a large extent all backward-compatible. For example, [POL] products implicitly include [NRB] products, while a coastal [NRB] or [POL] product can simply be made compatible with other [ORB] products by applying gamma-to-sigma conversion. Just as [GSLC] can be converted to [NRB], the inverse conversion can be made true by including the optional topographically flattened phase. In this way a [NRB] or [POL] product can be used like a [GSLC] for InSAR applications. Consequently, it becomes obvious that they all can follow a common approach, in terms of content and structure, in order to optimize their interoperability. 

For this generic **CEOS-ARD for Synthetic Aperture Radar** PFS, as for the individual **[NRB]**, **[POL]**, **[ORB]**, and **[GSLC]** PFSs, metadata requirements are defined under two categories: Threshold and Goal. **Threshold requirements** refer to metadata parameters or data files which are mandatorily required in a product in order to be CEOS-ARD compliant. **Goal requirements** (formerly referred to as Target) are complementary metadata parameters or data files that are desirable or more accurate but more constraining/challenging to achieve depending on the SAR missions and the data provider constraints. Since this document integrates four CEOS-ARD PFSs, it is worth noting that some requirements have been “relaxed” for a few Threshold parameters, depending on the applications/environment of the CEOS-ARD product. Exceptions are identified in the tables by specifying the usage.

# **Definitions and Abbreviations**

|Ancillary Data|Data other than instrument measurements, originating in the instrument itself or from the satellite, required to perform processing of the data. They include orbit data, attitude data, time information, spacecraft engineering data, calibration data, data quality information, and data from other instruments.|
| :-: | :- |
|Auxiliary Data|The data required for instrument processing, which does not originate in the instrument itself or from the satellite. Some auxiliary data will be generated in the ground segment, whilst other data will be provided from external sources.|
|CEOS-ARD|Committee on Earth Observation Satellites - Analysis Ready Data|
|CovMat|Normalised Radar Covariance Matrix|
|DOI|Digital Object Identifier|
|GSLC|Geocoded Single-Look Complex|
|InSAR|Interferometric Radar|
|Metadata|Structured information that describes other information or information services. With well-defined metadata, users should be able to get basic information about data without a need to have knowledge about its entire content.|
|NRB|Normalised Radar Backscatter|
|Pixel Spacing|Processed sample distance|
|POL|Polarimetric Radar|
|PRD|Polarimetric Radar Decomposition|
|RTC|Radiometrically Terrain Corrected|
|Spatial Resolution|The smallest size objects that can be distinguished by the sensor at the ground surface.|
|Spatial Sampling Distance|Spatial sampling distance is the great circle distance on the reference surface distance between adjacent spatial samples on the Earth's surface.|


   
# **Requirements**
## **General Metadata** 
*These are metadata records describing a distributed collection of pixels. The collection of pixels referred to must be contiguous in space and time. General metadata should allow the user to assess the overall suitability of the dataset and must meet the requirements listed below. The column “CEOS-ARD product” indicates to which CEOS-ARD SAR product (NRB, POL, ORB, GSLC) the parameter refers.*

<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>1.1</b></td><td colspan="1" rowspan="2"><b>Traceability</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Data must be traceable to SI reference standard. </p><p></p><p><i>Note 1: Relationship to 3.5. Traceability requires an estimate of measurement uncertainty.</i></p><p><i>Note 2: Information on traceability should be available in the metadata as a single DOI landing page.</i></p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.2</b></td><td colspan="1" rowspan="2"><b>Metadata Machine Readability</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Metadata is provided in a structure that enables a computer algorithm to be used consistently and to automatically identify and extract each component part for further use.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p><p></p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, but metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.0, or in a community endorsed standard that facilitates machine-readability, such as ISO 19115-2, Climate and Forecast (CF) convention and the Attribute Convention for Data Discovery (ACDD), etc.</p><p></p><p></p><p></p><p></p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.3</b></td><td colspan="1" rowspan="2"><b>Product Type</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>CEOS-ARD product type name – or names in case of compliance with more than one product type – and, if required by the data provider, copyright.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.4</b></td><td colspan="1" rowspan="2"><b>Document Identifier</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Reference to CEOS-ARD for Synthetic Aperture Radar PFS document as URL.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.5</b></td><td colspan="1" rowspan="2"><b>Data Collection Time</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Number of source data acquisitions of the data collection is identified. The start and stop UTC time of data collection is identified in the metadata, expressed in date/time.  In case of composite products, the dates/times of the first and last data takes and the per-pixel metadata 2.8 (Acquisition ID Image) is provided with the product.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1"><b>1.6</b></td><td colspan="1"><b>Source Data Attributes</b></td><td colspan="1"></td><td colspan="1"><p>Subsection describing (detailing) each SAR acquisition used to generate the ARD product.</p><p></p><p><i>Note: Source data attribute information are described for each acquisition and sequentially identified as acqID= 1, 2, 3, …</i></p></td><td colspan="1" valign="top"></td></tr>
</table>


<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.1</b></td><td colspan="1" rowspan="2"><b>Source Data Access</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>The metadata identifies the location from where the source data can be retrieved, expressed as a URL or DOI.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.2</b></td><td colspan="1" rowspan="2"><b>Instrument</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>The instrument used to collect the data is identified in the metadata:</p><p>- Satellite name</p><p>- Instrument name</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, but including a reference to the relevant CEOS Missions, Instruments and Measurements Database record.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.3</b></td><td colspan="1" rowspan="2"><p><b>Source Data Acquisition</b></p><p><b>Time</b></p></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>The start date and time of source data is identified in the metadata, expressed in UTC in date and time, at least to the second.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.4</b></td><td colspan="1" rowspan="2"><b>Source Data Acquisition Parameters</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Acquisition parameters related to the SAR antenna:</p><p>- Radar band</p><p>- Centre frequency </p><p>- Observation mode (i.e., Beam mode name)</p><p>- Polarization(s) (listed as in original product)</p><p>- Antenna pointing [Right/Left]</p><p>- Beam ID (i.e., Beam mode Mnemonic)</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.5</b></td><td colspan="1" rowspan="2"><b>Source Data Orbit Information</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Information related to the platform orbit used for data processing: </p><p>- Pass direction [asc/desc) *</p><p>- Orbit data source [e.g., predicted/ definite/ precise/ downlinked, etc.]</p><p></p><p><i>* For source data crossing the North or South Pole, it is recommended to produce two distinct CEOS-ARD products and to use the appropriate “Pass direction” in each.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, including also:</p><p>- Platform heading angle expressed in degrees [0 360] from North</p><p>- Orbit data file containing state vectors (minimum of 5 state vectors, from 10% of scene length <i>before</i> start time to 10% of scene length <i>after</i> stop time)</p><p>- Platform (mean) altitude.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.6</b></td><td colspan="1" rowspan="2"><b>Source Data Processing Parameters</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Processing parameters details of the source data:</p><p>- Processing facility</p><p>- Processing date</p><p>- Software version</p><p>- Product level</p><p>- Product ID (file name)</p><p>- Azimuth number of looks</p><p>- Range number of looks (separate values for each beam, as necessary)</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, plus additional relevant processing parameters, e.g., range- and azimuth look bandwidth and LUT applied.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.7</b></td><td colspan="1" rowspan="2"><b>Source Data Image Attributes</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Image attributes related to the source data:</p><p>- Source Data geometry (slant range/ground range)</p><p>- Azimuth pixel spacing</p><p>- Range pixel spacing</p><p>- Azimuth resolution</p><p>- Range resolution </p><p>- Near range incident angle</p><p>- Far range incident angle</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Geometry of the image footprint expressed in WGS84 in a standardised format (e.g., WKT).</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.8</b></td><td colspan="1" rowspan="2"><b>Sensor Calibration</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Sensor calibration parameters are identified in the metadata or can be accessed using details included in the metadata. Ideally this would support machine to machine access.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.9</b></td><td colspan="1" rowspan="2"><b>Performance Indicators</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Provide performance indicators on data intensity noise level (NEσ0 and/or NEβ0 and/or NEγ0 (noise equivalent Sigma- and/or Beta- and/or Gamma-Nought)). Provided for each polarization channel when available.</p><p></p><p>Parameter may be expressed as the mean and/or minimum and maximum noise equivalent values of the source data.</p><p></p><p>Values do not need to be estimated individually for each product, but may be estimated once for each acquisition mode, and annotated on all products.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Provide additional relevant performance indicators (e.g., ENL, PSLR, ISLR, and performance reference DOI or URL).</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.10</b></td><td colspan="1" rowspan="2"><b>Source Data Polarimetric Calibration Matrices</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>The complex-valued polarimetric distortion matrices with the channel imbalance and the cross-talk applied for the polarimetric calibration.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.11</b></td><td colspan="1" rowspan="2"><b>Mean Faraday Rotation Angle</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>The mean Faraday rotation angle estimated from the polarimetric data and/or from models with reference to the method or paper used to derive the estimate.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.6.12</b></td><td colspan="1" rowspan="2"><b>Ionosphere Indicator</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Flag indicating whether the backscatter imagery is “significantly impacted” by the ionosphere (0 – false, 1 – true). Significant impact would imply that the ionospheric impact on the backscatter exceeds the radiometric calibration requirement or goal for the imagery.</p></td></tr>
<tr><td colspan="1"><b>1.7</b></td><td colspan="1"><b>CEOS-ARD Product Attributes</b></td><td colspan="1"></td><td colspan="1">Subsection containing information related to the CEOS-ARD product generation procedure and geographic parameters.</td><td colspan="1" valign="top"></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.1</b></td><td colspan="1" rowspan="2"><b>Product Data Access</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Processing parameters details of the CEOS-ARD product:</p><p>- Processing facility</p><p>- Processing date</p><p>- Software version</p><p>- Location from where CEOS-ARD product can be retrieved, expressed as a URL or DOI.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>The metadata identifies an online location from where the data can be consistently and reliably retrieved by a computer algorithm without any manual intervention being required.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.2</b></td><td colspan="1" rowspan="2"><b>Auxiliary Data</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>The metadata identifies the sources of auxiliary data used in the generation process, ideally expressed as DOIs.</p><p></p><p><i>Note: Auxiliary data includes DEMs, etc., and any additional data sources used in the generation of the product.</i></p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.3</b></td><td colspan="1" rowspan="2"><b>Product Sample Spacing</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>CEOS-ARD product processing parameters details:</p><p>- Pixel (column) spacing</p><p>- Line (row) spacing</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.4</b></td><td colspan="1" rowspan="2"><b>Product Equivalent Number of Looks</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p></p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Equivalent Number of Looks (ENL)</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.5</b></td><td colspan="1" rowspan="2"><b>Product Resolution</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Average spatial resolution of the CEOS-ARD product along:</p><p>- Columns</p><p>- Rows</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.6</b></td><td colspan="1" rowspan="2"><p><b>Product</b></p><p><b>Filtering</b></p></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p></p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Flag if speckle filter has been applied [true/false]. </p><p></p><p>Metadata should include:</p><p>- Reference to algorithm as DOI or URL</p><p>- Input filtering parameters</p><p>&emsp;- Type</p><p>&emsp;- Window size in pixel units</p><p>&emsp;- Any other parameters defining the speckle filter used</p><p></p><p>Mandatory for [POL]: Advanced polarimetric filter preserving covariance matrix properties should be applied.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: … </p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.7</b></td><td colspan="1" rowspan="2"><b>Product Bounding Box</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Two opposite corners of the product file (bounding box, including any zero-fill values) are identified, expressed in the coordinate reference system defined in 1.7.11.</p><p></p><p>Four corners of the product file are recommended for scenes crossing the Antemeridian, or the North or the South Pole. </p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.8</b></td><td colspan="1" rowspan="2"><b>Product Geographical Extent</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>The geometry of the SAR image footprint expressed in WGS84, in a standardised format (e.g., WKT Polygon).</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.9</b></td><td colspan="1" rowspan="2"><b>Product Image Size</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Image attributes of the CEOS-ARD product:</p><p>- Number of lines</p><p>- Number of pixels/lines</p><p>- File header size (if applicable)</p><p>- Number of no-data border pixels (if appl.)</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.10</b></td><td colspan="1" rowspan="2"><p><b>Product</b> </p><p><b>Pixel Coordinate Convention</b></p></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Coordinate referring to the Centre, or the Upper Left Corner or the Lower Left Corner of a pixel.  Values are [pixel centre, pixel ULC or pixel LLC].</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.11</b></td><td colspan="1" rowspan="2"><b>Product Coordinate Reference System</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>The metadata lists the map projection (or geographical coordinates, if applicable) that was used and any relevant parameters required to geolocate data in that map projection, expressed in a standardised format (e.g., WKT). </p><p></p><p>Indicate EPSG code, if defined for the CRS.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.12</b></td><td colspan="1" rowspan="2"><b>Look Direction Polynomials</b></td><td colspan="1" rowspan="2">[ORB]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>In case the per-pixel item 2.11 (Look Direction Image) is not provided, then a list of the polynomial coefficients a<sub>i</sub> necessary to reconstruct the look direction angle*, together with an estimate of the added error from use of polynomial vs. per-pixel more accurate values, shall be provided. </p><p></p><p>Example polynomial:</p><p>LookDir = a<sub>1</sub>Lat<sup>2</sup> + a<sub>2</sub>Lon<sup>2</sup> + a<sub>3</sub>LatLon + a<sub>4</sub>Lat + a<sub>5</sub>Lon + a<sub>6</sub></p><p></p><p>where:</p><p>a<sub>i</sub> = polynomial coefficients</p><p>Lat = latitude </p><p>Lon = longitude</p><p>Lat and Lon are the related coordinates in the product map units [‘m’, ‘deg’, ‘arcsec’]</p><p></p><p><i>* The look direction angle represents the planar angle between north and each range direction. It is not constant in range, especially close to the poles.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.13</b></td><td colspan="1" rowspan="2"><b>Radar Unit Look Vector</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>3-D components radar unit look vector, specified at centre of scene, in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating - ECR) is provided. It consists of unit vectors from antenna to surface pixel (i.e., positive Z component). </p><p></p><p>Only required if per-pixel metadata 2.12 (Radar Unit Look Vector Grid Image) is not provided.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.14</b></td><td colspan="1" rowspan="2"><b>Slant Range Sensor to Surface</b>  </td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Slant range distance from the sensor to the surface, specified at centre of scene.</p><p>Only required if per-pixel metadata 2.13 (Slant Range Sensor to Surface Image) is not provided.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>1.7.15</b></td><td colspan="1" rowspan="2"><b>Reference Orbit</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p><b>Usage:</b> For <b>[NRB] & [POL]</b> only when per-pixel metadata 3.7 (Flattened phase) is provided. For <b>[GSLC]</b> when a reference orbit is used instead of a virtual orbit (see Annex A 1.2).</p><p></p><p>Provide the absolute orbit number used as reference for topographic phase flattening. In case a virtual orbit has been used, provide orbit parameters or orbit state vectors as DOI or URL.</p><p></p><p>Provide scene-centred perpendicular baseline for the for the source data relative to the reference orbit used (for approximate use only).</p></td></tr>
</table>

<a name="_heading=h.2et92p0"></a><a name="_heading=h.tyjcwt"></a>
## **Per-Pixel Metadata**
The following minimum metadata specifications apply to each pixel. Whether the metadata are provided in a single record relevant to all pixels or separately for each pixel is at the discretion of the data provider. Per-pixel metadata should allow users to discriminate between (choose) observations on the basis of their individual suitability for applications. Cloud optimized file formats are recommended.

*The column “CEOS-ARD product” indicates which CEOS-ARD SAR product(s) (NRB, POL, ORB, GSLC) the parameter refers to.*

<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>2.1</b></td><td colspan="1" rowspan="2"><b>Metadata Machine Readability</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Metadata is provided in a structure that enables a computer algorithm to be used to consistently and automatically identify and extract each component/variable/layer for further use.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, but metadata is formatted in accordance with CEOS-ARD SAR Metadata Specifications, v.1.0.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.2</b></td><td colspan="1" rowspan="2"><b>Data Mask Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Mask image indicating:</p><p>- Valid data</p><p>- Invalid data</p><p>- No data</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Mask]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int, ...]</p><p>- Bits per Sample</p><p>- Byte Order </p><p>- Bit Value Representation</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, including additional bit value representations, e.g.:</p><p>- Layover (masked as invalid data in threshold)</p><p>- Radar shadow (masked as invalid data in threshold)</p><p>- Ocean water</p><p>- Land (recommended for [ORB])</p><p>- RTC applied (e.g., for maritime scenes with land samples for which RTC has been applied)</p><p>- DEM gap filling (i.e., interpolated DEM over gaps)</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.3</b></td><td colspan="1" rowspan="2"><b>Scattering Area Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p><b>Usage:</b> Recommended for scenes that include land areas.</p><p></p><p>DEM-based scattering area image used for Gamma-Nought terrain normalisation is provided. This quantifies the local scattering area used to normalise for radiometric distortions induced by terrain to the measured β0 backscatter. The terrain-flattened γT0 is best understood as β0 divided by the local scattering area.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Scattering Area]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.4</b></td><td colspan="1" rowspan="2"><b>Local Incident Angle Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>DEM-based Local Incident angle image is provided.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p><p></p><p><i>Note: For maritime [ORB] scenes when no land areas are covered, a geoid model could be used for the calculation of the local incident angle</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.5</b></td><td colspan="1" rowspan="2"><b>Ellipsoidal Incident Angle Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Ellipsoidal incident angle is provided.</p><p></p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p><p>- Reference Ellipsoid Name</p><p></p><p><i>Note: For maritime [ORB] scenes when no land areas are covered, the ellipsoidal incident angle is nearly identical to the geoid based local incident angle.</i></p></td></tr>
</table>


<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>2.6</b></td><td colspan="1" rowspan="2"><b>Noise Power Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Estimated Noise Equivalent σ0 (or β0 or γ0, as applicable) used for noise removal, if applied, for each channel. NEσ0 and NEγ0 are both based on a simplified ellipsoid Earth model.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Gamma-Nought, Sigma-Nought, Beta-Nought] </p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.7</b></td><td colspan="1" rowspan="2"><b>Gamma-to- Sigma Ratio Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Ratio of the integrated area in the Gamma projection over the integrated area in the Sigma projection (ground). Multiplying RTC γT0 by this ratio results in an estimate of RTC σT0.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Ratio]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.8</b></td><td colspan="1" rowspan="2"><b>Acquisition ID Image</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p><b>Note: Required for multi-source product only.</b> </p><p></p><p>Acquisition ID, or acquisition date, for each pixel is identified. </p><p></p><p>In case of multi-temporal image stacks, use source acquisition ID (i.e., 1.6 acqID values) to list contributing images.</p><p></p><p>In case of Date, data represent (integer or fractional) day offset to reference observation date [UTC]. Date used as reference (“Day 0”) is provided in the metadata.</p><p></p><p>Pixels not representing a unique date (e.g., pixels averaged in image overlap zones) are flagged with a pre-set pixel value that is provided in the metadata.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Day, Time, ID]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per sample </p><p>- Byte Order</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>In case of image composites, the sources for each pixel are uniquely identified.</p></td></tr>
</table>


<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>2.9</b></td><td colspan="1" rowspan="2"><b>Per-pixel DEM</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Provide DEM or DSM as used during the geometric and radiometric processing of the SAR data, resampled to an exact geometric match in extent and resolution with the CEOS-ARD SAR image product. Can also be provided with [ORB] products containing land areas.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Height]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample </p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.10</b></td><td colspan="1" rowspan="2"><b>Per-pixel<br>Geoid</b></td><td colspan="1" rowspan="2">[ORB]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Provide Geoid as used during the geometric and radiometric processing of the SAR data, resampled to an exact geometric match in extent and resolution with the CEOS-ARD ORB image product.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Height]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p><p>- Ground Sampling Distance</p></td></tr>
<tr><td colspan="1"><b>#</b></td><td colspan="1"><b>Parameter</b></td><td colspan="1"><b>CEOS-ARD product</b></td><td colspan="1"><b>Requirements</b></td><td colspan="1"><b>Self-Assessment</b></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.11</b></td><td colspan="1" rowspan="2"><b>Look<br>Direction<br>Image</b></td><td colspan="1" rowspan="2">[ORB]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Look Direction Image is provided. It represents the planar angle between north and each range direction.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.12</b></td><td colspan="1" rowspan="2"><b>Radar Unit Look Vector Grid Image</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>3-D components radar unit look vector, specified at each pixel in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating – ECR) is provided. It consists of unit vectors from the antenna to the surface pixel (i.e., positive Z component). </p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [3D unit vector]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
</table>



<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>2.13</b></td><td colspan="1" rowspan="2"><b>Slant Range Sensor to Surface Image</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Slant range distance from the sensor to the surface, specified at each pixel in an Earth-Centred Earth-Fixed (ECEF) coordinate system (also called Earth Centred Rotating – ECR) is provided. </p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Distance]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.14</b></td><td colspan="1" rowspan="2"><b>InSAR Phase Uncertainty Image</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired)l Requirements</b></p><p>Estimate of uncertainty in InSAR phase is provided, such as finite signal to noise ratio, quantization noise, or DEM error. Identification of which error sources are included will be provided as DOI/URL reference or brief description. It represents statistical variation from known noise sources only. </p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
</table>


<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>2.15</b></td><td colspan="1" rowspan="2"><b>Atmospheric Phase Correction Image</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Phase correction value at each pixel, if applied. DOI/URL reference to algorithm or brief description is provided.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>2.16</b></td><td colspan="1" rowspan="2"><b>Ionospheric          Phase Correction Image</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Phase correction value at each pixel, if applied. DOI/URL reference to algorithm or brief description is provided.</p><p></p><p>File format specifications/ contents provided in metadata:</p><p>- Sample Type [Angle]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p></td></tr>
</table>

## <a name="_heading=h.3dy6vkm"></a>**
## <a name="_heading=h.1t3h5sf"></a>**Radiometrically Corrected Measurements** 
*The requirements indicate the necessary outcomes and, to some degree, the minimum steps necessary to be deemed to have achieved those outcomes. Radiometric corrections must lead to normalised measurement(s) of backscatter intensity and/or decomposed polarimetric parameters. As for the per-pixel metadata, information regarding data format specification needs to be provided for each record. The requirements below must be met for all pixels/samples/observations in a collection. Cloud optimized file formats are recommended.*

*The column “CEOS-ARD product” indicates which CEOS-ARD SAR product (NRB, POL, ORB, GSLC) the parameter refers to.*

<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>3.1</b></td><td colspan="1" rowspan="2"><b>Backscatter<br>Measurements</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p></p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements [NRB]</b></p><p>“Terrain-flattened” Radiometrically Terrain Corrected (RTC) Gamma-Nought backscatter coefficient (γT0) is provided for each polarization.</p><p>File format specifications/contents provided in metadata:</p><p>- Measurement Type [Gamma-Nought]</p><p>- Backscatter Expression Convention [linear amplitude or linear power*]</p><p>- Polarization [HH/HV/VV/VH]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p><p></p><p><i>*Note: Transformation to the logarithm decibel scale is not required or</i> desired <i>as this step can be completed by the user if necessary.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.1</b></td><td colspan="1" rowspan="2"><b>Backscatter<br>Measurements</b></td><td colspan="1" rowspan="2"><p></p><p>[POL]</p><p></p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements [POL]</b></p><p>Measurements can be:</p><p> </p><p>Normalised Radar Covariance Matrix (CovMat)</p><p>Diagonal (equivalent to [NRB]) and upper diagonal elements of the terrain-flattened Gamma-Nought (γT0) Covariance Matrix are provided for coherent dual (e.g., HH-HV, VV-VH, or …) and fully polarimetric (e.g., HH- HV-VH-VV) acquisitions.</p><p> </p><p>And/or</p><p> </p><p>Polarimetric Radar Decomposition (PRD)</p><p>The individual components of the polarimetric decomposition obtained from the terrain-flattened (Gamma-Nought (γT0)) covariance matrix.</p><p>File format specifications/contents provided in metadata:</p><p>-          Measurement Type [CovMat/PRD]</p><p>-          Measurement convention unit [linear amplitude, linear power,  </p><p>`        `angle]</p><p>-          Individual covariance matrix element or/and Individual component      </p><p>`        `of the decomposition [C3m11, C3m12, … or H, A, alpha, or ...]</p><p>-          Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>-          Data Type [Int/ Float/Complex, etc.]</p><p>-          Bits per Sample</p><p>-          Byte Order</p><p></p><p><i>Note: It is recommended to keep CovMat or PRD measurement files separated. Otherwise, specify the multi-channel format order [BIP, BIL, BSQ]</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.1</b></td><td colspan="1" rowspan="2"><b>Backscatter<br>Measurements</b></td><td colspan="1" rowspan="2"><p></p><p>[ORB]</p><p></p></td><td colspan="1" valign="top"><p><b>Threshold (Minimum) Requirements [ORB]</b></p><p>Geoid-corrected Sigma-Nought backscatter coefficient (σ<sup>0</sup>) is provided for each polarization.</p><p></p><p>File format specifications/contents provided in metadata:</p><p>-          Measurement Type [Sigma-Nought]</p><p>-          Backscatter Expression Convention [linear amplitude or linear power*]</p><p>-          Backscatter Conversion Equation</p><p>-          Polarization [HH/HV/VV/VH]</p><p>-          Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>-          Data Type [Int/Float, ...]</p><p>-          Bits per Sample</p><p>-          Byte Order</p><p><i>*Note: Transformation to the logarithm decibel scale is not required or</i> desired <i>as this step can be easily completed by the user if necessary.</i>            </p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Radiometrically Terrain-corrected Sigma-Nought backscatter coefficient       (σT0)  is provided for each polarization.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.1</b></td><td colspan="1" rowspan="2"><b>Backscatter<br>Measurements</b></td><td colspan="1" rowspan="2">[GSLC]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Radiometric and Phase Terrain-flattened Gamma-Nought backscatter coefficient (γT0), in complex number format, is provided for each polarization (e.g., HH, HV, VV, VH).</p><p></p><p>File format specifications/contents provided in metadata:</p><p>- Measurement Type [Gamma-Nought]</p><p>- Backscatter Expression Convention [linear amplitude or linear power*]</p><p>- Polarization [HH/HV/VV/VH]</p><p>- Data Format [Raw/GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p><p></p><p><i>*Note: Transformation to the logarithm decibel scale is not required or</i> desired <i>as this step can be easily completed by the user if necessary.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.2</b></td><td colspan="1" rowspan="2"><b>Scaling Conversion</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>If applicable, indicate the equation to convert pixel linear amplitude/power to logarithmic decibel scale, including, if applicable, the associated calibration (dB offset) factor, and/or the equation used to convert compressed data (int8/int16/float16) to float32.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold, but use of float32.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.3</b></td><td colspan="1" rowspan="2"><b>Noise Removal</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Flag if noise removal* has been applied (Y/N). Metadata should include the noise removal algorithm and reference to the algorithm as URL or DOI.</p><p></p><p><i>*Note: Thermal noise removal and image border noise removal to remove overall scene noise and scene edge artefacts, respectively.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>As threshold.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.4</b></td><td colspan="1" rowspan="2"><b>Radiometric Terrain Correction Algorithm</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Adjustments were made for terrain by modelling the local contributing scattering area using the preferred choice of a published peer-reviewed algorithm to produce radiometrically terrain corrected (RTC) γT0 backscatter estimates. </p><p></p><p>Metadata references, e.g.:</p><p>- a citable peer-reviewed algorithm</p><p>- technical documentation regarding the algorithm used to generate the backscatter estimates is expressed as URLs or DOIs</p><p>- the sources of auxiliary data used to make corrections</p><p></p><p><b>Goal</b> for [GSLC] product type</p><p></p><p><i>Note: Examples of technical documentation include an Algorithm, Theoretical Basis Document, product user guide, etc.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p></p><p><b>Goal</b> for [GSLC] product type</p><p></p><p>Require resolution of DEM better than the output product resolution when applying terrain corrections.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.5</b></td><td colspan="1" rowspan="2"><b>Radiometric<br>Accuracy</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Uncertainty (e.g., bounds on γ0 or σ0) information is provided as document referenced as URL or DOI. SI traceability is achieved.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.6</b></td><td colspan="1" rowspan="2"><b>Mean Wind- Normalised Backscatter Measurements</b></td><td colspan="1" rowspan="2">[ORB]</td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p><b>Usage:</b> Only for Maritime scene</p><p></p><p>Mean wind-normalised (over ocean) backscatter coefficient is provided for each available polarization. It is calculated as the ratio between the backscatter intensity and a simulated backscatter intensity image generated using an ocean surface wind model such as, e.g., Quilfen et al. (1998) or Vachon and Dobson (2000) for VV and HH polarization respectively.</p><p></p><p>File format specifications/contents provided in metadata:</p><p>- Measurement Type [Wind-Normalised Backscatter]</p><p>&emsp;Backscatter Expression Convention [intensity ratio]</p><p>- Polarization [HH/HV/VV/VH]</p><p>- Data Format [GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p><p></p><p><i>Note: Reference wind model, wind speed and direction used for reference backscattering coefficient should be provided</i>.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>3.7</b></td><td colspan="1" rowspan="2"><b>Flattened Phase</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p><b>Usage: Alternative to [GSLC] product for [NRB] and [POL] products</b></p><p>The Flattened Phase is the interferometric phase for which the topographic phase contribution is removed. It is derived from the range-Doppler SLC product using a DEM and the orbital state vectors with respect to a reference orbit (see Annex A1.2). The use of the Flattened Phase with the <b>[NRB]</b> or <b>[POL]</b> intensity (3.1 Backscatter measurement) provides the [GSLC] equivalent, as follows: </p><p><b>GSLC</b> = sqrt(<b>NRB</b>) x exp(j FlattenPhase)</p><p>File format specifications/contents provided in metadata:</p><p>- Measurement Type [Flattened Phase]</p><p>- Reference Polarization [HH/HV/VV/VH]</p><p>- Data Format [GeoTIFF/NetCDF, …]</p><p>- Data Type [Int/Float, ...]</p><p>- Bits per Sample</p><p>- Byte Order</p><p></p><p>In case of polarimetric data, indicate the reference polarization.</p></td></tr>
</table>

## <a name="_heading=h.4d34og8"></a>**
## <a name="_heading=h.2s8eyo1"></a>**Geometric Corrections**
Geometric corrections are steps that are taken to place the measurement accurately on the surface of the Earth (that is, to geolocate the measurement) allowing measurements taken through time to be compared. This section specifies any geometric correction requirements that must be met in order for the data to be analysis ready. 

*The column “CEOS-ARD product” indicates to which CEOS-ARD SAR product (NRB, POL, ORB, GSLC) the parameter refers.*

<table><tr><th colspan="1"><b>#</b></th><th colspan="1"><b>Parameter</b></th><th colspan="1"><b>CEOS-ARD product</b></th><th colspan="1"><b>Requirements</b></th><th colspan="1"><b>Self-Assessment</b></th></tr>
<tr><td colspan="1" rowspan="2"><b>4.1</b></td><td colspan="1" rowspan="2"><b>Geometric Correction Algorithm</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Metadata references, e.g.:</p><p>- A metadata citable peer-reviewed algorithm,</p><p>- Technical documentation regarding the implementation of that algorithm expressed as URLs or DOIs</p><p>- The sources of auxiliary data used to make corrections.</p><p>- Resampling method used for geometric processing of the source data.</p><p></p><p><i>Note: Examples of technical documentation can include e.g., an Algorithm Theoretical Basis Document (ATBD), a product user guide</i>.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>4.2</b></td><td colspan="1" rowspan="2"><p><b>Digital<br>Elevation</b></p><p><b>Model</b></p></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p><b>Usage:</b> For products including land areas</p><p></p><p>a) During ortho-rectification, the data provider shall use the same DEM that was used for the radiometric terrain flattening to ensure consistency of the data stack.</p><p>b) Provide reference to Digital Elevation Model used for geometric terrain correction.</p><p>c) Provide reference to Earth Gravitational Model (EGM) used for geometric correction</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>a) A DEM with comparable or better resolution to the resolution of the output CEOS-ARD product shall be used if available. Else, the upsampled DEM is identified.</p><p>b) Resampling method used for preparation of the DEM.</p><p>c) Method used for resampling the EGM. </p></td></tr>
<tr><td colspan="1" rowspan="2"><b>4.3</b></td><td colspan="1" rowspan="2"><b>Geometric Accuracy</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Accurate geolocation is a prerequisite to radar processing to correct for terrain and to enable interoperability between radar sensors.     </p><p>The absolute geolocation error (ALE) for a sensor is typically assessed through analysis of Single Look Complex (SLC) imagery and measured along the slant range and azimuth directions (case A: SLC ALE).  The end-to-end “ARD” ALE of the final CEOS-ARD product could be measured directly in the final image product in the chosen map projection, i.e., in the map coordinate directions: e.g., Northing and Easting (case B: ARD ALE). Providing accuracy estimates based on measurements following at least one scheme (A or B or both) meets the threshold requirement. </p><p>Estimates of the ALE is provided as a bias and a standard deviation, with (Case A) SLC ALE expressed in slant range and azimuth, and (Case B) ARD ALE expressed in map projection dimensions.</p><p><i>Note 1: This assessment is often made through comparison of measured corner reflector positions with their projected location in the imagery.  In some cases, other mission calibration/validation results may be used.                                         Note 2:  The ALE is not typically assessed for every processed image, but through an ALE assessment by the data processing team characterizing all or (usually a subset) of the generated products.</i>     </p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Output product sub-sample accuracy should be less than or equal to 0.1 (slant range) pixel radial root mean square error (rRMSE).</p><p></p><p>Provide documentation of estimates of ALE as DOI or URL.     </p></td></tr>
<tr><td colspan="1" rowspan="2"><b>4.4</b></td><td colspan="1" rowspan="2"><b>Geometric Refined Accuracy</b></td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>Not required.</p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Values provided under 4.3 Geometric accuracy are provided by the SAR mission Cal/Val team. </p><p></p><p>CEOS-ARD processing steps could include method refining the geometric accuracy, such as cross-correlation of the SAR data in slant range with a SAR scene simulated from a DSM or DEM. </p><p></p><p>Methodology used (name and reference), quality flag, geometric standard deviation values should be provided.</p></td></tr>
<tr><td colspan="1" rowspan="2"><b>4.5</b></td><td colspan="1" rowspan="2"><b>Gridding Convention</b> </td><td colspan="1" rowspan="2"><p>[NRB]</p><p>[POL]</p><p>[ORB]</p><p>[GSLC]</p></td><td colspan="1"><p><b>Threshold (Minimum) Requirements</b></p><p>A consistent gridding/sampling frame is used. The origin is chosen to minimise any need for subsequent resampling between multiple products (be they from the same or different providers).  This is typically accomplished via a “snap to grid” in relation to the most proximate grid tile in a global system.*</p><p></p><p><i>* If a product hierarchy of resolutions exists (or is planned), the multiple resolutions should nest within each other (e.g., 12.5m, 25m, 50m, 100m, etc.), and not be disjoint.</i></p></td><td colspan="1" rowspan="2" valign="top"><p>Achieved level: Threshold / Goal</p><p>Explanation / Justification: …</p><p>Other feedback: …</p></td></tr>
<tr><td colspan="1"><p><b>Goal (Desired) Requirements</b></p><p>Provide DOI or URL to gridding convention used.</p><p></p><p>When multiple providers share a common map projection, providers are encouraged to standardise the origins of their products among each other.</p><p></p><p>In the case of UTM/UPS coordinates, the upper left corner coordinates should be set to an integer multiple of sample intervals from a 100 km by 100 km grid tile of the Military Grid Reference System's 100k coordinates (“snap to grid”).   </p><p></p><p>For products presented in geographic coordinates (latitude and longitude), the origin should be set to an integer multiple of samples in relation to the closest integer degree.</p></td></tr>
</table>

# <a name="_heading=h.17dp8vu"></a>**Summary Self-Assessment Table**

||||**Threshold**|**Goal**|
| :-: | :- | :- | :-: | :-: |
|**1**|**CEOS-ARD product**|**General Metadata**|||
|1\.1|[ALL]|Traceability|||
|1\.2|[ALL]|Metadata Machine Readability|||
|1\.3|[ALL]|Product Type|||
|1\.4|[ALL]|Document Identifier|||
|1\.5|[ALL]|Data Collection Time|||
|**1.6**||**Source Data Attributes**|||
|1\.6.1|[ALL]|Source Data Access|||
|1\.6.2|[ALL]|Instrument|||
|1\.6.3|[ALL]|Source Data Acquisition Time|||
|1\.6.4|[ALL]|Source Data Acquisition Parameters|||
|1\.6.5|[ALL]|Source Data Orbit Information|||
|1\.6.6|[ALL]|Source Data Processing Parameters|||
|1\.6.7|[ALL]|Source Data Image Attributes|||
|1\.6.8|[ALL]|Sensor Calibration|||
|1\.6.9|[ALL]|Performance Indicators|||
|1\.6.10|[ALL]|Source Data Polarimetric Calibration Matrices|||
|1\.6.11|[ALL]|Mean Faraday Rotation Angle|||
|1\.6.12|[ALL]|Ionosphere indicator|||
|**1.7**||**CEOS-ARD Product Attributes**|||
|1\.7.1|[ALL]|Product Data Access|||
|1\.7.2|[ALL]|Auxiliary Data|||
|1\.7.3|[ALL]|Product Sample Spacing|||
|1\.7.4|<p>[NRB]</p><p>[POL]</p><p>[ORB]</p>|Product Equivalent Number of Looks|||
|1\.7.5|[ALL]|Product Resolution|||
|1\.7.6|<p>[NRB]</p><p>[POL]</p><p>[ORB]</p>|Product Filtering|||
|1\.7.7|[ALL]|Product Bounding Box|||
|1\.7.8|[ALL]|Product Geographical Extent|||
|1\.7.9|[ALL]|Product Image Size|||
|1\.7.10|[ALL]|Product Pixel Coordinate Convention|||
|1\.7.11|[ALL]|Product Coordinate Reference System|||
|1\.7.12|[ORB]|Look Direction Polynomials|||
|1\.7.13|[GSLC]|Radar Unit Look Vector|||
|1\.7.14|[GSLC]|Slant Range Sensor to Surface|||
|1\.7.15|<p>[NRB]</p><p>[POL]</p><p>[GSLC]</p>|Reference Orbit|||
|**2**|**CEOS-ARD product**|**Per-Pixel Metadata**|||
|2\.1|[ALL]|Metadata Machine Readability|||
|2\.2|[ALL]|Data Mask Image|||
|2\.3|[ALL]|Scattering Area Image|||
|2\.4|[ALL]|Local Incident Angle Image|||
|2\.5|[ALL]|Ellipsoidal Incident Angle Image|||
|2\.6|[ALL]|Noise Power Image|||
|2\.7|<p>[NRB]</p><p>[POL]</p><p>[GSLC]</p>|Gamma-to-Sigma Ratio Image|||
|2\.8|[ALL]|Acquisition ID Image|||
|2\.9|<p>[NRB]</p><p>[POL]</p><p>[GSLC]</p>|Per-pixel DEM|||
|2\.10|[ORB]|Per-pixel Geoid|||
|2\.11|[ORB]|Look Direction Image|||
|2\.12|[GSLC]|Radar Unit Look Vector Grid Image|||
|2\.13|[GSLC]|Slant Range Sensor to Surface Image|||
|2\.14|[GSLC]|InSAR Phase Uncertainty Image|||
|2\.15|[GSLC]|Atmospheric Phase Correction Image|||
|2\.16|[GSLC]|Ionospheric Phase Correction Image|||
||||**Threshold**|**Goal**|
|**3**|**CEOS-ARD product**|**Radiometrically Corrected Measurements**|||
|3\.1|[ALL]|Backscatter Measurements|||
|3\.2|[ALL]|Scaling Conversion |||
|3\.3|[ALL]|Noise Removal|||
|3\.4|<p>[NRB]</p><p>[POL]</p><p>[GSLC]</p>|Radiometric Terrain Correction Algorithms|||
|3\.5|[ALL]|Radiometric Accuracy|||
|3\.6|[ORB]|Mean Wind-Normalised Backscatter Measurements|||
|3\.7|[NRB]<br>[POL]|Flattened Phase|||
||||**Threshold**|**Goal**|
|**4**|**CEOS-ARD product**|**Geometric Corrections**|||
|4\.1|[ALL]|Geometric Correction Algorithms|||
|4\.2|[ALL]|Digital Elevation Model|||
|4\.3|[ALL]|Geometric Accuracy|||
|4\.4|[ALL]|Geometric Refined Accuracy|||
|4\.5|[ALL]|Gridding Convention|||

# **Guidance**
This section aims to provide background and specific information on the processing steps that can be used to achieve analysis ready data for a specific and well-developed Product Family Specification. This Guidance material does not replace or override the specifications. 
# **Introduction to CEOS-ARD**
**What is CEOS Analysis Ready Data?**

CEOS-ARD are products that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort. In general, these products would be resampled onto a common geometric grid (for a given product) and would provide baseline data for further interoperability both through time and with other datasets. 

CEOS-ARD products are intended to be flexible and accessible products suitable for a wide range of users for a wide variety of applications, including particularly time series analysis and multi-sensor application development. They are also intended to support rapid ingestion and exploitation via high-performance computing, cloud computing and other future data architectures. They may not be suitable for all purposes and are not intended as a ‘replacement’ for other types of satellite products.

**When can a product be called CEOS-ARD?**

The CEOS-ARD branding is applied to a particular product once:

- that product has been assessed as meeting CEOS-ARD requirements by the agency responsible for production and distribution of the product, and
- that the assessment has been peer reviewed by the relevant CEOS team(s).

Agencies or other entities considering undertaking an assessment process should consult the CEOS-ARD [Governance Framework](https://docs.google.com/document/d/15grQ79D-Ge8PN1_4_XDmci5iezs8HAcOpLcM7d2wmAo/edit?usp=sharing).

A product can continue to use CEOS-ARD branding as long as its generation and distribution remain consistent with the peer-reviewed assessment.

**What is the difference between Threshold and Goal?**

**Threshold (Minimum) Requirements** are the MINIMUM that is needed for the data to be analysis ready. This must be practical and accepted by the data producers.

**Goal (Desired) Requirements** (previously referred to as “Target”) are the ideal; where we would like to be. Some providers may already meet these.

Products that meet all threshold requirements should be immediately useful for scientific analysis or decision-making. 

Products that meet goal requirements will reduce the overall product uncertainties and enhance broad-scale applications. For example, the products may enhance interoperability or provide increased accuracy through additional corrections that are not reasonable at the *threshold* level. 

Goal requirements anticipate continuous improvement of methods and evolution of community expectations, which are both normal and inevitable in a developing field. Over time, *goal* specifications may (and subject to due process) become accepted as Threshold requirements.


# **Reference Papers [CEOS-ARD for SAR]**
*ISO 19115-2 (2009) Geographic information -- Metadata -- Part 2: Extensions for imagery and gridded data, [www.iso.org/standard/39229.html*](http://www.iso.org/standard/39229.html)*

## **Normalised Radar Backscatter [NRB]**
*Shiroma, G.H.X., M. Lavalle and S. M. Buckley, An Area-Based Projection Algorithm for SAR Radiometric Terrain Correction and Geocoding. IEEE Transactions on Geoscience and Remote Sensing, vol. 60, pp. 1-23, 2022, Art no. 5222723, doi: 10.1109/TGRS.2022.3147472.*

*Small, D. (2011) Flattening Gamma: Radiometric Terrain Correction for SAR Imagery, IEEE Trans. Geosci. Remote Sens., vol. 49, no. 8, pp. 3081-3093. doi: 10.1109/TGRS.2011.2120616*

## **Polarimetric Radar [POL]**
*Cameron, W.L., N.N. Youssef, and L.K. Leung (1996) Simulated polarimetric signatures of primitive geometrical shapes, IEEE Trans. Geosci. Remote Sens., vol. 34, no. 3, pp. 793–803.*

*Cloude, S.R. and E. Pottier (1996) A review of target decomposition theorems in radar polarimetry, IEEE Trans. Geosci. Remote Sens., vol. 34, no. 2, pp. 498–518.*

*Freeman, A. and S.L. Durden (1998) A three-component scattering model for polarimetric SAR data, IEEE Trans. Geosci. Remote Sens., vol. 36, no. 3, pp. 964–973.*

*Gens, R., D.K. Atwood and E. Pottier (2013) Geocoding of polarimetric processing results: Alternative processing strategies, Remote Sensing Letters, vol. 4, no. 1, pp.  38-44.* 

*Krogager, E. (1993) Aspects of polarimetric radar imaging, Ph.D. dissertation, Tech. Univ. Denmark, Electromagn. Inst., Lyngby, Denmark*

*Lee, J.-S., J.-H. Wen, T.L. Ainsworth, K.-S. Chen, and A.J. Chen (2009) Improved Sigma Filter for Speckle Filtering of SAR Imagery IEEE Trans. Geosci. Remote Sens., vol. 47, no. 1, pp. 202-213.*

*Raney, R.K., J.T.S. Cahill, G.W. Patterson and D.B.J. Bussey (2012) The m-chi decomposition of hybrid dual-polarimetric radar data with application to lunar craters Journal of Geophysical Research: Planets 117(E5)*

*Toutin, T., H. Wang, P. Chomaz and E. Pottier (2013) Orthorectification of Full-Polarimetric Radarsat-2 Data Using Accurate LIDAR DSM, IEEE Trans. Geosci. Remote Sens., vol. 51, no. 12, pp. 5252-5258.* 

*Yamaguchi, Y., A. Sato, W.M. Boerner, R. Sato and H. Yamada (2011) Four-Component Scattering Power Decomposition with Rotation of Coherency Matrix, IEEE Trans. Geosci. Remote Sens., vol. 49, no. 6, pp. 2251-2258.*

## **Ocean Radar Backscatter [ORB]**
*Quilfen, Y., Chapron, B., Elfouhaily, T., Katsaros, K., and Tournadre, J. (1998) Observation of tropical cyclones by high-resolution scatterometry, J. Geophys. Res., 103(C4), 7767– 7786, doi:10.1029/97JC01911*

*Vachon, P.W. and F.W. Dobson (2000) Wind Retrieval from RADARSAT SAR Images: Selection of a Suitable C-Band HH Polarization Wind Retrieval Model, Canadian Journal of Remote Sensing, 26:4, 306-313, DOI: 10.1080/07038992.2000.10874781*

## **Geocoded Single-Look Complex [GSLC]**
*Zebker, H. A., S. Hensley, P. Shanker and C. Wortham (2010) Geodetically Accurate InSAR Data Processor, IEEE Transactions on Geoscience and Remote Sensing, vol. 48, no. 12, pp. 4309-4321, Dec. 2010, doi: 10.1109/TGRS.2010.2051333.*

*Zebker, H. A. (2017) User-Friendly InSAR Data Products: Fast and Simple Timeseries Processing. IEEE Geoscience and Remote Sensing Letters 14(11): 2122-2126.*

*Zheng, Y. and H. A. Zebker (2017) Phase Correction of Single-Look Complex Radar Images for User-Friendly Efficient Interferogram Formation. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 10(6): 2694-2701.*


