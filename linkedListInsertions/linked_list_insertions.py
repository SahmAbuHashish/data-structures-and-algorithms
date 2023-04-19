from node import Node

class LinkedList():
   
    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        if self.head is None:
            return "This linked list is empty"
        else:
            current = self.head
            while(current):
                string += "{ " + f"{str(current.value)}" + " } -> "
                current = current.next
            string = string + "Null"
        return string    
    

    def __repr__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while (current):
                output = output + f'{current.value} --> '
                current = current.next
            output += "None"
        return output
    
    #Append a new node with the given value to the end of the linked list.
    def append(self, value):   
        node =  Node(value)  
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node  

    #inserts a new node at the beginning of the linked list with the given value.
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    #Returns True if a node with the given value is present in the linked list, False otherwise.
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
    
    #Insert a new node with the given new value before the node with the given value in the linked list. 
    def insert_before(self, value, new_value):
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            previous = None
            while(current):
                if current.value == value:
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    break
                else:
                    previous = current
                    current = current.next

    #Insert a new node with the given new value after the node with the given value in the linked list.
    def insert_after(self, value, new_value):
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current):
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    break
                else:
                    current = current.next


    # delete the first matched node key in linked list
    def delete_node(self,key): 
        temp = self.head
        # 1 empty liked list
        if (temp is None):
            return False
        # 2 if the target is the first node
        if (temp is not None):
            if(temp.value == key):
                self.head = temp.next
                temp = None
                return True
         # search for the key and delete the target    
        while(temp is not None):
            if temp.value == key:
                break   
            prev = temp
            temp = temp.next
        # 3 the key does not exists
        if(temp is None):
            return False    
        # unlike the target node from the linked list
        prev.next = temp.next    
        temp = None
        return True
    

    #Returns the value of the node that is k places from the tail of the linked list.
    def kthFromEnd(self,k):

        if k < 1:
            return None

        p1 = p2 = self.head
        
        # Move p1 k nodes ahead
        for i in range(k):
            if p1 is None:
                return None
            p1 = p1.next

        # Move both pointers until p1 reaches the end
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value