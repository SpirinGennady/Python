# Задача 2: 
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# n = int(input('Введите трёхзначное число: '))
# a = int(n / 100)
# b = int(n / 10 % 10)
# c = int(n % 10)
# print(f'Сумма чисел {a} + {b} + {c} равна {a + b + c}')



# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# Допустим Петя делает n журавликов и Серёжа тоже, тогда Катя делает 2n*2,
# а вместе они делают S = n + 2n*2 + n > из уравнения следует > Петя делает S/6 и Серёжа тоже,
# а Катя 4*S/6

# S = int(input('Введите количество сделанных журавликов: ' ))
# p = int(S/6)
# k = int(4*S/6)
# s = int(S/6)
# print(f'При общем количестве {S} журавликов - Петя сделал {p}, Катя {k}, а Серёжа {s}.')




# Задача 6: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

# b = int(input('Введите шестизначный номер билета: '))
# one = int(b / 100000 )
# two = int(b / 10000 % 10)
# three = int(b / 1000 % 10)
# four = int(b % 1000 / 100)
# five = int(b % 100 / 10)
# six = int(b % 10)
# if(one + two + three) != (four + five + six):
#     print('"No" - увы, билет несчастливый(') 
# else:
#     print('"Yes" - билет счастливый!')   

   

# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите количество долек по вертикали: "))
# m = int(input("Введите количество долек по горизонтали: "))
# k = int(input("Введите количество долек, которые хотите отломить: "))

# if (k % m == 0) or (k % n == 0):
#     print('"Yes" - удача!')
# else:
#     print('"No" - не выйдет(')