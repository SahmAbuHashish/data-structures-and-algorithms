from graph.graph import Graph

def breadth_first(Graph, start_node):
    visited = set() 
    queue = []  
    visited_order = []  
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        visited_order.append(current_node)
        neighbors = Graph.get_neighbors(current_node)
        for neighbor, _ in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return visited_order