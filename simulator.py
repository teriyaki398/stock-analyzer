from common_lib import *
from stock_analyzer_lib import *
from datetime import datetime
from tqdm import tqdm

MONEY = 300000

def main():
    config = config_loader.Config()

    start_date = datetime(2018, 1, 1)
    end_date = datetime(2019, 1, 1)

    all_stock_data = load_all_prices(start_date, end_date, config)

    result = {}
    for sc in all_stock_data.keys():
        result['win_count'] = 0
        result['lose_count'] = 0
        result[sc] = {}
        result[sc]['trading'] = []
        result[sc]['buy_timing'] = []
        result[sc]['sell_timing'] = []

    for sc in tqdm(all_stock_data.keys()):
        buy_price = None

        for i in range(len(all_stock_data[sc])):
            if all_stock_data[sc][i] == None:
                continue

            data = all_stock_data[sc][:i]

            try:
                if buy_price == None and is_buy_timing(data):
                    buy_price = all_stock_data[sc][i]
                    result[sc]['buy_timing'].append((i, buy_price))
                    continue

                if buy_price != None and is_sell_timing(data):
                    sell_price = all_stock_data[sc][i]
                    diff = sell_price - buy_price

                    if diff > 0:
                        result['win_count'] += 1
                    elif diff < 0:
                        result['lose_count'] += 1

                    stock_count = int(MONEY/buy_price)
                    benefit = diff * stock_count
                    result[sc]['trading'].append(benefit)
                    result[sc]['sell_timing'].append((i, sell_price))

                    with open("output/{}.txt".format(sc), "+w") as f:
                        f.write("{} {} {} {}\n".format(buy_price, sell_price, diff, benefit))

                    buy_price = None

            except:
                continue

    total_benefit = 0
    for sc in tqdm(all_stock_data.keys()):
        total_benefit += sum(result[sc]['trading'])

        if len(result[sc]['trading']) != 0:
            file_name = "output/{}".format(sc)
            ma5 = technical_analyzer.calc_moving_average(all_stock_data[sc], 5)
            ma25 = technical_analyzer.calc_moving_average(all_stock_data[sc], 25)
            ma75 = technical_analyzer.calc_moving_average(all_stock_data[sc], 75)

            data_list = [all_stock_data[sc], ma5, ma25, ma75]
            plot.plot_with_dots(data_list, result[sc]['buy_timing'], result[sc]['sell_timing'], file_name)

    print("#############")
    print("RESULT")
    print("Total Benefit = {}".format(total_benefit))
    print("Win Ratio = {}".format(result["win_count"] / (result["win_count"] + result["lose_count"])))

    return


def is_buy_timing(data):
    ma5 = technical_analyzer.calc_moving_average(data, 5)
    ma25 = technical_analyzer.calc_moving_average(data, 25)
    ma75 = technical_analyzer.calc_moving_average(data, 75)

    ma5_in_days = ma5[-5:]
    ma25_in_days = ma25[-5:]
    ma75_in_days = ma75[-10:]
    
    if None in ma5_in_days + ma25_in_days + ma75_in_days:
        return False

    if not technical_analyzer.is_all_prices_are_higher_than_trend(data, ma75, 10):
        return False

    if not technical_analyzer.has_one_golden_cross(ma25_in_days, ma75_in_days):
        return False

    if technical_analyzer.calc_regression_line_slope(ma25_in_days) < 0:
        return False

    if technical_analyzer.calc_regression_line_slope(ma75[-10:]) < 0:
        return False

    return True


def is_sell_timing(data):
    ma5 = technical_analyzer.calc_moving_average(data, 5)
    ma25 = technical_analyzer.calc_moving_average(data, 25)
    ma75 = technical_analyzer.calc_moving_average(data, 75)

    short_trend_in_days = ma5[-5:]
    long_trend_in_days = ma25[-5:]
    long_long_trend_in_days = ma75[-5:]

    if None in short_trend_in_days + long_trend_in_days:
        return False

    if technical_analyzer.calc_regression_line_slope(short_trend_in_days) < 0:
        return True

    if technical_analyzer.calc_regression_line_slope(long_trend_in_days) < 0:
        return True

    if technical_analyzer.calc_regression_line_slope(long_long_trend_in_days) < 0:
        return True

    if technical_analyzer.has_dead_cross(long_trend_in_days, long_long_trend_in_days):
        return True

    return False


def load_all_prices(start_date, end_date, config):
    for date in date_util.yield_date_except_holiday(start_date, end_date):
        if not file_util.is_target_date_file_existing(config, config.stock_data_key, date):
            continue
        start_date = date
        break

    start_date_stock = data_loader.load_all_stock_data(start_date, config)
    companies = list(start_date_stock.keys())

    print("---- start loading all stock data ----")
    all_stock_data = {}
    for sc in companies:
        all_stock_data[sc] = []

    for date in tqdm(date_util.yield_date_except_holiday(start_date, end_date)):
        d = data_loader.load_all_stock_data(date, config)
        if d == None:
            continue

        for sc in companies:
            price = d[sc]['price'] if sc in d.keys() else None
            all_stock_data[sc].append(price)
    print("---- finish loading stock data ----")

    return all_stock_data


if __name__ == "__main__":
    main()
