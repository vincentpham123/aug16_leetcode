def fib(n):
  sequence = [];
  memo = {}
  for i in range(n):
    sequence.append(_fib(i,memo));
  return sequence;
def _fib(n, memo):
  if n == 0 or n ==1:
    return n
  if n in memo:
    return memo[n]
  
  memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
  
  return memo[n]

def tribonacci(n):
  memo = {}
  return _trib(n, memo)

def _trib(n, memo):
  if n in memo:
    return memo[n]
  if n == 0 or n ==1:
    return 0
  if n ==2:
    return 1 
  memo[n] = _trib(n-1,memo) + _trib(n-2,memo) + _trib(n-3,memo)
  return memo[n]


def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})
def _sum_possible(amount, numbers, memo):
  # i will be subtracting from number from amount until it is 0 
  if amount == 0:
    return True 
  if amount < 0:
    return False 
  
  for num in numbers:
    if _sum_possible(amount-num, numbers, memo):
      memo[amount] = True 
      return True 
  memo[amount] =  False 
  return False


def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
    return -1
  else:
    return ans

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  if amount == 0:
    return 0
  if amount < 0 :
    return float('inf')
  
  size = float('inf')
  for coin in coins:
    temp_size = 1 + _min_change(amount-coin, coins, memo)
    size = min(size, temp_size)
    
  memo[amount] = size
  return size

def count_paths(grid):
  return _count_paths(grid, 0,0, {})

def _count_paths(grid,r,c, memo):
  
  pos = (r,c)
  
  if pos in memo: 
    return memo[pos]
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  if r== len(grid)-1 and c == len(grid[0]) -1:
    return 1
  memo[pos] = _count_paths(grid, r +1, c, memo) + _count_paths(grid, r,c+1,memo)
  return memo[pos]