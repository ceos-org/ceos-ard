InSAR analysis capabilities from CEOS-ARD SAR products are enabled with GSLC products, which is also the case when the Flattened Phase per-pixel data ([@sec:measurements-measurements-flattened-phase]) are included in the NRB or POL products. This is made possible since the simulated topographic phase relative to a given reference orbit has been subtracted.

From classical approach with SLC data, interferometric phase $\Delta \varphi_{1-2}$ between two SAR acquisitions is composed of a topographic phase $\Delta \varphi_{\text{Topo}\_1-2}$, a surface displacement phase $\Delta \varphi_{\text{Disp}\_1-2}$ and other noise terms $\Delta \varphi_{\text{Noise}\_1-2}$ ([@eq:sar-topographic-phase-removal-eq1]). The topographic phase consists to the difference in geometrical path length from each of the two antenna positions to the point on the SAR image ($\varphi_{\text{DEM}\_\text{SLC}}$) and is a function of their orbital baseline distance ([@eq:sar-topographic-phase-removal-eq2]). The surface displacement phase is related to the displacement of the surface that occurred in between the two acquisitions. The noise term is the function of the radar signal interaction with the atmosphere and the ionosphere during each acquisition and function of the system noise.

$$
\Delta \varphi_{1-2} = \Delta \varphi_{\text{Topo}\_1-2} + \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq1}

Where

$$
\Delta \varphi_{\text{Topo}\_1-2} = \varphi_{\text{DEM}\_\text{SLC}\_1} = \varphi_{\text{DEM}\_\text{SLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq2}

Since CEOS-ARD products are already geocoded, it is important to remove the wrapped simulated topographic phase $\varphi_{\text{SimDEM}\_\text{SLC}}$ from the data in slant range ([@eq:sar-topographic-phase-removal-eq3]) during their production, before the geocoding step. The key here is to simulate the topographic phase relatively to a constant reference orbit, as done in a regular InSAR processing. There are two different ways to simulate the topographic phase:

1. The use of a virtual circular orbit above a nonrotating planet [@zebker2010]
2. The use of a specific orbit cycle or a simulated orbit of the SAR mission

In both cases, the InSAR topographic phase $\Delta \varphi_{\text{Topo}\_\text{OrbRef}-2}$ is simulated against the position of a virtual sensor $\Delta \varphi_{\text{Topo}\_\text{OrbRef}}$ lying on a reference orbit, instead of being simulated relatively to an existing reference SAR acquisition ($\varphi_{\text{DEM}\_\text{SLC}\_1}$). The use of a virtual circular orbit is a more robust approach since the reference orbit is defined at a fixed height above scene nadir and assuming the reference orbital height constant for all CEOS-ARD products. While with the second approach, the CEOS-ARD data producer must select a specific archived orbit cycle of the SAR mission or define a simulated one, from which the relative orbit, matching the one of the SAR acquisitions to be processed (to be converted to CEOS-ARD), is defined as the reference orbit. With this second approach, it is important to always use the same orbit cycle (or simulated orbit) for all the CEOS-ARD produced for a mission, in order to preserve the relevant compensated phase in between them. Providing absolute reference orbit number information in the metadata (item 1.7.15) allows users to validate the InSAR feasibility in between CEOS-ARD products.

$$
\varphi_{\text{Flattended}\_\text{SLC}\_2} = \varphi_{\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-2}
$$ {#eq:sar-topographic-phase-removal-eq3}

This procedure is equivalent to bring the position of the sensor platform of all the SAR acquisitions at the same orbital position (i.e., zeros baseline distance in between), which results in a Flattened phase  $\varphi_{\text{Flattended}\_\text{SLC}}$, independent of the local topography.

The phase subtraction could be performed by using a motion compensation approach [@zebker2010] or directly on the SLC data. Then the geometrical correction is performed on the Flattened SLC, which results in a GSLC product.

GSLC can also be saved as a NRB product by including the Flattened Phase per-pixel data ([@sec:measurements-measurements-flattened-phase]) as follows:

$$\text{NRB:} \quad \gamma_T^0 = |GSLC|^2 $$

$$\text{Flattended Phase:} \quad \varphi_{\text{Flattended}} = \arg (GSLC) $$

For POL product, the Flattened phase needs also to be subtracted from the complex number phase of the off-diagonal elements of the covariance matrix.

Demonstration:

From CEOS-ARD flattened SAR products, InSAR processing can be easily performed without dealing with topographic features and orbital sensor position, as for example with two GSLC products

$$
\varphi_{\text{Flattened}\_\text{GSLC}\_1} = \varphi_{\text{SLC}\_1} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-1} = \varphi_{\text{SLC}\_1} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_1}
$$ {#eq:sar-topographic-phase-removal-eq4}

$$
\varphi_{\text{Flattened}\_\text{GSLC}\_2} = \varphi_{\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_\text{OrbRef}-2} = \varphi_{\text{SLC}\_2} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq5}

The differential phase is

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} =  \varphi_{\text{Flattened}\_\text{GSLC}\_1} - \varphi_{\text{Flattened}\_\text{GSLC}\_2}
$$ {#eq:sar-topographic-phase-removal-eq6}

Which can be expanded using ([@eq:sar-topographic-phase-removal-eq3])

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\varphi_{\text{SLC}\_1} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_1}) - (\varphi_{\text{SLC}\_2} - \varphi_{\text{DEM}\_\text{OrbRef}} - \varphi_{\text{DEM}\_\text{SLC}\_2})
$$ {#eq:sar-topographic-phase-removal-eq7}

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\varphi_{\text{SLC}\_1} - \varphi_{\text{SLC}\_2}) - (\varphi_{\text{DEM}\_\text{SLC}\_1}) - \varphi_{\text{DEM}\_\text{SLC}\_2})
$$ {#eq:sar-topographic-phase-removal-eq8}

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = \Delta\varphi_{\text{SLC}\_1-\text{SLC}\_2} - \Delta\varphi_{\text{Topo}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq9}

Where $\Delta\varphi_{\text{SLC}\_1-\text{SLC}\_2}$ can be express as [@eq:sar-topographic-phase-removal-eq1], which gives

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = (\Delta \varphi_{\text{Topo}\_1-2} + \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2}) - \Delta\varphi_{\text{Topo}\_1-2}
$$ {#eq:sar-topographic-phase-removal-eq10}

Consequently, the differential phase of two CEOS-ARD products doesn’t contain a topographic phase and is already unwrapped (at least over stable areas). It is only function of the surface displacement and of the noise term. Depending on the reference DEM and the satellite orbital state vector accuracies, some residual topographic phase could be present. Atmospheric (item 2.15) and ionospheric (item 2.16) phase corrections could be performed during the production of CEOS-ARD products, which reduces the differential phase noise in an InSAR analysis.

$$
\Delta \varphi_{\text{CARD}\_1-\text{CARD}\_2} = \Delta \varphi_{\text{Disp}\_1-2} + \Delta \varphi_{\text{Noise}\_1-2})
$$ {#eq:sar-topographic-phase-removal-eq11}
