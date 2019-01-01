'''

  Creating a very basic module in Python

'''
languages = {'Basic', 'QBasic', 'Cobol', 'Pascal', 'Assembly', 'C/C++', 'Java', 'Python', 'Ruby'}

values = 10, 50, 60, 11, 98, 75, 65, 32

def add(*args: float) -> float:
  sum = 0.0
  for value in args:
    sum += value
  return sum

def multiply(*args: float) -> float:
  prod = 1.0
  for value in args:
    prod *= value
  return prod

def _prime(number: int) -> bool:
  if number <= 1:
    return False
  elif number == 2:
    return True
  elif number % 2 == 0:
    return False
  else:
    for n in range(3, int(number ** 0.5), 2):
      if number % n == 0:
        return False
    else:
      return True



