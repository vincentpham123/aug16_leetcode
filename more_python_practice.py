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