from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    #Adds a new node with the given value to the back of the queue.
    def enqueue(self,value):
        node = Node(value)
        #if the queue is empty
        if not self.back:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node


    #Removes and returns the value of the front node of the queue.
    def dequeue(self):
        #if the queue is empty
        if self.front == None:
            raise Exception( "This queue is empty")
        # if the queue contains only one node
        if self.front == self.back:
            self.back = None
            #self.front = None
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value


    #Returns the value of the front node of the queue without removing it.
    def peek(self):
        if self.front == None:
            raise Exception("this queue is empty")
        else:
           return self.front.value
    

    #Returns True if the queue is empty, else False.
    def is_empty(self):
        return self.front is None
    
#-------------------------------------------

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0
    

    #Adds a new node with the given value to the top of the stack.
    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    

    #Removes and returns the value of the top node of the stack.
    def pop(self):
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            raise Exception("Stack is empty")


    # Returns The Value of the node located at the top of the stack
    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise Exception("Stack is empty")


    #Returns True if the stack is empty, Else False .
    def is_empty(self):
        return self.top == None  