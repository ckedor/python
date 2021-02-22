import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot


dados_carros = pd.read_csv("cars.csv")
dados_carros = dados_carros.drop(['Unnamed: 0'], axis = 1)

x = dados_carros.iloc[:, 1].values
x = x.reshape(-1, 1)
y = dados_carros.iloc[:, 0].values
y = y.reshape(-1, 1)
correlacao = np.corrcoef(x, y)

modelo = LinearRegression()
modelo = modelo.fit(x, y)
modelo.intercept_
modelo.coef_

plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color = 'red')

modelo._residues

visualizador = ResidualsPlot(modelo)
visualizador.fit(x, y)
visualizador.poof()
