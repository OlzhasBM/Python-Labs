#1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

print(' ')
print('***')
print(' ')

#2
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
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}




