#Lista simplesmente encadeada (linked list)
class Node:

	def __init__ (self, label):
		self.label = label
		self.next = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next


class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.len_list = 0

	def empty(self):
		if self.len_list == 0:
			return True
		return False

	def push(self, label, index):

		if index >= 0:
			#Cria o novo nó
			node = Node(label)

			if self.empty():
				self.first = node
				self.last = node
			else:
				if index == 0:
					# inserção no início
					node.setNext(self.first)
					self.first = node
				elif index >= self.len_list:
					# inserção no final
					self.last.setNext(node)
					self.last = node
				else:
					# inserção no meio
					prev_node = self.first
					curr_node = self.first.getNext()
					curr_index = 1

					while curr_node != None:

						if curr_index == index:
							node.setNext(curr_node)
							prev_node.setNext(node)
							break

						prev_node = curr_node
						curr_node = curr_node.getNext()
						curr_index += 1

			#atualiza o tamanho da lista
			self.len_list += 1

	def pop(self, index):

		if not self.empty() and index >= 0 and index < self.len_list:

			flag_remove = False

			if self.first.getNext() == None:
				#só tem um elemento
				self.first = None
				self.last = None
				flag_remove = True
			elif index == 0:
				#remove do inicio mas possui mais de um elemento
				self.first = self.first.getNext()
				flag_remove = True
			else:
				#possui mais de um elemento e remoção não é no inicio
				prev_node = self.first
				curr_node = self.first.getNext()
				curr_index = 0 
				while curr_node != None:
					if index == curr_index:
						prev_node.setNext(curr_node.getNext())
						curr_node.setNext(None)
						flag_remove = True
						break
					prev_node = curr_node
					curr_node = curr_node.getNext()
					curr_index += 1
			if flag_remove:
				self.len_list -= 1


	def show(self):
		no_atual = self.first
		for i in range(self.len_list):
			print(no_atual.getLabel(), end = ' ')
			no_atual = no_atual.getNext()

	def lenght(self):
		return self.len_list




lista = LinkedList()

lista.push("bonita", 0)
lista.push("brother", 1)
lista.push("sister", 1)

lista.pop(1)

lista.show()
print("\nTamanho da lista: %d" % lista.lenght())