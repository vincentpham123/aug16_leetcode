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


def has_cycle(graph):
  
  visited = set()
  visiting = set()
  
  for node in graph:
    if cycling(graph, node, visited, visiting) == True:
      return True 
  return False
    
def cycling(graph, node, visited, visiting):
  
  if node in visited:
    return False
  
  if node in visiting:
    return True 
  
  visiting.add(node)
  
  for neighbor in graph[node]:
    if cycling(graph, neighbor, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)
  return False

def prereqs_possible(num_courses, prereqs):
  
  # if there is a cycle, then it is not True
  graph = create_graph(num_courses, prereqs)
  
  visited=set()
  visiting=set()
  for node in graph:
    if _prereqs_possibel(graph, node,visited, visiting):
      return False
  return True


def _prereqs_possibel(graph, node, visited, visiting):
  if node in visited:
    return False 
  
  if node in visiting:
    return True
  
  visiting.add(node)
  
  for neighbor in graph[node]:
    if _prereqs_possibel(graph, neighbor, visited, visiting):
      return True 
  visiting.remove(node)
  visited.add(node)
  return False
def create_graph(num_courses, prereqs):
  
  graph={}
  
  for i in range(num_courses):
    graph[i] = []
    
  for pairs in prereqs:
    x,y = pairs 
    graph[x].append(y)
    
  return graph


def timeConversion(s):
    # Write your code here
    # split the strong by ':'
    # the last index[2:]
    # check for am and pm
    # decide how to convert the time from there
    # if PM, add 12 to the first index[0]
    # if am, change 12 to 1, add 1 to any other 
    
    s_array = s.split(":")
    day_period = s_array[-1][2:]
    print(day_period)
    result =''
    hour = int(s_array[0])
    if day_period == "AM":
        hour = hour%12
    else:
        hour = hour%12+12
    if hour < 10:
        result += '0'+str(hour)+':'
    else:
        result += str(hour)+":"
    result+=str(s_array[1])+':'
    result+=str(s_array[-1][:2])
    return result