# Write a function greet that takes in a string argument, s, and returns the string "hey s". No tricks here. Run the tests to check your work.

def greet(s):
    print("hey " + s)


greet('hi')

def max_value(nums):
    max=float('-inf')
    for num in nums:
      if num>max:
        max=num 
        
    return max
# time:  O(n)
# space: O(1)
def is_prime(n):
  if n<2:
    return False
  for num in range(2,n-1):
    if n%num ==0:
      return False 
    
  return True
from math import sqrt, floor
def is_prime_sqrt(n):
  if n<2:
    return False
  for num in range(2, floor(sqrt(n)+1)):
    if n % num == 0:
      return False 
    
  return True
# my solution
def uncompress(s):
  result=""
  num=""
  for i in range(0,len(s)):
    if s[i].isdigit():
      num=num+s[i]
    else:
      result = result + int(num)*s[i]
      num=""
      
  return result

# using two pointers
def uncompress(s):
# a number greater than 9 
# i will need to loop through the string
# i will need a result to store the uncompressed string

  result =[]
  # i am using a list because python adds to strings in linear time 
  #  i will need to use two pointers in order to identify the number and letters
  pointer_1 = 0 
  #  this pointer will be used to track the start of a number
  pointer_2 = 0
  # this pointer will be used to track the end of a number 

  while pointer_1 < len(s):
    if s[pointer_2].isdigit():
      pointer_2+=1 
    else:
      num = int(s[pointer_1:pointer_2])  
  #     turn the num into an int 
      result.append(num*s[pointer_2])
      pointer_2+=1
      pointer_1=pointer_2
  return "".join(result)

def compress(s):
  s+='!'
  result=[]
  i=0
#   this first pointer will be used for the start of a character
  j=0
  # this second is to determine the end of a character
  
  while j < len(s):
    if s[i] == s[j]:
      j+=1
    else:
      num = str(j-i)
      if (int(num)==1):
        result.append(s[i])
      else:
        result.append(num+s[i])
      i=j 
  return ''.join(result)


def five_sort(nums):
  pointer_5=0 
  pointer_not5=0 
  while pointer_not5 < len(nums):
    if (nums[pointer_not5]==5):
      pointer_not5+=1
    else:
      nums[pointer_5], nums[pointer_not5] = nums[pointer_not5], nums[pointer_5]
      pointer_not5+=1
      pointer_5+=1
      # nums[pointer_5], nums[pointer_not5] = nums[pointer_not5], nums[pointer_5]
  return nums