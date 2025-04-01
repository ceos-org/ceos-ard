In contrast to basic NRB and **POL products**, CEOS-ARD Geocoded SLC GSLC products are kept close to the native resolution in complex data format for which local topographic InSAR phases, relative to a reference orbit [@zebker2010; @zebker2017], have been removed. Having a volume of GSLC products acquired over repeat cycles, already radiometric and phase terrain corrected and geocoded ([@fig:sar-gslc-example-fig1a; @fig:sar-gslc-example-fig1b]), allows user-friendly production of a first iteration of the InSAR coherence ([@eq:sar-gslc-example-eq1; @fig:sar-gslc-example-fig1c]) and differential phases ([@eq:sar-gslc-example-eq2; @fig:sar-gslc-example-fig1d]) in between GSLC pairs, simply by applying local averaging window over the product of a GSLC product (GSLC1) with the complex conjugate of a second GSLC (GSLC2) divided by their local averaged intensities. These intermediate files could be used for coherent change detection analysis and surface displacement monitoring.

$$
\text{Complex coherence:} \quad \rho = \frac{\sum [ GSLC_1 * conj (GSLC_2)]}{ \sqrt{ \sum |GSLC_1|^2 * \sum |GSLC_2|^2}}
$$ {#eq:sar-gslc-example-eq1}

The InSAR differential phase ([@eq:sar-gslc-example-eq2]) is the argument of the complex coherence estimated with [@eq:sar-gslc-example-eq1].

$$
\text{InSAR differential phase:} \quad \varphi =\arg(\rho)
$$ {#eq:sar-gslc-example-eq2}

Some advanced NRB or POL products could include per-pixel “Flattened Phase” data ([@sec:rcm.measurements-flattened-phase]). This “Flattened Phase” enables the possibility to perform InSAR analysis as with two GSLC products. As for example, from two different NRB products (NRB1) and (NRB2), acquired over repeat cycles (i.e., on the same relative orbit), containing $\gamma_T^0$ and their corresponding “Flattened Phase” (FPh1) and (FPh2) per-pixel data, the complex InSAR coherence ([@eq:sar-gslc-example-eq3]) can be estimated in the similar manner as [@eq:sar-gslc-example-eq1] for GSLC products.

$$
\text{Complex coherence:} \quad \rho_{NRB} = \frac{\sum [ (\sqrt{NRB_1} \cdot e^{i\cdot FPh1}) \cdot conj (\sqrt{NRB_2} \cdot e^{i\cdot FPh2})]}{ \sqrt{ \sum NRB_1 * \sum NRB_2}}
$$ {#eq:sar-gslc-example-eq3}

The following figures show Sentinel-1 GSLC product examples over Death Valley National Park, California, US:

![GSLC1: Intensity data of the first GSLC product (2017-05-27)](assets/sar-gslc-example/S1-GSLC1.jpeg){#fig:sar-gslc-example-fig1a}

![GSLC2: Intensity data of the second GSLC product (2017-06-08)](assets/sar-gslc-example/S1-GSLC2.jpeg){#fig:sar-gslc-example-fig1b}

![InSAR coherence map generated directly from [@fig:sar-gslc-example-fig1a] and [@fig:sar-gslc-example-fig1b]](assets/sar-gslc-example/S1-InSAR-coherence.png){#fig:sar-gslc-example-fig1c}

![InSAR differential phase map generated directly from [@fig:sar-gslc-example-fig1a] and [@fig:sar-gslc-example-fig1b]](assets/sar-gslc-example/S1-InSAR-differential-phase.png){#fig:sar-gslc-example-fig1d}

Some advanced GSLC product can be provided with “Radar Unit Look Vector Grid Image” per-pixel metadata ([@fig:sar-gslc-example-fig2a; @fig:sar-gslc-example-fig2b; @fig:sar-gslc-example-fig2c]) which gives the accurate 3-D components radar unit look vector used as for example in decomposing the vertical and horizontal component of an InSAR surface displacement estimate.

The following figures show 3-D components radar unit look vector of the GSLC product:

![x unit component](assets/sar-gslc-example/S1-GSLC-x-component.png){#fig:sar-gslc-example-fig2a}

![y unit component](assets/sar-gslc-example/S1-GSLC-y-component.png){#fig:sar-gslc-example-fig2b}

![z unit component](assets/sar-gslc-example/S1-GSLC-z-component.png){#fig:sar-gslc-example-fig2c}
