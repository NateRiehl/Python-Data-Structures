# Implementation of Binary Search Tree
from BSTreeNode import BSTreeNode
import threading
from queue import Queue
class BSTree:
	def __init__(self):
		self.root = None
	
	# Returns if BST is empty
	def is_empty(self):
		return self.root == None

	#Add data to BSTree
	def add(self, data):
		if self.is_empty(): # Set Root
			self.root = BSTreeNode(data)
		else:
			done = False
			node = self.root
			while done == False and node.is_leaf() == False: #Iterate through tree until reaching appropriate parent for new node
				if node.data > data:
					if node.left_child == None:
						done = True
					else:
						node = node.left_child
				else:
					if node.right_child == None:
						done = True
					else:
						node = node.right_child
			if node.data > data: # New node is left child
				node.left_child = BSTreeNode(data)
			else: # New node is right child
				node.right_child = BSTreeNode(data)
				
	# Remove data from BSTree
	def remove(self, data):
		if self.is_empty(): # Empty BST. Nothing can be removed
			return False
		else:
			node = self.root
			parent_node = node
			found = False
			while node != None and found is False: #Traverse tree
				if node.data == data:
					found = True
				elif node.data > data:
					parent_node = node
					node = node.left_child
				else:
					parent_node = node
					node = node.right_child	
			if node is None: # Data is not in tree
				return None
			elif node.is_leaf():# Data is in a leaf node so simply Nullify reference to it
				if parent_node.data > node.data:
					parent_node.left_child = None
				else:
					parent_node.right_child = None
			elif node.left_child != None: # Data is in internal node with left child
				if node.right_child != None: # Also has right child
					node.data = self.get_max_left_subtree(node.left_child) # Replace data with max from left subtree
				else: # Target node only has left child, skip over it (Similar to Linked List removal Alg)
					node.data = node.left_child.data
					node.left_child = node.left_child.left_child
			elif parent_node != None: #Internal node with parent and no left child, skip over it like above
				if parent_node.data > node.data:
					parent_node.left_child = node.right_child
				else:
					parent_node.right_child = node.right_child
			else: # Final case: Null parent (AKA is root) and right child. Update root reference
				self.root = node.right_child
			return True
				

	# Searches for data and returns it if in tree. Returns None otherwise
	def get(self, data):
			node = self.root
			found = false
			while node != None and found is False:
				if node.data == data:
					found = True
				elif node.data > data:
					node = node.left_child
				else:
					node = node.right_child
			if node != None:
				return node.data
			else:
				return None
				
	# Helper method for remove()
	# Returns max from left subtree
	def get_max_left_subtree(self, node):
		parent = None
		while node.right_child != None:
			parent = node
			node = node.right_child
		data = node.data
		if parent is not None:
			parent.right_child = node.left_child		
		return data
	
	# Recursive contains method 
	# Returns if data is contained in node
	def contains(self, data):
		return self.contains(self.root, data)
	
	def contains(self, node, data):
		if node == None:
			return False
		if node.data == data:
			return True
		elif node.data > data:
			 node.left_child
		else:
			node = node.right_child
			
	
	#Print BST in Level-Order	
	def level_order(self):
		queue = Queue()
		queue.put(self.root)
		bst = ""
		while queue.qsize() > 0:
			node = queue.get()
			bst += str(node.data) + " "
			if node.left_child != None:
				queue.put(node.left_child)
			if node.right_child != None:
				queue.put(node.right_child)
		print(bst)
		
	# In order traversal of BST
	def in_order(self, node):
		order = ""
		if node is not None:
			order = self.in_order(node.left_child) + str(node.data) + " " + self.in_order(node.right_child)
		return order
		
	# pre-order traversal of BST
	def pre_order(self, node):
		order = ""
		if node is not None:
			order =  str(node.data) + " " + self.pre_order(node.left_child) + self.pre_order(node.right_child)
		return order
	
	# post-order traversal of BST
	def post_order(self, node):
		order = ""
		if node is not None:
			order = self.post_order(node.left_child) + self.post_order(node.right_child) + str(node.data) + " " 
		return order
		
			
				
				
				
				
				
				
				
				
				
				
				
						
	