"""

  Comparators, Flow Control, Boolean Operators, If/Else/Elif

"""

print(3.14159265358979 != 3.1415, 3.1415 < 3.1415, 3.1415 == 3.14159)
print(True and False, True or False, not True, not False and not True or not False)

number = int(input('Give a number: '))

if number <= 10:
  print('%s is a very small number.'%(number))
elif number <= 100:
  print('%s is a small number.'%(number))
elif number <= 10000:
  print('%s is a big number.'%(number))
elif number <= 10000000:
  print('%s is a very big number.'%(number))
else:
  print('%s is a huge number.'%(number))

if 10 <= number <= 120:
  if input('Are you %s years old ? '%number) in 'yes YES Yes yap YAP Yap':
    print('I\'ve guessed it!')
  else:
    print('Ups! I thought so...')
elif 0 <= number and number <= 9:
  if input('Are you a child? ') in 'yes YES Yes yap YAP Yap':
    print('I\'ve guessed it!')
  else:
    print('Ups! I thought so...')
else:
  print('This cannot be a human age...')