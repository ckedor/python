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

medias_ano = sec_returns[['PG', 'BEI.DE']].mean() * 250
desvios_padrao_ano = sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5

PG_var = sec_returns['PG'].var() * 250  # o 250 é para anualizar
print("Variância PG:", PG_var)

BeiDe_var = sec_returns['BEI.DE'].var() * 250
print("Variância BEI.DE:", BeiDe_var)

cov_matrix = sec_returns.cov() * 250
print("Covariância entre os ativos:", cov_matrix)

# O método COV resulta em um dataframe com variância e covariância entre os ativos:
# pd.Dataframe cov_matrix:
#        PG             | BEI.DE
# PG    |var(PG)        | cov(PG, BEI.DE)
# BEI.DE|cov(BEI.DE, PG)| var(BEI.DE)

# O dataframe que mostra a correlação dos retornos dos ativos reflete a dependência entre
# os preços em diferentes momentos e se concentra nos retornos de seu portfólio (Não nos níveis de preço)
# Essa tabela não deve ser anualizada.
corr_matrix = sec_returns.corr()
print("matriz de correlação:", corr_matrix)

