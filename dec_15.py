def uncompress(s):
  result =[]
  numbers = '01233456789'
  # when i come across a number, i know I have to multiply it 
  
  i = 0
  j=0
  
  while j < len(s):
    if s[j] in numbers:
      # i know i have hit a number 
      j+=1 
    else:
      num = int(s[i:j])
      result.append(s[j]*num)
      j+=1 
      i=j 
  return ''.join(result)

def compress(s):
  # this is also a two pointer
  # the only difference is that i am checking for different letters
  s +='!'
  i = 0
  j = 0
  result =[]
  
  while j < len(s):
    if s[j] == s[i]:
      j+=1
    else:
      # when i hit a different letter 
      # j will be at the different number
      num = j - i 
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num))
        result.append(s[i])
      i = j
  
  return ''.join(result)


def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)
  
def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] +=1 
  return count