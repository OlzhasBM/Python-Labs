#1
print("#1")
list1 = [1,2,3,4,5,5,3,2,5,6,7,8,9,0,8]
list2 = [1,2,3,6,7]
list3 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list3.append(i)
print(list3)

print(' ')
print('***')
print(' ')

#2
print("#2")
import os
directory = "."
files = os.listdir(directory)
print(files)

print(' ')
print('***')
print(' ')

#3
print("#3")
a = int(524)
b = (a % 100) // 10
c = (a % 100) % 10
d = a // 100
print(b + c + d)

print(' ')
print('***')
print(' ')

#4
print("#4")
string = "hello world"
char = "o"
count = string.count(char)
print(count)

print(' ')
print('***')
print(' ')

#5
print("#5")
a = 5
b = 10
a, b = b, a
print(a, b)

print(' ')
print('***')
print(' ')

#6
print("#6")
numbers = [10, 15, 30, 45, 50, 22, 75]
result = []
for j in numbers:
    if (lambda n: n % 15 == 0)(j):
        result.append(j)
print(result)

print(' ')
print('***')
print(' ')

#7
print("#7")
s = [1, 2, 3, 4 , 4, 5]
for i in range(len(s)):
    for j in range(i + 1,len(s)):
        if s[i] == s[j]:
            print('false')
            break
        else:
            print('true')
            break
print(' ')
print('***')
print(' ')