import numpy as np


def calculate_sma(series, sma):
    sma = series.rolling(sma).mean()
    return sma


def calculate_sma_position(sma_series_1, sma_series_2):
    position = np.where(sma_series_1 > sma_series_2, 1, -1)
    return position


def calculate_log_return(price_series, position_series):
    """log returns might be prefered for its normality properties and time additivity
    Reference
    ---------
    https://quantivity.wordpress.com/2011/02/21/why-log-returns/
    """
    log_return = np.log(price_series / price_series.shift(1)) * position_series
    return log_return


def calculate_cum_return(log_return_series):
    cum_return = log_return_series.cumsum().apply(np.exp)
    return cum_return
