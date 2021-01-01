import time

import yaml

from tools.file_util import *
from tools.kabuplus_client import KabuPlusClient

KABU_PLUS_CONFIG_PATH = "../../configs/kabu_plus.yaml"
SAVE_BASE_DIR = os.environ.get("SAVE_BASE_DIR")
KABU_PLUS_ID = os.environ.get("KABU_PLUS_ID")
KABU_PLUS_PW = os.environ.get("KABU_PLUS_PW")

DEFAULT_INTERVAL = 1

def validate_config_is_ready():
    if SAVE_BASE_DIR == None:
        print("SAVE_BASE_DIR is not specified")
        exit(1)
    if KABU_PLUS_ID == None:
        print("KABU_PLUS_ID is not specified")
        exit(1)
    if KABU_PLUS_PW == None:
        print("KABU_PLUS_PW is not specified")
        exit(1)


def main():
    validate_config_is_ready()

    with open(KABU_PLUS_CONFIG_PATH) as f:
        kabu_plus_config = yaml.safe_load(f)

    # Download data if new data is existing
    for key in kabu_plus_config.keys():
        config = kabu_plus_config.get(key)
        last_save_date = define_latest_saved_date(SAVE_BASE_DIR, key)

        for date in yield_date_prefix_without_holiday(last_save_date):
            client = KabuPlusClient(KABU_PLUS_ID, KABU_PLUS_PW)

            file_name = "{}_{}.csv".format(config.get("file_name_without_ext"), date)
            target_file_name = "{}/{}/{}".format(SAVE_BASE_DIR, key, file_name)
            target_url = config.get("base_url") + file_name

            print("---")
            print("{}".format(file_name))
            if not os.path.exists(target_file_name):
                time.sleep(DEFAULT_INTERVAL)
                try:
                    res = client.get(target_url)
                    print("success to download")
                    with open(target_file_name, "w+") as f:
                        f.write(res)

                except IOError:
                    print("not found")
            else:
                print("file is already existing.")

if __name__ == "__main__":
    main()