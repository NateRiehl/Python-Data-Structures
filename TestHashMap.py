# Test cases for Hashmap
from HashMap import HashMap
map = HashMap()
print(str(map))
map.put(5, "moo")
map.put(4, "cow")
map.put(3, "yo")
map.put(5, "mo")
map.put("Fuck", "mo")
map.put("Luck", "mo")
print(str(map))
print(str(map.get(3)))