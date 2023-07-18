# Graph

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add vertex
Arguments: value
Returns: The added vertex
Add a vertex to the graph
- add edge
Arguments: 2 vertices to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two vertices in the graph
If specified, assign a weight to the edge
Both vertices should already be in the Graph
- get vertices
Arguments: none
Returns all of the vertices in the graph as a collection (set, list, or similar)
Empty collection returned if there are no vertices
- get neighbors
Arguments: vertex
Returns a collection of edges connected to the given vertex
Include the weight of the connection in the returned collection
Empty collection returned if there are no vertices
- size
Arguments: none
Returns the total number of vertices in the graph
0 if there are none

---

## Whiteboard Process

![Whiteboard](./Screenshot%202023-07-13%20154103.png)

---

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big o for this approach will be:
add vertex, get neighbors, add edge, size :

- Time complexity : O(1) 
- Space complexity : O(1)

get vertices :

- Time complexity:  O(1) 
- Space complexity: O(v) # V is the number of vertices

---

## Solution

### [code](./graph.py)

### [test](./test/test_graph.py)
