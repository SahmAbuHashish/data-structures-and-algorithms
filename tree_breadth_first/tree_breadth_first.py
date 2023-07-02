# from collections import deque
from stack_and_queue.stack_and_queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first(tree):
    if tree.root is None:
        return [] 

    result = []
    queue = Queue()  

    queue.enqueue(tree.root) 

    while not queue.is_empty():
        node = queue.dequeue()  
        result.append(node.value)  

        if node.left:
            queue.enqueue(node.left)  
        if node.right:
            queue.enqueue(node.right)  



