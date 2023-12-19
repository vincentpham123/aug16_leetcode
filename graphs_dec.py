def has_path(graph, src, dst):
  
  if src == dst:
    return True 
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True 
  return False

from collections import deque
def has_path(graph, src, dst):
  
# BFS

  queue = deque([src])
  
  while queue:
    # i want to pop the node, then iterate through the neighbors
    
    node = queue.popleft()
    for neighbor in graph[node]:
      if neighbor == dst:
        return True
      else:
        queue.append(neighbor)
  return False

def undirected_path(edges, node_A, node_B):
  graph = create_graph(edges)
  return has_path(graph, node_A, node_B, set())
def create_graph(edges):
  graph = {}
  
  for pair in edges:
    a , b = pair 
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
  return graph

def has_path(graph, src, dst, visited):
  # visited is to keep track of nodes:
  # i know if i visited and the path isnt right, there is no point and checking its neighbors
  
  if src == dst:
    return True 
  if src in visited:
    return False
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True 
    
def largest_component(graph):
  
  visited = set()
  max = 0
  for node in graph:
    size = find_path_count(graph, node, visited)
    if size > max:
      max = size 
  return max
  

def find_path_count(graph, node, visited):
  
  
  if node in visited:
    return 0
  
  visited.add(node)
  
  size = 1
  for neighbor in graph[node]:
    size += find_path_count(graph, neighbor, visited)
  return size

from collections import deque
def shortest_path(edges, node_A, node_B):
  #BFS always finds the shortest path 
  
  visited = set([node_A])
  
  graph = create_graph(edges)
  
  queue = deque([(node_A, 0)])
  
  # using a tuple to keep track of the path
  while queue:
    node, path = queue.popleft()
    
    visited.add(node)
    if node == node_B:
      return path
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append((neighbor, path+1))
    
  return -1

def create_graph(edges):
  graph={}
  
  for pair in edges:
    x, y = pair 
    
    if x not in graph:
      graph[x] = []
      
    if y not in graph:
      graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
    
  return graph 

from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  # since i need to find the carrot, i can take advtange of BFS which always finds the shortest path 
  queue = deque([(starting_row, starting_col, 0)])
  # i use that to keep track of the position, and distance to the carrot
  visited = set([(starting_row, starting_col)])
  
  while queue:
    x,y, distance = queue.popleft()
    
    if grid[x][y] == 'C':
      return distance 
    
    deltas = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for delta in deltas:
      delta_row, delta_col = delta 
      neighbor_row = x + delta_row
      neighbor_col = y + delta_col
      pos = (neighbor_row, neighbor_col)
      row_check = 0<= neighbor_row < len(grid)
      col_check = 0 <= neighbor_col < len(grid[0])
      
      if row_check and col_check and pos not in visited and grid[neighbor_row][neighbor_col] !='X':
        visited.add(pos)
        queue.append((neighbor_row, neighbor_col, distance+1))
  return -1