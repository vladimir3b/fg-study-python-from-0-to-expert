'''

  Importing a module in Python

'''

import m01_module_math_functions as mf

print(dir())
print(dir(mf))
print(mf.__name__)
print(mf.__file__)
help(mf)
print(mf._prime(21))

from m01_module_math_functions import *

print(languages)
print(add(1, 2, 3, 4, 5, 6))
# print(_prime(21)) - this won't work

from m01_module_math_functions import _prime
print(_prime(21)) # now this will work

import module1.submodule1.default as default

default.module_testing()

from module1.test import message

print(message)