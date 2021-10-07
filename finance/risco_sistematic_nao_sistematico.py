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

def calculate_portfolio_variance(returns_df, weights):
    return np.dot(weights.T, np.dot(returns_df.cov() * 250, weights))    ##produto de arrays

weights = np.array([0.5, 0.5])
pfolio_var = calculate_portfolio_variance(sec_returns, weights)

############################################################################
## Risco diversificável = variância do portfolio - variância anual ponderada
## == Risco não-sistemático

PG_var_a = sec_returns['PG'].var() * 250
BEI_var_a = sec_returns['BEI.DE'].var() * 250
variancia_anual_ponderada = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a) 
risco_diversificavel = pfolio_var - variancia_anual_ponderada

print(f"Risco diversificável: {round(risco_diversificavel*100, 3)}%")

############################################################################
## Risco não-diversificável = variancia do portfolio - risco diversificável
## == Risco sistemático

risco_nao_diversificavel = pfolio_var - risco_diversificavel
risco_nao_diversificavel = variancia_anual_ponderada
print(f"Risco não diversificável: {round(risco_nao_diversificavel*100, 3)}%")
print(f"Variância do portfolio: {round(pfolio_var*100, 3)}% (soma)")

