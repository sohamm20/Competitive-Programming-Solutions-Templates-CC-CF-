
# UNDIRECTED PATH
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

def buildGraph(edges):
  
  graph = {}
  
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = []
    if edge[1] not in graph:
      graph[edge[1]] = []
    
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
  
  return graph

def hasPath(graph, src, dst, visited):
  
  if src in visited:
    return False
  
  if src == dst:
    return True
  
  for node in graph.get(src):
    visited.add(src)
    if hasPath(graph, node, dst, visited):
      return True
  return False
  

def undirected_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  
  visited = set()
  
  if hasPath(graph, node_A, node_B, visited):
    return True
  return False
  
