# Singly-Linked List Implementation
from LinkNode import LinkNode

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	# Returns if LL is empty
	def is_empty(self):
		return self.head == None
	
	# Add data to LL
	def add(self, data):
		if self.is_empty():
			self.head = LinkNode(None, data)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = LinkNode(None, data)
		self.size +=1
	
	# Remove first occurrence of data from LL
	def remove(self, data):
		if self.head == None:
			return False
		elif self.head.data == data:
			self.head = self.head.next
			self.size -= 1
			return True
		else:
			current = self.head
			previous = None
			while current != None and current.data != data:
				previous = current
				current = current.next
			if current != None:
				previous.next = current.next
				self.size -= 1
				return True
			return False
	
	# Set data at index to new data and return old data
	def set(self, index, data):
		if index > self.size or index < 0:
			return None
		else:
			current = self.head
			count = 0
			while count < index:
				current = current.next
				count += 1
			temp = current.data
			current.data = data
			return temp
	
	# Returns index of element or -1 if not present
	def index_of(self, data):
		current = self.head
		index = 0
		while current != None:
			if current.data == data:
				return index
			index += 1
			current = current.next
		return -1
	
	# Returns if data is contained in LL
	def contains(self, data):
		if self.is_empty():
			return False
		found = False
		current = self.head
		while not found and current != None:
			if current.data == data:
				found = true
			else:
				current = current.next
		return found
	# To string
	def __str__(self):
		current = self.head
		list = ""
		while current != None:
			list += current.__str__() + "\n"
			current = current.next
		return list