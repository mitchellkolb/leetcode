


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
   

"""

def dijkstra():
    pass

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
