# Разбор домашки № 3, 16-18
# import random

# size = int(input('Введите размер списка: '))
# min_limit = int(input('Введите минимальный предел: '))
# max_limit = int(input('Введите максимальный предел: '))

# my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
# print(my_list)

# number = int(input('Введите искомое число: '))

# count = my_list.count(number)
# closest = my_list[0]
# if count == 0:
#     for item in my_list:
#         if abs(number - item) < abs(number - closest):
#             closest = item
# print(f'Число {number} встречается {count} раз' if count > 0 else f'Ближайшее число к {number} : {closest}')



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# F, H, V, W, Y – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# scrabble = {'AEIOULNSTRАВЕИНОРСТ' : 1,
#             'DGДКЛМПУ' : 2,
#             'BCMPБГЁЬЯ' : 3,
#             'FHVWY' : 4,
#             'KЖЗХЦЧ' : 5,
#             'JXШЭЮ' : 8,
#             'QZФЩЪ' : 10}

# word = input('Введите слово: ')

# total = 0

# for letter in word.upper():
#     for letters in scrabble.keys():
#         if letter in letters:
#             total += scrabble.get(letters)
#             break
# print(f'Слово {word.upper()} весит {total} балов.')

# 2 способ:

# scrabble = {1 :'AEIOULNSTRАВЕИНОРСТ',
#             2 :'DGДКЛМПУ',
#             3 :'BCMPБГЁЬЯ',
#             4 : 'FHVWY',
#             5 : 'KЖЗХЦЧ',
#             8 : 'JXШЭЮ',
#             10 : 'QZФЩЪ'}

# word = input('Введите слово: ')

# total = 0

# for letter in word.upper():
#     for points, letters in scrabble.items():
#         if letter in letters:
#             total += points
#             break
# print(f'Слово {word.upper()} весит {total} балов.')


# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# text = list(input('Введите строку: '))

# count_dict = {}

# for letter in text:
#     count_dict[letter] = count_dict.get(letter, 0) + 1 
#     print (f'{letter}' if count_dict.get(letter) == 1 else f'{letter} _ {count_dict.get(letter) - 1}', end=' ')
