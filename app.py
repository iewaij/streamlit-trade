import streamlit as st
from datetime import date
from SimpleMovingAverage import SimpleMovingAverage


def app():
    st.sidebar.title("Parameters")
    symbol = st.sidebar.selectbox(
        label="Symbol",
        options=["AAPL", "AMD", "AMZN", "BABA", "FB", "GOOG", "MSFT"],
    )
    st.title("Simple Moving Average")
    st.subheader("Backtesting")

    start = st.date_input(
        label="Start Date",
        value=date(2010, 1, 1),
        min_value=date(2010, 1, 1),
        max_value=date.today(),
    )
    end = st.date_input(
        label="End Date",
        value=date.today(),
        min_value=date(2010, 1, 1),
        max_value=date.today(),
    )
    sma_1 = st.slider(
        label="Short Period Days", min_value=1, max_value=100, step=1, value=10
    )
    sma_2 = st.slider(
        label="Long Period Days", min_value=1, max_value=100, step=1, value=50
    )
    strategy = SimpleMovingAverage(symbol, sma_1, sma_2)
    st.altair_chart(
        strategy.chart(
            start,
            end,
        ),
        use_container_width=True,
    )
    st.altair_chart(
        strategy.returns_chart(
            start,
            end,
        ),
        use_container_width=True,
    )


if __name__ == "__main__":
    app()
