#Estacionarias - Flutuam em torno de uma mesma média e variança
#Não Estacionárias

#Estocásticas - Formula + Fator Aleatório
#Deterministicas - Explicadas através de uma fórmula/função

# Valores Observados
#     - Tendência
#     - Sazonalidade
#     - Aleatoriedade
# É interessante decompor (trend, seasonal, random)

# ciclos
# variações nas séries temporais que não dependem do tempo (crise econômica)

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime 

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)

time_series = base['#Passengers']                 
time_series[:'1950-07-31']
plt.plot(time_series)


#Valores agrupados por ano
ts_ano = time_series.resample('A').sum()
plt.plot(ts_ano)

#valores agrupados por mês
ts_mes = time_series.groupby([lambda x: x.month]).sum()
#plt.plot(ts_mes)

ts_datas = time_series['1960-01-01':'1960-12-01']
plt.plot(ts_datas)


