class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c 
c.next = d

#a -> b -> c -> d

def printList(head):
    # current = head 
    # while current is not None: 
    #     print(current.val)
    #     current=current.next
    if head is None:
        return 
    print(head.val) 
    printList(head.next)

printList(a)

def linked_list_values(head):
  result=[]
  current = head
  while current is not None:
    result.append(current.val)
    current=current.next
  return result


def sum_list(head):
  sum=0 
  current=head 
  while current is not None:
    sum +=current.val 
    current=current.next 
  return sum 

def linked_list_find(head, target):
  if head is None:
    return False 
  if head.val == target:
    return True 
  
  return linked_list_find(head.next,target)

def get_node_value(head, index):
  list_order=0 
  current = head 
  while current is not None:
    if list_order == index:
      return current.val 
    current = current.next 
    list_order+=1
  return None
    #recursive method
    # if head is None:
    #     return None
    # if index==0:
    #     return head.val 
    # return get_node_value(head.next,index-1)

def reverse_list(head):
  # need to change the next to the prev 
  # track prev and next 
  prev = None
  current = head
  while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node 
  return prev


def zipper_lists(head_1, head_2):
  tail = head_1 
 #start off the tail with head_1 
# from there I will switch between head_2 and head_1
  #to keep track i know that head_2 will be all odd indexes
  
  turn = 'odd'
  current_1 = head_1.next
  current_2 = head_2 
  
  while current_1 is not None and current_2 is not None:
    if turn == 'odd':
      tail.next = current_2 
      current_2 = current_2.next 
      turn = 'even'
    else:
      tail.next = current_1 
      current_1 = current_1.next 
      turn = 'odd'
    tail = tail.next 
  # once one of the linked list runs out
  # the condition will fail
  if current_1 is not None:
    tail.next = current_1 
  if current_2 is not None:
    tail.next = current_2
  return head_1

def merge_lists(head_1, head_2):
  dummy_tail = Node(None) 
  tail = dummy_tail 
  current_1 = head_1
  current_2 = head_2 
  
  while current_1 is not None and current_2 is not None:
    if current_1.val <= current_2.val:
      tail.next = current_1 
      current_1 = current_1.next 
    else:
      tail.next = current_2 
      current_2 = current_2.next 
    tail = tail.next 