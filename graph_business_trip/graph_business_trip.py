from graph.graph import Graph

def business_trip(Graph, cities):
    if not cities or len(cities) < 2:
        return None
    
    total_cost = 0
    
    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]
        
        neighbors = Graph.get_neighbors(current_city)
        found_next_city = False
        
        for neighbor, weight in neighbors:
            if neighbor == next_city:
                total_cost += weight
                found_next_city = True
                break

        if not found_next_city:
            return None

    return total_cost