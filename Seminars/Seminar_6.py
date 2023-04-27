# Задача 39
# Даны два списка чисел. 
# Требуется вывести те элементы первого списка 
# (в том порядке, в каком они идут в первом списке), 
# которых нет во втором списке.

# import random

# list_1 = [random.randint(0, 20) for _ in range(20)]
# list_2 = [random.randint(0, 20) for _ in range(10)]

# print(list_1)
# print(list_2)

# list_new = [ i for i in list_1 if i not in list_2]
# print(list_new)


# Дан список, состоящий из целых чисел. 
# Напишите программу, которая в данном списке определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.


# from random import randint

# my_list = [randint(10, 20) for i in range(15)]
# count = 0
# print(my_list)

# for i in range(1, len(my_list) - 1):
#     if my_list[i - 1] < my_list[i] > my_list[i + 1]:
#         count += 1

# print(f'Количество элементов в списке: {count}')

# n = [1 for i in range(1, len(my_list) - 1) if my_list[i - 1] < my_list[i + 1]]

# print(f'Количество элементов в списке: {len(n)}')

# ЭТУ НЕ ПОНЯЛ, ДАЛЬШЕ ДАЖЕ НЕ СТАЛ ПИСАТЬ!