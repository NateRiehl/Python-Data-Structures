# Stack implementation
class MyStack:
	def __init__(self):
		self.stack = []
		self.size = 0
	# Returns if stack is empty	
	def is_empty(self):
		return self.size == 0
	# Pop data off of stack
	def pop(self):
		if self.size > 0:
			self.size -= 1
			return self.stack.pop()
		return None
	# Push data onto stack
	def push(self, data):
		self.stack.append(data)
		self.size += 1
	# Look at data on stack	
	def peek(self):
		return self.stack[self.size - 1]
	# ToString	
	def __str__(self):
		return str(self.stack)