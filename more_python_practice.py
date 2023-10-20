def binary_search(numbers, target):
  if len(numbers) == 0:
    return -1
  
  midpoint = len(numbers)//2
  
  if numbers[midpoint] < target:
    # result= binary_search(numbers[midpoint+1:],target)
    # if result == -1:
    #   return -1
    # else:
    #   return result + midpoint + 1
    return binary_search(numbers[midpoint+1:],target)
  elif numbers[midpoint] > target:
    return binary_search(numbers[:midpoint],target)
  else:
    return midpoint