# insert Shift Array

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

---

## Whiteboard Process

- Create a new array with the same length as the original array plus one
- Copy the first half of the original array into the new array
- Insert the new value into the middle index of the new array
- Copy the second half of the original array into the new array

![Whiteboard](./Screenshot%202023-04-05%20220940.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

by iterating the original array and assigning the first half in a new array then adding an element to the middle index that adds the second half 
the big o for this approach will be O(n) 

---

## Solution

python insertShiftArray.py

arr = [1, 2, 3, 4, 5]
val = 10
new_arr = insertShiftArray(arr, val)
print(new_arr)

---

## [code](./insert_Shift_Array.py)

## [test](./test/test_insert%20Shift%20Array.py)
