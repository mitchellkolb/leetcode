

# BFS or breath first search is like exploring a map layer by layer. Starting from a node, it checks all its immediate neighbors first before diving deeper into their neighbors. Think of it like a ripple in water, spreading outward evenly, ensuring you cover everything close before heading further away.

"""
The time complexity of BFS is
    O( V + E )
Where V is the number of vertices or nodes and E is the number of edge

BFS vists each node once in the graph and examines each edge once, making it linear in terms of the size of the graph
"""


from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the start node
    visited.add(start)
    
    while queue:
        current = queue.popleft()  # Get the next node in the queue
        print(current)  # Process the current node (e.g., print it)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call BFS starting from node 'A'
bfs(graph, 'A')