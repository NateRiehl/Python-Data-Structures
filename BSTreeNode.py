# Implementation of binary search tree node
class BSTreeNode:
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None
		
	def __str__(self):
		return str(data)
		
	def is_leaf(self):
		return self.left_child == None and self.right_child == None