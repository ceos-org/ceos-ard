## Annex 1: CARD4L Requirement Examples

### 1. General Metadata

#### 1.1 Traceability

Example of measurement traceability in metadata:

```xml
<band add_offset="0.000000" category="image" data_type="INT16" fill_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale_factor="0.100000">
    <short_name>LC08ST</short_name>
    <long_name>Surface Temperature</long_name>
    <file_name>ST</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="3730.000000" min="1500.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

Example of measurement uncertainty in metadata:

```xml
<band category="qa" data_type="INT16" fill_value="-9999" name="STQA" nlines="5000" nsamps="5000" product="st_qa" scale_factor="0.010000" source="toa_refl">
    <short_name>LC08STQA</short_name>
    <long_name>Surface temperature quality band</long_name>
    <file_name>STQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="32767.000000" min="0.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```
#### 1.3 Data Collection Time

Example of scene center time (UTC):

```xml
<scene_center_time>17:23:57.201686Z</scene_center_time>
```

The granule start and end times are contained in the XML metadata:

```xml
<metadataObject ID="acquisitionPeriod" classification="DESCRIPTION" category="DMD">
    <metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Acquisition Period">
    <xmlData>
        <sentinel-safe:acquisitionPeriod>
            <sentinel-safe:startTime>2018-10-07T05:04:50.425838Z</sentinel-safe:startTime>
            <sentinel-safe:stopTime>2018-10-07T05:07:50.425838Z</sentinel-safe:stopTime>
        </sentinel-safe:acquisitionPeriod>
    </xmlData>
    </metadataWrap>
</metadataObject>
```

Per pixel times are derived using information from the "time_in.nc" and “indices_in.nc” datafiles following a prescribed recipe.

#### 1.4 Geographical Area

Example of the bounding coordinates in decimal degrees (WGS84):

```xml
<bounding_coordinates>
    <west>-99.9109607425</west>
    <east>-98.0134952569</east>
    <north>43.3609828699</north>
    <south>41.9778528562</south>
</bounding_coordinates>
```

Example of the corner points in the map projection system (Albers):

```xml
<corner_point location="UL" x="-315585.000000" y="2264805.000000"/>
<corner_point location="LR" x="-165585.000000" y="2114805.000000"/>
```

#### 1.6 Map Projection

```xml
<projection_information datum="WGS84" projection="AEA" units="meters">
    <corner_point location="UL" x="-315585.000000" y="2264805.000000"/>
    <corner_point location="LR" x="-165585.000000" y="2114805.000000"/>
    <grid_origin>UL</grid_origin>
    <albers_proj_params>
        <standard_parallel1>29.500000</standard_parallel1>
        <standard_parallel2>45.500000</standard_parallel2>
        <central_meridian>-96.000000</central_meridian>
        <origin_latitude>23.000000</origin_latitude>
        <false_easting>0.000000</false_easting>
        <false_northing>0.000000</false_northing>
    </albers_proj_params>
</projection_information>
```

#### 1.7 Geometric Correction Source

Example of elevation source:

```xml
<elevation_source>GLS2000</elevation_source>
```

The XML wrapper provides the source of the geometric calibration:

```xml
<sentinel-safe:resource name="S3A_SL_1_GEC_AX_20160216T000000_20991231T235959_20180202T120000___________________MPC_O_AL_007.SEN3" role="SLSTR Geometric Calibration Data File">
   <sentinel-safe:processing name="AdfProcessing">
  	<sentinel-safe:facility name="ESA Mission Performance Coordinating Centre (MPC)" organisation="ESA Mission Performance Coordinating Centre" site="Sophia Antipolis" country="France">
     	<sentinel-safe:hardware name="OPE"/>
         <sentinel-safe:software name="ADC" version="1.0"/>
      </sentinel-safe:facility>
   </sentinel-safe:processing>
</sentinel-safe:resource>
```

#### 1.8 Geometric Accuracy of the Data

```xml
<geometric_rmse_model>9.021</geometric_rmse_model>
<geometric_rmse_model_x>6.864</geometric_rmse_model_x>
<geometric_rmse_model_y>5.854</geometric_rmse_model_y>
```

#### 1.9 Instrument

```xml
<satellite>LANDSAT_8</satellite>
<instrument>OLI/TIRS_Combined</instrument>
```

The XML wrapper provides the instrument details:

```xml
 <metadataObject ID="platform" classification="DESCRIPTION" category="DMD">
    <metadataWrap mimeType="text/xml" vocabularyName="Sentinel-SAFE" textInfo="Platform Description">
       <xmlData>
          <sentinel-safe:platform>
             <sentinel-safe:nssdcIdentifier>2016-011A</sentinel-safe:nssdcIdentifier>
             <sentinel-safe:familyName>Sentinel-3</sentinel-safe:familyName>
             <sentinel-safe:number>A</sentinel-safe:number>
             <sentinel-safe:instrument>
                <sentinel-safe:familyName abbreviation="SLSTR">Sea and Land Surface Temperature Radiometer</sentinel-safe:familyName>
                <sentinel-safe:mode identifier="EO">Earth Observation</sentinel-safe:mode>
             </sentinel-safe:instrument>
          </sentinel-safe:platform>
       </xmlData>
    </metadataWrap>
 </metadataObject>
```

#### 1.11 Sensor Calibration

```xml
<cpf_name>LC08CPF_20180101_20180331_01.02</cpf_name>
```

#### 1.13 Algorithms

Example for Surface Temperature algorithm version:

```xml
<app_version>st_1.3.0</app_version>
```

#### 1.14 Auxiliary Data

All Auxiliary Datafiles (ADFs) are listed in the XML wrapper:

```xml
<sentinel-safe:resource name="S3__SL_2_LSTBAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST biome data file" version="06.16">
<sentinel-safe:resource name="S3__SL_2_LSTVAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST vegetation fraction data file" version="06.16">
<sentinel-safe:resource name="S3__SL_2_LSTWAX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3" role="SLSTR LST water vapour data file" version="06.16">
```

#### 1.15 Processing Chain Provenance

Processing chain provenance information is stored in the XML wrapper under the following tag:

```xml
<metadataObject ID="processing" classification="PROVENANCE" category="PDI">
```

#### 1.17 Overall Data Quality

Overall data quality information is stored in the XML wrapper under the following tag:

```xml
<metadataObject ID="measurementQualityInformation" classification="DESCRIPTION" category="DMD">
```

### 2. Per-Pixel Metadata

#### 2.2 No Data

Example of the fill_value specified for each band in metadata:

```xml
<band add_offset="0.000000" category="image" data_type="INT16" fill_value="-9999" name="ST" nlines="5000" nsamps="5000" product="st" scale_factor="0.100000">
    <short_name>LC08ST</short_name>
    <long_name>Surface Temperature</long_name>
    <file_name>ST</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>temperature (kelvin)</data_units>
    <valid_range max="3730.000000" min="1500.000000"/>
    <app_version>st_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
	confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
	confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing" ;
```

#### 2.3 Incomplete Testing

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
	confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
	confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing”;
```

#### 2.4 Saturation

Example of RADSATQA band showing the saturation information for the thermal bands used for Surface Temperature calculation:

```xml
<band category="qa" data_type="UINT16" fill_value="1" name="RADSATQA" nlines="5000" nsamps="5000" product="toa_refl" source="level1">
    <short_name>LC08RADSAT</short_name>
    <long_name>saturation mask</long_name>
    <file_name>RADSATQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>bitmap</data_units>
    <bitmap_description>
        <bit num="0">Data Fill Flag (0 = valid data, 1 = invalid data)</bit>
        <bit num="1">Band 1 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="2">Band 2 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="3">Band 3 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="4">Band 4 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="5">Band 5 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="6">Band 6 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="7">Band 7 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="8">N/A</bit>
        <bit num="9">Band 9 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="10">Band 10 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
        <bit num="11">Band 11 Data Saturation Flag (0 = valid data, 1 = saturated data)</bit>
    </bitmap_description>
    <app_version>LaSRC_1.3.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains per-pixel information on "no / bad data through saturation / incomplete testing etc". The following field has an "unfilled" flag:

```netcdf
ushort confidence_in(rows, columns) ;
	confidence_in:flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
	confidence_in:flag_meanings = "coastline ocean tidal land inland_water unfilled spare spare cosmetic duplicate day twilight sun_glint snow summary_cloud summary_pointing" ;
```

#### 2.5 Cloud

Example of PIXELQA showing the bit value for cloud pixels (as well as cloud and cirrus confidence):

```xml
<band category="qa" data_type="UINT16" fill_value="1" name="PIXELQA" nlines="5000" nsamps="5000" product="level2_qa" source="level1">
    <short_name>LC08PQA</short_name>
    <long_name>level-2 pixel quality band</long_name>
    <file_name>PIXELQA</file_name>
    <pixel_size units="meters" x="30" y="30"/>
    <resample_method>none</resample_method>
    <data_units>quality/feature classification</data_units>
    <bitmap_description>
        <bit num="0">fill</bit>
        <bit num="1">clear</bit>
        <bit num="2">water</bit>
        <bit num="3">cloud shadow</bit>
        <bit num="4">snow</bit>
        <bit num="5">cloud</bit>
        <bit num="6">cloud confidence</bit>
        <bit num="7">cloud confidence</bit>
        <bit num="8">cirrus confidence</bit>
        <bit num="9">cirrus confidence</bit>
        <bit num="10">terrain occlusion</bit>
        <bit num="11">unused</bit>
        <bit num="12">unused</bit>
        <bit num="13">unused</bit>
        <bit num="14">unused</bit>
        <bit num="15">unused</bit>
    </bitmap_description>
    <app_version>generate_pixel_qa_1.6.0</app_version>
    <production_date>2018-11-30T04:47:38Z</production_date>
</band>
```

The "flags_in.nc" datafile contains all the cloud masking flags. Three fields are relevant:

1. cloud_in
2. confidence_in
3. bayes_in

The "cloud_in" field contains all the individual threshold-based mask:

```xml
flag_masks = 1US, 2US, 4US, 8US, 16US, 32US, 64US, 128US, 256US, 512US, 1024US, 2048US, 4096US, 8192US, 16384US, 32768US ;
cloud_in:flag_meanings = "visible 1.37_threshold 1.6_small_histogram 1.6_large_histogram 2.25_small_histogram 2.25_large_histogram 11_spatial_coherence gross_cloud thin_cirrus medium_high fog_low_stratus 11_12_view_difference 3.7_11_view_difference thermal_histogram spare spare"
```

The "confidence_in" field contains the "summary_cloud_mask" from the most appropriate cloud_in flags; the value of the bit is 16384US.
The "bayes_in" field contains the "single_moderate" probabilistic cloud flag; the value of the bit is 2UB.

#### 2.6 Cloud Shadow

Please see the cloud shadow part in the example provided in requirement 2.5

#### 2.7 Snow/Ice Mask

Please see the snow part in the example provided in requirement 2.5

### 3. Radiometric and Atmospheric Corrections

*No examples provided*

### 4. Geometric Corrections

*No examples provided*
