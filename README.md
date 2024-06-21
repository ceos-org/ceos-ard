# CEOS-ARD

> **CEOS Analysis Ready Data (CEOS-ARD) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.**

Visit [ceos.org/ard](https://ceos.org/ard) for more information on CEOS-ARD, self-assessments and CEOS-ARD certified datasets.
[ceos.org/ard](https://ceos.org/ard) is the official reference for all CEOS-ARD documentation, while this repository remains a development version.

## Framework

Many satellite data users lack the expertise, infrastructure and internet bandwidth to efficiently and effectively access, preprocess, and utilize the growing volume of space-based data for local, regional, and national decision-making. Furthermore, even sophisticated users of EO data typically invest a large proportion of their effort into data preparation. This is a major barrier to full and successful utilization of space-based data, and threatens the success of major global and regional initiatives supported by the Committee on Earth Observation Satellites (CEOS). As data volumes grow, this barrier is becoming more significant for all users.

Countries and international organizations have expressed a desire for support from CEOS to facilitate access to and processing of satellite data into CEOS Analysis Ready Data (CEOS-ARD) products. Systematic and regular provision of CEOS-ARD will greatly reduce the burden on global satellite data users.

Read also into the [CEOS-ARD Strategy 2021](./CEOS-ARD%20Strategy%202021.pdf).

## Product Family Specifications

The following Product Family Specifications are currently defined:

- [Aquatic Reflectance (Optical)](./Specifications/Aquatic-Reflectance/README.md)
- [Nighttime Lights Surface Radiance (Optical)](./Specifications/Nighttime-Lights-Surface-Radiance/README.md)
- [Surface Reflectance (Optical)](./Specifications/Surface-Reflectance/README.md)
- [Surface Temperature (Optical)](./Specifications/Surface-Temperature/README.md)
- [Synthetic Aperture Radar](./Specifications/Synthetic-Aperture-Radar/README.md)

## Governance Framework

The [CEOS-ARD Governance Framework](./CEOS-ARD%20Governance%20Framework%202021.pdf) covers:

### Definition

The definition of CEOS-ARD is not exclusive or prescriptive. The definition of CEOS-ARD reflects the attributes of fundamental measurement products for the majority of global remote sensing users with land imaging applications, and are the minimum level required to support time series analysis and data interoperability.

### Product Family Specifications

All of them detail specific 'Threshold' and 'Goal' requirements for:

- General Metadata
- Per-pixel Metadata
- Radiometric and Atmospheric Corrections
- Geometric Corrections

A [Product Family Specification Template](./Template) has been developed to provide a starting point for future PFS, to ensure commonality in layout, general structure, interpretation and approach. It provides a foundation and common suite of assessment factors for all PFS.

### Product Assessments

Product Assessments checks how well the specific product complies with each of the metadata and calibration criteria in the Product Family Specification. Includes a description of ‘how’ it complies.

The CEOS Working Group on Calibration & Validation (WGCV) has defined formal processes for how these assessments will be carried out, including the peer reviews that will be undertaken by the WGCV.

A [self-assessment guide](./CEOS-ARD%20Self-Assessment%20Guide%202023.pdf) has been made available.

## STAC Extensions

The CEOS-ARD Extension to the SpatioTemporal Asset Catalog (STAC) specification specifies how to create STAC Items and Collections that comply to the various CEOS-ARD product family specifications. The repository for this extension can be found [here](https://github.com/stac-extensions/ceos-ard).

## Contact

The CEOS-ARD team can be contacted at <ard-contact@lists.ceos.org>
