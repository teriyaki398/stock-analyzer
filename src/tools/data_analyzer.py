def calc_moving_average(data, days):
    result = []
    for i in range(len(data)):
        d = data[i-days:i]
        if len(d) != days:
            result.append(None)
        else:
            result.append(sum(d)/days)
    return result


def average_slope():
    return 0