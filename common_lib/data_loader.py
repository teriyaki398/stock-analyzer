import re
from pathlib import Path

from common_lib import date_util, data_converter, file_util

STOCK_DATA_KEY = "stock_data"
STOCK_VARIATION_DATA_KEY = "stock_variation_data"
FINANCIAL_RESULTS_KEY = "financial_results"

SC_KEY = "sc"

def load_all_stock_data(date, config):
    all_data = load_target_date_data_by_key(date, config, STOCK_DATA_KEY)
    if all_data == None:
        return None

    result = {}
    for data in all_data:
        d = data_converter.convert_raw_stock_data_list_to_dict(data)
        if str.isdecimal(d[SC_KEY]):
            result[d[SC_KEY]] = d
    return result


def load_all_stock_variation_data(date, config):
    all_data = load_target_date_data_by_key(date, config, STOCK_VARIATION_DATA_KEY)
    if all_data == None:
        return None

    result = {}
    for data in all_data:
        d = data_converter.convert_raw_stock_variation_data_list_to_dict(data)
        if str.isdecimal(d[SC_KEY]):
            result[d[SC_KEY]] = d
    return result


def load_all_financial_results(date, config):
    all_data = load_target_month_data_of_key(date, config, FINANCIAL_RESULTS_KEY)
    if all_data == None:
        return None

    result = {}
    for data in all_data:
        d = data_converter.convert_raw_financial_results_list_to_dict(data)
        if str.isdecimal(d[SC_KEY]):
            result[d[SC_KEY]] = d
    return result


def load_sc_stock_data(sc, date, config):
    all_data = load_all_stock_data(date, config)
    try:
        return all_data[str(sc)]
    except Exception:
        return None


def load_sc_stock_variation_data(sc, date, config):
    all_data = load_all_stock_variation_data(date, config)
    try:
        return all_data[str(sc)]
    except Exception:
        return None


def load_sc_financial_results_data(sc, date, config):
    all_data = load_all_financial_results(date, config)
    try:
        return all_data[str(sc)]
    except Exception:
        return None


"""
Return all data contained in file specified by key and date
"""
def load_target_date_data_by_key(date, config, key):
    target_file_name = search_target_date_file_by_key(date, config, key)
    if target_file_name == None:
        return None

    path = Path(config.local_resource_dir, key, target_file_name)
    with open(str(path)) as f:
        data_str_list = f.read().split("\n")

    result = []
    for data_str in data_str_list:
        if data_str != "":
            result.append([d.replace('"', '') for d in data_str.split(",")])
    return result


"""
Return all data contained in specified month file
"""
def load_target_month_data_of_key(date, config, key):
    target_file_name = search_target_month_file_by_key(date, config, key)
    if target_file_name == None:
        return None

    path = Path(config.local_resource_dir, key, target_file_name)
    with open(str(path)) as f:
        data_str_list = f.read().split("\n")

    result = []
    for data_str in data_str_list:
        if data_str != "":
            result.append([d.replace('"', '') for d in data_str.split(",")])
    return result


"""
Search file contained in key directory by specified date_str
"""
def search_target_date_file_by_key(date, config, key):
    all_file_list = file_util.get_all_file_list_by_key(config, key)
    for file_name in all_file_list:
        if date == file_util.get_saved_date_by_file_name(file_name):
            return file_name
    return None


"""
Search file contained in key directory by specified date_str
Return the first file whose month is matched
"""
def search_target_month_file_by_key(date, config, key):
    date_str = date_util.datetime_to_date_str(date)
    m = re.search(r"20[1-2][0-9][0-1][0-9]", date_str)
    if m == None:
        return None

    month_str = m.group()
    all_file_list = file_util.get_all_file_list_by_key(config, key)

    for file_name in all_file_list:
        if month_str == file_util.get_saved_month_by_file_name(file_name):
            return file_name
    return None