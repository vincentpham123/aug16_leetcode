# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  result = []
  
  current = head 
  while current is not None:
    result.append(current.val)
    current = current.next 

  return result


def sum_list(head):
  sum = 0
  current = head 
  
  while current is not None:
    sum += current.val 
    current = current.next 
  return sum


def linked_list_find(head, target):
  current = head 
  
  while current is not None:
    if current.val == target:
      return True 
    current = current.next 
    
  return False

#     if head is None:
#     return False 
  
#   if head.val == target:
#     return True 
  
#   return linked_list_find(head.next, target)

def get_node_value(head, index):
  
  if index == 0:
    return head.val 
  
  if head is None:
    return None 
  
  return get_node_value(head.next, index-1)

def reverse_list(head):
  
  prev = None 
  current = head 
  
  while current is not None:
    # i need to change current.next to prev 
    next = current.next 
    current.next = prev 
    prev = current 
    current = next 
  return prev
    