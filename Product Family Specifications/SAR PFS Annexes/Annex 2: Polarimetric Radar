# **Annex 2: Polarimetric Radar [POL]**
# **A2.1: Normalised Covariance Matrices (CovMat)**
In order to preserve the inter-channel polarimetric phase and thus the full information content of coherent dual-pol and fully polarimetric data, the covariance matrix is proposed as the data storage format. Covariance matrices are generated from the complex cross product of polarimetric channels, as shown in Eq. A2.1 for fully polarimetric data (C3) and in Eq. A2.2 for dual polarization data (C2). Since these matrices are complex symmetrical, only the upper diagonal elements (bold elements) need to be stored in the ARD database.

**Fully polarimetric** 

|![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.003.png)|**Eq. A2.1**|
| :-: | -: |

Where HV = VH, under the reciprocity assumption. | | and \* mean respectively complex modulus and the complex conjugate. 

**Dual polarization**

|<p></p><p>**HH-HV**</p><p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.004.png)</p><p></p><p>**VV-VH**</p><p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.005.png)</p><p></p><p>**CH-CV**</p><p>![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.006.png)</p>|**Eq. A2.2**|
| - | -: |

Where CH and CV refer to dual polarization transmitting a circular polarized signal. [CH, CV] can be replaced by [LH, LV] or [RH, RV] for left (L) or right (R) hand circular transmission respectively, although RCM will offer only right-hand circular transmission. The coherent HH-VV configuration available on TerraSAR-X could also be represented as C2 format. 

Polarimetric decomposition methods like Yamaguchi et al. (2011) for fully polarimetric, or m-chi (Raney et al., 2012) for compact polarimetric data, can be applied directly on averaged (speckle filtered) C3 and C2 matrices respectively. These decompositions enhance scattering information, bring it to a more comprehensible level to end-users, and raise the performance of thematic classification methodologies. For SAR products that were acquired with single polarization the use of the covariance matrix does not result in superfluous storage requirements, since only the matrix elements that are populated are retained and the diagonal matrix elements are the backscatter intensities. Thus, a single channel intensity product would yield only one matrix element and the storage needs would not change.
#
#
In order to ease the data structure and the metadata in between C3 and C2, Eq. A2.1 should be redefined as Eq. A2.3. Users will have to take care of this non-standard representation when applying their polarimetric analytic tools. “< >” means that ARD matrix elements are speckle filtered. Eq. A2.3 is valid both for dual-linear and quad polarization.

|![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.007.png)|**Eq. A2.3**|
| :-: | -: |

Furthermore, for compact polarimetric data, it is recommended to store them, by simple transformation, under the circular-circular basis, since RR and RL polarizations (Eq. A2.4) permit faster and more intuitive RGB visualizations (R=RR, G=RR/(RR+RL), B= RL).

|` `**![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.008.png)**|**Eq. A2.4**|
| - | :-: |
# **
# **A2.2: Polarimetric Radar Decomposition (PRD)**
Different methodologies allow decomposition of coherent dual-polarization data or fully polarimetric data to meaningful components summarizing the scattering processing with the interacting media. Decomposition techniques are divided in two categories: Coherent and incoherent.

1. **Coherent decompositions** express the scattering matrix by the summation of elementary objects of known signature (ex.: a sphere, a diplane, a cylinder, a helix, …). They are used mainly to describe point targets which are coherent. As for examples, coherent PRD could be (but not limited to):

1. Pauli decomposition (3 layers)

|α|<sup>2</sup> : sphere (odd-bounce interaction) [Intensity]

|β|<sup>2</sup> : 0<sup>o</sup> diplane (even-bounce interaction) [Intensity]

|γ|<sup>2</sup> : 45<sup>o</sup> diplane (volumetric interaction) [Intensity]

1. Krogager decomposition (5 layers) (Krogager, 1993)

|κ<sub>σ</sub>|<sup>2</sup> : sphere (odd-bounce interaction) [Intensity]

|κ<sub>δ</sub>|<sup>2</sup> : diplane (odd-bounce interaction) [Intensity]

|κ<sub>η</sub>|<sup>2</sup> : helix [Intensity]

θ: orientation angle [degrees]

φ<sub>s</sub>: sphere to diplane angle [degrees]

1. Cameron (nine classes) – non-dimensional layers (Cameron et al., 1996)

**Table A2.1**

|**Classes**|**ID**|
| :-: | :-: |
|Trihedral|1|
|Dihedral|2|
|Narrow Dihedral|3|
|Dipole|4|
|Cylinder|5|
|¼ wave|6|
|Right Helix|7|
|Left Helix|8|
|Asymmetrical|9|

#
#
1. **Incoherent decompositions** describe distributed targets in terms of scattering mechanisms and their diversity. They are generated from averaged Covariance, Coherence or Kennaugh matrices. As for examples, incoherent PRD could be (but not limited to):
1. Based and saved on intensity of scattering mechanisms can be (Freeman and Durden, 1998; Yamaguchi et al., 2011; Raney et al., 2012)

**Table A2.2**

<table><tr><th colspan="1" rowspan="2"><p><b>Level 2b - Layers</b> </p><p><b>[Intensity]</b></p></th><th colspan="3"><b>Incoherent Decompositions</b></th></tr>
<tr><td colspan="1"><b>Freeman-Durden</b></td><td colspan="1"><b>Yamaguchi</b></td><td colspan="1"><b>m-chi</b></td></tr>
<tr><td colspan="1" valign="top"><b>Odd-bounce (surface/trihedral)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Even-bounce (dihedral)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Random (volumetric)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Helix</b></td><td colspan="1"></td><td colspan="1">X</td><td colspan="1"></td></tr>
</table>

1. Based on eigenvector-eigenvalue decomposition expressing the diversity of scattering mechanisms (Cloude and Pottier, 1996) and types:

H : Entropy [ ]  is the polarization diversity

A : Anisotropy [ ]  is weighted difference between the 2<sup>nd</sup> and 3<sup>rd</sup> eigenvalues

α : Odd-even bounce angle [Degrees]

β : orientation angle [Degrees]
# **A2.3: Polarimetric Radar Decomposition Product Examples**
From fully polarimetric covariance matrix ARD format **[POL]** (Level-2a), it is possible to apply any version of the popular Yamaguchi methodology, which decomposes the polarimetric information under relative intensities of 4 scattering types: Odd bounce, Even bounce, Random (volume) and helix. Figure A2.1b) shows HH intensity of a RADARSAT fully polarimetric acquired over a Spanish area. Decomposition using Yamaguchi methodology (Yamaguchi et al., 2011) can be expressed in RGB colour composite (Figure A2.1c) where Red channel refers to even bounce scattering like urban area; Green channel is random scattering like vegetation; and Blue channel is odd bounce scattering like bare soil. Figure A2.1d) is equivalent to c) where radiometric normalisation (terrain flattening) has been applied with the help of the DEM of the scene (Figure A2.1a).

![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.009.jpeg)

***Figure A2.1**  Example of polarimetric decomposition generated from ARD covariance format.  **a)** Shaded DEM of the area; **b)** RADARSAT-2 HH intensity; **c)** Yamaguchi decomposition colour composite (Red: even bounce, Green: random, Blue: odd bounce); **d)** Same as c) with terrain flattening option. Generated from Radarsat-2 FQ18W acquired over Murcia, Spain on 18 June 2014 ©MDA 2014*

#
Figure A2.2 is a **[PRD]** compact polarimetric m-chi decomposition (Raney et al., 2012) simulated from two Canadian prairies Radarsat-2 fully polarimetric scenes acquired in May and June 2012. In May, before the growing season (Figure A2.2a), m-chi shows mainly surface scattering from bare soil (blue channel) and vegetation interaction from forested areas (green channel), while in June (Figure A2.2b) growth of vegetation modifies the radar signal with interacting media function of the vegetation density and geometry which increase the amount of even bounce (red channel) and random scattering. 

![](Aspose.Words.3976f99d-ad59-4f2d-99f2-ac2937000340.010.jpeg)

***Figure A2.2.**  m-chi decomposition colour composite of simulated compact polarimetry from Radarsat-2 over an agriculture area. RGB representation: Red: even bounce, Green: random, Blue: odd bounce. **a)** 3 May 2012; and **b)** 18 June 2012. Generated from Radarsat-2 FQ6W acquired over SMAPVEX12 campaign Manitoba, Canada on 3 May and 20 June 2012 ©MDA 2012*



