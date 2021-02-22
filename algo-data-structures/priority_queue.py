'''
	Implementação da priority queue com lista ordenada
'''

class Person:

	'''
		nome -> nome da pessoa
		prior -> prioridade da pessoa
	'''

	def __init__(self, name, prior):
		self.name = name
		self.prior = prior

	def getName(self):
		return self.name

	def getPrior(self):
		return self.prior

class PriorityQueue:

	def __init__(self):
		self.pq = []
		self.len = 0

	#insere descrescentemente pela prioridade
	def push(self, person):

		if self.empty():
			self.pq.append(person)
		else:
			flag_push = False
			#procurar-se onde inserir para manter a fila ordenada
			for i in range(self.len):
				if self.pq[i].getPrior() < person.getPrior():
					self.pq.insert(i, person)
					flag_push = True
					break
			if not flag_push:
				#Menor prioridade, deve ser inserido ao final da fila.
				self.pq.append(person)
		self.len += 1

	def pop(self):
		if not self.empty():
			return self.pq.pop(0)
			self.len -= 1

	def empty(self):
		if self.len == 0:
			return True
		else: return False

	def show(self):
		for p in self.pq:
			print("Nome: %s" % p.getName())
			print("Prioridade: %d\n" % p.getPrior())


#criando os objetos Person
p1 = Person('Marcos', 28)
p2 = Person('Catarina', 3)
p3 = Person('Pedro', 20)
p4 = Person('João', 35)

pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

print ("Exibindo após as inserções:\n")
pq.show() #João, Marcos, Pedro, Catarina

VIP = pq.pop()

print("______________________")
pq.show()

print(VIP.getName())