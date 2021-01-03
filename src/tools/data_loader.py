import re
from pathlib import Path

from . import file_util

STOCK_DATA_KEY = "stock_data"
STOCK_VARIATION_DATA_KEY = "stock_variation_data"
FINANCIAL_RESULTS_KEY = "financial_results"


"""
Return stock data of given date_str and given sc
date_str: YYYYMMdd
"""
def load_stock_data_by_sc(sc, date_str, config):
    data = load_target_date_data_of_key(date_str, config, STOCK_DATA_KEY)
    if data == None:
        return None

    selected_data = select_data_by_sc(sc, data)
    if selected_data == None:
        return None

    result = {}
    result["sc"] = selected_data[0] # sc
    result["company_name"] = selected_data[1]   # 名称
    result["market"] = selected_data[2]     # 市場
    result["business_category"] = selected_data[3]  # 業種
    result["datetime"] = selected_data[4]   # 日時 2020/01/01 00:00:00
    result["prices"] = selected_data[5]  # 株価
    result["ratio_with_yesterday"] = selected_data[6]    # 前日比
    result["ratio_with_yesterday_percent"] = selected_data[7]    # 前日比 %
    result["end_price_yesterday"] = selected_data[8]    # 前日終値
    result["start_price"] = selected_data[9]    # 始値
    result["highest_price"] = selected_data[10]    # 高値
    result["lowest_price"] = selected_data[11]    # 安値
    result["stock_trading_volume"] = selected_data[12]    # 出来高
    result["stock_trading_value"] = selected_data[13]    # 売買代金
    result["market_capitalization"] = selected_data[14]    # 時価総額
    result["lower_limit_price_range"] = selected_data[15]    # 値幅下限
    result["upper_limit_price_range"] = selected_data[16]    # 値幅上限

    return result


"""
Return stock variation data of given date_str and given sc
date_str: YYYYMMdd
"""
def load_stock_variation_data_by_sc(sc, date_str, config):
    data = load_target_date_data_of_key(date_str, config, STOCK_VARIATION_DATA_KEY)
    if data == None:
        return None

    selected_data = select_data_by_sc(sc, data)
    if selected_data == None:
        return None

    result = {}
    result["sc"] = selected_data[0] # "SC"
    result["company_name"] = selected_data[1]   # "名称"
    result["market"] = selected_data[2]   # "市場"
    result["business_category"] = selected_data[3]   # "業種"
    result["market_capitalization"] = selected_data[4]   # "時価総額（百万円）"
    result["outstanding_shares_number"] = selected_data[5]   # "発行済株式数"
    result["dividend_yield"] = selected_data[6]   # "配当利回り"
    result["dividend"] = selected_data[7]   # "1株配当"
    result["per"] = selected_data[8]   # "PER（予想）"
    result["pbr"] = selected_data[9]   # "PBR（実績）"
    result["eps"] = selected_data[10]  # "EPS（予想）"
    result["bps"] = selected_data[11]  # "BPS（実績）"
    result["minimum_perchase_price"] = selected_data[12]  # "最低購入額"
    result["unit_share"] = selected_data[13]  # "単元株"
    result["highest_price_date"] = selected_data[14]  # "高値日付"
    result["highest_price_in_this_year"] = selected_data[15]  # "年初来高値"
    result["lowest_price_date"] = selected_data[16]  # "安値日付"
    result["lowest_price_in_this_year"] = selected_data[17]  # "年初来安値"
    return result


"""
Return financial results data of given date_str and given sc
"""
def load_financial_results_by_sc(sc, date_str, config):
    data = load_target_month_data_of_key(date_str, config, FINANCIAL_RESULTS_KEY)
    if data == None:
        return None

    selected_data = select_data_by_sc(sc, data)
    if selected_data == None:
        return None

    result = {}
    result["sc"] = selected_data[0] # SC
    result["company_name"] = selected_data[1]   # 名称
    result["settlement_season"] = selected_data[2]  # 決算期
    result["settlement_report_date"] = selected_data[3] # 決算発表日(本決算)
    result["sales_amount"] = selected_data[4]       # 売上高
    result["operating_income"] = selected_data[5]   # 営業利益
    result["ordinary_income"] = selected_data[6]    # 経常利益
    result["net_income"] = selected_data[7]     # 当期利益
    result["total_assets"] = selected_data[8]   # 総資産
    result["net_worth"] = selected_data[9]       # 自己資本
    result["capital"] = selected_data[10]    # 資本金
    result["interest_bearing_debt"] = selected_data[11]    # 有利子負債
    result["equity_ratio"] = selected_data[12]    # 自己資本比率
    result["ROE"] = selected_data[13]    # ROE
    result["ROA"] = selected_data[14]    # ROA
    result["outstanding_shares_number"] = selected_data[15]    # 発行済株式数

    return result


"""
Return all data contained in file specified by key and date
"""
def load_target_date_data_of_key(date_str, config, key):
    target_file_name = search_target_date_file_by_key(date_str, config, key)
    if target_file_name == None:
        return None

    path = Path(config.local_resource_dir, key, target_file_name)

    with open(str(path)) as f:
        data = f.read().split("\n")

    return data


"""
Return all data contained in specified month file
"""
def load_target_month_data_of_key(date_str, config, key):
    target_file_name = search_target_month_file_by_key(date_str, config, key)
    if target_file_name == None:
        return None

    path = Path(config.local_resource_dir, key, target_file_name)
    with open(str(path)) as f:
        data = f.read().split("\n")

    return data


"""
Search file contained in key directory by specified date_str
"""
def search_target_date_file_by_key(date_str, config, key):
    all_file_list = file_util.get_all_file_list_by_key(config, key)
    for file_name in all_file_list:
        if date_str == file_util.get_saved_date_by_file_name(file_name):
            return file_name
    return None


"""
Search file contained in key directory by specified date_str
Return the first file whose month is matched
"""
def search_target_month_file_by_key(date_str, config, key):
    m = re.search(r"20[1-2][0-9][0-1][0-9]", date_str)
    if m == None:
        return None

    month_str = m.group()
    all_file_list = file_util.get_all_file_list_by_key(config, key)

    for file_name in all_file_list:
        if month_str == file_util.get_saved_month_by_file_name(file_name):
            return file_name
    return None


"""
return list data extracted by sc
"""
def select_data_by_sc(sc, all_data_list):
    for data_str in all_data_list:
        data = [d.replace('"', '') for d in data_str.split(",")]
        if str(sc) == data[0]:
            return data
