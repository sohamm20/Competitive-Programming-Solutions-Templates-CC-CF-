# island count
# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

def island_count(grid):
  
  count = 0
  
  visited = set()
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if explore(grid, i, j, visited) == True:
        count += 1
  return count

def explore(grid, i, j, visited):
  
  if (not (i >= 0 and i <= len(grid) - 1)) or (not (j >= 0 and j <= len(grid[0]) - 1)):
    return False
  
  if grid[i][j] == "W":
    return False
  
  if (i, j) in visited:
    return False
  
  visited.add((i, j))
  
  explore(grid, i + 1, j, visited)
  explore(grid, i - 1, j, visited)
  explore(grid, i, j + 1, visited)
  explore(grid, i, j - 1, visited)
  
  return True
