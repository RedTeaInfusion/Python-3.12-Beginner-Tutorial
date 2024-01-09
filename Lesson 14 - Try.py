'''
Lesson 14 - Try
try except else finally
pass
'''
try:
    print(10/0)
except Exception as e:
    print(e)
    # pass
print('Program terminated')

try:
    i = input('Insert a number: ')
    i = int(i)
    print(i)
    print(10/i)
except ValueError:
    print(i, 'is not a number')
except ZeroDivisionError:
    print('i can\'t be 0')
else:
    print('I print if there aren\'t errors')
finally:
    print('I print always')