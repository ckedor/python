import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

sec_returns = np.log(sec_data / sec_data.shift(1))

medias_ano = sec_returns[['PG', 'BEI.DE']].mean() * 250
desvios_padrao_ano = sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5