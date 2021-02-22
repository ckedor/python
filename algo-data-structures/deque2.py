from collections import deque

d = deque()
d.append(1) #Adiciona do lado direito (Fim da fila)
d.appendleft(2) #Adiciona do lado esquerdo (Inicio da fila)
d.append(3)
d.appendleft(4)

#4, 2, 1, 3

d.pop()
d.popleft()

d.remove(2)

for i in d:
	print(i, end=' ')



