'''

  Lists and Tuples in Python

'''
# lists
list_example = [1, 2, 5, 54, 36.5, 8, 55]
print(list_example, type(list_example), id(list_example))
print('List has %s elements.'%len(list_example))
# print(list_example[100]) - this will throw an error
print(list_example[2:])
print(list_example[:3])
print(list_example[2:4])
print(list_example[::-1])

array1 = [ 0, 1, 2, 3, 4 ,5 ,6 ,7, 8, 9 ]
array2 = [ 10, 11, 12, 13, 14 ,15 ,16 ,17, 18, 19 ]
arrays = [array1, array2]
print(arrays[0][::2])
print(arrays[1][1::2])


tuple_example1 = 'a', 'b', 'r', 'error'
print(tuple_example1)
tuple_example2 = list_example, [2, 5, 6]
# tuple_example1[0] = [1, 2, 5, 54, 36.5, 8, 55] - this will throw an error
tuple_example2[0][2] = 6 # but this will work
print(tuple_example2, type(tuple_example2))
tuple_example3 = (4, 3, 32, 23, 54, 1, 54)
print(tuple_example3, len(tuple_example3))
tuple_example4 = 4,
print(tuple_example4, len(tuple_example4), type(tuple_example4))