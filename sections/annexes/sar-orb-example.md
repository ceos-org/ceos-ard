In contrast to NRB and POL, CEOS-ARD Ocean Radar Backscatter ORB products are geoid corrected and are provided in the Sigma-Nought (σE0) backscatter convention (Figure A3.1a), which is recommended for most ocean applications. In addition, availability of the “Local (or Ellipsoidal) Incidence Angle Image” (Figure A3.1d) and “Look Direction Image” per-pixel metadata are highly recommended (otherwise the general metadata “Look Direction Polynomials”) since they required for operational applications like ocean wind field estimates. 

![Figure A3.1a](assets/sar-orb-examples/S1-ORB-VV.png) **a)** VV intensity
![Figure A3.1b](assets/sar-orb-examples/S1-ORB-VH.png) **b)** VH intensity
![Figure A3.1c](assets/sar-orb-examples/S1-ORB-data-mask.png) **c)** Data mask image
![Figure A3.1d](assets/sar-orb-examples/S1-ORB-local-indicident-angle.png) **d)** Local incident angle

**Figure A3.1**  Sentinel-1 ORB product. Tropical Cyclone Harold passing Vanuatu on April 6, 2020. *Processing: A. Rosenqvist (soloEO).*

Another useful file is the “Mean Wind-Normalised Backscatter Measurements” (Figure A3.2b) which efficiently attenuates intensity variation along range and visually enhances oceanic features. This file is calculated as the ratio between the backscatter intensity and a simulated backscatter intensity image generated using an ocean surface wind model, like CMOD\_IRF2 [@quilfen1998] for VV polarization or CMOD\_IRF2K [@vachon2000] for HH polarization, and the SAR local incidence angle and the look direction information.

![Figure A3.2 Left](assets/sar-orb-examples/S1-ORB-sigma-nought.png) ![Figure A3.1 Right](assets/sar-orb-examples/S1-ORB-intesity-compensated.png)

**Figure A3.2**  Sentinel-1 EW ORB product.  **Left:** ORB intensity (Sigma-Nought); **Right:** Intensity compensated with the “Mean Wind-Normalised Backscatter Measurement” (i.e., not Sigma-Nought) and geocoded. *Processing: G. Hajduch (CLS).*
