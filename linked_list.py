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