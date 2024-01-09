'''
Lesson 11 - Tuple
tuple
'''
t = (10, 20, 30)
print(type(t), t)

t1 = 11, 12, 13, 14
print(type(t1), t1)

t2 = (9)
t3 = (9,)
print(type(t2), t2)
print(type(t3), t3)

a, b, c, d = t1
print(a, b, c, d)

for item in t:
    print(item)

for i in range(len(t1)):
    print(t1[i])