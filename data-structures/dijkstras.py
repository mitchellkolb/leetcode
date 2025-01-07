


"""
“Dijkstras algorithm is used to calculate the shortest path for a weighted graph.
            
         
Dijkstras algorithm works when all the weights are positive.
            
                 
If you have negative weights, use the Bellman-Ford algorithm.”

Excerpt From
Grokking Algorithms: An illustrated guide for programmers and other curious people
Aditya Y. Bhargava
This material may be protected by copyright.

Finds the shortest path from the start node to all other nodes in the graph.
    
    graph: dict - A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    start: any - The starting node for Dijkstra's algorithm.
    
Returns a dictionary with the shortest distance from the start node to each node.
   

Time Complexity: The time complexity of Dijkstras algorithm is O(V^2). This is because the algorithm uses two nested loops to traverse the graph and find the shortest path from the source node to all other nodes.

Space Complexity: The space complexity of Dijkstras algorithm is O(V), where V is the number of vertices in the graph. This is because the algorithm uses an array of size V to store the distances from the source node to all other nodes
"""

def dijkstra(graph, start):
    # Initialize distances for each node, with infinity for all except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Set to track visited nodes
    visited = set()
    
    # List of unvisited nodes with their distances
    unvisited_nodes = [(start, 0)]  # Each item is a tuple (node, current_distance)
    
    while unvisited_nodes:
        # Sort unvisited nodes based on the distance (like a priority queue)
        unvisited_nodes.sort(key=lambda x: x[1])
        
        # Get the node with the smallest distance
        current_node, current_distance = unvisited_nodes.pop(0)
        
        if current_node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            
            new_distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update the distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                unvisited_nodes.append((neighbor, new_distance))
        

        return distances

# Weighted graph as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'

# Call the Dijkstra algorithm function
result = dijkstra(graph, start_node)

# if __name__ == "__main__":
#     main()
