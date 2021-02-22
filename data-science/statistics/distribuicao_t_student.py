"""""""""""""""""""""""""""""
     Teste de Hipótese

p-value > alfa: não rejeita H0
p-value < alfa: rejeita H0

Erro Tipo 1: Rejeitar H0 quando não deveria
Erro Tipo 2: Não rejeita H0 quando deveria

"""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""

Distribuição de T-Student

"""""""""""""""""""""""""""""


#t caculado = 1.5, grau de liberdade = 8
from scipy.stats import t
import numpy as np
x = t.cdf(1.5, 8)
y = t.sf(1.5,8)

x = np.random.choice(a = [0, 1], size = 50, replace = True, p = [0.5, 0.5, 0.2])



