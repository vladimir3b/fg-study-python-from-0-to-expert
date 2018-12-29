"""

  A very basic study on variables, their types and some operators

"""

# defining variables and values
integer_value, floatValue, boolean_value = 36, 5.3, True
adition = integer_value + floatValue
division = integer_value / floatValue
exponention1 = 3 ** 3
exponention2 = 27 ** (1 / 3)
floor = integer_value // floatValue
modulo = 50 % 9
string1 = 'I never liked the song "Nothing Else Matters" by Metallica.'
string2 = "I've always loved the song \"Until It Sleeps\", also by Metallica."
quote = string1[23]
substring1 = string2[:17]
substring2 = string1[24:44]
substring3 = string2[51:]

# printing variables
print(integer_value, floatValue, boolean_value)
print(adition, division, exponention1, exponention2, floor, modulo)
print(string1, string2)
print(substring1, quote ,substring2, quote, substring3)
print(len(string1), str(floatValue)[1], string1.lower(), string2.upper())
print(type(string1), type(integer_value), type(floatValue))
print(id(string1), id(integer_value), id(floatValue))

# input values from user
name = input('What is your name? ')
age = input('How old are you? ')
occupation = input('What do yo do for living? ')

print('User %s is %s years old and works like a %s.' %(name, age, occupation))

# older = age * 1.5 - this is WRONG
# print('older =', older)