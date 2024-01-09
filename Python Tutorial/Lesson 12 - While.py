'''
Lesson 12 - While
while else
continue
'''
count = 0
while count < 10: # for i in range(10)
    print(count)
    count += 1 # count = count + 1
else:
    print('count equals 10')

count = 0
while True:
    print(count)
    count += 1
    if count == 10:
        break
else:
    print('unusable')

count = 0
while count < 10:
    count += 1
    if count == 5:
        continue
    print(count)