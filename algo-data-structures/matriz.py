#Matriz
matriz =  [["joão", 6, 7, 6],
		  ["pedro", 4.5, 9, 10],
		  ["marcos", 6, 6, 8]]

for linha in matriz:
	for col in linha:
		print(str(col) + '\t', end = ' ')
	print ('')
