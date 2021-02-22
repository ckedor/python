from scipy.stats import binom


#Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
prob = binom.pmf(3, 5, 0.5)

#Passar por um sinal de 4 tempos, qual a probabilidade de pegar sinal verda
#nenhuma, 1, 2, 3 ou 4 vezes seguidas?
prob0 = binom.pmf(0, 4, 0.25)
prob1 = binom.pmf(1, 4, 0.25)
prob2 = binom.pmf(2, 4, 0.25)
prob3 = binom.pmf(3, 4, 0.25)
prob4 = binom.pmf(4, 4, 0.25)

#Probabilidade acumulativa
prob5 = binom.cdf(4, 4, 0.25)


