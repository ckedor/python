import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA
#from pmdarima.arima import auto_arima

#from pandas.plotting import register_matplotlib_converters
#register_matplotlib_converters()

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']

plt.figure(figsize=(10,5))          
plt.plot(ts)

#p, q, d
modelo = ARIMA(ts, order=(2, 1, 2))
modelo_treinado = modelo.fit()
sumary = modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 40)[0]

eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1970-01-01', ax = eixo, plot_insample = True)
