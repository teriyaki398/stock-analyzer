import os

import yaml


class Config:

    def __init__(self):
        self.__kabu_plus_save_dir = os.environ.get("SAVE_BASE_DIR")
        self.__kabu_plus_id = os.environ.get("KABU_PLUS_ID")
        self.__kabu_plus_pw = os.environ.get("KABU_PLUS_PW")

        if self.__kabu_plus_save_dir == None:
            print("SAVE_BASE_DIR is not specified")
            exit(1)

        if self.__kabu_plus_id == None:
            print("KABU_PLUS_ID is not specified")
            exit(1)

        if self.__kabu_plus_pw == None:
            print("KABU_PLUS_PW is not specified")
            exit(1)

    @property
    def kabu_plus_save_dir(self):
        return self.__kabu_plus_save_dir

    @property
    def kabu_plus_id(self):
        return self.__kabu_plus_id

    @property
    def kabu_plus_pw(self):
        return self.__kabu_plus_pw

    def load_kabu_plus_config(self):
        path = "../configs/kabu_plus.yaml"
        with open(path) as f:
            return yaml.safe_load(f)