import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

sec_returns = np.log(sec_data / sec_data.shift(1))

print("SEC RETURNS:", sec_returns)

################################# CALCULANDO RISCO PORTFOLIO #############################################

def calculate_portfolio_variance(returns_df, weights):
    return np.dot(weights.T, np.dot(returns_df.cov() * 250, weights))    ##produto de arrays

weights = np.array([0.5, 0.5])
pfolio_var = calculate_portfolio_variance(sec_returns, weights)
pfolio_volatility = pfolio_var ** 0.5

print("Portfolio Variance: ", f"{round(pfolio_var, 5) * 100}%")
print("Portfolio Volatility: ", f"{round(pfolio_volatility, 5) * 100}%")


