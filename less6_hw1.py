# 1 Подсчитать, сколько было выделено памяти под переменные в ранее 
# разработанных программах в рамках первых трех уроков. Проанализировать 
# результат и определить программы с наиболее эффективным использованием памяти

import sys

# Linux x64 , Python ver 3.8.0

# (1)

num1 = int(input("Введите первое число\n >>> "))
num2 = int(input("Введите второе число\n >>> "))
num3 = int(input("Введите третье число\n >>> "))

if num2 < num1 < num3 or num3 < num1 < num2:
    print('Среднее:', num1)
elif num1 < num2 < num3 or num3 < num2 < num1:
    print('Среднее:', num2)
else:
    print('Среднее:', num3)

all_size = 0
all_size += sys.getsizeof(num1)
all_size += sys.getsizeof(num2)
all_size += sys.getsizeof(num3)
print("В 1 варианте кода переменные занимают: {}".format(all_size))

# (2)

nums = []
for i in range(3):
    num = int(input("Введите число: "))
    nums.append(num)


if nums[1] < nums[0] < nums[2] or nums[2] < nums[0] < nums[1]:
    print('middle is {}'.format(nums[0]))
elif nums[0] < nums[1] < nums[2] or nums[2] < nums[1] < nums[0]:
    print('middle is {}'.format(nums[1]))
else:
    print('middle is {}'.format(nums[2]))

all_size2 = 0
all_size2 += sys.getsizeof(nums)
all_size2 += sys.getsizeof(num)
print("В 2 варианте кода переменные занимают: {}".format(all_size2))

