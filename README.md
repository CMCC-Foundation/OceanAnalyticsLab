# MEI Development Toolkit

This toolkit aims to underpin the development of scientific algorithms for the processing of geospatial data and information, 
especially focusing their implementation in production environment. 
The considered scope is to serve societal needs with the extraction of new knowledge, 
that can be related to the healthiness of the marine environment, from big ocean data.

###### References
- Stefano Nativi, Mattia Santoro, Gregory Giuliani & Paolo Mazzetti (2020) Towards a knowledge base to support global change policy goals, International Journal of Digital Earth, 13:2, 188-216, DOI: 10.1080/17538947.2018.1559367
- United Nations Decade of Ocean Science for Sustainable Developments, Challenges, https://www.oceandecade.org/challenges/
- The Global Risks Report 2022, 17th Edition, World Economic Forum, ISBN: 978-2-940631-09-4



# The VLab Marine Environmental Indicators
A new VLab to serve environmental monitoring activities was implemented in the scope of Blue-Cloud EU project, 
inside the VRE framework D4Science. The VLab aims to provide analytics services to target users, who are usually active actors 
in the monitoring and management of marine areas. Also, the scientific developers play an important role and are part of the VLab users.
The VLab offers several federated services, for the data access, storage and processing (Jupiter, OGC WPS,...), 
which ease the development of new innovative solutions, and the sharing of results and achievements.
Results: notebooks xxx, web processing services xxx, web application DSS/interface,...
TRL...

spatial decision support system, GIS
https://www.eoscsecretariat.eu/news-opinion/water-forecasts-agriculture-eosc-use-cases

###### References
- The VLab Marine Environmental Indicators, https://blue-cloud.d4science.org/web/marineenvironmentalindicators/
- Drudi, Massimiliano; Palermo, Francesco; Mariani, Antonio; Lecci, Rita; Garcia Juan, Andrea; Balem, Kevin; Maze, Guillaume; Bachelot, Loïc; Noteboom, Jan Willem; Pfeil, Benjamin; Castaño-Primo, Rocío; Paul, Julien; Dussurget, Renaud; Arnaud, Alain. (2022). Blue-Cloud Project, presentation. Test the Blue-Cloud Virtual Labs: Marine Environmental Indicators. https://doi.org/10.5281/zenodo.6628701 
- Bachelot Loïc, Balem Kevin, Drago Federico, Drudi Massimiliano, & Garcia Juan Andrea. (2021). Blue-Cloud project, report. Applying machine learning methods to ocean patterns and ocean regimes indicators. Zenodo. https://doi.org/10.5281/zenodo.5896651
- M. Assante, L. Candela, D. Castelli, R. Cirillo, G. Coro, L. Frosini, L. Lelii, F. Mangiacrapa, P. Pagano, G. Panichi, F. Sinibaldi, Enacting open science by D4Science, Future Generation Computer Systems, Volume 101, 2019, Pages 555-563, ISSN 0167-739X, https://doi.org/10.1016/j.future.2019.05.063.
- Santoro, M.; Mazzetti, P.; Nativi, S. The VLab Framework: An Orchestrator Component to Support Data to Knowledge Transition. Remote Sens. 2020, 12, 1795. https://doi.org/10.3390/rs12111795
- United Nations Decade of Ocean Science for Sustainable Developments, Challenges, "Challenge 9 - Skills, knowledge and technology for all", https://www.oceandecade.org/challenges/
- Héder, Mihály. (2017). From NASA to EU: the evolution of the TRL scale in Public Sector Innovation. Innovation Journal. 22. 1. URL: https://www.innovation.cc/volumes-issues/vol22-no2.htm
- jupyter, WPS,...


# The Interoperability and Reusability Challenges
The exploitation of datasets and algorithms, without barriers for the scientific investigation, is highly desired, 
and for the pursuing of this objective, the interoperability and reusability aspects play an important role. 
Indeed, the toolkit copes several specific issues, that can rise when working in an infrastructure 
with federated services for the access to different data sources from different catalogues available across Internet, 
and for the execution of different web processing services.
The expected outcome of using this toolkit is the capability to build, or compose, with a reasonable effort, 
new customized analytics services, that embrace the needed or selected data sources and processing services. 
In addition to that, keeping in mind how the scientific methodology works, the toolkit supports also the tracking of 
information and dependencies for the assessment of output data.

The toolkit includes:
- data access functionalities, based on generalized API
- reader of input parameters, based on a generalized IDL
- manager of logging/provenance information (will be based on W3C-PROV)
- plot generator, for data in NetCDF format, convention xxx, and new convention defined here yyy

###### References
- National Academies of Sciences, Engineering, and Medicine. 2019. Reproducibility and Replicability in Science. Washington, DC: The National Academies Press. https://doi.org/10.17226/25303.
- Hoogenkamp Bram, Farshidi Siamak, Xin Ruyue, Shi Zeshun, Chen Peng, & Zhao Zhiming. (2022, March 22). conference paper. A Decentralized Service Control framework for Decentralized Applications in Cloud Environments. 9th European Conference On Service-Oriented And Cloud Computing (ESOCC), Online. https://doi.org/10.1007/978-3-031-04718-3_4
- Wang, Yuandou; Zhao, Zhiming. (2020, October 18). Decentralized workflow management on software defined infrastructure. Workshop on The 1st Workshop On Data-Centric Workflows On Heterogeneous Infrastructures: Challenges And Directions (DAWHI), in the context of IEEE Service Congress (DAWHI, IEEE Service), Online. https://doi.org/10.1109/SERVICES48979.2020.00059
- European Commission, Directorate-General for Research and Innovation, Turning FAIR into reality : final report and action plan from the European Commission expert group on FAIR data, Publications Office, 2018, https://data.europa.eu/doi/10.2777/1524
- Paul Groth; Luc Moreau; eds. PROV-OVERVIEW: An Overview of the PROV Family of Documents. 30 April 2013, W3C Note. URL: http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/
- PANGEO, A community platform for Big Data geoscience, https://pangeo.io/

# How to Implement a new Algorithm

The repository includes prototype versions of modules which are implementing several functionalities, such as 
the **data access**, the interpretation of **input parameters**, the generation of **static preview plots**, 
the generation of **logging information**.

This is a simple tool that developers can deploy on D4Science, following the tutorial **mockup_method_guide.pptx**.
The implemented mockup method inside the repository shows how to download netCDF files from WEkEO and StorageHub, 
and how to receive the input parameters from an external call.

###### References
- Balem Kevin, Garcia Juan Andrea, Bachelot Loïc, & Maze Guillaume. (2022, May 25). Blue-Cloud project, presentation. Blue-Cloud Marine Environmental Indicators Virtual Lab - The Ocean Regimes Notebook. Zenodo. https://doi.org/10.5281/zenodo.6584430 
- Pittonet Sara, Giuffrida Rita, Mari Marialetizia, & Schaap Dick. (2022). Blue-Cloud Project, Deliverable D6.1, Fact Sheets for cluster projects and other core initiatives (Release 1) (Version 1). Zenodo. https://doi.org/10.5281/zenodo.5549789
- Héder, Mihály. (2017). From NASA to EU: the evolution of the TRL scale in Public Sector Innovation. Innovation Journal. 22. 1. URL: https://www.innovation.cc/volumes-issues/vol22-no2.htm
- Paul Groth; Luc Moreau; eds. PROV-OVERVIEW: An Overview of the PROV Family of Documents. 30 April 2013, W3C Note. URL: http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/


- TRL:
lab -> Jupyter Notebook, command line
relevant environment -> VLab dev (multiple small local datasets)
production environment -> VLab production or web application

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

- OGC Web Processing Service 1.0.0, 2007
- United Nations Decade of Ocean Science for Sustainable Developments, Challenges, "Challenge 9 - Skills, knowledge and technology for all", https://www.oceandecade.org/challenges/
- TBC handbook, roadmap, exploitation plan...
- The VLab Marine Environmental Indicators, https://blue-cloud.d4science.org/web/marineenvironmentalindicators/
- Drudi, Massimiliano; Palermo, Francesco; Mariani, Antonio; Lecci, Rita; Garcia Juan, Andrea; Balem, Kevin; Maze, Guillaume; Bachelot, Loïc; Noteboom, Jan Willem; Pfeil, Benjamin; Castaño-Primo, Rocío; Paul, Julien; Dussurget, Renaud; Arnaud, Alain. (2022). Blue-Cloud Project, presentation. Test the Blue-Cloud Virtual Labs: Marine Environmental Indicators. https://doi.org/10.5281/zenodo.6628701 
- Balem Kevin, Garcia Juan Andrea, Bachelot Loïc, & Maze Guillaume. (2022, May 25). Blue-Cloud project, presentation. Blue-Cloud Marine Environmental Indicators Virtual Lab - The Ocean Regimes Notebook. Zenodo. https://doi.org/10.5281/zenodo.6584430 
- Pittonet Sara, Giuffrida Rita, Mari Marialetizia, & Schaap Dick. (2022). Blue-Cloud Project, Deliverable D6.1, Fact Sheets for cluster projects and other core initiatives (Release 1) (Version 1). Zenodo. https://doi.org/10.5281/zenodo.5549789
- Hoogenkamp Bram, Farshidi Siamak, Xin Ruyue, Shi Zeshun, Chen Peng, & Zhao Zhiming. (2022, March 22). conference paper. A Decentralized Service Control framework for Decentralized Applications in Cloud Environments. 9th European Conference On Service-Oriented And Cloud Computing (ESOCC), Online. https://doi.org/10.1007/978-3-031-04718-3_4
- The Global Risks Report 2022, 17th Edition, World Economic Forum, ISBN: 978-2-940631-09-4
- Bachelot Loïc, Balem Kevin, Drago Federico, Drudi Massimiliano, & Garcia Juan Andrea. (2021). Blue-Cloud project, report. Applying machine learning methods to ocean patterns and ocean regimes indicators. Zenodo. https://doi.org/10.5281/zenodo.5896651
- Wang, Yuandou; Zhao, Zhiming. (2020, October 18). Decentralized workflow management on software defined infrastructure. Workshop on The 1st Workshop On Data-Centric Workflows On Heterogeneous Infrastructures: Challenges And Directions (DAWHI), in the context of IEEE Service Congress (DAWHI, IEEE Service), Online. https://doi.org/10.1109/SERVICES48979.2020.00059
- Santoro, M.; Mazzetti, P.; Nativi, S. The VLab Framework: An Orchestrator Component to Support Data to Knowledge Transition. Remote Sens. 2020, 12, 1795. https://doi.org/10.3390/rs12111795 
- Stefano Nativi, Mattia Santoro, Gregory Giuliani & Paolo Mazzetti (2020) Towards a knowledge base to support global change policy goals, International Journal of Digital Earth, 13:2, 188-216, DOI: 10.1080/17538947.2018.1559367
- M. Assante, L. Candela, D. Castelli, R. Cirillo, G. Coro, L. Frosini, L. Lelii, F. Mangiacrapa, P. Pagano, G. Panichi, F. Sinibaldi, Enacting open science by D4Science, Future Generation Computer Systems, Volume 101, 2019, Pages 555-563, ISSN 0167-739X, https://doi.org/10.1016/j.future.2019.05.063.
- National Academies of Sciences, Engineering, and Medicine. 2019. Reproducibility and Replicability in Science. Washington, DC: The National Academies Press. https://doi.org/10.17226/25303.
- European Commission, Directorate-General for Research and Innovation, Turning FAIR into reality : final report and action plan from the European Commission expert group on FAIR data, Publications Office, 2018, https://data.europa.eu/doi/10.2777/1524
- Héder, Mihály. (2017). From NASA to EU: the evolution of the TRL scale in Public Sector Innovation. Innovation Journal. 22. 1. URL: https://www.innovation.cc/volumes-issues/vol22-no2.htm
- Paul Groth; Luc Moreau; eds. PROV-OVERVIEW: An Overview of the PROV Family of Documents. 30 April 2013, W3C Note. URL: http://www.w3.org/TR/2013/NOTE-prov-overview-20130430/




This toolkit contributes to the change of paradigm process for the moving from a data-drive approach to a knowledge-driven one,
focusing all the attention on the implementing methodology for processing services, first facilitating the exploitation 
of scientific model, with their implementation as geospatial processing services on the Internet.

Starting from the adoption of OGC WPS specification, additional conventions and implementing modules are offered from the toolkit 
to accelerate the developments and reduce the amount of programming, with a special focus to those related 
to the processing of marine environmental indicators, today useful contribution to address the challenges 
of UN Ocean Decade, and cope the major environmental risks.