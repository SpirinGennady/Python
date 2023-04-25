
# n = int(input('Введите число Фибонначи: '))
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib( n - 2)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random

# def switch_value(list):
#     min_value = min(list)
#     max_value = max(list)

#     for i in range(len(list)):
#         if list[i] == max_value:
#             list[i] = min_value
#     print (list)

# value_amount = int(input('Введите количество оценок: '))
# value = []
# for i in range(value_amount):
#     value.append(random.randint(1,5))
# print(value)
# switch_value(value)

# 2 способ:

# import random

# mark_list = [random.randint(1,5) for _ in range(10)]  заполнение списка одной строкой!
# print(mark_list)
# mark_list = [min(mark_list) if i == max(mark_list) else i for i in mark_list] тернарный оператор
# print(mark_list)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

# number = int(input('Введите число: '))

# def is_simple(num: int) -> bool:
#     if num in [1,2]:
#         return True
#     elif not num % 2:
#         return False
#     else:
#         for i in range(3, num // 2 + 1, 2): 
#             if num % i == 0:
#              return False
#     return True

# print(f'Число {number} ' + ('простое' if is_simple(number) else 'комплексное'))


# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
 
# def reverse_list(n):
#     return ('1' if n == 1 else f'{n} {reverse_list(n - 1)}')
# num = int(input('Input number: '))
# print(reverse_list(num))

# 2 способ:

# def reverse(text: str):
#     if len(text) == 1:
#         return text
#     return text[-1] + reverse(text[:-1])
# txt = input('Введите строку: ')
# print(reverse(txt))