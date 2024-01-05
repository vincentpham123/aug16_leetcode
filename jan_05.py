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