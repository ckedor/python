#Deque - Double Ended Queue

class Deque():

	def __init__(self):
		self.deque = []
		self.len_deque = 0

	def push_front(self, a):
		self.deque.insert(0, a)
		self.len_deque += 1

	def push_back(self, a):
		self.deque.append(a)
		self.len_deque += 1

	def pop_front(self):
		if not self.empty():
			self.deque.pop(0)
			self.len_deque -= 1

	def pop_back(self):
		if not self.empty():
			self.deque.pop(self.len_deque - 1)
			self.len_deque -= 1

	def empty(self):
		if self.len_deque == 0:
			return True
		return False

	def front(self):
		if not self.empty():
			return self.deque[0]
		return None

	def back(self):
		if not self.empty():
			return self.deque[-1]
	
	def lenght(self):
		return self.len_deque

	def show(self):
		for i in self.deque:
			print(i, end = ' ')


