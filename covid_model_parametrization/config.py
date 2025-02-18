import os.path
from covid_model_parametrization.utils import utils


class Config:

    ####################### General settings section

    INPUT_DIR = "Inputs"
    CONFIG_DIR = "config"
    SHAPEFILE_DIR = "Shapefiles"
    MAIN_OUTPUT_DIR = "Outputs"

    ####################### SADD Exposure section

    SADD_OUTPUT_DIR = "Exposure_SADD"
    VULNERABILITY_OUTPUT_DIR = "Vulnerability"
    COVID_OUTPUT_DIR = "COVID"
    GRAPH_OUTPUT_DIR = "Graph"

    def __init__(self):
        self.DIR_PATH = getattr(
            self, "DIR_PATH", os.path.split(os.path.dirname(os.path.realpath(__file__)))
        )[0]
        self._parameters = None

    def parameters(self, country_iso3):
        if self._parameters is None:
            self._parameters = utils.parse_yaml(os.path.join(self.CONFIG_DIR, f'{country_iso3.lower()}.yml'))
        return self._parameters

    ####################### SADD section

    EXPOSURE_GEOJSON = "{}_Exposure.geojson"

    CO_DIR = "InputsFromCOs"

    GENDER_CLASSES = ["f", "m"]
    AGE_CLASSES = [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    WORLDPOP_DIR = "WorldPop"
    WORLDPOP_FILENAMES = {
        "sadd": "{country_iso3}_{gender}_{age}_2020.tif",
        "pop": "{country_iso3}_ppp_2020.tif",
        "unadj": "{country_iso3}_ppp_2020_UNadj.tif",
    }
    WORLDPOP_URL = {
        "age_sex": "ftp://ftp.worldpop.org.uk/GIS/AgeSex_structures/Global_2000_2020/2020/{0}/{1}_{2}_{3}_2020.tif",
        "pop": "ftp://ftp.worldpop.org.uk/GIS/Population/Global_2000_2020/2020/{0}/{1}_ppp_2020.tif",
        "unadj": "ftp://ftp.worldpop.org.uk/GIS/Population/Global_2000_2020/2020/{0}/{1}_ppp_2020_UNadj.tif",
    }

    def SADD_output_dir(self):
        return os.path.join(
            self.DIR_PATH, self.MAIN_OUTPUT_DIR, "{}", self.SADD_OUTPUT_DIR
        )

    ####################### Mobility section

    MOBILITY_DIR = 'mobility'

    ROAD_WEIGHTS_FILENAME = 'road_weights.csv'

    MOBILITY_FILENAME = '{country_iso3}_mobility_matrix.csv'
    MOBILITY_FIGNAME = '{country_iso3}_mobility_matrix_hist.png'

    ROADS_HDX_ADDRESS = 'hotosm_{country_iso3}_roads'
    ROADS_FILENAME = 'hotosm_{country_iso3}_roads_gpkg.zip'
    ROADS_SHAPEFILE = 'hotosm_{country_iso3}_roads.gpkg'

    CROSSINGS_FILENAME = 'crossings.gpkg'
    DISTANCES_FILENAME = 'distances.csv'

    ####################### Vulnerability section

    VULNERABILITY_FILENAME = "{country_iso3}_Vulnerabilities.geojson"

    # Shape stuff
    SHP_CRS = "EPSG:4326"

    # IPC
    IPC_DIR = "IPC"

    # GHS data
    GHS_DIR = "GHS"
    GHS_URL_BASE = "https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL"
    GHS_URL = {
        "SMOD": "GHS_SMOD_POP_GLOBE_R2019A/GHS_SMOD_POP2015_GLOBE_R2019A_54009_1K/V2-0/tiles/"
        "GHS_SMOD_POP2015_GLOBE_R2019A_54009_1K_V2_0_{column}_{row}.zip",
        "POP": "GHS_POP_MT_GLOBE_R2019A/GHS_POP_E2015_GLOBE_R2019A_54009_1K/V1-0/tiles/"
        "GHS_POP_E2015_GLOBE_R2019A_54009_1K_V1_0_{column}_{row}.zip",
    }
    OUTPUT_GHS = {
        "SMOD": "{country_iso3}_SMOD_2015_1km_mosaic.tif",
        "POP": "{country_iso3}_POP_2015_1km_mosaic.tif",
    }
    GHS_CRS = "ESRI:54009"
    URBAN_MIN_MAX = (21, 30)
    RURAL_MIN_MAX = (11, 13)

    def vulnerability_output_dir(self):
        return os.path.join(
            self.DIR_PATH, self.MAIN_OUTPUT_DIR, "{}", self.VULNERABILITY_OUTPUT_DIR
        )

    ####################### COVID section

    def COVID_output_dir(self):
        return os.path.join(
            self.DIR_PATH, self.MAIN_OUTPUT_DIR, "{}", self.COVID_OUTPUT_DIR
        )

    COVID_OUTPUT_CSV = "{}_COVID.csv"

    # maybe we can move this to the yml file?
    HLX_TAG_TOTAL_CASES = "#affected+infected+confirmed+total"
    HLX_TAG_TOTAL_DEATHS = "#affected+infected+dead+total"
    HLX_TAG_DATE = "#date"
    HLX_TAG_ADM1_NAME = "#adm1+name"
    HLX_TAG_ADM2_NAME = "#adm2+name"
    HLX_TAG_ADM1_PCODE = "#adm1+pcode"
    HLX_TAG_ADM2_PCODE = "#adm2+pcode"

    ####################### Graph section

    GRAPH_OUTPUT_FILE = "{}_graph.json"
    GRAPH_OUTPUT_FILE_JSON = "{}_graph.json"
    GRAPH_OUTPUT_FILE_PICKLE = "{}_graph.p"

    CONTACT_MATRIX_DIR = "contact_matrices_152_countries"
    CONTACT_MATRIX_FILENAME = "MUestimates_{contact_matrix_type}_{file_number}.xlsx"
    CONTACT_MATRIX_TYPES = ["home", "work", "school", "other_locations"]

    PSEUDO_MERCATOR_CRS = "EPSG:3857"

    ####################### NPI section

    ACAPS_HDX_ADDRESS = 'acaps-covid19-government-measures-dataset'
    ACAPS_DIR = 'ACAPS_NPIs'
    ACAPS_FILENAME = 'ACAPS_npis_raw_data.xlsx'
    MEASURE_EQUIVALENCE_FILENAME = 'NPIs - ACAPS NPIs.csv'

    NPI_DIR = 'NPIs'
    NPI_INTERMEDIATE_OUTPUT_FILENAME = '{}_NPIs_input.xlsx'
    NPI_TRIAGED_INTERMEDIATE_OUTPUT_FILENAME = '{}_NPIs_triaged.csv'
    NPI_FINAL_OUTPUT_FILENAME = '{}_NPIs.csv'


    #################### MISC

    WHO_HDX_ADDRESS = 'coronavirus-covid-19-cases-and-deaths'
    WHO_DIR = 'WHO_COVID_cases'
    WHO_FILENAME = 'WHO_covid_cases.csv'
