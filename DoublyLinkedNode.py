# Implementation of node for Doubly-Linked List. Inherits from LinkNode
from LinkNode import LinkNode
class DoublyLinkedNode(LinkNode):
	
	def __init__(self, data):
		LinkNode.__init__(self, None, data)
		self.previous = None
	
	def __str__(self):
		return "<== ( " + str(self.data) + " ) ==>"