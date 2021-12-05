# shortest path
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

from collections import deque 

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

def shortest_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  
  visited = set()
  
  visited.add(node_A)
  
  queue = deque()
  
  queue.appendleft((node_A, 0))
  
  while (len(queue) > 0):
    
    temp = queue.pop()
    
    if temp[0] == node_B:
      return temp[1]
    
    visited.add(temp[0])
    
    for node in graph.get(temp[0]):
      if not node in visited:
        queue.appendleft((node, temp[1] + 1))
    
  return -1
