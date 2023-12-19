def depth_first_values(root):
  # DFS always uses a stack 
  if not root:
    return []
  stack = [root]
  values = []
  
  # can be done recursively or non recursively 
  
  while len(stack) > 0:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values

from collections import deque
def breadth_first_values(root):
  if root is None:
    return []
  #bfs uses a queue 
  
  queue =deque([root])
  values = []
  while len(queue) > 0:
    node = queue.popleft()
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
  return values


def tree_sum(root):
  # i can solve this using DFS or BFS
  
  if root is None:
    return 0 
  
  left_sum = tree_sum(root.left)
  right_sum = tree_sum(root.right)
  
  return root.val + left_sum + right_sum

def tree_sum_dfs_iterative(root):
  # i can solve this using DFS or BFS
  if root is None:
    return 0
  stack = [(root,root.val)]
  sum = 0
  
  while stack:
    node, val = stack.pop()
    sum += val 
    
    if node.right:
      stack.append((node.right, node.right.val))
    if node.left:
      stack.append((node.left, node.left.val))
  return sum

def tree_sum_bfs(root):
  if root is None:
    return 0
  sum = 0 
  queue = deque([root])
  
  while queue:
    node = queue.popleft()
    sum += node.val 
    
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
      
  return sum

def tree_includes(root, target):
  # i can solve this using BFS or DFS
  
  if root is None:
    return False 
  if root.val == target:
    return True 
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)

def tree_min_value(root):
  
  if root is None:
    return float("inf")
  left = tree_min_value(root.left)
  right = tree_min_value(root.right)
  return min(root.val, left, right)

def max_path_sum(root):
  
  if root is None:
    return float("-inf")
  if root.left is None and root.right is None:
    return root.val
  
  left = max_path_sum(root.left)
  right = max_path_sum(root.right)
  
  return root.val + max(left, right)

def max_path_sum(root):
  
  if root is None:
    return float("-inf")
  
  if root.left is None and root.right is None:
    # i have hit a leaf
    return root.val 
  
  return root.val + max(max_path_sum(root.left),max_path_sum(root.right))

def max_path_sum(root):
  stack = [(root, root.val)]
  
  max_sum = float('-inf')
  
  while stack:
    node, sum = stack.pop()
    
    if node.left is None and node.right is None:
      max_sum = max(sum, max_sum)
      
    if node.left:
      stack.append((node.left, node.left.val+sum))
      
    if node.right:
      stack.append((node.right, node.right.val+sum))
  return max_sum


def path_finder(root, target):
  
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [root.val, *left_path]
  
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [root.val, *right_path]
  
  return None

def path_finder_bfs(root, target):
  if root is None:
    return None
  queue = deque([(root, [root.val])])
  
  while queue:
    node, path = queue.popleft()
    if node.val == target:
      return path 
    
    if node.left:
      queue.append((node.left, [*path, node.left.val]))
      
    if node.right:
      queue.append((node.right, [*path, node.right.val]))
  
  return None

def tree_value_count(root, target):
  if root is None:
    return 0
  count = 0 
  queue = deque([root])
  
  while queue:
    node = queue.popleft()
    
    if node.val == target:
      count +=1 
      
    if node.left:
      queue.append(node.left)
    
    if node.right:
      queue.append(node.right)
  return count

def how_high(node):
  
  if node is None:
    return -1
  
  return 1 + max(how_high(node.left), how_high(node.right))


def all_tree_paths(root):
  # i can do this with DFS, or BFS
  
  # i can store the paths in a tuple
  # and store once there is no left or right 
  if root is None:
    return []
  
  if root.left is None and root.right is None:
    return [ [root.val]]
  
  paths = []
  
  left_sub_paths = all_tree_paths(root.left)
  
  for sub_path in left_sub_paths:
    paths.append([root.val, *sub_path])
  
  right_sub_paths = all_tree_paths(root.right)
  
  for sub_path in right_sub_paths:
    paths.append([ root.val, *sub_path])
  return paths

def tree_levels(root):
  levels=[]
  _tree_levels(root, levels, 0)
  return levels
  
      
def _tree_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([root.val])
  else:
    levels[level_num].append(root.val)
  
  _tree_levels(root.left, levels, level_num_+1)
  _tree_levels(root.right, levels, level_num+1)

def leaf_list(root):
  leaves = []
  _fill_leaves(root, leaves)
  return leaves
def _fill_leaves(root, leaves ):
  if root is None:
    return 
  
  if root.left is None and root.right is None:
    leaves.append(root.val)
  _fill_leaves(root.left, leaves)
  _fill_leaves(root.right, leaves)