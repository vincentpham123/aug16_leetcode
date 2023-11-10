def binary_search(numbers, target):
  if len(numbers) == 0:
    return -1
  
  midpoint = len(numbers)//2
  
  if numbers[midpoint] < target:
    result= binary_search(numbers[midpoint+1:],target)
    if result == -1:
      return -1
    else:
      return result + midpoint + 1
 
  elif numbers[midpoint] > target:
    return binary_search(numbers[:midpoint],target)
  else:
    return midpoint
  
def binary_search(numbers, target):
  
  
  left = 0 
  right = len(numbers)-1
  
  while left <= right:
    midpoint = right+left //2 
    
    if numbers[midpoint] < target:
      left = midpoint +1 
    elif numbers[midpoint] > target:
      right = midpoint-1 
    else:
      return midpoint
  return -1

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def binary_search_tree_includes(root, target):
  if root is None:
    return False
  if root.val == target:
    return True 
  
  if root.val < target:
      return binary_search_tree_includes(root.right, target)
  else:
      return binary_search_tree_includes(root.left, target)
  

def is_binary_search_tree(root,min_val = float('-inf'),max_val=float('inf')):
    if root is None:
        return True

    if not (min_val <= root.val <= max_val):
        return False 

    return (is_binary_search_tree(root.left, min_val, root.val) and
        is_binary_search_tree(root.right, root.val, max_val))


def post_order(root):
  values=[]
  _post_order(root,values)
  return values
def _post_order(root,values):
  if root is None:
    return
  
  _post_order(root.left, values)
  _post_order(root.right, values)
  values.append(root.val)