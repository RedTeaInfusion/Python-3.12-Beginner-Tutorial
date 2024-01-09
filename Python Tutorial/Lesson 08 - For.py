'''
Lesson 08 - For
for else
len()
range()
break
'''
numbers = [0, 1, 2, 3]
print(numbers)

for n in numbers:
    print(n)
for i in range(10):
    print(i)

my_name = 'Red'
print(my_name[0])
print(len(my_name))

for i in range(len(my_name)):
    print(my_name[i])

matrix = []
for i in range(1,3):
    for j in range(4):
        pair = [i, j]
        matrix.append(pair)
        print('i =', i, 'j =', j)
print(matrix)

for i in range(50):
    if i > 7:
        break
    print(i)
else:
    print('the loop is finished')