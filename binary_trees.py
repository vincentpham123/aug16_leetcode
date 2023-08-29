
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