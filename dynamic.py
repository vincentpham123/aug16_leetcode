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