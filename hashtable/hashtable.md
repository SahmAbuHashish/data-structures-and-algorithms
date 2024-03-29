# hashtable 

Implement a Hashtable Class with the following methods:

- set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
- get
Arguments: key
Returns: Value associated with that key in the table
- has
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
- keys
Returns: Collection of keys
- hash
Arguments: key
Returns: Index in the collection for that key

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-06-26%20133832.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big o for this approach will be:
set(key, value):

- Time complexity:  O(1)
- Space complexity: O(1)

get(key):

- Time complexity:  O(1)
- Space complexity: O(1)

has(key):

- Time complexity:  O(1)
- Space complexity: O(1)

keys():

- Time complexity:  O(1)
- Space complexity: O(1)

hash(key): O(1)

- Time complexity:  O(1)
- Space complexity: O(1)

---

## Solution

### [code](./hashtable.py)

### [test](./test/test_hashtable.py)
