from MovingAverage import SimpleMovingAverage

# strategies as class
sma_aapl = SimpleMovingAverage("AAPL")
# stragegies accept multiple instruments
sma_faang = SimpleMovingAverage(["FB", "AAPL", "AMZN", "NFLX", "GOOG"])
sma_aapl.set_params(10, 60)
sma_aapl.backtest.metrics()
sma_aapl.backtest.sharpe()
sma_aapl.backtest.strategy_chart()
sma_aapl.backtest.return_chart()
# strategies can be optimized according to metrics and sampling method
sma_aapl.backtest.optimize(metric="sharpe")
sma_aapl.backtest.optimize(metric="sharpe", sampling="rolling")
# strategies accept customised data (prices) or retrive data mannualy
sma_aapl.backtest.metrics(prices)
sma_aapl.backtest.strategy_chart()
sma_aapl.backtest.return_chart()
# strategies can be used for paper or live trading
sma_aapl.trade(budget=1000, broker="ib")
sma_aapl.trade.metrics()
sma_aapl.trade.strategy_chart()
sma_aapl.trade.return_chart()
# strategies can be stacked into a portofolio with optimized weights
portofolio = Portofolio(strategies=[sma_aapl, sma_faang], budget=10000)
portofolio.backtest.optimize()
portofolio.backtest.metrics()
portofolio.backtest.frontier_chart()
portofolio.trade.strategy_chart()
portofolio.trade.return_chart()
portofolio.trade()
