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

def pair_sum(numbers, target_sum):
  
  prev_nums = {}
  
  for index, num in enumerate(numbers):
    other_sum = target_sum - num
    
    if other_sum in prev_nums:
      return(index, prev_nums[other_sum])
    # i will always record numbers in the dictionary, this way i have a linear look up time 
    
    prev_nums[num] = index

def pair_product(numbers, target_product):
  
  previous_num = {}
  
  for index, num in enumerate(numbers):
    other_num = target_product/num
    
    if other_num in previous_num:
      return (index, previous_num[other_num])
    previous_num[num] = index

def intersection(a, b):
  result_1 = set()
  
  result = []
  
  for num in a:
    result_1.add(num)
    
  for num in b:
    if num in result_1:
      result.append(num)
      
  return result


def five_sort(nums):
  
  i = 0 
  j = len(nums) - 1
  # i need i to check for 5s and J to keep track of numbers at the end that arent 5
  # when i come across a 5 on index i, i switch with j 
  # my conditions will check if j is not on a 5, and if i is on a 5 
  # i will keep doing this until i and j meet 
  
  while i < j:
    if nums[j]==5:
      j-=1 
    elif nums[i]!=5:
      i+=1 
    else:
      # this condition will hit when i = 5
      nums[i], nums[j] = nums[j], nums[i]
      
      i+=1 
      
  return nums