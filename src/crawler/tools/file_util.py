import os
import re
from datetime import datetime
from datetime import timedelta
from pathlib import Path

"""
start_date: YYYYMMdd
"""
def yield_date_prefix(start_date):
    start_dt = datetime.strptime(start_date, '%Y%m%d')
    end_dt = datetime.now()

    total_days = (end_dt - start_dt).days + 1

    for i in range(total_days):
        next = start_dt + timedelta(i)
        yield next.strftime("%Y%m%d")


"""
start_date: YYYYMMdd
"""
def yield_date_prefix_without_holiday(start_date):
    start_dt = datetime.strptime(start_date, '%Y%m%d')
    end_dt = datetime.now()

    total_days = (end_dt - start_dt).days + 1

    for i in range(total_days):
        next = start_dt + timedelta(i)
        if next.weekday() == 5 or next.weekday() == 6:
            continue
        else:
            yield next.strftime("%Y%m%d")


def define_latest_saved_date(base_dir, key):
    path = Path(base_dir, key)

    files = os.listdir(str(path))
    files.sort()
    last_file = files[-1]

    last_date = re.search(r"\d{8}", last_file).group()
    return last_date