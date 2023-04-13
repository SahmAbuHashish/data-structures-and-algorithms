from node import Node

class Linked_list:
    def __init__(self):
        self.head = None
    
    def __str__(self):
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
    
    # def append(self, value):   
    #     node =  Node(value)  
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         current = self.head
    #         while current.next is not None:
    #             current = current.next
    #         current.next = node
      
     #delete the first matched node key in linked list
    # def delete_node(self,key): 
    #     temp = self.head
    #     # 1 empty liked list
    #     if (temp is None):
    #         return False
    #     # 2 if the target is the first node
    #     if (temp is not None):
    #         if(temp.value == key):
    #             self.head = temp.next
    #             temp = None
    #             return True
    #      # search for the key and delete the target    
    #     while(temp is not None):
    #         if temp.value == key:
    #             break   
    #         prev = temp
    #         temp = temp.next
    #     # 3 the key does not exists
    #     if(temp is None):
    #         return False    
    #     # unlike the target node from the linked list
    #     prev.next = temp.next    
    #     temp = None
    #     return True
    

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


    def to_string(self):
        temp = ""
        current = self.head
        while current:
            temp += "{ " + str(current.value) + " } -> "
            current = current.next
        temp += "NULL"
        return temp