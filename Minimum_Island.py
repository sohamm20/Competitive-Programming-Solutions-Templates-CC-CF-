# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

import math

def explore(grid, i, j, visited):

  if (not (i >= 0 and i <= len(grid) - 1)) or (not (j >= 0 and j <= len(grid[0]) - 1)):
    return 0
    
  if (i, j) in visited:
    return 0
  
  if grid[i][j] == "W":
    return 0
  
  visited.add((i, j))
  
  count = 1
  
  count += explore(grid, i + 1, j, visited)
  count += explore(grid, i - 1, j, visited)
  count += explore(grid, i, j + 1, visited)
  count += explore(grid, i, j - 1, visited)
  
  return count
  

def minimum_island(grid):
  
  smallest = math.inf
  
  visited = set()
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "W" or (i, j) in visited:
        continue
      count = explore(grid, i, j, visited)
      smallest = min(smallest, count)
  return smallest
