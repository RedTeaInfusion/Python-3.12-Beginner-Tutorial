'''
Lesson 06 - If
if elif else
nested if
ternary operator
'''
t = True
if t:
    print('t is True')

f = False
if f:
    print('f is True')
else:
    print('f is False')

x = 2
print(x)

if x == 1:
    print('x is equal to 1')
elif x < 1:
    # print('x is less than 1')
    if x == 0:
        print('x is equal to 0')
    else:
        print('x is negative')
else:
    print('x is greater than 1')

result = 'x is even' if x % 2 == 0 else 'x is odd'
print(result)