import pandas as pd
import numpy as np
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao / amostra)   #arredonda

r = np.random.randint(low = 1, high = k+1, size =1)


acumulador = r[0]
sorteados = []
for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
    
base = pd.read_csv("iris.csv")
base_final = base.loc[sorteados]
