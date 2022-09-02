# Algorithm Development Framework

This is a simple tool that developers can deploy on D4Science, following the tutorial **mockup_method_guide.pptx**.
The repository includes prototype versions of modules which are implementing several functionalities, such as 
the **data access**, the interpretation of **input parameters**, the generation of **static preview plots**, 
the generation of **logging information**.
The implemented mockup method inside the repository shows how to download netCDF files from WEkEO and StorageHub, 
and how to receive the input parameters from an external call.

# The VLab Marine Environmental Indicators

xxx what resources it is federating, TRL

# The Interoperability Challenge

xxx FAIR, data, algorithms, catalogue

# How to Implement a new Algorithm

New algorithms can be implemented in new methods with their specific interface for the inputs and outputs.

The mockup method can generally be considered as a convenient baseline for a new implementation, which will have its own
input parameters, access and download of the input data, processing, and output preparation.

To ease the following integration between interface/s and method/s, the recommended best practice consists 
in implementing also a corresponding new mockup method which implement the new input/output interface, without actual actions 
(i.e.: data download, processing,...). 


## Instructions to use the mockup method

### Preparation
To run this tools locally, follow this steps:
1. run  [get_variables.sh](./get_globalvariables.sh) passing as 
argument the user token (you can find it when log into D4Science):

`./get_variables.sh $TOKEN`

A file named **globalvariables.csv** will be created and used to download the file correctly.
##### Attention: do not upload this file when upload the method, it will be created at runtime by dataminer itself


2. Generate the WEkEO api key using the command:

` python wekeo_api_key.py wekeo_username wekeo_password`

then put your key in hdaKey param [daccess.py](./download/daccess.py)

##### Attention: by default the system use bluecloud proxy to request the token to access to hda, if you put your hda key the proxy will be disabled

3. (Optional) you can change dirID in  [daccess.py](./download/daccess.py) if you want
to download your dataset from StorageHub


### Run the algorithm
The mockup method supports two different output type:

- **mockup_download**: download a netCDF file and produce a plot (with some data source)
- **mockup_input_read**: print the input parameters send as input
- 
To launch the tools simply run the command:


- `python mockup.py "{ 'id_output_type': 'mockup_download', 'id_field': 'sea_water_potential_temperature', 'data_source': ['MEDSEA_MULTIYEAR_PHY_006_004'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1987-01', 'end_time': '1987-01' }"` -> download from WEkEO

- `python mockup.py "{ 'id_output_type': 'mockup_download', 'id_field': 'sea_water_potential_temperature', 'data_source': ['MEDSEA_MULTIYEAR_PHY_006_004_STHUB'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1987-01', 'end_time': '1987-01' }"` -> download from StorageHub

- `python mockup.py "{ 'id_output_type': 'mockup_download', 'id_field': 'mass_concentration_of_chlorophyll_a_in_sea_water', 'data_source': ['OCEANCOLOUR_MED_CHL_L4_NRT_OBSERVATIONS_009_041'], 'working_domain': {'box': [[-6,30.15625,36.28125,45.96875]], 'depth_layers': [[1.472102,5334.648]]}, 'start_time': '2020-07', 'end_time': '2020-07'}"` -> download from WEkEO

- `python mockup.py "{ 'id_output_type': 'mockup_download', 'id_field': 'wind_speed', 'data_source': ['C3S_ERA5_MEDSEA_1979_2020_STHUB'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1979-01-01', 'end_time': '2021-01-31' }"` -> download from StorageHub (plot is not produced)

or

- `python mockup.py "{ 'id_output_type': 'mockup_input_read', 'id_field': 'sea_water_potential_temperature', 'data_source': ['MEDSEA_MULTIYEAR_PHY_006_004'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1987-01', 'end_time': '1987-01' }"` -> download from WEkEO

- `python mockup.py "{ 'id_output_type': 'mockup_input_read', 'id_field': 'sea_water_potential_temperature', 'data_source': ['MEDSEA_MULTIYEAR_PHY_006_004_STHUB'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1987-01', 'end_time': '1987-01' }"` -> download from StorageHub

- `python mockup.py "{ 'id_output_type': 'mockup_input_read', 'id_field': 'mass_concentration_of_chlorophyll_a_in_sea_water', 'data_source': ['OCEANCOLOUR_MED_CHL_L4_NRT_OBSERVATIONS_009_041'], 'working_domain': {'box': [[-6,30.15625,36.28125,45.96875]], 'depth_layers': [[1.472102,5334.648]]}, 'start_time': '2020-07', 'end_time': '2020-07'}"` -> download from WEkEO

- `python mockup.py "{ 'id_output_type': 'mockup_input_read', 'id_field': 'wind_speed', 'data_source': ['C3S_ERA5_MEDSEA_1979_2020_STHUB'], 'working_domain': { 'box': [[-6, 30.15625, 36.28125, 45.96875]], 'depth_layers': [[1.472102, 5334.648]] }, 'start_time': '1979-01-01', 'end_time': '2021-01-31' }"` -> download from StorageHub (plot is not produced)


# References

- The VLab Marine Environmental Indicators, https://blue-cloud.d4science.org/web/marineenvironmentalindicators/
- Drudi, Massimiliano; Palermo, Francesco; Mariani, Antonio; Lecci, Rita; Garcia Juan, Andrea; Balem, Kevin; Maze, Guillaume; Bachelot, Loïc; Noteboom, Jan Willem; Pfeil, Benjamin; Castaño-Primo, Rocío; Paul, Julien; Dussurget, Renaud; Arnaud, Alain. (2022). Test the Blue-Cloud Virtual Labs: Marine Environmental Indicators. https://doi.org/10.5281/zenodo.6628701 
- National Academies of Sciences, Engineering, and Medicine. 2019. Reproducibility and Replicability in Science. Washington, DC: The National Academies Press. https://doi.org/10.17226/25303.
- European Commission, Directorate-General for Research and Innovation, Turning FAIR into reality : final report and action plan from the European Commission expert group on FAIR data, Publications Office, 2018, https://data.europa.eu/doi/10.2777/1524
- Héder, Mihály. (2017). From NASA to EU: the evolution of the TRL scale in Public Sector Innovation. Innovation Journal. 22. 1. URL: https://www.innovation.cc/volumes-issues/vol22-no2.htm
- Paul Groth; Luc Moreau; eds. PROV-OVERVIEW: An Overview of the PROV Family of Documents. 30 April 2013, W3C Note. URL: http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/
