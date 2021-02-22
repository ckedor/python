#Programação Funcional

def fat(n):
	if (n == 0):
		return 1
	return (n * fat (n-1))



fat_ = lambda n: n * fat_(n-1) if n > 1 else 1

print(fat_(5))