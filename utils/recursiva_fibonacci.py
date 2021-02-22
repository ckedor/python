
'''
# fibonacci = 1, 1, 2, 3, 5, 8, 13... ()
# retorna a nzimo numero da sequencia de fibonnaci
# recursivo
'''
def fib(n):
	if (n == 1 or n == 2):
		return 1
	return (fib(n-1) + fib(n-2))

print(fib(7))
