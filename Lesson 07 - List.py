'''
Lesson 07 - List
list
select elements
append insert pop remove reverse sort copy extend clear
'''
first_list = [0, 1, 0.9, True, "string", []]
print(first_list)
print(type(first_list))
print(first_list[0], first_list[-6])
print(first_list[5], first_list[-1])
print(first_list[0:4])

numbers = [10, 11, 12]
print(numbers)
numbers.append(13)
print(numbers)
numbers.insert(1,14)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.remove(11)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
n = numbers.copy()
print(n)
numbers.extend(n)
print(numbers)
numbers.clear()
print(numbers, n)