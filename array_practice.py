def uncompress(s):
  result=[]
  numbers = '0123456789'
  i = 0
  j = 0
  
  while j < len(s):
    if s[j] in numbers:
      j +=1
    else:
      num = int(s[i:j])
      result.append(s[j]*num)
      j+=1 
      i=j 
  return ''.join(result)

def compress(s):
  s+='!'
  result=[]
  
  i=0
  j=0 
  
  while j<len(s):
    if s[i]==s[j]:
      j+=1 
    else:
      num = j-i
      if num==1:
        result.append(s[i])
      else:
        result.append(str(num)+s[i])
      i=j
      j+=1 
      
  return ''.join(result)

def compress(s):
  s +='!'
  result = []
  i=0
  j=0 
  
  while j < len(s):
    if s[i] == s[j]:
      j+=1
    else:
      # i now know that their is a different letter 
      num_of_letters = j - i
      # this will provide the amount of letters to add to the result
      if num_of_letters ==1:
        result.append(s[i])
      else:
        result.append(str(num_of_letters))
        result.append(s[i])
      i=j 
      
  return ''.join(result)