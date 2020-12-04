import pandas as pd
import pandas_datareader.data as web
from datetime import timedelta, datetime, date
import requests_cache


def get_stock_data(symbols, start=datetime(2010, 1, 1), end=date.today()):
    expire_after = timedelta(days=1)
    session = requests_cache.CachedSession(
        cache_name="cache", backend="sqlite", expire_after=expire_after
    )
    data = web.DataReader(symbols, "yahoo", start, end, session=session)
    return data
