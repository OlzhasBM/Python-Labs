#1
print('#1')
word = "olzhas"
if word == word[::-1]:
    print("true")
else:
    print("false")

print(' ')
print('***')
print(' ')
#2
print('#2')
seconds = int(15132)
days = seconds // (24 * 3600)
seconds %= (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days} days, {hours:02}:{minutes:02}:{seconds:02}")

print(' ')
print('***')
print(' ')
#3
print('#3')
numbers = "4, 5, 5, 2, 7, 86, 45, 6"
num_list = numbers.split(",")
num_tuple = tuple(num_list)
print(f"List: {num_list}")
print(f"Tuple: {num_tuple}")

print(' ')
print('***')
print(' ')
#4
print('#4')
list = ["apple", "banana", "cherry"]
print(f"First item: {list[0]}")
print(f"Last item: {list[-1]}")

print(' ')
print('***')
print(' ')
#5
print('#5')
filename = "filename.docx"
if "." in filename:
    print(f"File extension: {filename.split('.')[-1]}")
else:
    print("Cannot determine the file extension.")

print(' ')
print('***')
print(' ')
#6
print('#6')
n = int(5)
result = int(n) + int(n ** 2) + int(n ** 3)
print(f"Result: {result}")

print(' ')
print('***')
print(' ')

#7
print('#7')
numbers = [10, 23, 44, 237, 50, 62]
for num in numbers:
    if num == 237:
        print(num)
        break
    if num % 2 == 0:
        print(num)
print(' ')
print('***')
print(' ')