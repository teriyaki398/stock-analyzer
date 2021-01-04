def convert_raw_stock_data_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # sc
    result["company_name"] = data[1]  # 名称
    result["market"] = data[2]  # 市場
    result["business_category"] = data[3]  # 業種
    result["datetime"] = data[4]  # 日時 2020/01/01 00:00:00
    result["price"] = convert_to_float(data[5])  # 株価
    result["ratio_with_yesterday"] = convert_to_float(data[6])  # 前日比
    result["ratio_with_yesterday_percent"] = convert_to_float(data[7])  # 前日比 %
    result["end_price_yesterday"] = convert_to_float(data[8])  # 前日終値
    result["start_price"] = convert_to_float(data[9])  # 始値
    result["highest_price"] = convert_to_float(data[10])  # 高値
    result["lowest_price"] = convert_to_float(data[11])  # 安値
    result["stock_trading_volume"] = convert_to_float(data[12])  # 出来高
    result["stock_trading_value"] = convert_to_float(data[13])  # 売買代金
    result["market_capitalization"] = convert_to_float(data[14])  # 時価総額
    result["lower_limit_price_range"] = convert_to_float(data[15])  # 値幅下限
    result["upper_limit_price_range"] = convert_to_float(data[16])  # 値幅上限
    return result


def convert_raw_stock_variation_data_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # "SC"
    result["company_name"] = data[1]  # "名称"
    result["market"] = data[2]  # "市場"
    result["business_category"] = data[3]  # "業種"
    result["market_capitalization"] = convert_to_float(data[4])  # "時価総額（百万円）"
    result["outstanding_shares_number"] = convert_to_float(data[5])  # "発行済株式数"
    result["dividend_yield"] = convert_to_float(data[6])  # "配当利回り"
    result["dividend"] = convert_to_float(data[7])  # "1株配当"
    result["per"] = convert_to_float(data[8])  # "PER（予想）"
    result["pbr"] = convert_to_float(data[9])  # "PBR（実績）"
    result["eps"] = convert_to_float(data[10])  # "EPS（予想）"
    result["bps"] = convert_to_float(data[11])  # "BPS（実績）"
    result["minimum_perchase_price"] = convert_to_float(data[12])  # "最低購入額"
    result["unit_share"] = convert_to_float(data[13])  # "単元株"
    result["highest_price_date"] = data[14]  # "高値日付"
    result["highest_price_in_this_year"] = convert_to_float(data[15])  # "年初来高値"
    result["lowest_price_date"] = data[16]  # "安値日付"
    result["lowest_price_in_this_year"] = convert_to_float(data[17])  # "年初来安値"
    return result


def convert_raw_financial_results_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # SC
    result["company_name"] = data[1]  # 名称
    result["settlement_season"] = data[2]  # 決算期
    result["settlement_report_date"] = data[3]  # 決算発表日(本決算)
    result["sales_amount"] = convert_to_float(data[4])  # 売上高
    result["operating_income"] = convert_to_float(data[5])  # 営業利益
    result["ordinary_income"] = convert_to_float(data[6])  # 経常利益
    result["net_income"] = convert_to_float(data[7])  # 当期利益
    result["total_assets"] = convert_to_float(data[8])  # 総資産
    result["net_worth"] = convert_to_float(data[9])  # 自己資本
    result["capital"] = convert_to_float(data[10])  # 資本金
    result["interest_bearing_debt"] = convert_to_float(data[11])  # 有利子負債
    result["equity_ratio"] = convert_to_float(data[12])  # 自己資本比率
    result["ROE"] = convert_to_float(data[13])  # ROE
    result["ROA"] = convert_to_float(data[14])  # ROA
    result["outstanding_shares_number"] = convert_to_float(data[15])  # 発行済株式数
    return result


def convert_to_float(value):
    if value == "-":
        return None
    try:
        return float(value)
    except ValueError:
        return None