import streamlit as st
from datetime import date
from strategy import SimpleMovingAverage


def app():
    st.sidebar.title("Backtest")
    symbol = st.sidebar.selectbox(
        label="Symbol",
        options=["AAPL", "AMD", "AMZN", "BABA", "FB", "GOOG", "MSFT"],
    )
    st.title("Simple Moving Average")

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
    n_fast = st.slider(
        label="Fast Period", min_value=1, max_value=100, step=1, value=10
    )
    n_slow = st.slider(
        label="Slow Period", min_value=1, max_value=100, step=1, value=50
    )
    strategy = SimpleMovingAverage(symbol, n_fast, n_slow)
    # st.altair_chart(
    #     strategy.strategy_chart(
    #         start,
    #         end,
    #     ),
    #     use_container_width=True,
    # )
    # st.table(strategy.log_return(start, end))
    # st.altair_chart(
    #     strategy.return_chart(
    #         start,
    #         end,
    #     ),
    #     use_container_width=True,
    # )
    # st.table(strategy.position(start, end))
    # st.table(strategy.margin(start, end))
    # st.altair_chart(
    #     strategy.returns_chart(
    #         start,
    #         end,
    #     ),
    #     use_container_width=True,
    # )


if __name__ == "__main__":
    app()
