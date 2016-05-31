# HashMap implementation with separate chaining
from HashEntry import HashEntry
class HashMap:
	
	def __init__(self):
		self.map = []
		
	def put(self, key, value):
		hash_key = hash(key)
		hash_key = hash_key % self.map.size
		entry = HashEntry(key, value)
		if map[hash_key] == None:
			map[hash_key] = list()
			map[hash_key].append(entry)
		else:
			map[hash_key].append(entry)
	
	def get(self, key)
		hash_key = hash(key)