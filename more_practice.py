def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  
  for i in range(length):
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
    if value_1 < value_2:
      return True 
    elif value_2 < value_1:
      return False 
  return True

def linked_palindrome(head):
  values = []
  current = head 
  while current is not None:
    values.append(current.val)
    current = current.next 
    
  return values == values[::-1]

def paired_parentheses(string):
  count = 0
  
  for char in string:
    if char == '(':
      count +=1
    if char == ')':
      if count == 0:
        return False 
      count -=1
  
  return count == 0


def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
  }
  
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False 
  return len(stack) == 0 


def decompress_braces(string):
  numbers = '12345789'
  stack = []
  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      # i know that i will be encounter my brackets
      if char == '}':
        segment =''
        while isinstance(stack[-1],str):
          popped = stack.pop()
          segment = popped + segment 
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)


def subsets(elements):
  if len(elements) == 0:
    return [[]]
  first = elements[0]
  without_first = elements[1:]
  
  subs_withoutfirst = subsets(without_first)
  subsets_with_first=[]
  for sub in subs_withoutfirst:
    subsets_with_first.append([first,*sub])
  
  return subs_withoutfirst + subsets_with_first

def nesting_score(string):
  stack = [0]
  
  for char in string:
    if char == '[':
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] +=1 
      else:
        stack[-1] += 2 * popped 
  return stack[0]

def linked_palindrome(head):
  values = []
  current = head 
  while current is not None:
    values.append(current.val)
    current = current.next 
    
  return values == values[::-1]
def middle_value(head):
    values = []
    
    current = head 
    
    while current is not None:
      values.append(current.val)
      current = current.next 
    return values[len(values)//2]

def middle_value(head):
  slow = head 
  fast = head 
  
  while fast is not None and fast.next is not None:
    slow = slow.next 
    fast = fast.next.next 
  return slow.val

def linked_list_cycle(head):
  nodes = set()
  
  current = head 
  
  while current is not None:
    if current in nodes:
      return True
    
    nodes.add(current)
    current = current.next 
  return False

def lowest_common_ancestor(root, val1, val2):
  path1 = find_path(root,val1)
  path2 = find_path(root,val2)
  set2 = set(path2)
  
  for val in path1:
    if val in set2:
      return val

def find_path(root, target_val):
  if root is None:
    return None 
  
  if root.val == target_val:
    return [ root.val]
  
  left_path = find_path(root.left, target_val)
  
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  right_path = find_path(root.right, target_val)
  
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  return None