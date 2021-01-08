
"""
Return moving average line in given days
"""
def calc_moving_average(data, days):
    result = []
    for i in range(len(data)):
        d = data[i-days:i]
        if len(d) != days or None in d:
            result.append(None)
        else:
            result.append(sum(d)/days)
    return result


"""
Check it contains only one golden cross.
"""
def has_one_golden_cross(short_trend, long_trend):
    diff = [short_trend[i] - long_trend[i] for i in range(len(short_trend))]

    positive_inversion_count = 0
    for i in range(len(diff)):
        if i == 0:
            continue
        if diff[i] >= 0 and diff[i-1] < 0:
            positive_inversion_count += 1
    if positive_inversion_count == 1:
        return True
    else:
        return False

"""
Check it contains only one dead cross.
"""
def has_dead_cross(short_trend, long_trend):
    diff = [short_trend[i] - long_trend[i] for i in range(len(short_trend))]

    positive_inversion_count = 0
    for i in range(len(diff)):
        if i == 0:
            continue
        if diff[i] < 0 and diff[i-1] >= 0:
            positive_inversion_count += 1
    if positive_inversion_count > 0:
        return True
    else:
        return False


"""
Return true if all prices are higher than each prices of trend
"""
def is_all_prices_are_higher_than_trend(prices, trend, days):
    prices_in_days = prices[-1*days:]
    trend_in_days = trend[-1*days:]
    if None in prices_in_days or None in trend_in_days:
        return False

    diff = [prices_in_days[i] - trend_in_days[i] for i in range(days)]

    for d in diff:
        if d < 0:
            return False
    return True


"""
Return regression line (回帰直線) calculated by least square method
x, y: list
"""
def calc_regression_line(x_list, y_list):
    n = len(x_list)
    x_ave = sum(x_list) / n
    y_ave = sum(y_list) / n

    x_dispersion = sum([(xi - x_ave)**2 for xi in x_list]) / n
    covariance = sum([(xi - x_ave)*(yi - y_ave) for xi, yi in zip(x_list, y_list)]) / n

    a = covariance / x_dispersion
    b = y_ave - (a * x_ave)
    def f(x):
        return a*x + b

    return [f(x) for x in x_list]


"""
Return trend (slope a)
"""
def calc_regression_line_slope(data):
    if None in data:
        return None

    x_list = list(range(len(data)))
    y_list = data

    n = len(x_list)
    x_ave = sum(x_list) / n
    y_ave = sum(y_list) / n

    x_dispersion = sum([(xi - x_ave) ** 2 for xi in x_list]) / n
    covariance = sum([(xi - x_ave) * (yi - y_ave) for xi, yi in zip(x_list, y_list)]) / n

    return covariance / x_dispersion