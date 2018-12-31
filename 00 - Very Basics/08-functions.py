'''

  Functions in Python

'''

def add(a: float, b: float) -> float:
  return a + b

print(int(add(10, 20)))

def total_marks(m1:int, m2: int, m3: int) -> int:
  return m1 + m2 + m3

def average(m1: int, m2: int, m3: int) -> float:
  return total_marks(m1, m2, m3) / 3

def grade(m1, m2, m3) -> str:
  avg = average(m1, m2, m3)
  if avg >= 80:
    return 'A'
  elif avg >=60:
    return 'B'
  elif avg >= 40:
    return 'C'
  else:
      return 'F'

print(grade(10, 80, 100))

def say_hello(name: str) -> None:
  print('Hello, {}!'.format(name))

say_hello('John')

variable1 = 50

def increment_with_10() -> int :
  variable1 = 50 # variable1 will be a local variable
  variable1 += 10
  print('Local scope:', variable1, id(variable1))
  return variable1

print('Global scope:', variable1, id(variable1))
print(increment_with_10())
print(variable1)
print('*' * 100)

def increment_with_20() -> int :
  global variable1 # variable1 will access global variable1
  variable1 += 20
  print('Local(?) scope:', variable1, id(variable1))
  return variable1

print(increment_with_20())
print('Global scope:', variable1, id(variable1))
print(variable1)

help(increment_with_10)

array1 = [3, 5, 6, 3, 3, 33, 44, 5, 30, 903, 13, 44]
print(min(array1))
print(max(array1))

def documented_sum(a: float, b: float) -> float:
  '''
    This function will add 2 floats:
    :param a:
    :param b:
    :return a + b

  '''
  return a + b

print('{} + {} = {}'.format(10, 20, documented_sum(10, 20)))
print(documented_sum.__doc__)
help(documented_sum)

def function(
  arg1: int,
  arg2: int,
  arg3: int,
  arg4: int
) -> int:
  return arg1 + arg2 + arg3 + arg4

print(function(10, 30, 40, 50))

def calculate(n: int, *args:int) -> int:
  return n * sum(args)

help(sum)

print(calculate(2, 5, 6, 2))

student_marks = [25, 68, 88, 95, 100, 32, 45, 70, 90, 98, 2]
print(tuple(filter(lambda mark: mark > 60, student_marks)))

