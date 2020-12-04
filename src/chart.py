import altair as alt


def returns_chart(self, start=None, end=None):
    returns = self.check_returns(returns)
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


def sma_chart(self, start=None, end=None):
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
