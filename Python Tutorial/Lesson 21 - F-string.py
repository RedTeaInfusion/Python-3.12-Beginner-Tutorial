'''
Lesson 21 - F-string
f''
title()
replace()
format .2f 010d
'''
s = 'python'
print(f'{s.title()}')

n1 = 1
n2 = 2
print(f'{n1} + {n2} = {n1 + n2}')

pi = 3.14159265
print(f'pi = {pi:.2f}')

print(f"n1 = {n1:010d}")

print(f'{s.replace("p","P")}\n'\
      f'It\'s {s}')

print(f'''{s.replace('p','P')}
It's {s}''')
