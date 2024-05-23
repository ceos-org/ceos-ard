# **Annex 2: Polarimetric Radar [POL]**
## **A2.1: Normalised Covariance Matrices (CovMat)**
In order to preserve the inter-channel polarimetric phase and thus the full information content of coherent dual-pol and fully polarimetric data, the covariance matrix is proposed as the data storage format. Covariance matrices are generated from the complex cross product of polarimetric channels, as shown in Eq. A2.1 for fully polarimetric data (C3) and in Eq. A2.2 for dual polarization data (C2). Since these matrices are complex symmetrical, only the upper diagonal elements (bold elements) need to be stored in the ARD database.

**Fully polarimetric** 

$$ \tag {Eq. A2.1}
C3 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* & \mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \\
\sqrt{2} \cdot HV \cdot HH^* & 2 \cdot |\mathbf{H}\mathbf{V}|^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{V} \cdot \mathbf{H}\mathbf{V}^* \\
VV \cdot HH^* & \sqrt{2} \cdot VV \cdot HV^* & |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$



Where HV = VH, under the reciprocity assumption. | | and \* mean respectively complex modulus and the complex conjugate. 

**Dual polarization**

$$ \text{HH-HV:} \quad C2 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \\
HV \cdot HH^* &  |\mathbf{H}\mathbf{V}|^2
\end{bmatrix}
$$

$$ \tag{Eq. A2.2} \text{VV-VH:} \quad C2 = \begin{bmatrix}
| \mathbf{V} \mathbf{H} |^2 & \mathbf{V}\mathbf{H} \cdot \mathbf{V}\mathbf{H}^* \\
VH \cdot VH^* &  |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$

$$ \text{CH-CV:} \quad C2 = \begin{bmatrix}
| \mathbf{C} \mathbf{H} |^2 & \mathbf{C}\mathbf{H} \cdot \mathbf{C}\mathbf{V}^* \\
CV \cdot CH^* &  |\mathbf{C}\mathbf{V}|^2
\end{bmatrix}
$$

Where CH and CV refer to dual polarization transmitting a circular polarized signal. [CH, CV] can be replaced by [LH, LV] or [RH, RV] for left (L) or right (R) hand circular transmission respectively, although RCM will offer only right-hand circular transmission. The coherent HH-VV configuration available on TerraSAR-X could also be represented as C2 format. 

Polarimetric decomposition methods like Yamaguchi et al. (2011) for fully polarimetric, or m-chi (Raney et al., 2012) for compact polarimetric data, can be applied directly on averaged (speckle filtered) C3 and C2 matrices respectively. These decompositions enhance scattering information, bring it to a more comprehensible level to end-users, and raise the performance of thematic classification methodologies. For SAR products that were acquired with single polarization the use of the covariance matrix does not result in superfluous storage requirements, since only the matrix elements that are populated are retained and the diagonal matrix elements are the backscatter intensities. Thus, a single channel intensity product would yield only one matrix element and the storage needs would not change.

In order to ease the data structure and the metadata in between C3 and C2, Eq. A2.1 should be redefined as Eq. A2.3. Users will have to take care of this non-standard representation when applying their polarimetric analytic tools. “< >” means that ARD matrix elements are speckle filtered. Eq. A2.3 is valid both for dual-linear and quad polarization.

$$ \tag {Eq. A2.3}
\text{C3 modified:} \quad C3_m = \begin{bmatrix}
| \langle \mathbf{H} \mathbf{H} |^2 \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \rangle\\
\langle HV \cdot HH^* \rangle & \langle|\mathbf{H}\mathbf{V}|^2 \rangle & \langle\mathbf{H}\mathbf{V} \cdot \mathbf{V}\mathbf{V}^* \rangle \\
\langle VV \cdot HH^* \rangle& \langle VV \cdot HV^* \rangle & \langle|\mathbf{V}\mathbf{V}|^2 \rangle
\end{bmatrix}
$$

Furthermore, for compact polarimetric data, it is recommended to store them, by simple transformation, under the circular-circular basis, since RR and RL polarizations (Eq. A2.4) permit faster and more intuitive RGB visualizations (R=RR, G=RR/(RR+RL), B= RL).

$$ \tag{Eq. A2.4} 
\text{CH-CV (C2 circular):} \quad C2_c = \begin{bmatrix}
\langle | \mathbf{R} \mathbf{R} |^2 \rangle & \langle\mathbf{R}\mathbf{R} \cdot \mathbf{R}\mathbf{¬}^* \rangle \\
\langle RL \cdot RR^* \rangle &  \langle|\mathbf{R}\mathbf{L}|^2\rangle
\end{bmatrix}
$$

## **A2.2: Polarimetric Radar Decomposition (PRD)**
Different methodologies allow decomposition of coherent dual-polarization data or fully polarimetric data to meaningful components summarizing the scattering processing with the interacting media. Decomposition techniques are divided in two categories: Coherent and incoherent.

1. **Coherent decompositions** express the scattering matrix by the summation of elementary objects of known signature (ex.: a sphere, a diplane, a cylinder, a helix, …). They are used mainly to describe point targets which are coherent. As for examples, coherent PRD could be (but not limited to):

a. Pauli decomposition (3 layers)
$|\alpha|^2$: sphere (odd-bounce interaction) [Intensity]

$|\beta|^2$: 0<sup>o</sup> diplane (even-bounce interaction) [Intensity]

$|\gamma|^2$: 45<sup>o</sup> diplane (volumetric interaction) [Intensity]

b. Krogager decomposition (5 layers) (Krogager, 1993)

$|\kappa_\sigma|^2$ : sphere (odd-bounce interaction) [Intensity]

$|\kappa_\delta|^2$ : diplane (odd-bounce interaction) [Intensity]

$|\kappa_\eta|^2$ : helix [Intensity]

$\theta$: orientation angle [degrees]

$\Phi_s$: sphere to diplane angle [degrees]

c. Cameron (nine classes) – non-dimensional layers (Cameron et al., 1996)

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


2. **Incoherent decompositions** describe distributed targets in terms of scattering mechanisms and their diversity. They are generated from averaged Covariance, Coherence or Kennaugh matrices. As for examples, incoherent PRD could be (but not limited to):
a. Based and saved on intensity of scattering mechanisms can be (Freeman and Durden, 1998; Yamaguchi et al., 2011; Raney et al., 2012)

**Table A2.2**
<table><tr><th colspan="1" rowspan="2"><p><b>Level 2b - Layers</b> </p><p><b>[Intensity]</b></p></th><th colspan="3"><b>Incoherent Decompositions</b></th></tr>
<tr><td colspan="1"><b>Freeman-Durden</b></td><td colspan="1"><b>Yamaguchi</b></td><td colspan="1"><b>m-chi</b></td></tr>
<tr><td colspan="1" valign="top"><b>Odd-bounce (surface/trihedral)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Even-bounce (dihedral)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Random (volumetric)</b></td><td colspan="1">X</td><td colspan="1">X</td><td colspan="1">X</td></tr>
<tr><td colspan="1" valign="top"><b>Helix</b></td><td colspan="1"></td><td colspan="1">X</td><td colspan="1"></td></tr>
</table>

1. Based on eigenvector-eigenvalue decomposition expressing the diversity of scattering mechanisms (Cloude and Pottier, 1996) and types:

$H$ : Entropy [ ]  is the polarization diversity

$A$ : Anisotropy [ ]  is weighted difference between the 2<sup>nd</sup> and 3<sup>rd</sup> eigenvalues

$\alpha$ : Odd-even bounce angle [Degrees]

$\beta$ : orientation angle [Degrees]


## **A2.3: Polarimetric Radar Decomposition Product Examples**
From fully polarimetric covariance matrix ARD format **[POL]** (Level-2a), it is possible to apply any version of the popular Yamaguchi methodology, which decomposes the polarimetric information under relative intensities of 4 scattering types: Odd bounce, Even bounce, Random (volume) and helix. Figure A2.1b) shows HH intensity of a RADARSAT fully polarimetric acquired over a Spanish area. Decomposition using Yamaguchi methodology (Yamaguchi et al., 2011) can be expressed in RGB colour composite (Figure A2.1c) where Red channel refers to even bounce scattering like urban area; Green channel is random scattering like vegetation; and Blue channel is odd bounce scattering like bare soil. Figure A2.1d) is equivalent to c) where radiometric normalisation (terrain flattening) has been applied with the help of the DEM of the scene (Figure A2.1a).

![](https://github.com/libbyrose/ceos-ard/blob/main/Product%20Family%20Specifications/SAR%20Example%20Products/figA2.1-POL-decomposition.jpeg)

***Figure A2.1**  Example of polarimetric decomposition generated from ARD covariance format.  **a)** Shaded DEM of the area; **b)** RADARSAT-2 HH intensity; **c)** Yamaguchi decomposition colour composite (Red: even bounce, Green: random, Blue: odd bounce); **d)** Same as c) with terrain flattening option. Generated from Radarsat-2 FQ18W acquired over Murcia, Spain on 18 June 2014 ©MDA 2014*

#
Figure A2.2 is a **[PRD]** compact polarimetric m-chi decomposition (Raney et al., 2012) simulated from two Canadian prairies Radarsat-2 fully polarimetric scenes acquired in May and June 2012. In May, before the growing season (Figure A2.2a), m-chi shows mainly surface scattering from bare soil (blue channel) and vegetation interaction from forested areas (green channel), while in June (Figure A2.2b) growth of vegetation modifies the radar signal with interacting media function of the vegetation density and geometry which increase the amount of even bounce (red channel) and random scattering. 

![](https://github.com/libbyrose/ceos-ard/blob/main/Product%20Family%20Specifications/SAR%20Example%20Products/figA2.2-m-chi-decomposition.jpeg)

***Figure A2.2.**  m-chi decomposition colour composite of simulated compact polarimetry from Radarsat-2 over an agriculture area. RGB representation: Red: even bounce, Green: random, Blue: odd bounce. **a)** 3 May 2012; and **b)** 18 June 2012. Generated from Radarsat-2 FQ6W acquired over SMAPVEX12 campaign Manitoba, Canada on 3 May and 20 June 2012 ©MDA 2012*



