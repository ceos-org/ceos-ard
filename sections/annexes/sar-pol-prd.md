Different methodologies allow decomposition of coherent dual-polarization data or fully polarimetric data to meaningful components summarizing the scattering processing with the interacting media. Decomposition techniques are divided in two categories: Coherent and incoherent.

#### Coherent decompositions

Coherent decompositions express the scattering matrix by the summation of elementary objects of known signature (ex.: a sphere, a diplane, a cylinder, a helix, …). They are used mainly to describe point targets which are coherent. As for examples, coherent PRD could be (but not limited to):

1. Pauli decomposition (3 layers)
   - $`|\alpha|^2`$: sphere (odd-bounce interaction) \[Intensity]
   - $`|\beta|^2`$: 0° diplane (even-bounce interaction) \[Intensity]
   - $`|\gamma|^2`$: 45° diplane (volumetric interaction) \[Intensity]
2. Krogager decomposition (5 layers) [@krogager1993]
   - $`|\kappa_\sigma|^2`$ : sphere (odd-bounce interaction) \[Intensity]
   - $`|\kappa_\delta|^2`$ : diplane (odd-bounce interaction) \[Intensity]
   - $`|\kappa_\eta|^2`$ : helix \[Intensity]
   - $`\theta`$: orientation angle \[degrees]
   - $`\Phi_s`$: sphere to diplane angle \[degrees]
3. Cameron (nine classes) – non-dimensional layers [@cameron1996]
   
   **Table** Class to ID mapping
   
   | Classes         |  ID  |
   | :-------------- | :--: |
   | Trihedral       |  1   |
   | Dihedral        |  2   |
   | Narrow Dihedral |  3   |
   | Dipole          |  4   |
   | Cylinder        |  5   |
   | ¼ wave          |  6   |
   | Right Helix     |  7   |
   | Left Helix      |  8   |
   | Asymmetrical    |  9   |

#### Incoherent decompositions

Incoherent decompositions describe distributed targets in terms of scattering mechanisms and their diversity. They are generated from averaged Covariance, Coherence or Kennaugh matrices. As for examples, incoherent PRD could be (but not limited to):

1. Based and saved on intensity of scattering mechanisms can be [@freeman1998; @yamaguchi2011; @raney2012]
   
   **Table A2.2**  Incoherent Decompositions: Freeman-Durden, Yamaguchi, m-chi
   
   | Level 2b - Layers [Intensity]  | Freeman-Durden | Yamaguchi | m-chi |
   | :----------------------------- | :------------: | :-------: | :---: |
   | Odd-bounce (surface/trihedral) |       X        |     X     |   X   |
   | Even-bounce (dihedral)         |       X        |     X     |   X   |
   | Random (volumetric)            |       X        |     X     |   X   |
   | Helix                          |                |     X     |       |
   
2. Based on eigenvector-eigenvalue decomposition expressing the diversity of scattering mechanisms [@cloude1996] and types:
   - $`H`$ : Entropy \[ \]  is the polarization diversity
   - $`A`$ : Anisotropy \[ \]  is weighted difference between the 2ⁿᵈ and 3ʳᵈ eigenvalues
   - $`\alpha`$ : Odd-even bounce angle \[Degrees]
   - $`\beta`$ : orientation angle \[Degrees]
