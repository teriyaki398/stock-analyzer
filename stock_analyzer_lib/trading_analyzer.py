from . import technical_analyzer


def is_buy_timing(data):
    ma5 = technical_analyzer.calc_moving_average(data, 5)
    ma25 = technical_analyzer.calc_moving_average(data, 25)
    ma75 = technical_analyzer.calc_moving_average(data, 75)

    ma5_in_days = ma5[-5:]
    ma25_in_days = ma25[-10:]
    ma75_in_days = ma75[-20:]

    if None in ma5_in_days + ma25_in_days + ma75_in_days:
        return False

    if not technical_analyzer.is_all_prices_are_higher_than_trend(data[-5:], ma5_in_days):
        return False

    if not technical_analyzer.has_one_golden_cross(ma25_in_days[-3:], ma75_in_days[-3:]):
        return False

    if technical_analyzer.calc_regression_line_slope(ma25_in_days) < 0:
        return False

    if technical_analyzer.calc_regression_line_slope(ma75_in_days) < 0:
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

    # if technical_analyzer.calc_regression_line_slope(short_trend_in_days) < 0:
    #     return True

    if technical_analyzer.calc_regression_line_slope(long_trend_in_days) < 0:
        return True

    if technical_analyzer.calc_regression_line_slope(long_long_trend_in_days) < 0:
        return True

    if technical_analyzer.has_dead_cross(short_trend_in_days, long_trend_in_days):
        return True

    if technical_analyzer.has_dead_cross(long_trend_in_days, long_long_trend_in_days):
        return True

    return False
