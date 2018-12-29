"""

  Mutable and immutable objects in Python

  OBS! In Python everything is an object!

"""


# numbers are immutable:
print(type(10), id(10));
print(type(100), id(100));

a = 10
print(a, type(a), id(a))

a *= a
print(a, type(a), id(a))

a = 100
print(a, type(a), id(a))


# strings are immutable
print(type('aaa'), id('aaa'));
print(type('AAA'), id('AAA'));

b = 'aaa'
print(b, type(b), id(b))

b = 'AAA'
print(b, type(b), id(b))


# booleans are immutable
print(type(False), id(False))
print(type(True), id(True))

c = True
print(c, type(c), id(c))

c = not c
print(c, type(c), id(c))


# lists are mutable
list_ex = [10, 52, 65, 85]
print(list_ex, type(list_ex), id(list_ex))

list_ex.append(75)
print(list_ex, type(list_ex), id(list_ex))

list_ex.append(True)
print(list_ex, type(list_ex), id(list_ex))

list_ex.append(False)
print(list_ex, type(list_ex), id(list_ex))

list_ex.append('Marius is drinking beer.') # with mypy this will show a warning
print(list_ex, type(list_ex), id(list_ex))

list_ex.append([1, 2, 3]) # with mypy this will show a warning
print(list_ex, type(list_ex), id(list_ex))


# tuples are immutable
tuple_ex = 'Borsa Street', 46, 'sectorul 1', 'Bucharest' # with mypy this will show a warning
print(tuple_ex, type(tuple_ex), id(tuple_ex))
print(tuple_ex[0], tuple_ex[1], tuple_ex[2])
# tuple_ex[2] = 'sectorul 2' - this will throw an error
print(tuple_ex, type(tuple_ex), id(tuple_ex))