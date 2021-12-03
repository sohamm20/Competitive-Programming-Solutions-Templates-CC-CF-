# largest component
# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

def countComponents(graph, node, visited):
  if node in visited:
    return 0
  
  visited.add(node)
  
  count = 1
  
  for Node in graph.get(node):
    count += countComponents(graph, Node, visited)
  
  return count

def largest_component(graph):
  largest = 0
  
  visited = set()
  
  for node in graph:
    count = countComponents(graph, node, visited)
    largest = max(largest, count)
  return largest
