'''

  Objects in Python

'''

# Basic notions

class Student:
  '''

    A simple example of a stundent class

    Properties:
      * mark1, mark2, mark3 - student's marks
      * name: student's name
      * roll_number
      * class_number

    Methods:
      * grade() -  calculates student's grade
      * display() - display the student's details

  '''

  # Properties
  mark1: int
  mark2: int
  mark3: int
  name: str
  roll_number: int
  class_number: int

  # Class properties
  school_name = 'Very Good Highschool'
  address = 'Str. Somewhere No. 652'

  # Constructor
  def __init__(self,
    name: str,
    roll_number: int,
    class_number: int
  ):
    self.name = name
    self.roll_number = roll_number
    self.class_number = class_number

  # Methods
  def __total_marks(self) -> int:
    return self.mark1 + self.mark2 + self.mark3

  def __average(self) -> float:
    return self.calculate_average(self.mark1, self.mark2, self.mark3)

  def grade(self) -> str:
    if self.__average() >= 80:
      return 'A'
    elif self.__average() >= 60:
      return 'B'
    elif self.__average() >= 40:
      return 'C'
    else:
      return 'F'

  def display(self) -> None:
    print('Student Name: {}, Roll number: {}, Class number: {}, Grade: {}'.format(
      self.name,
      self.roll_number,
      self.class_number,
      self.grade()
    ))

  # Class methods
  @classmethod
  def modify_class_name(cls, new_name) -> None:
    cls.school_name = new_name

  # Static Methods
  @staticmethod
  def calculate_average(*numbers:int) -> float:
    return sum(numbers) / len(numbers)


student1 = Student('Ion Popescu', 5464, 665)
print(student1, type(student1))
print(isinstance(student1, Student))
student1.mark1 = 80
student1.mark2 = 54
student1.mark3 = 68
student1.display();

print(student1.school_name)
student1.school_name = 'This is not possible'
print(student1.school_name)
print(Student.school_name)

print('\n\nInstance\'s properties :')
for prop in dir(student1):
  if not prop in dir(Student):
    print(prop)

print('\n\nClass\'s properties :')
for prop in dir(Student):
  if not prop in dir(student1):
    print(prop)
print('-' * 30)

print(student1.__doc__)

Student.modify_class_name('Better Highschool')
print(Student.school_name)
print(student1.school_name)

print(student1.calculate_average(6,7,8))

# print(round(student1._Student__average(), 2)) # like this you can access a private method

number = 20
print(isinstance(number, int))
print(isinstance(number, float))
print(isinstance(number, Student))

# Inheritance

from typing import List

class Person:
  '''

    Very general person class

    Properties:
      * first_name
      * last_name
      * age
      * gender
      * address

    Methods:
      * resume() - returns details of the person

  '''

  # Properties
  first_name: str
  last_name: str
  age: int
  gender: str
  address: str

  # Constructor
  def __init__(self,
    first_name: str,
    last_name: str,
    age: int,
    gender: str,
    address: str
  ):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.gender = gender
    self.address = address

  # Methods
  def resume(self) -> str:
    return '{} {} {} is {} years old and lives on {}.'.format(
      'Mr.' if self.gender == 'male' else 'Mrs.' if self.gender == 'female' else 'Creature',
      self.first_name,
      self.last_name,
      self.age,
      self.address
    )
  def __str__(self) -> str:
    return 'Name: {} {} Age: {} Gender: {}'.format(self.first_name, self.last_name, self.age, self.gender)



class Employee(Person):
  '''

    Class Employee extends class Person

    Properties:
      * employee_id
      * department
      * salary

    Methods:
      * resume() - returns details about employee

  '''

  # Properties
  employee_id: str
  department: str
  salary: int

  # Constructor
  def __init__(self,
    first_name: str,
    last_name: str,
    age: int,
    gender: str,
    address: str,
    employee_id: str,
    department: str,
    salary: int
  ):
    super().__init__(first_name, last_name, age, gender, address)
    self.employee_id = employee_id
    self.department = department
    self.salary = salary

  # Methods
  def resume(self) -> str:
    return '{}\n{} has employee id {}, works at {} and has salary {}.'.format(
      super().resume(),
      'He' if self.gender == 'male' else 'She' if self.gender == 'female' else 'Creature',
      self.employee_id,
      self.department,
      self.salary
    )
  def __add__(self, other) -> int:
    return self.salary + other.salary

class Team:
  '''

    Class Team

    Properties:
      * team_name
      * team_size

  '''

  # Properties
  team_name: str
  team_size: int

  # Constructor
  def __init__(self,
    team_name: str,
    team_size: int
  ):
    self.team_name = team_name
    self.team_size = team_size

class Manager(Employee, Team):
  '''

    Class Manager extends class Employee

    Properties:
      * teams
      * projects

    Methods:
      * resume() - returns details about manager

  '''

  # Properties
  teams: List[Team]
  projects: List[str]

  # Constructor
  def __init__(self,
    first_name: str,
    last_name: str,
    age: int,
    gender: str,
    address: str,
    employee_id: str,
    department: str,
    salary: int,
    teams: List[Team],
    projects: List[str]
  ):
    super().__init__(first_name, last_name, age, gender, address, employee_id, department, salary)
    self.teams = teams
    self.projects = projects

  # Methods
  def resume(self) -> str:
    manager_details = super().resume()
    manager_details += '\n{} manages teams:'.format(
      'He' if self.gender == 'male' else 'She' if self.gender == 'female' else 'Creature'
    )
    for team in self.teams:
      manager_details += '\n Team: {} Size: {}'.format(team.team_name, team.team_size)
    manager_details += '\n{} manages projects:'.format(
      'He' if self.gender == 'male' else 'She' if self.gender == 'female' else 'Creature'
    )
    for project in self.projects:
      manager_details += '\n Project name: {}'.format(project)
    return manager_details


manager1 = Manager(
  'Vladimir-Ioan',
  'Vararu',
  37,
  'male',
  'Borsa Street, no. 45',
  'RO65687',
  'Python Programming',
  4500,
  [
    Team('Python Newbies', 12),
    Team('Python Experts', 6),
    Team('Javascript Experts', 15)
  ],
  [
    'Best Python Project',
    'Best Javascript Project'
  ]
)

manager2 = Manager(
  'Serban',
  'Vararu',
  37,
  'male',
  'Borsa Street, no. 45',
  'RO65687',
  '.net Programming',
  4700,
  [
    Team('.net Newbies', 22),
    Team('.net Experts', 3),
    Team('Javascript Newbies', 5),
    Team('C# Newbies', 7),
    Team('C# Experts', 4)
  ],
  [
    'Learn C#',
    'Best ASP.net Project',
    'Backend in C# and ASP.net'
  ]
)

print(manager1.resume())
print(manager2.resume())
print(manager1)
print(manager2)
print(manager1 + manager2)


