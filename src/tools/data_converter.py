def convert_raw_stock_data_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # sc
    result["company_name"] = data[1]  # 名称
    result["market"] = data[2]  # 市場
    result["business_category"] = data[3]  # 業種
    result["datetime"] = data[4]  # 日時 2020/01/01 00:00:00
    result["price"] = data[5]  # 株価
    result["ratio_with_yesterday"] = data[6]  # 前日比
    result["ratio_with_yesterday_percent"] = data[7]  # 前日比 %
    result["end_price_yesterday"] = data[8]  # 前日終値
    result["start_price"] = data[9]  # 始値
    result["highest_price"] = data[10]  # 高値
    result["lowest_price"] = data[11]  # 安値
    result["stock_trading_volume"] = data[12]  # 出来高
    result["stock_trading_value"] = data[13]  # 売買代金
    result["market_capitalization"] = data[14]  # 時価総額
    result["lower_limit_price_range"] = data[15]  # 値幅下限
    result["upper_limit_price_range"] = data[16]  # 値幅上限
    return result


def convert_raw_stock_variation_data_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # "SC"
    result["company_name"] = data[1]  # "名称"
    result["market"] = data[2]  # "市場"
    result["business_category"] = data[3]  # "業種"
    result["market_capitalization"] = data[4]  # "時価総額（百万円）"
    result["outstanding_shares_number"] = data[5]  # "発行済株式数"
    result["dividend_yield"] = data[6]  # "配当利回り"
    result["dividend"] = data[7]  # "1株配当"
    result["per"] = data[8]  # "PER（予想）"
    result["pbr"] = data[9]  # "PBR（実績）"
    result["eps"] = data[10]  # "EPS（予想）"
    result["bps"] = data[11]  # "BPS（実績）"
    result["minimum_perchase_price"] = data[12]  # "最低購入額"
    result["unit_share"] = data[13]  # "単元株"
    result["highest_price_date"] = data[14]  # "高値日付"
    result["highest_price_in_this_year"] = data[15]  # "年初来高値"
    result["lowest_price_date"] = data[16]  # "安値日付"
    result["lowest_price_in_this_year"] = data[17]  # "年初来安値"
    return result


def convert_raw_financial_results_list_to_dict(data):
    result = {}
    result["sc"] = data[0]  # SC
    result["company_name"] = data[1]  # 名称
    result["settlement_season"] = data[2]  # 決算期
    result["settlement_report_date"] = data[3]  # 決算発表日(本決算)
    result["sales_amount"] = data[4]  # 売上高
    result["operating_income"] = data[5]  # 営業利益
    result["ordinary_income"] = data[6]  # 経常利益
    result["net_income"] = data[7]  # 当期利益
    result["total_assets"] = data[8]  # 総資産
    result["net_worth"] = data[9]  # 自己資本
    result["capital"] = data[10]  # 資本金
    result["interest_bearing_debt"] = data[11]  # 有利子負債
    result["equity_ratio"] = data[12]  # 自己資本比率
    result["ROE"] = data[13]  # ROE
    result["ROA"] = data[14]  # ROA
    result["outstanding_shares_number"] = data[15]  # 発行済株式数
    return result