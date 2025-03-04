In contrast to NRB and POL, CEOS-ARD Ocean Radar Backscatter ORB products are geoid corrected and are provided in the Sigma-Nought (σE0) backscatter convention ([@fig:sar-orb-example-fig1a]), which is recommended for most ocean applications. In addition, availability of the “Local (or Ellipsoidal) Incidence Angle Image” ([@fig:sar-orb-example-fig1d]) and “Look Direction Image” per-pixel metadata are highly recommended (otherwise the general metadata “Look Direction Polynomials”) since they required for operational applications like ocean wind field estimates.

The following figures show Sentinel-1 ORB products of the Tropical Cyclone Harold passing Vanuatu on April 6, 2020:

![VV intensity; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-VV.png){#fig:sar-orb-example-fig1a}

![VH intensity; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-VH.png){#fig:sar-orb-example-fig1b}

![Data mask image; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-data-mask.png){#fig:sar-orb-example-fig1c}

![Local incident angle; Processing: A. Rosenqvist (soloEO)](assets/sar-orb-examples/S1-ORB-local-indicident-angle.png){#fig:sar-orb-example-fig1d}

Another useful file is the “Mean Wind-Normalised Backscatter Measurements” ([@fig:sar-orb-example-fig2b]) which efficiently attenuates intensity variation along range and visually enhances oceanic features. This file is calculated as the ratio between the backscatter intensity and a simulated backscatter intensity image generated using an ocean surface wind model, like CMOD\_IRF2 [@quilfen1998] for VV polarization or CMOD\_IRF2K [@vachon2000] for HH polarization, and the SAR local incidence angle and the look direction information.

The following figures show Sentinel-1 EW ORB products:

![ORB intensity (Sigma-Nought); Processing: G. Hajduch (CLS)](assets/sar-orb-examples/S1-ORB-sigma-nought.png){#fig:sar-orb-example-fig2a}

![Intensity compensated with the “Mean Wind-Normalised Backscatter Measurement” (i.e., not Sigma-Nought) and geocoded; Processing: G. Hajduch (CLS)](assets/sar-orb-examples/S1-ORB-intesity-compensated.png){#fig:sar-orb-example-fig2b}
