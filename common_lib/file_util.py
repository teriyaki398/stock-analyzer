import os
import re
from pathlib import Path

from common_lib import date_util

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
    file_list.sort()
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
    m_date = re.search(r"20[1-2][0-9][0-1][0-9][0-3][0-9]", file_name)
    if m_date != None:
        date_str = m_date.group()
        return date_util.date_str_to_datetime(date_str)
    return m_date


def is_target_date_file_existing(config, key, date):
    date_prefix = date_util.datetime_to_date_str(date)
    file_name = generate_file_name(config, key, date_prefix)
    file_path = generate_file_path(config, key, file_name)
    return os.path.exists(file_path)


def generate_file_name(config, key, date_prefix):
    return "{}_{}.csv".format(config.kabu_plus_config.get(key).get("file_name_without_ext"), date_prefix)


def generate_file_path(config, key, file_name):
    return "{}/{}/{}".format(config.local_resource_dir, key, file_name)