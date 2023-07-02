class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
         arr=[]
         def order(node):
            if node:
                arr.append(node.value)
                if node.left:
                    order(node.left)
                if node.right:
                    order(node.right)
         order(self.root)
         return arr

    def in_order(self):
        arr=[]
        def order(node):
            if node:               
                if node.left:
                    order(node.left)
                arr.append(node.value)
                if node.right:
                    order(node.right)
        order(self.root)
        return arr

    def post_order(self):
        arr=[]
        def order(node):
            if node:               
                if node.left:
                    order(node.left)
                if node.right:
                    order(node.right)
                arr.append(node.value)
        order(self.root)
        return arr


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right
        pass

    def contains(self, value):
        if not self.root:
            return False
        else:
            temp = self.root
            while temp:
                if temp.value == value:
                    return True
                elif temp.value > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right


