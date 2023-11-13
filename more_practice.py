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