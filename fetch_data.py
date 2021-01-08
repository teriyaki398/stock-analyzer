import os
from datetime import datetime

from common_lib import config_loader, date_util, file_util
from common_lib.kabuplus_client import KabuPlusClient


def main():
    config = config_loader.Config()

    # Download data if new data is existing
    for key in config.kabu_plus_config.keys():
        last_updated_date = file_util.get_last_updated_date(config, key)
        print("Start downloading {}. last updated = {}".format(key, last_updated_date))

        target_key_config = config.kabu_plus_config.get(key)
        start_date = date_util.datetime_after_num_days(last_updated_date, 1)

        for date in date_util.yield_date_except_holiday(start_date, datetime.now()):
            client = KabuPlusClient(config.kabu_plus_id, config.kabu_plus_pw)

            date_prefix = date_util.datetime_to_date_str(date)
            file_name = file_util.generate_file_name(config, key, date_prefix)
            target_file_path = file_util.generate_file_path(config, key, file_name)
            target_url = target_key_config.get("base_url") + file_name

            print("---")
            print("{}".format(file_name))
            if not os.path.exists(target_file_path):
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