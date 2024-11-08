#1
print("#1")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

print(' ')
print('***')
print(' ')

#2
print("#2")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            print(a[i])
            break

print(' ')
print('***')
print(' ')

#3
print("#3")
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascencion = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(ascencion)
descending = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(descending)

print(' ')
print('***')
print(' ')

#4
print("#4")
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
dict_b = dict_a | dict_b | dict_c
print(dict_b)

print(' ')
print('***')
print(' ')

#5
print("#5")
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(my_keys)

print(' ')
print('***')
print(' ')

#6
print("#6")
def numberToBase(n, b):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = digits[n % b] + result
        n //= b
    return result

number = 42
base_5_string = numberToBase(number, 2)
base_16_string = numberToBase(number, 16)
print(base_5_string)
print(base_16_string)

print(' ')
print('***')
print(' ')

#7
print("#7")
from math import (factorial)
n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    print()