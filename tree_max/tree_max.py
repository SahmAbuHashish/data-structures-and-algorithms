class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_maximum_value(self):

        if self.root is None:
            raise ValueError("Binary Tree is empty")
        return self.traverse(self.root)

    def traverse(node,self):
            if node is None:
                return float('-inf')  # Return negative infinity for empty nodes
            
            max_value = node.value
            left_max = self.traverse(node.left)
            right_max = self.traverse(node.right)

            if left_max > max_value:
                 max_value = left_max
            if right_max > max_value:
                 max_value = right_max

            return max_value

        # return traverse(self.root)
