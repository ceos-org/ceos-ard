---
title: CEOS-ARD Product Family Specification
subtitle: {{ title }}
---

![CEOS Analysis Ready Data](../../Logo/CEOS_ARD_Logo_for_PFS.png)

## Document History

{{ history }}

## Contributing Authors

{{ authors }}

## Description

**Product Family Specification Title: {{ title }} (CEOS-ARD {{ short_title }})**

**Applies to:** {{ applies_to }}

## Background to CEOS-ARD for Synthetic Aperture Radar

The CEOS Analysis Ready Data (CEOS-ARD) Product Family Specification (PFS) for Synthetic Aperture Radar (SAR) data is specifically aimed at users interested in exploring the potential of SAR but who may lack the expertise or facilities for SAR processing. 

This CEOS-ARD for Synthetic Aperture Radar PFS incorporates, into a single generic document, the following four CEOS-ARD SAR specifications endorsed by CEOS Land Surface Imaging-Virtual Constellation (CEOS LSI-VC):

- Normalised Radar Backscatter (version 5.5)
- Polarimetric Radar (version 3.5)
- Ocean Radar Backscatter (version 1.0)
- Geocoded Single-Look Complex (version 1.0)

The **CEOS-ARD Normalised Radar Backscatter \[NRB]** specification describes products that have been subject to Radiometric Terrain Correction (RTC) and are provided in the Gamma-Nought ($`\gamma^0_T`$) backscatter convention (Small, 2011), which mitigates the variations from diverse observation geometries and is recommended for most land applications. An additional metadata layer can be optionally provided for conversion of $`\gamma^0_T`$ to Sigma-Nought ($`\sigma^0_T`$) backscatter layer for compatibility with legacy software or numerical models. As the **\[NRB]** product contains backscatter values only, it cannot be directly used for SAR polarimetry or interferometric applications that require relative polarization phase or local phase estimates respectively. However, as an option, a “flattened” phase data layer can be provided with an **\[NRB]** product for enabling InSAR analysis. The flattened phase is the interferometric phase, with respect to a reference orbit and to a DEM, for which the topographic phase contribution is removed. 

The **CEOS-ARD** **Polarimetric Radar \[POL]** product format is an extension of the CEOS-ARD Normalised Radar Backscatter format **\[NRB]**. This extension is required in order to better support Level-1 SLC polarimetric data, including full-polarimetric modes (e.g., RADARSAT-2, ALOS-2/4, SAOCOM-1 and future missions), and hybrid or linear dual-polarimetric modes (i.e., Compact Polarimetric mode available on RCM, SAOCOM and the upcoming NISAR mission). The **\[POL]** product can be defined in two processing levels:

The **normalised covariance matrix \[CovMat]** representation (C2 or C3) which preserves the inter-channel polarimetric phase(s) and maximizes the available information for users. Interoperability within current CEOS-ARD SAR backscatter definition is preserved, since diagonal elements of the covariance matrix are backscatter intensities. Scattering information enhancement can be achieved by applying incoherent polarimetric decomposition techniques (e.g., Freeman-Durden, van Zyl, Cloude-Pottier, Yamaguchi-based) directly on the C2 or C3 matrix. 

**Polarimetric Radar Decomposition \[PRD]** refers to ARD products where polarimetric information is broken down into simplified parameters to facilitate user interpretation of the data. They are derived from coherent or incoherent polarimetric decomposition techniques. 

**Notice and Limitations \[POL]**

For Polarimetric Radar **\[POL]** products, optimal incoherent Polarimetric Radar Decomposition **\[PRD]** should be performed under the slant range projection (Gens et al., 2013, Toutin et al., 2013). In order to minimise bias in the CEOS-ARD SAR Level-2a covariance matrix product, speckle filtering and averaging of the covariance matrix should be applied in the slant range projection, and geocoding should be performed using nearest-neighbour resampling. Specifically, nearest-neighbour resampling ensures that the averaged covariance matrix elements in slant range and in geocoded ground projection are exactly the same. Consequently, the polarimetrically derived parameters are exactly equal in both approaches (assuming that no further averaging is performed on the ARD product for decomposing the polarimetric information). Bilinear and average resampling methods are also suitable for resampling the covariance matrix, but some differences with polarimetric parameters generated in slant range and then resampled (bilinear) might be observed on sloped terrains. Even if Sinc interpolation may be more robust for spatial resampling, it does not preserve covariance matrix integrity, and should consequently not be used for this ARD product.

It is recommended that ARD providers who desire to distribute **\[PRD]** products decompose the polarimetric information starting from Level-1 SLC data and then geocode the derived parameters rather than use the **\[CovMat]** ARD product. Resampling can be performed using any of the supported methods (nearest-neighbour, bilinear, average, bi-cubic spline or Lanczos are recommended), which need to be indicated in the product metadata. Note that coherent decomposition techniques cannot be performed on **\[CovMat]** ARD products.

Covariance matrix products contain a variable number of layers (or bands) with different data types depending on the polarimetric mode (full or dual) and decomposition technique. The **\[CovMat]** products for the C2 matrix have 3 layers (2 real-valued diagonal elements and 1 complex-valued off-diagonal element). **\[CovMat]** products for the C3 matrix have 6 layers (3 real-valued diagonal elements and 3 complex-valued off-diagonal elements). Layers that can be obtained via a complex conjugation of other layers are not provided within the product. Polarimetric Decomposition products contain typically 2 to 4 (or more) real-valued layers depending on the particular decomposition algorithm. Within the **\[CovMat]** product files, ARD layers are organized in order to reduce access delays and maximize efficiency in extracting the desired information. In **\[CovMat]** products, geographically contiguous samples for each layer may be stored next to each other and organized “layer by layer”. Alternatively, samples belonging to the same covariance matrix might be stored next to each other and organized “matrix by matrix”. **\[PRD]** products are organized “layer by layer”, i.e., with bands corresponding to the output of the polarimetric decomposition stored next to each other. ). 

The **CEOS-ARD Ocean Radar Backscatter \[ORB]** product specification describes products that have been projected on a geoid and are provided in the Sigma-Nought ($`\sigma^0`$) backscatter convention, which is recommended for most ocean applications. Backscatter may be calibrated to the ellipsoid ($`\sigma^0_E`$) or radiometrically terrain corrected ($`\sigma^0_T`$) prior to geometric terrain correction. As the basic **\[ORB]** product contains backscatter values only, it *cannot* be directly used for SAR polarimetry or interferometric applications that require local phase estimates. Nonetheless, an advanced **\[ORB]** product could include the upper diagonal of the polarimetric $`\sigma^0`$ covariance matrix for enabling advanced polarimetric analysis (similar to the **\[POL]** product). 

The **CEOS-ARD Geocoded Single-Look Complex \[GSLC]** product is relevant to interferometric studies. The **\[GSLC]** product is derived from the range-Doppler (i.e. slant range) Single-Look Complex (SLC) product using a DEM and the orbital state vectors and output in the map projected system. The phase of a geocoded SLC is “flattened” with respect to a reference orbit and to a DEM, to eliminate topographic phase contributions \[Zebker et al., 2017 and Zheng and Zebker, 2017]. The sample spacing of the **\[GSLC]** product in the map coordinate directions is comparable to the full resolution original SLC product. The **\[GSLC]** product can be directly overlaid on a map or combined with other similar **\[GSLC]** products to derive interferograms and create change maps, for example. Since the **\[GSLC]** phase is flattened, the phase difference between two **\[GSLC]** products** acquired on a same relative orbit produces an interferogram referring only to surface displacement and noise (i.e., no topographic fringes). The **\[GSLC]** product may optionally** be radiometrically terrain corrected such that the squared amplitude yields $`\gamma^0_T`$.

As can be seen from the above PFS descriptions, only a few minor details in terms of generated parameters and/or the addition of supplemental data distinguish these CEOS-ARD products. In part, they are to a large extent all backward-compatible. For example, \[POL] products implicitly include \[NRB] products, while a coastal \[NRB] or \[POL] product can simply be made compatible with other \[ORB] products by applying gamma-to-sigma conversion. Just as \[GSLC] can be converted to \[NRB], the inverse conversion can be made true by including the optional topographically flattened phase. In this way a \[NRB] or \[POL] product can be used like a \[GSLC] for InSAR applications. Consequently, it becomes obvious that they all can follow a common approach, in terms of content and structure, in order to optimize their interoperability. 

For this generic **CEOS-ARD for Synthetic Aperture Radar** PFS, as for the individual **\[NRB]**, **\[POL]**, **\[ORB]**, and **\[GSLC]** PFSs, metadata requirements are defined under two categories: Threshold and Goal. **Threshold requirements** refer to metadata parameters or data files which are mandatorily required in a product in order to be CEOS-ARD compliant. **Goal requirements** (formerly referred to as Target) are complementary metadata parameters or data files that are desirable or more accurate but more constraining/challenging to achieve depending on the SAR missions and the data provider constraints. Since this document integrates four CEOS-ARD PFSs, it is worth noting that some requirements have been “relaxed” for a few Threshold parameters, depending on the applications/environment of the CEOS-ARD product. Exceptions are identified in the tables by specifying the usage.

&#12;

## Definitions and Abbreviations

{{ terms }}

&#12;

## Requirements

{{ requirements }}

## Summary Self-Assessment Table

{{ requirements_summary }}

&#12;

## Guidance

{{ include:fragments/guidance.md }}

## Introduction to CEOS-ARD

{{ include:fragments/ceos_ard_intro.md }}

## Reference Papers

{{ references }}
