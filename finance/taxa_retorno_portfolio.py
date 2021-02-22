import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

mydata.info()


mydata.iloc[0]
(mydata / mydata.iloc[0] * 100).plot(figsize= (15,6))

returns = (mydata / mydata.shift(1)) - 1
returns.head()

annual_returns = returns.mean() * 250

#Carteira de investimento 2
weights = np.array([0.25, 0.25, 0.25, 0.25])
retorno = np.dot(annual_returns, weights)

pfolio_1 = str(round(retorno, 5) * 100) + " %"
print(pfolio_1)

#Carteira de investimento 1
weights = np.array([0.4, 0.4, 0.15, 0.05])
retorno = np.dot(annual_returns, weights)

pfolio_2 = str(round(retorno, 5) * 100) + " %"
print(pfolio_2)
