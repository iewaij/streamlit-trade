class Accessor:
    """
    References
    ----------
    Descriptor HowTo Guide, https://docs.python.org/3/howto/descriptor.html
    """

    def __init__(self, accessor):
        self._accessor = accessor

    def __get__(self, obj, objtype=None):
        return self._accessor(obj)


class Backtest:
    """
    Parameters
    ----------
    strategy : Strategy
        The object for which the backtest is called.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def show_symbol(self):
        print(self._strategy.symbol)


class Trade:
    """
    Parameters
    ----------
    strategy : Strategy
        The object for which the trade is called.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def show_symbol(self):
        print(self._strategy.symbol)


class Strategy:
    def __init__(self, symbol=None, n_fast=None, n_slow=None):
        self.symbol = symbol
        self.n_fast = n_fast
        self.n_slow = n_slow

    backtest = Accessor(Backtest)
    trade = Accessor(Trade)
    # backtest = Backtest(self)
    # trade = Trade(self)


sma = Strategy("AAPL", 3, 10)
sma.backtest.show_symbol()
sma.trade.show_symbol()
