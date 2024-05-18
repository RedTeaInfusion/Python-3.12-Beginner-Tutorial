'''
Lesson 22 - Set
set
set()
add remove discard copy intersection difference union
'''
s = {1, 3, 2, 4, 5, 5, 5}
print(type(s), s)

empty = set()
print(type(empty), empty)

s1 = {'a', True, 2, 3.14}
print(s1)
try:
    print(s[0])
except:
    print('You cannot access values by index')

if 1 in s:
    print('1 is present')

for element in s:
    print(element)

l = [1, 2, 1, 2, 1, 1, 3, 3, 3]
print(set(l))

s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.discard(5)
print(s)
s2 = s.copy()
print(s2)
print(s1.intersection(s))
print(s1.union(s))
print(s1.difference(s))
