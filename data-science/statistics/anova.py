#Teste T de Student
#Teste de hipótese com duas médias

#Pré-requistos
#Duas populações independentes
#Variável dependente normalmente distribuída
#Variância entre as duas variáveis é aproximada
#Util para comparar duas populações

#Anova - Análise de Variância
#Usada para comparar 3 ou mais grupos
#Uma variável quantitativa e uma ou mais variáveis categóricas
#Em vez de comparações em pares de grupos, "olha" todo o conjunto
#Busca a variação entre os grupos comparado à variação "dentro" dos grups

#Exemplo:
#   remedio 1 | remedio 2 | remedio 4

#Fem 
#   |   7    |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |

#Masc
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |
#   |       |       |       |

#Ho: Não há diferença significativa no tempo de cura entre as diferentes marcas de remédio
#Ha (Valor-p < alfa): Existe uma diferença significativa no tempo de cura entre as diferentes marcas de remédio

#Teste F
# X = Graus de Liberdade = Grupos - 1 = 3
# Y = Graus de liberdade no denominador: numero de observações - numero de grupos

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv('anova.csv', sep= ';')
tratamento.boxplot(by = 'Remedio')

modelo = ols('Horas ~ Remedio * Sexo', data = tratamento).fit()
resultados = sm.stats.anova_lm(modelo)

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()












