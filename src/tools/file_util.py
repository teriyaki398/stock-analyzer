import os
import re
from datetime import datetime
from datetime import timedelta
from pathlib import Path


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


"""
if given file name is like this; file_20200801.csv
then return 202008
"""
def get_saved_month_by_file_name(file_name):
    month = re.search(r"20[1-2][0-9][0-1][0-9]", file_name)
    if month != None:
        return month.group()
    return month


"""
if given file name is like this; file_20200801.csv
then return 20200801
"""
def get_saved_date_by_file_name(file_name):
    date = re.search(r"20[1-2][0-9][0-1][0-9][0-3][0-9]", file_name)
    if date != None:
        return date.group()
    return date


def generate_file_name(config, key, date):
    return "{}_{}.csv".format(config.kabu_plus_config.get(key).get("file_name_without_ext"), date)


def generate_file_path(config, key, file_name):
    return "{}/{}/{}".format(config.local_resource_dir, key, file_name)