import altair as alt
import pandas as pd
from data import import_stock_data
from calculate import *


class SimpleMovingAverage:
    def __init__(self, symbol, sma_1, sma_2):
        self.symbol = symbol
        self.sma_1 = sma_1
        self.sma_2 = sma_2
        self.load_data()
        self.run()

    def load_data(self):
        self.data = import_stock_data(self.symbol)

    def run(self):
        price_series = self.data["Adj Close"]
        self.data = self.data.assign(
            SMA1=calculate_sma(price_series, self.sma_1),
            SMA2=calculate_sma(price_series, self.sma_2),
        ).dropna()
        self.data["Position"] = calculate_sma_position(
            self.data["SMA1"], self.data["SMA2"]
        )
        # self.data["Position"] = self.data["Position"].shift(1)

    def returns(self, start=None, end=None):
        returns = self.data.loc[start:end, ["Adj Close", "Position"]]
        returns["Log Return"] = calculate_log_return(
            returns["Adj Close"], returns["Position"]
        )
        returns["Cum Return"] = calculate_cum_return(returns["Log Return"])
        return returns

    def returns_chart(self, start=None, end=None):
        returns = self.returns(start, end).rename_axis("Date").reset_index()
        returns_chart = (
            alt.Chart(returns)
            .mark_area(
                line={"color": "darkgreen"},
                color=alt.Gradient(
                    gradient="linear",
                    stops=[
                        alt.GradientStop(color="white", offset=0),
                        alt.GradientStop(color="darkgreen", offset=1),
                    ],
                    x1=1,
                    x2=1,
                    y1=1,
                    y2=0,
                ),
            )
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(format="%Y/%m/%d")),
                y=alt.Y("Cum Return:Q", title="Cumulative Return"),
            )
        )
        return returns_chart

    def chart(self, start=None, end=None):
        sma_source = (
            pd.melt(
                self.data.loc[start:end, ["SMA1", "SMA2"]],
                var_name="Indicators",
                value_name="Price",
                ignore_index=False,
            )
            .rename_axis("Date")
            .reset_index()
        )
        sma_chart = (
            alt.Chart(sma_source)
            .mark_line()
            .encode(
                x=alt.X("Date:T", axis=alt.Axis(format="%Y/%m/%d")),
                y=alt.Y("Price:Q", scale=alt.Scale(zero=False)),
                color=alt.Color(
                    "Indicators:N",
                    legend=alt.Legend(orient="top"),
                    sort=["SMA1", "SMA2"],
                ),
            )
        )
        return sma_chart

    def metrics(self, start=None, end=None):
        pass
