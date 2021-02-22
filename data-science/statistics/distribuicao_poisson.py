#a distribuição de Poisson é uma distribuição de probabilidade de variável aleatória discreta 
#que expressa a probabilidade de uma série de eventos ocorrer num certo período de tempo se 
#estes eventos ocorrem independentemente de quando ocorreu o último evento

from scipy.stats import poisson

#Média de acidentes de carro é 2 por dia

# Qual a probabilidade de ocorrerem 3 acidentes no dia?
p3 = poisson.pmf(3,2)

#Qual a probabilidade de ocorrerem 3 ou menos por dia?
p3ouMenos = poisson.pmf(0,2) + poisson.pmf(1,2) + poisson.pmf(2,2) + poisson.pmf(3,2)
p3ouMenos2 = poisson.cdf(3,2)

#Qual a probabilidade de ocorrerem mais de 3 acidentes no dia?
p3ouMais = poisson.sf(3,2)