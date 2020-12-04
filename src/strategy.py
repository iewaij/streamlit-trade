import numpy as np
import pandas as pd
import altair as alt
from data import get_stock_data


def simple_moving_average(series, n):
    sma = series.rolling(n).mean()
    return sma


def exponential_moving_average(series, n):
    ema_series = series.rolling(n).mean()
    return ema_series


def log_return(prices, positions):
    """log returns might be prefered for its normality properties and time additivity
    Reference
    ---------
    https://quantivity.wordpress.com/2011/02/21/why-log-returns/
    """
    log_returns = np.log(prices / prices.shift(1)) * positions
    return log_returns


def cum_return(prices, positions):
    log_returns = log_return(prices, positions)
    cum_returns = log_returns.apply(np.exp)
    return cum_returns


class BaseMovingAverage:
    def __init__(self, instruments=None, n_fast=None, n_slow=None):
        self.instruments = instruments
        self.n_fast = n_fast
        self.n_slow = n_slow
        self._prices = None
        self._positions = None
        self._returns = None

    def get_prices(self, start, end):
        data = get_stock_data(self.instruments, start, end)
        self._prices = data["Adj Close"]
        prices = self._prices
        return prices

    def check_prices(self, prices, start, end):
        if prices == None and self._prices == None:
            prices = self.get_prices(start, end)
        elif prices == None and self._prices != None:
            prices = self._prices
        return prices

    def check_positions(self, positions):
        if positions == None and self._positionss == None:
            positions = self.position()
        elif positions == None and self._positions != None:
            positions = self._positions
        return positions

    def log_return(self, prices=None, positions=None):
        prices = self.check_prices(prices)
        positions = self.check_positions(positions)

        slef._returns = log_return(prices, positions)
        returns = slef._returns

        return returns

    def cum_return(self, prices=None, positions=None):
        prices = self.check_prices(prices)
        positions = self.check_positions(positions)
        cum_return = cum_return(prices, positions)
        return cum_return

    def optimize(self, prices=None, start=None, end=None):
        pass

    def metrics(self, prices=None, positions=None, returns=None):
        pass


class SimpleMovingAverage(BaseMovingAverage):
    def margin(self, start, end, prices=None):
        prices = self.check_prices(prices, start, end)

        n_fast = self.n_fast
        n_slow = self.n_slow

        sma_1 = simple_moving_average(prices, n_fast)
        sma_2 = simple_moving_average(prices, n_slow)

        margin = sma_1 - sma_2

        return margin

    def position(self, start, end, prices=None):
        margins = self.margin(start, end, prices)

        self._positions = np.sign(margins)
        positions = self._positions

        return positions

    def strategy_chart(self, start, end, prices=None):
        prices = self.check_prices(prices, start, end)

        n_fast = self.n_fast
        n_slow = self.n_slow

        sma_1 = simple_moving_average(prices, n_fast)
        sma_2 = simple_moving_average(prices, n_slow)

        source = pd.DataFrame({"Adj Close": prices, "SMA1": sma_1, "SMA2": sma_2})
        # source = pd.DataFrame({"SMA1": sma_1, "SMA2": sma_2})
        source = (
            pd.melt(
                source,
                var_name="Indicators",
                value_name="Price",
                ignore_index=False,
            )
            .rename_axis("Date")
            .reset_index()
        )
        chart = (
            alt.Chart(source)
            .mark_line()
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(format="%Y/%m")),
                y=alt.Y("Price:Q", scale=alt.Scale(zero=False)),
                color=alt.Color(
                    "Indicators:N",
                    legend=alt.Legend(orient="top"),
                    sort=["Adj Close", "SMA1", "SMA2"],
                    scale=alt.Scale(
                        scheme="tableau20",
                    ),
                ),
            )
        )
        return chart

    def return_chart(self, start, end):
        source = self.calculate_log_return(start, end)

        chart = (
            alt.Chart(source)
            .mark_area(
                line={"color": "darkblue"},
                color=alt.Gradient(
                    gradient="linear",
                    stops=[
                        alt.GradientStop(color="white", offset=0),
                        alt.GradientStop(color="darkblue", offset=1),
                    ],
                    x1=1,
                    x2=1,
                    y1=1,
                    y2=0,
                ),
            )
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(format="%Y/%m")),
                y=alt.Y("Cum Return:Q", title="Cumulative Return"),
            )
        )
        return chart
