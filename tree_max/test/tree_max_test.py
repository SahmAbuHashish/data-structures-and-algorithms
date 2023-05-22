import pytest
from tree_max.tree_max import BinaryTree,Node

class TestBinaryTree():
    def test_find_maximum_value(self):
        tree = BinaryTree()
        node1 = Node(7)
        node2 = Node(5)
        node3 = Node(9)
        node4 = Node(11)
        node5 = Node(3)

        tree.root = node1
        node1.left = node2
        node1.right = node3
        node2.right = node4
        node3.left = node5

    

