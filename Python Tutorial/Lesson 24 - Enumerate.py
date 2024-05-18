'''
Lesson 24 - Enumerate
enumerate()
'''
s = 'python'
for index, element in enumerate(s): # for index in range(len(s)) # for element in s
    print(f'index = {index}, element = {element}')

l = ['a', 'b', 'c', 'd']
for index, element in enumerate(l[3:], start=3):
    print(f'index = {index}, element = {element}')

d = {'a': 1, 'b': 2, 'c': 3}
for index, (key, value) in enumerate(d.items()):
    print(f'index = {index}, key = {key}, value = {value}')
