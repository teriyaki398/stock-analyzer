from . import file_util
from pathlib import Path

STOCK_DATA_KEY = "stock_data"
STOCK_VARIATION_DATA_KEY = "stock_variation_data"
FINANCIAL_RESULTS_KEY = "financial_results"



"""
Return financial results data of given date_str and given sc
"""
def load_financial_results_by_sc(sc, date_str, config):
    target_file_name = search_target_date_str_file_name_by_key(date_str, config, FINANCIAL_RESULTS_KEY)
    if target_file_name == None:
        return None

    path = Path(config.local_resource_dir, FINANCIAL_RESULTS_KEY, target_file_name)

    with open(str(path)) as f:
        data = f.read().split("\n")

    selected_data = select_data_by_sc(sc, data)

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
Search file contained in key directory by specified date_str
"""
def search_target_date_str_file_name_by_key(date_str, config, key):
    all_file_list = file_util.get_all_file_list_by_key(config, key)
    for file_name in all_file_list:
        if date_str == file_util.get_saved_date_by_file_name(file_name):
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
