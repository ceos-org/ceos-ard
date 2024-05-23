**Annex 4: Geocoded Single-Look Complex [GSLC] example**

In contrast to basic **[NRB]** and **[POL] products**, CEOS-ARD Geocoded SLC **[GSLC]** products are kept close to the native resolution in complex data format for which local topographic InSAR phases, relative to a reference orbit (Zebker et al., 2010; Zebker 2017), have been removed. Having a volume of **[GSLC]** products acquired over repeat cycles, already radiometric and phase terrain corrected and geocoded (Figure A4.1a) and Figure A4.1b), allows user-friendly production of a first iteration of the InSAR coherence (Eq. A4.1 and Figure A4.1c) and differential phases (Eq. A4.2 and Figure A4.1d) in between **[GSLC]** pairs, simply by applying local averaging window over the product of a **[GSLC]** product (GSLC1) with the complex conjugate of a second **[GSLC]** (GSLC2) divided by their local averaged intensities. These intermediate files could be used for coherent change detection analysis and surface displacement monitoring.

|![ref1]![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.018.png)|<p></p><p>**Eq. A4.1**</p>|
| :- | -: |

The InSAR differential phase (Eq. A4.2) is the argument of the complex coherence estimated with
Eq. 4.1.

|![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.019.png)**InSAR differential phase**:         |<p></p><p>**Eq. A4.2**</p>|
| :- | -: |

Some advanced [NRB] or [POL] products could include per-pixel “Flattened Phase” data (item 3.7). This “Flattened Phase” enables the possibility to perform InSAR analysis as with two [GSLC] products. As for example, from two different [NRB] products (NRB1) and (NRB2), acquired over repeat cycles (i.e., on the same relative orbit), containing γT 0and their corresponding “Flattened Phase” (FPh1) and (FPh2) per-pixel data, the complex InSAR coherence (Eq. A4.3) can be estimated in the similar manner as Eq. A4.1 for [GSLC] products.

|![ref1]       **![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.020.png)** |<p>` `**Eq. A4.3**</p><p></p>|
| :- | :- |

# **.**

|`                                                                                `**![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.021.jpeg)      a)**|<p></p><p></p>|
| :-: | :-: |
|`                                                                                   `**![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.022.jpeg)        b)**|<p></p><p></p>|
![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.023.png)**c)**

![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.024.png)**d)**

***Figure A4.1**  Sentinel-1 [GSLC] products example over Death Valley National Park, California, US.
**a)** GSLC1: Intensity data of the first [GSLC] product (2017-05-27); **b)** GSLC2: Intensity data of the second [GSLC] product (2017-06-08); **c)** InSAR coherence map generated directly from A4.1a) and b); **d)** InSAR differential phase map generated directly from A4.1a) and b).*

#
Some advanced [GSLC] product can be provided with “2.12 Radar Unit Look Vector Grid Image” per-pixel metadata (Figure A4.2) which gives the accurate 3-D components radar unit look vector used as for example in decomposing the vertical and horizontal component of an InSAR surface displacement estimate.

|<p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.025.png)</p><p>**a)** </p>|
| :- |
|<p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.026.png)</p><p>**b)** </p>|
|<p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.027.png)</p><p>**c)** </p>|

***Figure A4.2**  3-D components radar unit look vector of the [GSLC] product in Figure A4.1.  **a)** x unit component; **b)** y unit component; **c)** z unit component*.

[ref1]: Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.017.png
