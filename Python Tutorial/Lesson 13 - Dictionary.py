'''
Lesson 13 - Dictionary
dictionary
keys values
list()
'''
lessons = {'Lesson 01': 'String', 'Lesson 02': 'Variable'}
print(type(lessons), lessons)
print(lessons['Lesson 01'])
print(lessons.keys())
print(lessons.values())
lessons['Lesson 03'] = 'Integer'
print(lessons)

for key in lessons:
    print('key =', key, ' value =', lessons[key])

del lessons['Lesson 03']
for i in range(len(lessons)):
    print(list(lessons.values())[i])