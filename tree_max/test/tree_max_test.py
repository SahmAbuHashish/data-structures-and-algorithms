import pytest
from tree_max.tree_max import BinaryTree,Node

class TestBinaryTree():
    def test_find_maximum_value(self):
        tree = BinaryTree()
        tree.root = Node(2)
        tree.root.left = Node(7)
        tree.root.right = Node(5)

        tree.root.left.left = Node(2)
        tree.root.left.right = Node(6)
        tree.root.left.right.left = Node(5)
        tree.root.left.right.right = Node(11)

        tree.root.right.right = Node(9)
        tree.root.right.right.left = Node(4)
        return tree
    
    
def test_find_maximum_value():
    assert BinaryTree.find_maximum_value() == 11

def test_find_maximum_value_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.find_maximum_value()  

   

