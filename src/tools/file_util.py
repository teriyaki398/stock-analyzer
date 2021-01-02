import os
import re
from datetime import datetime
from datetime import timedelta
from pathlib import Path

"""
start_date: YYYYMMdd
"""
def yield_date_prefix(start_date):
    start_dt = datetime.strptime(start_date, '%Y%m%d')
    end_dt = datetime.now()

    total_days = (end_dt - start_dt).days + 1

    for i in range(total_days):
        next = start_dt + timedelta(i)
        yield next.strftime("%Y%m%d")


"""
start_date: YYYYMMdd
"""
def yield_date_prefix_without_holiday(start_date):
    start_dt = datetime.strptime(start_date, '%Y%m%d')
    end_dt = datetime.now()

    total_days = (end_dt - start_dt).days + 1

    for i in range(total_days):
        next = start_dt + timedelta(i)
        if next.weekday() == 5 or next.weekday() == 6:
            continue
        else:
            yield next.strftime("%Y%m%d")


"""
return list of all files contained in key directory
"""
def get_all_file_list_by_key(config, key):
    resource_dir_path = config.local_resource_dir
    dir_path = Path(resource_dir_path, key)
    return os.listdir(str(dir_path))


"""
return latest file contained in key directory
"""
def get_latest_file_name(config, key):
    file_list = get_all_file_list_by_key(config, key)
    return file_list[-1]


"""
return last updated date extracted by file prefix
"""
def get_last_updated_date(config, key):
    latest_file_name = get_latest_file_name(config, key)
    return get_saved_date_by_file_name(latest_file_name)


def get_saved_date_by_file_name(file_name):
    date = re.search(r"\d{8}", file_name)
    if date != None:
        return date.group()
    return date


def generate_file_name(config, key, date):
    return "{}_{}.csv".format(config.kabu_plus_config.get(key).get("file_name_without_ext"), date)


def generate_file_path(config, key, file_name):
    return "{}/{}/{}".format(config.local_resource_dir, key, file_name)