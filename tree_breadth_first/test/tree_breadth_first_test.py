import pytest
from tree_breadth_first.tree_breadth_first import breadth_first,Node
from Trees.Tree import BinaryTree

# Create the tree
def sample_binary_tree():

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(6)
    tree.root.left.left.right = Node(7)

    return tree


# Perform breadth-first traversal
def test_breadth_first_empty_tree():
    tree = BinaryTree()
    assert breadth_first(tree) == []

def test_breadth_first(sample_binary_tree):
    expected_output = [1, 2, 3, 4, 5, 6, 7]
    assert breadth_first(sample_binary_tree) == expected_output