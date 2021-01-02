import time

from config_loader import Config
from tools.file_util import *
from tools.kabuplus_client import KabuPlusClient

DEFAULT_INTERVAL = 600


def main():
    config = Config()

    # Download data if new data is existing
    for key in config.kabu_plus_config.keys():
        last_updated_date = get_last_updated_date(config, key)
        target_key_config = config.kabu_plus_config.get(key)

        for date in yield_date_prefix_without_holiday(last_updated_date):
            client = KabuPlusClient(config.kabu_plus_id, config.kabu_plus_pw)

            file_name = generate_file_name(config.kabu_plus_config, key, date)
            target_file_path = generate_file_path(config, key, file_name)
            target_url = target_key_config.get("base_url") + file_name

            print("---")
            print("{}".format(file_name))
            if not os.path.exists(target_file_path):
                time.sleep(DEFAULT_INTERVAL)
                try:
                    res = client.get(target_url)
                    print("success to download")
                    with open(target_file_path, "w+") as f:
                        f.write(res)

                except IOError:
                    print("not found")
            else:
                print("file is already existing.")


if __name__ == "__main__":
    main()