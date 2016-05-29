# Linked list node implementation
class LinkNode:
	def __init__(self, next, data):
		self.next = next
		self.data = data
	
	def __str__(self):
		return "Link Node: " + str(self.data)
	
	