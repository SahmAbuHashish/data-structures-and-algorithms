# insert Shift Array

a function called BinarySearch which has a 2 parameters: a sorted array and the search key. return the index of the array’s element that is equal to the value of the binary search key, or -1 if the element is not in the array.

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-04-10%20183528.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

declare the variable that tack middle index and then loop to iteration on the arr from the middle to change it to the input number that tack from the argument and shift all the still numbers on the last of an array then return this array

the big o for this approach will be O(log(n)) space will be O(1)

---

## Solution

python insertShiftArray.py

arr = [4, 8, 15, 16, 23, 42]
key = 15

Binary_Search = BinarySearch(arr, key)
print(Binary_Search)

---

## [code](./array_binary_search.py)

## [test](./test/test_array_binary_search.py)
