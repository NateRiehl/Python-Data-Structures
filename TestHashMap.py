# Test cases for Hashmap
from HashMap import HashMap
map = HashMap()
map.put(5, "foo")
map.put(4, "test")
map.put(3, "ba")
map.put(5, "testing")
map.put("Nate", "S")
map.put("Riehl", "S")
print(str(map))
print(str(map.get(3)))
print(str(map.remove(5)))
print(str(map))