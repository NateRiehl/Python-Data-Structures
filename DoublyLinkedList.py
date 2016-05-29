# Implementation of Doubly-Linked List. Inherits from LinkedList
from DoublyLinkedNode import DoublyLinkedNode
from LinkedList import LinkedList

class DoublyLinkedList(LinkedList):

	def __init__(self):
		LinkedList.__init__(self)
		self.tail = None
		
	# Add data to DLL
	def add(self, data):
		new_node = DoublyLinkedNode(data)
		if self.is_empty():
			self.head = new_node
			self.tail = self.head
		else:
			self.tail.next = new_node
			new_node.previous = self.tail
			self.tail = new_node
			
	# Remove first occurrence of data from DLL
	def remove(self, data):
		if self.is_empty():
			return False
		elif self.head.data == data:
			self.head = self.head.next
			return True
		else:
			removed = False
			current = self.head
			previous = current
			while current != None and current.data != data:
				current = current.next
			if current != None and current.next != None:
				next = current.next
				next.previous = previous
				previous.next = next
				return True
			elif current != None:
				previous.next = None
				self.tail = previous
				return True
			return False
	
	# To String
	def __str__(self):
		current = self.head
		list = ""
		while current != None:
			list += str(current)
			current = current.next
		return list
		
	def str_backwards(self):
		current = self.tail
		list = ""
		while current != None:
			list += str(current)
			current = current.previous
		return list
			
		
		