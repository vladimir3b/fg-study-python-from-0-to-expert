'''

  Sets and Dictionaries

'''

# sets - sets are mutable
A = {1, 0, 6, 7, 9, 9, 6, 10, 25, 66, 38}
B = set({0, 6, 9, 25, 40, 90, 125, 654, 826})
print(A, type(A))
print(B, type(B))
print(10 in A)
print(666 in B)
for element in A:
  print(element)
A.add(75)
print(A)
print(A.pop())
A.remove(38)
A.add(4)
A.add(697)
A.add(0)
print(A)

print('{} | {} = {}'.format(A, B, A | B)) # union
print('{} | {} = {}'.format(A, B, A - B)) # difference
print('{} | {} = {}'.format(A, B, A & B)) # intersection
print('{} | {} = {}'.format(A, B, A ^ B)) # symmetric difference
print('*' * 200)

# dictionaries
users = {
  2423425: 'John',
  2342412: 'Elvis',
  3423121: 'Maria',
  2578322: 'Elisa',
  1214124: 'Elsa',
  9342320: 'Joseph',
  2420441: 'Josephina',
  8920132: 'Carol',
  9941332: 'Timotei',
  8779945: 'Elsa'
}
languages = dict({
  (0, 1): 'Java',
  (0, 2): 'JavaScript',
  ('a', 'b'): 'Python',
  ('c', 'd'): 'Angular',
  'a': 'Cobol',
  'b': 'Pascal'
})
print(users, type(users))
print(languages, type(languages))
for key in languages.keys():
  print('languages[{}] = {}'.format(key, languages[key]))
for key, value in users.items():
  print('{} : {}'.format(key, value))
print(languages.values())
print(languages.get('a'))
print(languages.get((7, 9))) # this will return None
print(languages['a'])
# print(languages[(7, 9)]) - this will throw an error
