import pytest
from Node import Node
from Tree import BinaryTree, BinarySearchTree


tree = BinarySearchTree()

assert tree.pre_order() == []
assert tree.in_order() == []
assert tree.post_order() == []
assert tree.contains(10) is False


tree.root = Node(10)
assert tree.pre_order() == [10]
assert tree.in_order() == [10]
assert tree.post_order() == [10]
assert tree.contains(10) is True
assert tree.contains(5) is False

tree.add(5)
tree.add(15)
tree.add(3)
tree.add(7)
tree.add(12)
tree.add(17)

assert tree.pre_order() == [10, 5, 3, 7, 15, 12, 17]
assert tree.in_order() == [3, 5, 7, 10, 12, 15, 17]
assert tree.post_order() == [3, 7, 5, 12, 17, 15, 10]
assert tree.contains(10) is True
assert tree.contains(5) is True
assert tree
