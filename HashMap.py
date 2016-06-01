# HashMap implementation with separate chaining
from HashEntry import HashEntry
class HashMap:
	
	def __init__(self):
		self.map = [None] * 10
		self.count = 0
	# Add new element to hashmap. Return previous entry if replacement or None if new entry
	def put(self, key, value):
		fill_rate = self.count/len(self.map)
		if fill_rate == 1:
			self.re_hash()
		hash_key = hash(key)
		hash_key = hash_key % len(self.map)
		entry = HashEntry(key, value)
		if self.map[hash_key] == None:
			self.map[hash_key] = list()
			self.count += 1
			self.map[hash_key].append(entry)
			return None
		else:
			for elem in self.map[hash_key]:
				if elem.key == key:
					temp = elem.value
					elem = entry	
					return temp
			self.count += 1
			self.map[hash_key].append(entry)
			return None
	# Given key, get value from hashmap or None if not present
	def get(self, key):
		hash_key = hash(key) % len(self.map)
		if self.map[hash_key] is None:
			return None
		for entry in self.map[hash_key]:
			if entry.key == key:
				return entry.value
		return None
	
	# Removes key from map if present and returns value. Returns None otherwise
	def remove(self, key):
		hash_key = hash(key) % len(self.map)
		if self.map[hash_key] is None:
			return None
		for entry in self.map[hash_key]:
			if entry.key == key:
				temp = entry.value
				self.map[hash_key].remove(entry)
				return temp
		return None
	
	# Refactor map if too full
	def re_hash(self):
		new_map = [None] * (self.map.size * 2)
		for list in self.map:
			if list is not None:
				for entry in list:
					hash_key = hash(entry.key) % new_map.size
					if new_map[hash_key] is None: 
						new_map[hash_key] = list()
					new_map[hash_key].append(entry)
	# ToString		
	def __str__(self):
		s = ""
		for list in self.map:
			s += "List: "
			if list is not None:
				for entry in list:
					s+= str(entry) + "--> "
			s+="\n"
		return s	