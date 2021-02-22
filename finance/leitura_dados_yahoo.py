import numpy as np
import pandas as pd
from pandas_datareader import data as wb

ser = pd.Series(np.random.random(5), name = "Column 01");

b = np.array([[1,2,3], [4,5,6]])

pg = wb.DataReader('AAPL', 'iex', start='2015-12-1')

tickers = ['PG', 'MSFT', 'T', 'F', 'GE']

new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-12-1')['Close']


