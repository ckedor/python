#filter
# somente selecionará elementos com predicado True

f = filter(lambda x: x%2 == 0, range(10))

for i in f:
	print(i)