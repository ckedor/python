import random

#Escolher um número aleatório de uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
x = random.choice(lista)

#Escolher um número aleatório entre 1 e 10 inclusive
y = random.randint(1, 10)

#Embaralhar lista
random.shuffle(lista)

#Pegar elementos aleatórios da lista
z = random.sample(lista, 3)

#Gerar pontos flutuantes de 0 à n = 100
print(random.random()*100)

#Gerar pontos flutuantes de n1 a [n2
print(random.uniform(1, 60))
