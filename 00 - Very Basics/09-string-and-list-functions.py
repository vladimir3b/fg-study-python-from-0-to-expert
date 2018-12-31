'''

  String and List special functions

'''

# string functions
string = 'I love to learn Python Programming. I am new to Python now but I am learning fast.'
email = 'radu.banciu@b1tv.ro'
message = '                   Elisa is here with John.        '
print(len(string))
print(string.upper())
print(string.lower())
print(string.index('Python', 20, 100))
print(string.center(len(string) + 2).center(len(string) + 40, '*'))
print(string.replace('Python', 'Javascript', 1))
print(string.count('Angular'))
print(string.startswith('I love'))
print(string.startswith('That'))
print(email.endswith('b1tv.ro'))
print(message.strip())

# list functions
courses = ['Python', 'Javascript', 'Angular', 'Typescript', 'Spanish', 'Portuguese', 'English']
print(courses.count('Python'))
courses.append('NodeJS')
print(courses.index('NodeJS', 5))
courses.append('C++')
print(courses)
courses.remove('C++')
print(courses)
print(courses.pop(3))
print(courses)
courses.sort()
print(courses)
courses.sort(reverse = True)
print(courses)
courses.insert(4, 'CSS')
courses.insert(4, 'SASS')
courses.insert(4, 'Web Design')
print(courses)
courses.sort()
print(courses)
new_courses = ['Django', 'WordPress', 'Ruby On Rails', 'Bootstrap']
courses.extend(new_courses)
print(courses)
courses.reverse()
print(courses)