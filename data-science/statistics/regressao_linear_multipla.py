import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sn


base = pd.read_csv("mt_cars.csv")
base = base.drop(['Unnamed: 0'], axis = 1)

x = base.iloc[:, 2].values
y = base.iloc[:, 0].values
correlacao = np.corrcoef(x, y)

x = x.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(x,y)
modelo.intercept_
modelo.coef_

score = modelo.score(x,y)

previsoes = modelo.predict(x)
modelo_ajustado = sn.ols(formula = 'mpg ~ disp', data = base)
modelo_treinado = modelo_ajustado.fit()
print(modelo_treinado.summary())

plt.scatter(x,y)
plt.plot(x, previsoes, color='r')

modelo.predict([[20]]) 


#Regressão Múltipla
X1 = base.iloc[:, 1:4].values
Y1 = base.iloc[:, 0].values
modelo2 =LinearRegression()
modelo2.fit(X1,Y1)
score2 = modelo2.score(X1, Y1)

modelo_ajustado2 = sn.ols(formula = 'mpg ~ disp', data = base)
modelo_treinado2 = modelo_ajustado.fit()
print(modelo_treinado2.summary())

novo = np.array([4, 200, 100])
novo = novo.reshape(1,-1)
modelo2.predict(novo)















