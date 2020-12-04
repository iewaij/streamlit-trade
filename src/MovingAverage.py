import pandas as pd
from data import get_stock_data
from calculate import *

def simple_moving_average(series, n):
    sma_series = series.rolling(n).mean()
    return sma_series


def exponential_moving_average(series, n):
    ema_series = series.rolling(n).mean()
    return ema_series

# def moving_average_oscillator(series, n_1, n_2):
#     positions = series_1 - series_2
#     return positions

# def moving_average_position(positions):
#     orders = np.where(positions > 0, 1, -1)
#     return orders


def calculate_log_returns(price_series, position_series):
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

class BaseMovingAverage:
    def __init__(self, instruments=None, short=None, long=None):
        self.instruments = instruments
        self.short = short
        self.long = long
        self._prices = None
        self._positions = None
        self._orders = None
        self._returns = None

    def get_prices(self, start, end):
        data = get_stock_data(self.instruments, start, end)
        self._prices = data["Adj Close"]
        prices = self._prices
        return prices

    def check_prices(self, prices, start, end):
        if prices == None and self._pricess = None:
            prices = self.get_prices(start, end)
        elif prices == None and self._prices != None:
            prices = self._prices
        return prices

    def check_positions(self, positions):
        if positions == None and self._positionss = None:
            positions = self.position()
        elif positions == None and self._positions != None:
            positions = self._positions
        return positions
    
    def check_orders(self, orders):
        if orders == None and self._orderss = None:
            orders = self.order()
        elif orders == None and self._orders != None:
            orders = self._orders
        return orders

    def check_returns(self, returns, start, end):
        if returns == None and self._returnss = None:
            returns = self.calculate_returns(start, end)
        elif returns == None and self._returns != None:
            returns = self._returns
        return returns

    def calculate_returns(self, prices=None, orders=None, start, end):
        prices = self.check_prices(prices, start, end)
        orders = self.check_orders(orders, start, end)
        
        slef._returns = calculate_log_return(prices, orders)
        returns = slef._returns

        return returns

    def optimize(self, prices=None, start=None, end=None):
        pass

    def metrics(self, prices=None, positions=None, returns=None, start, end):
        returns = self.check_returns(returns, start, end)
    
        cum_returns = calculate_cum_return(returns)
        sharpe = calculate_sharpe(returns)
        return cum_returns

class SimpleMovingAverage(BaseMovingAverage):
    def position(self, prices=None, start, end):
        prices = self.check_prices(prices)

        short = self.short
        long = self.long

        sma_series_1 = simple_moving_average(prices, self.short)
        sma_series_2 = simple_moving_average(prices, self.long)

        self._positions = calculate_ma_positionss(sma_series_1, sma_series_2)
        positions = self._positions

        return positions

    def order(self, prices=None, positions=None, start, end):
        # TODO: add shift terms
        positions = self.check_positions()
        self._orders = calculate_ma_orders(positions)
        orders = self._orders

        return orders


class ExponentialMovingAverage(BaseMovingAverage):
    def oscillate(self, prices=None, start, end):
        prices = self.check_prices(prices)

        short = self.short
        long = self.long

        ema_series_1 = calculate_ema(prices, self.short)
        ema_series_2 = calculate_ema(prices, self.long)

        self._positions = calculate_ma_positions(ema_series_1, ema_series_2)
        positions = self._positions

        return positions

    def order(self, prices=None, positions=None, start, end):
        # TODO: add shift terms
        positions = self.check_positions()
        self._orders = calculate_ma_orders(positions)
        orders = self._orders

        return orders
