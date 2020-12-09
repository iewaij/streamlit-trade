class CachedAccessor:
    def __init__(self, name, accessor):
        self._name = name
        self._accessor = accessor

    def __get__(self, obj, cls):
        if obj is None:
            return self._accessor
        accessor_obj = self._accessor(obj)
        object.__setattr__(obj, self._name, accessor_obj)
        return accessor_obj


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

    backtest = CachedAccessor("backtest", Backtest)
    trade = CachedAccessor("trade", Trade)


sma = Strategy("AAPL", 3, 10)
sma.backtest.show_symbol()
sma.trade.show_symbol()
