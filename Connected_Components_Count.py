
# connected components count
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

def explore(graph, node, visited):
  if node in visited:
    return False
  visited.add(node)
  
  for Node in graph.get(node):
    explore(graph, Node, visited)
  
  return True

def connected_components_count(graph):
  count = 0
  
  visited = set()
  
  for node in graph:
    if explore(graph, node, visited):
      count += 1
  return count
