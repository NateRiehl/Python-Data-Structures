# HashEntry for HashMap
class HashEntry:	
	def __init__(self, key, value):
		self.key = key
		self.value = value
		
	def __str__(self):
		return "Key: " + str(self.key) + ", Value: " + str(self.value)