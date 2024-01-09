'''
Lesson 17 - List Comprehension
list comprehension
'''
numbers = [x for x in range(5)]
print(numbers)

squares = [x**2 for x in range(5)]
print(squares)

double_even = [x*2 for x in numbers if x % 2 == 0]
print(double_even)

matrix = [numbers for x in range(3)]
print(matrix)

matrix2 = [[x for x in range(5)] for y in range(3)]
print(matrix2)