'''

  Math and Random modules

'''

# Math module
from math import pi

pi = 666 # this will overwrite pi value

print(pi)

from math import *

print(factorial(round(pow(pi, 2))))

import math as m

print(m.pi)
print(m.floor(m.pi))
print(m.ceil(m.pi))

print(-m.pi)
print(m.floor(-m.pi))
print(m.ceil(-m.pi))

# Random module
import random
print(random.random())
print(round(random.random() * 100, 2))

print(random.choice([1, 2, 9, 20 ,21, 54, 56, 24, 14, 12, 16, 12, 14, 16, 192, 60]))

numbers = list(range(10, 200, random.randint(2, 9)))
print(random.choice(numbers))
print(random.choices(numbers, k = random.randint(2, 15)))