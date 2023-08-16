# Write a function greet that takes in a string argument, s, and returns the string "hey s". No tricks here. Run the tests to check your work.

def greet(s):
    print("hey " + s)


greet('hi')

def max_value(nums):
    max=nums[0]
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