from collections import deque

def bfs(graph, start_node, target_node):
    """
    Breadth-First Search (BFS) algorithm to find a target node in a graph.

    Parameters:
        graph (dict): A dictionary representing the graph.
        start_node: The starting node for the search.
        target_node: The node we want to find.

    Returns:
        list: A list of nodes representing the path from the start_node to the target_node.
    """
    queue = deque([(start_node, [start_node])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == target_node:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))

    return []

def dfs(graph, start_node, target_node):
    """
    Depth-First Search (DFS) algorithm to find a target node in a graph.

    Parameters:
        graph (dict): A dictionary representing the graph.
        start_node: The starting node for the search.
        target_node: The node we want to find.

    Returns:
        list: A list of nodes representing the path from the start_node to the target_node.
    """
    stack = [(start_node, [start_node])]
    visited = set()

    while stack:
        current_node, path = stack.pop()

        if current_node == target_node:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                stack.append((neighbor, path + [neighbor]))

    return []

# Sample Graph Representation
sample_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}   

# Example Usage:
print("Sample Graph:")
for node, neighbors in sample_graph.items():
    print(f"{node} -> {neighbors}")

start_node = 'A'
target_node = 'H'

print("\nBFS Path:")
bfs_path = bfs(sample_graph, start_node, target_node)
print(" -> ".join(bfs_path))

print("\nDFS Path:")
dfs_path = dfs(sample_graph, start_node, target_node)
print(" -> ".join(dfs_path))
