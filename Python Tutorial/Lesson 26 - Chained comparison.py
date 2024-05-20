'''
Lesson 26 - Chained comparison
chained comparison
id()
is not
'''
n1, n2, n3 = 1, 2, 3
if n1 < n2 < n3:
    print('n1 < n2 < n3')

l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy()
print(l1, l2, l3)
print(f'l1: {id(l1)}\nl2: {id(l2)}\nl3: {id(l3)}')

if l1 == l2 == l3:
    print('l1 = l2 = l3')

if l1 is l2 is l3:
    print('l1, l2 and l3 have the same id')
elif l1 is l2 is not l3:
    print('l1 and l2 have the same id, but l3 has a different id')
else:
    print('l1, l2 or l3 have different ids')

l2[0] = 10
print(l1, l2, l3)
