#Distribuicao Normal
from scipy.stats import norm
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


# conjunto de objetos em uma cesta, a média é 8 e o desvio padrão é 2.
# a) Qual a probablidade de tirar um objeto que pesa menos que 6 quilos?

probMenorQueSeis = norm.cdf(6, 8, 2)

# b) Qual a probababilidade de tirar um objeto que pesa mais de 6 quilos?
probMaiorQueSeis = norm.sf(6, 8, 2)

# c) Qual a probablidade de tirar um objeto que o peso é menor do que 6 ou maior do que 10 quilos?
probMenorQueSeisMaiorQueDez = norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# d) Qual a probabildade de tirar um objeto que o peso é menor do que 10 e maior do que 8?
probMenorQueDezEMaiorQueOito = 0.5 - norm.sf(10, 8, 2)


#Testes para ver se a distribuicao é normal
dados = norm.rvs(size = 100)
stats.probplot(dados, plot = plt)

testeShapiro = stats.shapiro(dados)