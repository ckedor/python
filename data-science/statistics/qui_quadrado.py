#Qui Quadrado

#As variáveis são independentes?
#Hipótese nula: H0: Não existe diferença significativa além do acaso


#            Gostam   ñ gostam    de novela
#   Homens   |  19  |  6  |
#   Mulheres |  43  |  32 |
#

import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19,6], [43,32]])
chi_results = chi2_contingency(novela)

alfa = 0.05

if chi_results[2] > alfa:
    print("p-value > alfa: Não podemos decartar a hipotese nula. Ou seja, não há diferença significativa além do acaso")