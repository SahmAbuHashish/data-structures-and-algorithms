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
    

    def append(self, value):   
        node =  Node(value)  
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node  


    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
    
     
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


    #  delete the first matched node key in linked list
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