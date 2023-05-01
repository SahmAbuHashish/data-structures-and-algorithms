# linked list 

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

- Within your Linked List class, include a head property.
   The class should contain the following methods:

 insert

 includes

 to string

 append

 insert after

 insert before

 kth from end

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-04-19%20221746.png)

---

## Approach & Efficiency

the big o for this approach will be :

- to string
Big o   Time--->O(n)  
        Space--->O(n)  
- insert
Big o Time --->O(1)   
      Space--->O(1)  

- includes
Big o  Time--->O(1)  
       Space--->O(1)        

- append
Big o Time --->O(n)  
      Space--->O(1)

- insert before
Big o Time -->O(n)  
      Space--->O(1)    

- insert after
Big o Time --->O(n)  
      Space--->O(1)  

- delete
Big o Time --->O(n)  
      Space--->O(1)    

- kthFromEnd
Big o Time --->O(n)  
      Space--->O(1)  


---

## Solution

run the code by:

- python3 -m venv .venv

- source .venv/bin/activate


---

## [code](./linked_list.py)

## [code](../linkedListInsertions/linked_list_insertions.py)


## [test](./test/liked_list_test.py)

