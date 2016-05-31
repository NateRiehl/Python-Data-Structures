# Test cases for BSTree
from BSTree import BSTree
bst = BSTree()
bst.add(1)
bst.add(3)
bst.add(4)
bst.add(5)
bst.add(2)
bst.remove(4)
bst.add(10)
bst.add(7)
bst.add(8)
bst.add(0)
print(str(bst.contains(bst.root,18)))
bst.remove(7)
bst.remove(1)
bst.level_order()
print(bst.in_order(bst.root))