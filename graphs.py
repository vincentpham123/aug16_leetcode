def has_path(graph, src, dst):
#   stack = [src]
  
#   path=[]
  
#   while len(stack) > 0:
#     current = stack[-1]
#     if current == dst:
#       return True
#     path.append(current)
#     node = stack.pop()
#     for neighbor in graph[node]:
#       stack.append(neighbor)
#   return False
    # DFS
    queue = deque( [src])

    while len(queue) > 0:
      node = queue.popleft()
      if node == dst:
        return True
      for neighbor in graph[node]:
        queue.append(neighbor)
    return False

def undirected_path(edges, node_A, node_B):
  graph = create_graph(edges)
  return has_path(graph, node_A, node_B, set())
#   graph = create_graph(edges)
  
#   visited = set()
#   queue = deque ( [node_A])
  
#   while len(queue) > 0:
#     node = queue.popleft()
#     if node not in queue:
#       visited.add(node)
#     if node == node_B:
#       return True 
#     for neighbor in graph[node]:
#       if neighbor not in visited:
#         queue.append(neighbor)
#   return False
  
def has_path(graph, src, dst, visited):
  if src == dst:
    return True 
  if src in visited:
    return False
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True 
  return False
  
  
def create_graph(edges):
    graph = {}
    
    for edge in edges:
      a, b = edge
      # collecting the edge pairs
      
      if a not in graph:
        graph[a] = []
      if b not in graph:
        graph[b] = []
      graph[a].append(b)
      graph[b].append(a)
    return graph

def largest_component(graph):
  max = 0
  # this will be used to check the intersection length
  visited = set()
  for node in graph:
    size = explore_size(graph,node, visited)
    if size>max:
      max = size 
  return max
def explore_size(graph, node, visited):
  if node in visited:
    return 0
  visited.add(node)
  
  size=1
  for neighbor in graph[node]:
    size+=explore_size(graph, neighbor, visited)
  return size
