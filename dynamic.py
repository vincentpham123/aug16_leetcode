def fib(n):
  memo = {}
  return _fib(n, memo)
def _fib(n,memo):
  if n == 0 or n==1:
    return n
  if n in memo:
    return memo[n]
  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
  return memo[n]

def sum_possible(amount, numbers, memo={}):
    # will subtract from amount until it is too small
    # i know if i am able to subtract the amount to zero, 
    #using the numbers then sumpossible is true else false
    if amount in memo:
      return memo[amount]
    if amount == 0:
      return True
    if amount < 0:
      return False
    
    for num in numbers:
      if sum_possible(amount-num, numbers) == True:
        memo[amount] = True
        return True
    
      # i need to check that true is returned from sumpossible
      # it will recursivelysubtract from amount until it is 0 or less than 0
    memo[amount] = False
    return False  

def max_path_sum(grid):
  return _max_path_sum(grid,0,0,{})
def _max_path_sum(grid, r=0, c=0,memo={}):
  pos = (r,c)
  if pos in memo:
    return memo[pos]
  if r== len(grid) or c== len(grid[0]):
    return float('-inf')
  # returning negative infinity because it be compared with another sum
  if r==len(grid)-1 and c== len(grid[0])-1:
    return grid[r][c]
  
  down = _max_path_sum(grid,r+1,c)
  right = _max_path_sum(grid,r,c+1)
  
  memo[pos] = grid[r][c] + max(down,right)
  return memo[pos]

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})
def _non_adjacent_sum(nums, i=0,memo={}):
  if i in memo:
    return memo[i]
  if i >= len(nums):
    return 0
  
  # exmaple 
  # [2,3,5,12,7]
  # when we call at i =0 (2)
  # we need to choose if we are including 2 into the sum
  
  exclude = _non_adjacent_sum(nums, i+1)
  include = nums[i] + _non_adjacent_sum(nums, i+2)
  memo[i] = max(include, exclude)
  
  return memo[i]