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
    

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None 
  if head_1 is None:
    return head_2 
  if head_2 is None:
    return head_1
  
  next_1 = head_1.next 
  next_2 = head_2.next 
  head_1.next = head_2 
  head_2.next = zipper_lists(next_1, next_2)
  
  return head_1 

def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2 
  if head_2 is None:
    return head_1 
  
  # i need to compare the values of head_1 and head_2 
  if head_1.val < head_2.val:
    # if this is the case, i know that head_1 will be first and 
    next_1 = head_1.next 
    head_1.next = merge_lists(next_1, head_2)
    return head_1 
  else:
    next_2 = head_2.next 
    head_2.next = merge_lists(head_1, next_2)
    return head_2 
  
def merge_lists(head_1, head_2):
  
  # i know that i will need to compare each val of head_1 and head_2 
  
  dummy = Node(None)
  tail = dummy 
  # i can use a dummy_head to start off the new linked list 
  
  current_1 = head_1 
  current_2 = head_2 
  
  while current_1 is not None and current_2 is not None:
    
    # this is when i will compare the values 
    
    if current_1.val < current_2.val:
      tail.next = current_1 
      current_1 = current_1.next 
    else:
      tail.next = current_2 
      current_2 = current_2.next 
    tail = tail.next
  if current_1 is None:
    tail.next = current_2 
  if current_2 is None:
    tail.next = current_1 
    
  return dummy.next
    
def is_univalue_list(head, prev = None):
  if head is None:
    return True 
  if prev is None or head.val == prev:
    return is_univalue_list(head.next, head.val)
  else:
    return False
  
def longest_streak(head):
  
  max_streak = 0
  current_streak = 0 
  prev_val = None
  
  current_node = head 
  
  while current_node is not None:
    if current_node.val == prev_val:
      current_streak+=1 
    else:
      current_streak = 1 
    prev_val = current_node.val 
    
    if current_streak > max_streak:
      max_streak = current_streak
    
    current_node = current_node.next 
  return max_streak

def remove_node(head, target_val):
  # in order to remove the node, i need to keep track of the prev 
  
  current = head 
  prev = None 
  if head.val == target_val:
    next = head.next 
    head.next = prev 
    return next
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      return head
    prev = current 
    current = current.next 
## recursively 
#   if head is None:
#     return None 
  
#   if head.val == target_val:
#     return head.next 
  
#   head.next = remove_node(head.next, target_val)
  
#   return head

def insert_node(head, value, index):
  
  if index == 0:
    new_head = Node(value)
    new_head.next = head 
    return new_head 
  count = 0
  current = head 
  
  while current is not None:
    if count == index -1:
      temp = current.next 
      current.next = Node(value)
      current.next.next = temp 
    count +=1 
    current = current.next 
  return head

def insert_node_recursive(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head 
    return new_head 
  
  if head is None:
    return None
  
  if index == 1:
    temp = head.next 
    head.next = Node(value)
    head.next.next = temp 
    return 
  insert_node(head.next, value, index-1)
  return head 

def create_linked_list(values):
  dummy_head = Node(None)
  current = dummy_head
  for value in values:
    current.next = Node(value)
    current = current.next 
  return dummy_head.next

#   if index == len(values):
#     return None
#   head = Node(values[index])
#   head.next = create_linked_list(values, index+1)
#   return head
