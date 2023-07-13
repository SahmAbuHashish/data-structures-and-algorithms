# hashmap-left-join

Write a function called left join

1. Arguments: two hash maps

- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

2. Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-07-08%20151740.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big o for this approach will be:

- Time complexity:  O(n) 
- Space complexity: O(k) # k is the number of resulting key-value pairs.

---

## Solution

### [code](./hashmap_left_join.py)

### [test](./test/test_hashmap_left_join.py)
