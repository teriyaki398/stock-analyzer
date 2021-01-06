from datetime import datetime
from datetime import timedelta

DATE_FORMAT = "%Y%m%d"

def date_str_to_datetime(date_str):
    return datetime.strptime(date_str, DATE_FORMAT)


def datetime_to_date_str(dt):
    return dt.strftime(DATE_FORMAT)


def datetime_before_num_days(dt, days):
    return dt - timedelta(days=days)


def yield_date_prefix_except_holiday(start_dt, end_dt):
    total_days = (end_dt - start_dt).days + 1

    for i in range(total_days):
        next = start_dt + timedelta(i)
        if next.weekday() == 5 or next.weekday() == 6:
            continue
        else:
            yield next