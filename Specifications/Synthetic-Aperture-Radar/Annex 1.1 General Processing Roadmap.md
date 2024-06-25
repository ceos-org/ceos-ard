<!--lint disable-->
# **Annex 1.1: General Processing Roadmap**
The radiometric interoperability of CEOS-ARD SAR products is ensured by a common processing chain during production. The recommended processing roadmap involves the following steps:

- Apply the best possible orbit parameters to give the most accurate product possible. These will have been projected to an ellipsoidal model such as WGS84. To achieve the level of geometric accuracy required for the DEM-based correction, precise orbit determination will be required.
- Apply instrument calibration to produce Beta-Nought values with high fidelity.
- Convert Single-Look-Complex (SLC) radiometric channel(s) to intensity **[NRB]**, **[ORB]** and **[POL]** and in addition for **[POL]**, the cross-product element(s) of the covariance as shown in Annex 2.1.
- Perform radiometric terrain correction (gamma backscatter convention terrain-flattening) on the covariance matrix by applying the local surface normalisation factor to each backscatter measurement element (Small, 2011; Shiroma et al., 2022).
- Perform polarimetric speckle filtering (optional for **[NRB]** and **[ORB]**), before geocoding, to optimally preserve the polarimetric information. Most popular polarimetric decomposition methodologies are incoherent in nature, which requires averaging the covariance matrix for stationarity. Depending on the application, a polarimetric filter that preserves local point targets and locally average extended targets may be used, e.g., Sigma Lee filter with 7x7 window and 3-point target (Lee et al., 2009). Multi-looking could be performed to meet optimal output sample spacing before the geometric correction step. No speckle filtering or multi-looking is performed for **[GSLC]** products.
- For [GSLC] products, the topographic phase is estimated relative to a reference orbit and removed from the SLC data (Zebker et al., 2010; Zebker, 2017) (see Annex A1.2)
- Geometric terrain correction (relative to geoid for **[ORB]**) is applied to the normalized backscatter measurement data. For **[POL]**, the resampling methodology should be nearest-neighbour, bilinear or average in order to preserve integrity of the covariance matrix as other resampling functions can introduce artefacts due to the mix of intensity and complex number elements in the matrix. Geocoding to a common grid structure with specified pixel spacings for true data cube format.
- Generate CEOS format metadata to accompany product layers.
- Optionally, a SpatioTemporal Asset Catalog (STAC) file is added to the product.


Table A1.1 lists possible sequential steps and existing software tools (e.g., Gamma software (GAMMA, 2018)) and scripting tasks that can be used to form the CEOS-ARD SAR processing roadmap.

**Table A1.1  SAR ARD processing roadmap and software options. RADARSAT-2 Example**

|**Step**|**Implementation option**|
| :- | :- |
|1\. Orbital data refinement|Check xml date and delivered format. RADARSAT-2, pre EDOT (July 2015) replace. Post July 2015, check if ‘DEF’, otherwise replace. (Gamma - RSAT2\_vec)|
|2\. Apply radiometric scaling Look-Up Table (LUT) to Beta-Nought|<p>Specification of LUT on ingest. </p><p>(Gamma - par\_RSAT2\_SLC/SG)</p>|
|3\. Generate covariance matrix elements|Gamma – COV\_MATRIX|
|4\. Radiometric terrain normalisation|Gamma - geo\_radcal2|
|5\. Speckle filtering (Boxcar or Sigma Lee)|Custom scripting|
|6\. Geometric terrain correction/Geocoding|Gamma – gc\_map and geocode\_back|
|7\. Create metadata|Custom scripting|


