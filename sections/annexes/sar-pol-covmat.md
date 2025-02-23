In order to preserve the inter-channel polarimetric phase and thus the full information content of coherent dual-pol and fully polarimetric data, the covariance matrix is proposed as the data storage format. Covariance matrices are generated from the complex cross product of polarimetric channels, as shown in [@eq:sar-pol-covmat-eq1] for fully polarimetric data (C3) and in [@eq:sar-pol-covmat-eq3] for dual polarization data (C2). Since these matrices are complex symmetrical, only the upper diagonal elements (bold elements) need to be stored in the ARD database.

**Fully polarimetric**

$$
C3 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* & \mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \\
\sqrt{2} \cdot HV \cdot HH^* & 2 \cdot |\mathbf{H}\mathbf{V}|^2 & \sqrt{2} \cdot \mathbf{H}\mathbf{V} \cdot \mathbf{H}\mathbf{V}^* \\
VV \cdot HH^* & \sqrt{2} \cdot VV \cdot HV^* & |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq1}

Where HV = VH, under the reciprocity assumption. \| \| and \* mean respectively complex modulus and the complex conjugate.

**Dual polarization**

$$
\text{HH-HV:} \quad C2 = \begin{bmatrix}
| \mathbf{H} \mathbf{H} |^2 & \mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \\
HV \cdot HH^* &  |\mathbf{H}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq2}

$$
\text{VV-VH:} \quad C2 = \begin{bmatrix}
| \mathbf{V} \mathbf{H} |^2 & \mathbf{V}\mathbf{H} \cdot \mathbf{V}\mathbf{H}^* \\
VH \cdot VH^* &  |\mathbf{V}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq3}

$$
\text{CH-CV:} \quad C2 = \begin{bmatrix}
| \mathbf{C} \mathbf{H} |^2 & \mathbf{C}\mathbf{H} \cdot \mathbf{C}\mathbf{V}^* \\
CV \cdot CH^* &  |\mathbf{C}\mathbf{V}|^2
\end{bmatrix}
$$ {#eq:eq:sar-pol-covmat-eq4}

Where CH and CV refer to dual polarization transmitting a circular polarized signal. \[CH, CV] can be replaced by \[LH, LV] or \[RH, RV] for left (L) or right (R) hand circular transmission respectively, although RCM will offer only right-hand circular transmission. The coherent HH-VV configuration available on TerraSAR-X could also be represented as C2 format.

Polarimetric decomposition methods like [@yamaguchi2011] for fully polarimetric, or m-chi [@raney2012] for compact polarimetric data, can be applied directly on averaged (speckle filtered) C3 and C2 matrices respectively. These decompositions enhance scattering information, bring it to a more comprehensible level to end-users, and raise the performance of thematic classification methodologies. For SAR products that were acquired with single polarization the use of the covariance matrix does not result in superfluous storage requirements, since only the matrix elements that are populated are retained and the diagonal matrix elements are the backscatter intensities. Thus, a single channel intensity product would yield only one matrix element and the storage needs would not change.

In order to ease the data structure and the metadata in between C3 and C2, [@eq:sar-pol-covmat-eq1] should be redefined as [@eq:sar-pol-covmat-eq5]. Users will have to take care of this non-standard representation when applying their polarimetric analytic tools. “\< \>” means that ARD matrix elements are speckle filtered. [@eq:sar-pol-covmat-eq5] is valid both for dual-linear and quad polarization.

$$
\text{C3 modified:} \quad C3_m = \begin{bmatrix}
| \langle \mathbf{H} \mathbf{H} |^2 \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{H}\mathbf{V}^* \rangle & \langle\mathbf{H}\mathbf{H} \cdot \mathbf{V}\mathbf{V}^* \rangle\\
\langle HV \cdot HH^* \rangle & \langle|\mathbf{H}\mathbf{V}|^2 \rangle & \langle\mathbf{H}\mathbf{V} \cdot \mathbf{V}\mathbf{V}^* \rangle \\
\langle VV \cdot HH^* \rangle& \langle VV \cdot HV^* \rangle & \langle|\mathbf{V}\mathbf{V}|^2 \rangle
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq5}

Furthermore, for compact polarimetric data, it is recommended to store them, by simple transformation, under the circular-circular basis, since RR and RL polarizations ([@eq:sar-pol-covmat-eq6]) permit faster and more intuitive RGB visualizations (R=RR, G=RR/(RR+RL), B= RL).

$$
\text{CH-CV (C2 circular):} \quad C2_c = \begin{bmatrix}
\langle | \mathbf{R} \mathbf{R} |^2 \rangle & \langle\mathbf{R}\mathbf{R} \cdot \mathbf{R}\mathbf{¬}^* \rangle \\
\langle RL \cdot RR^* \rangle &  \langle|\mathbf{R}\mathbf{L}|^2\rangle
\end{bmatrix}
$$ {#eq:sar-pol-covmat-eq6}
