import pandas as pd

def backtest(portfolio, returns):
    portfolio_returns = (returns * portfolio.weights).sum(axis=1)
    cumulative_returns = (1 + portfolio_returns).cumprod()
    return cumulative_returns
