# Test cases for BSTree
from BSTree import BSTree
bst = BSTree()
bst.add(1)
bst.add(3)
bst.add(4)
bst.add(5)
bst.add(2)
bst.remove(4)
bst.level_order()
print(bst.in_order(bst.root))