import os

import yaml


class Config:
    KABU_PLUS_CONFIG = "configs/kabu_plus.yaml"
    __STOCK_DATA_KEY = "stock_data"
    __STOCK_VARIATION_DATA_KEY = "stock_variation_data"
    __FINANCIAL_RESULTS_KEY = "financial_results"

    def __init__(self):
        self.__kabu_plus_config = self.load_kabu_plus_config()
        self.__local_resource_dir = os.environ.get("SAVE_BASE_DIR")
        self.__kabu_plus_id = os.environ.get("KABU_PLUS_ID")
        self.__kabu_plus_pw = os.environ.get("KABU_PLUS_PW")

        if self.__local_resource_dir == None:
            print("SAVE_BASE_DIR is not specified")
            exit(1)

        if self.__kabu_plus_id == None:
            print("KABU_PLUS_ID is not specified")
            exit(1)

        if self.__kabu_plus_pw == None:
            print("KABU_PLUS_PW is not specified")
            exit(1)

    @property
    def stock_data_key(self):
        return self.__STOCK_DATA_KEY

    @property
    def stock_variation_data_key(self):
        return self.__STOCK_VARIATION_DATA_KEY

    @property
    def financial_results_key(self):
        return self.__FINANCIAL_RESULTS_KEY

    @property
    def kabu_plus_config(self):
        return self.__kabu_plus_config

    @property
    def local_resource_dir(self):
        return self.__local_resource_dir

    @property
    def kabu_plus_id(self):
        return self.__kabu_plus_id

    @property
    def kabu_plus_pw(self):
        return self.__kabu_plus_pw

    def load_kabu_plus_config(self):
        with open(self.KABU_PLUS_CONFIG) as f:
            return yaml.safe_load(f)