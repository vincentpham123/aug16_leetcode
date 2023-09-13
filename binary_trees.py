
def depth_first_values(root):
  # will use a stack 
  if not root:
    return []
  stack=[root]
  result=[]
  while stack:
    node = stack.pop()
    result.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return result

def depth_first_values_recursive(root):
  # will use a stack 
  if not root:
    return []
  left_value = depth_first_values(root.left)
  right_value= depth_first_values(root.right)
  
  return [root.val,*left_value,*right_value]

def breadth_first_values(root):
  # will use a queue
  if root is None:
    return []
  queue=[root]
  result=[]
  
  while queue:
    node = queue.pop(0)
    result.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return result


def tree_includes(root, target):
  stack=[root]
  if not root:
    return False
  while stack:
    node = stack.pop()
    if node.val == target:
      return True 
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return False

def tree_includes(root, target):
  if not root:
    return False
  
#   stack=[root]
 
#   while stack:
#     node = stack.pop()
#     if node.val == target:
#       return True 
#     if node.left:
#       stack.append(node.left)
#     if node.right:
#       stack.append(node.right)
#   return False  
  queue = [root]
  while queue:
    node = queue.pop(0)
    if node.val == target:
      return True 
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return False

def tree_min_value(root):
  if root is None:
    return float("inf")
  min_left = tree_min_value(root.left)
  min_right = tree_min_value(root.right)
  
  return min(root.val,min_left,min_right)

def max_path_sum(root):
    if not root:
      return 0
    stack = [(root,root.val)]
    
    max_sum=float("-inf")
    
    while stack:
      node, current_sum = stack.pop()
      if node.left is None and node.right is None:
        max_sum = max(max_sum,current_sum)
      if node.left:
        stack.append((node.left,current_sum+node.left.val))
      if node.right:
        stack.append((node.right, current_sum + node.right.val))
    return max_sum

from collections import deque
def bottom_right_value(root):
  # take advantage of breath first search
  # depending on if i add from left node or right node 
  # i can return the last node from the queue 
  # i can reassign a node everytime 
  queue = deque ([root])
  
  result = root.val
  
  while queue:
    node = queue.popleft()
    result = node.val
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return result

def all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]
  paths=[]
  
  left = all_tree_paths(root.left)
  for sub_path in left:
    paths.append([root.val,*sub_path])
  right = all_tree_paths(root.right)
  for sub_path in right:
    paths.append([root.val,*sub_path])
  return paths

from collections import deque
def tree_levels(root):
  if root is None:
    return []
  queue = deque([(root,0)])
  levels = []
  while queue:
    node, current_level = queue.popleft()
    if len(levels) == current_level:
      levels.append([node.val])
    else:
      levels[current_level].append(node.val)
    
    
    if node.left:
      queue.append((node.left,current_level + 1 ))
    if node.right:
      queue.append((node.right, current_level +1))
  return levels

from statistics import mean
def level_averages(root):
  levels= []
  fill_levels(root,levels, 0)
  avgs=[]
  for level in levels:
    avgs.append(mean(level))
  return avgs

def fill_levels(root,levels, level_num):
  if root is None:
    return
  if level_num == len(levels):
    levels.append( [ root.val ])
  else:
    levels[level_num].append(root.val)
  
  fill_levels(root.left, levels, level_num + 1)
  fill_levels(root.right, levels, level_num+1)
from collections import deque
def leaf_list(root):
  leaves = []
  _leaf_list(root,leaves)
  return leaves 
def _leaf_list(root,leaves):
  if root is None:
    return 
  if root.left is None and root.right is None:
    leaves.append(root.val)
  _leaf_list(root.left,leaves)
  _leaf_list(root.right,leaves)