
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