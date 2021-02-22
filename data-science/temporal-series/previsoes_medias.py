import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']
          
media_movel = ts.rolling(window = 12).mean()


plt.plot(media_movel, color = 'red')
plt.plot(ts)


previsoes = []
for i in range(1, 13):
    superior = len(media_movel) - i
    inferior = superior - 11
    previsoes.append(media_movel[inferior:superior].mean())

previsoes = previsoes[::-1]

plt.figure(figsize=(10,5))
#plt.plot(media_movel, color = 'red')
#plt.plot(ts)
plt.plot(previsoes)