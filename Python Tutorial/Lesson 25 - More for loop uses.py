'''
Lesson 25 - More for loop uses
for _
range()
zip()
dict comprehension
'''
for _ in range(2):
    print('Hello')

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x, _, z in l:
    print(x, z)

for index in range(0, 10, 2):
    print(index)

names = ['Fred', 'Bob', 'Carl']
ages = [28, 19]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

d = {n: n**2 for n in range(3)}
print(type(d), d)
