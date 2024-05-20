'''
Lesson 27 - Documentation
dir()
help()
filter()
sorted()
__doc__
stdlib_module_names
terminal python
'''
import math, sys
print(dir())
print(dir(__builtins__))

print('#' * 50)
print(dir(print))
print(print.__doc__)
#help(print)

print('#' * 50)
print(list.append.__doc__)
help(list.append)

print('#' * 50)
print(dir(math))
print(math.log.__doc__)

print('#' * 50)
print(sorted(set(filter(lambda x: not x.startswith('_'),sys.stdlib_module_names))))
print(filter.__doc__)
