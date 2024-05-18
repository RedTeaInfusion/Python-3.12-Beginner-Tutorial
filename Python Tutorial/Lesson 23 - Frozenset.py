'''
Lesson 23 - Frozenset
frozenset
frozenset()
union intersection difference symmetric_difference issubset issuperset
'''
fs = frozenset([1, 3, 2])
print(type(fs), fs)

fs1 = frozenset((2, 4, 3, 6, 5))
print(type(fs1), fs1)

s = {1, 3, 2, 6}
fs2 = frozenset(s)
print(type(fs2), fs2)

print(fs.union(fs1))
print(fs.intersection(fs2))
print(fs.difference(s))
print(fs.symmetric_difference(fs1))
print(fs.issubset(fs2))
print(fs.issuperset(fs2))
fs3 = frozenset({3, 2, 1})
print(fs3 == fs)

for element in fs3:
    print(element)
