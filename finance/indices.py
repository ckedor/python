#indices de mercado dos Eua
#Standard&Poor's S&P500
#Dowjones - 30 maiores igualmente ponderadas
#NASDAQ - Ativos agrupados, empresas de TI, taxa de retorno

#MSCI - Global - mercados em desenvolvimento
#FTSE - Reino Unido
#Dax30 - Alemanha

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI'] #S&P500, NASDAQ, GDAXI(Alemão)
ind_data = pd.DataFrame()
for t in tickers:
    ind_data[t] =wb.DataReader(t, data_source='yahoo', start='1997-1-1')['Adj Close']

ind_data.head()

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15,6))

#retornos simples dos indices

ind_returns = (ind_data / ind_data.shift(1)) - 1
ind_returns.tail()

annual_ind_returns = ind_returns.mean() * 250


tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))

data_2.tail()