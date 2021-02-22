#fila (FIFO  First In First Out)

class Queue():

	def __init__(self):
		self.queue = []
		self.len_queue = 0

	def push(self, a):
		self.queue.append(a)
		self.len_queue += 1

	def pop(self):
		if not self.empty():
			self.queue.pop(0)
			self.len_queue -= 1

	def empty(self):
		if self.len_queue == 0:
			return True
		return False

	def front():
		if not self.empty():
			return self.queue[0]
		return None

	def back():
		if not self.empty():
			return self.queue[-1]
	
	def lenght():
		return self.len_queue

