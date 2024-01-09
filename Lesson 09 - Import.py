'''
Lesson 09 - Import
import from as
os random datetime math
'''
import os
from random import randint
from datetime import datetime as dt
from datetime import timedelta
import math as mt

cwd = os.getcwd()
print(cwd)
files = os.listdir()
print(files)
os.system('cls||clear')

for i in range(10):
    print(randint(1,10))

time = dt(2022, 6, 1, 2, 3, 4)
print(time)
print(time + timedelta(2))

print(mt.cos(3.14))