'''

  Exception Handeling in Python


'''

string = 'Python Programming'
word = input('What word do you want to search for? ')
index = -1

try:
  index = string.index(word)
except ValueError:
  print('Cannot find the substring you are searching.')
finally:
  # This will be run no matter what.
  print('String {} contains word {} at position {}.'.format(string, word, index))

print(string.upper())
print(len(string))

while True:
  try:
    a = int(input('a = '))
    b = int(input('b = '))
    if b < 0:
      raise TypeError('The second value must be positive.', 'I hate negative numbers.', 'David Bowie is dead...')
    division = a / b
    print('{} / {} = {}'.format(a, b, division))
  except ZeroDivisionError as error:
    print(error)
  except ValueError:
    print('Please enter 2 integers...')
  except Exception as error:
    print('There was an error: {}.'.format(error.args[2]))
  else:
    print('Everything worked fine... Have a nice day!')
    break
