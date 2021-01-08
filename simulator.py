from common_lib import *
from stock_analyzer_lib import *
from datetime import datetime
from tqdm import tqdm

MONEY = 300000

def main():
    config = config_loader.Config()

    start_date = datetime(2018, 6, 1)
    end_date = datetime.now()

    candidates = get_candidates(start_date, config)
    all_stock_data = load_all_prices(start_date, end_date, candidates, config)

    result = {}
    for sc in candidates:
        result['win_count'] = 0
        result['lose_count'] = 0
        result[sc] = {}
        result[sc]['trading'] = []
        result[sc]['buy_timing'] = []
        result[sc]['sell_timing'] = []

    print("---- start analyzing ----")
    for sc in tqdm(candidates):
        buy_price = None

        for i in range(len(all_stock_data[sc])):
            if all_stock_data[sc][i] == None:
                continue

            data = all_stock_data[sc][:i]

            try:
                if buy_price == None and trading_analyzer.is_buy_timing_only_golden_cross(data):
                    buy_price = all_stock_data[sc][i]
                    result[sc]['buy_timing'].append((i, buy_price))
                    continue

                if buy_price != None and trading_analyzer.is_sell_timing_only_golden_cross(data):
                    sell_price = all_stock_data[sc][i]
                    diff = sell_price - buy_price

                    if diff > 0:
                        result['win_count'] += 1
                    elif diff < 0:
                        result['lose_count'] += 1

                    benefit_ratio = sell_price / buy_price
                    result[sc]['trading'].append(benefit_ratio)
                    result[sc]['sell_timing'].append((i, sell_price))

                    with open("output/{}.txt".format(sc), "+w") as f:
                        f.write("{} {} {}\n".format(buy_price, sell_price, benefit_ratio))

                    buy_price = None

            except:
                continue
    print("---- finish analyzing ----")

    print("---- creating summary ----")
    benefit_ratio_list = []
    for sc in tqdm(candidates):
        benefit_ratio_list += result[sc]['trading']

        if len(result[sc]['trading']) != 0:
            file_name = "output/{}".format(sc)
            ma5 = technical_analyzer.calc_moving_average(all_stock_data[sc], 5)
            ma25 = technical_analyzer.calc_moving_average(all_stock_data[sc], 25)
            ma75 = technical_analyzer.calc_moving_average(all_stock_data[sc], 75)

            data_list = [all_stock_data[sc], ma5, ma25, ma75]
            plot.plot_with_dots(data_list, result[sc]['buy_timing'], result[sc]['sell_timing'], file_name)

    print("#############")
    print("RESULT")
    print("Average Benefit Ratio= {}".format(sum(benefit_ratio_list)/len(benefit_ratio_list)))
    print("Win Ratio = {}".format(result["win_count"] / (result["win_count"] + result["lose_count"])))

    return


def load_all_prices(start_date, end_date, candidates, config):
    print("---- start loading all stock data ----")
    all_stock_data = {}
    for sc in candidates:
        all_stock_data[sc] = []

    for date in tqdm(date_util.yield_date_except_holiday(start_date, end_date)):
        d = data_loader.load_all_stock_data(date, config)
        if d == None:
            continue

        for sc in candidates:
            price = d[sc]['price'] if sc in d.keys() else None
            all_stock_data[sc].append(price)
    print("---- finish loading stock data ----")

    return all_stock_data


def get_candidates(start_date, config):
    target_date = None
    dt = start_date
    while True:
        if file_util.is_target_date_file_existing(config, config.financial_results_key, dt):
            target_date = dt
            break

        dt = date_util.datetime_before_num_days(dt, 1)

    financial_results = data_loader.load_all_financial_results(target_date, config)
    return fundamental_analyzer.company_candidates(financial_results)


if __name__ == "__main__":
    main()
