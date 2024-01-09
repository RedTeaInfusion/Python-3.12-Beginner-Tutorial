'''
Lesson 15 - Function
def
return
*args
'''
def my_function():
    print('Hello World')

def greet(name = 'World'):
    print('Hello', name)

def add(a, b = 3):
    return a + b

def add_args(*args):
    result = 0
    for n in args:
        result += n
    return result

my_function()
greet('Red')
greet()
number = add(2)
print(number)
print(add_args(1, 2, 3, 4, 5, 6))