# graph-business-trip

Write a function called business trip

- Arguments: graph, array of city names
- Return: the cost of the trip (if it’s possible) or null (if not)
Determine whether the trip is possible with direct flights, and how much it would cost.

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-07-19%20152433.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big o for this approach will be:

- Time complexity: O(n*m),  n # of cities and m is the average # of neighbors for each city. 
- Space complexity: O(1)

---

## Solution

### [code](./graph_business_trip.py)

### [test](./test/test_graph_business_trip.py)
