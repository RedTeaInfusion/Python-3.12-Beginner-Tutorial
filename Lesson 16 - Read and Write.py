'''
Lesson 16 - Read and write
open()
with as
read()
write()
remove()
'''
import os

file = open('Lesson 01 - String.py', 'r')
content = file.read()
print(content)
file.close()

with open('Lesson 02 - Variable.py', 'r') as file:
    content = file.read()
    print(content)

with open('output.txt', '')as file:
    file.write('First line\n')
    file.write('Second line')
    print(file.read())

with open('output.txt', 'r') as file:
    print(file.read())

with open('output.txt', 'a') as file:
    file.write(' Second line')

with open('output.txt', 'r') as file:
    print(file.read())

os.remove('output.txt')