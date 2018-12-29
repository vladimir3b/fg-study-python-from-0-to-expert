'''

  Loops in Python

'''

# while loop
number = int(input('Give me a number: '))
original_number = number
factorial = 1
while number >= 2:
  factorial *= number
  number -= 1
print('%s! = %s'%(original_number, factorial))

i = 0
while (i <= original_number):
  i += 1
  if (i % 30 == 0):
    break # This means 'exit loop'
  if (i % 5 == 0):
    continue # This means 'skip to next value'
  if (i % 3 == 0):
    pass # This means 'do nothing'
  print(i, end = ', ')
else:
  print('\b\b \nThere was no number divisible by 30')

# for loop
array1 = [21, 25, 45, 45, 87, 96, 55, 69, 1, 0, 2]
for element in array1:
  print(element, end = ' ')
print('\n', '*' * 20)

for index in range(0, len(array1), 2):
    print('array1[%s] = %s'%(index, array1[index]))

for element in reversed(sorted(array1)):
  print(element, end = ' ')

for element1 in enumerate(array1):
  print(element1, end = ' ')

for index, element in enumerate(array1):
  print('%s : %s'%(index, element), end = '\n')

persons = 'John', 'Elisa', 'Marry', 'Maria', 'Joseph', 'Elisabeth', 'Bon', 'Ben', 'Nick'
ages = [40, 25, 60, 21, 33, 28]
professions = 'cook', 'programmer', 'boxer', 'hitman', 'salesman', 'designer', 'photographer'

for [person, age, profession] in zip(persons, ages, professions):
  print('Name : %s, Age : %s, Profession : %s'%(person, age, profession))

print('*' * 20)

for (person, age, profession) in zip(persons, ages, professions):
  print('Name : %s, Age : %s, Profession : %s'%(person, age, profession))

print('*' * 20)

for person, age, profession in zip(persons, ages, professions):
  print('Name : %s, Age : %s, Profession : %s'%(person, age, profession))

while True:
  number1 = int(input('Give me a number '))
  if number1 % 2 == 0:
    print('%s is not a prime number.'%number1)
  else:
    for i in range(3, int(number1 ** 0.5), 2):
      if number1 % i == 0:
        print('%s is not a prime number.'%number1)
        break
    else:
      print ('%s is a prime number.'%number1)
  if input('Do you want to continue? ') in 'yes YES yap YAP':
    continue
  else:
    break

while True:
  limit = int(input('Give the superior limit(must be greater than 2) '))
  if limit >= 3:
    break
print('Prime numbers smaller than %s are : 2, '%limit, end = '')
for number in range(2, limit):
  if number % 2 == 0:
    continue
  for i in range(3, int(number * 0.5), 2):
    # print(number, i, number % i)
    if number % i == 0:
      break
  else:
    print(number, end = ', ')
print(end = '\b\b.')


