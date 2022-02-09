import math
import random

# 1.	Вывести квадрат числа

# num = int(input('Enter the number: '))
# print(f'The number {num ** 2} is the square of the {num}')

# 2.	По двум заданным числам проверять является ли первое квадратом второго

# first_num = int(input('Enter the first number: '))
# second_num = int(input('Enter the second number: '))
# if second_num ** 2 == first_num:
#     print(f'{first_num} is the square of the {second_num}')
# else:
#     print(f'The number {first_num} is not square of the {second_num}')

# 3.	Даны два числа. Показать большее и меньшее число

# first_number = int(input('Enter the first number: '))
# second_number = int(input('Enter the second number: '))
# print(f'A larger number is the {first_number} ' if first_number > second_number else
#       f'A large number is the {second_number}')

# 4.	По заданному номеру дня недели вывести его название

# week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
# day_number = int(input('Enter the number of the day of the week: '))
# print(f'{week[day_number]}' if week.get(day_number) else f'No such a day!')

# 5.	Найти максимальное из трех чисел

# a, b, c = map(int, input('Enter a numbers: ').split())
# print('Large number is -', max(a, b, c))

# 6.	Написать программу вычисления значения функции y = f(a)

# def f(a):
#     return a * 2
#
#
# print(f(4))


# 7.	Выяснить является ли число чётным

# number = int(input('Enter a number: '))
# if number % 2 == 0:
#     print(f'The number {number} is even')
# else:
#     print(f'The number {number} is odd')

# 8.	Показать числа от -N до N

# number = int(input('Enter a number: '))
# print(list(range(-number, number + 1)))

# 9.	Показать четные числа от 1 до N

# number = int(input('Enter a number: '))
# for num in range(1, number + 1):
#     if num % 2 == 0:
#         print(num, end=' ')
# print()
# print(list(filter(lambda x: x % 2 == 0, range(1, number + 1))))
# print(list(n for n in range(1, number + 1) if n % 2 == 0))

# 10.	Показать последнюю цифру трёхзначного числа

# number = int(input('Enter a three-digit number: '))
# print(f'The last digit is {number % 10}')

# 11.	Показать вторую цифру трёхзначного числа

# number = int(input('Enter a three-digit number: '))
# print(f'The second digit is {(number // 10) % 10}')

# 12.	Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# number = int(input('Enter a two-digit number: '))
# last_digit = number % 10
# first_digit = number // 10
# print(f'The large number is {first_digit}' if first_digit > last_digit else f'The large number is {last_digit}')

# 13.	Удалить вторую цифру трёхзначного числа

# number = int(input('Enter a two-digit number: '))
# last_digit = number % 10
# first_digit = number // 100
# print(str(first_digit) + str(last_digit))

# 14.	Выяснить, кратно ли число заданному, если нет, вывести остаток.
# specified_number = 3
# user_number = int(input('Enter a number: '))
# print(
#     f'The number {user_number} is a multiple of the {specified_number}' if user_number % specified_number == 0 else
#     f'The remainder of the division = {user_number % specified_number}'
# )

# 15.	Найти третью цифру числа или сообщить, что её нет

# number = input('Enter a number: ')
# print(number[2] if len(number) >= 3 else f'There is no third digit')

# 15.	Дано число. Проверить кратно ли оно 7 и 23

# number = int(input('Enter a number: '))  # 161
# print(f'The number {number} is a multiple of 7 and 23' if number % 7 == 0 and number % 23 == 0 else
#       f'The number {number} is not a multiple of 7 and 23')

# 16.	Дано число обозначающее день недели. Выяснить является номер дня недели выходным

# day = int(input('Enter the number of the day of the week: '))
# if day > 7 or day < 1:
#     print('There is no such day of the week!')
# else:
#     print('Weekend!' if day == 6 or day == 7 else 'Workday!')

# 17.	По двум заданным числам проверять является ли одно квадратом другого

# x = int(input('Enter the first number: '))
# y = int(input('Enter the second number: '))
# if math.sqrt(x) == y:
#     print(f'The number {x} is the square of the number {y}')
# elif math.sqrt(y) == x:
#     print(f'The number {y} is the square of the number {x}')
# else:
#     print(f'The numbers {x} and {y} are not squares of each other')

# 18.	Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# X = 0
# Y = 0
# a = not (X or Y)
# b = not X and not Y
# k = 0
# while k < 2:
#     m = 0
#     while m < 2:
#         print(f'{X} - {Y}', a == b)
#         Y += 1
#         m += 1
#     X += 1
#     Y -= 2
#     k += 1

# 19.	Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0


# def show_quarter(coord_x, coord_y):
#     if coord_x > 0 and coord_y > 0:
#         print('the point is in the first quarter')
#     elif coord_x < 0 and coord_y > 0:
#         print('the point is in the second quarter')
#     elif coord_x < 0 and coord_y < 0:
#         print('the point is in the third quarter')
#     elif coord_x > 0 and coord_y < 0:
#         print('the point is in the fourth quarter')


# show_quarter(3, -4)

# 20.	Задать номер четверти, показать диапазоны для возможных координат


# def show_coordinate(quarter_number):
#     if quarter_number == 1:
#         print('x > 0 and y > 0')
#     elif quarter_number == 2:
#         print('x < 0 and y > 0')
#     elif quarter_number == 3:
#         print('x < 0 and y < 0')
#     elif quarter_number == 4:
#         print('x > 0 and y < 0')


# show_coordinate(4)

# 21.	Программа проверяет пятизначное число на палиндром.

# number = input('Enter a five-digit number: ')
# print(f'The number {number} is a palindrome!' if number[0] == number[-1] and number[1] == number[-2] else
#       f'The number {number} is not a palindrome!')

# 22.	Найти расстояние между точками в пространстве 2D/3D

# def point_distance(x1, x2, y1, y2, z1, z2):
#     distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))
#     return distance


# print(round(point_distance(2, 5, 3, 6, 4, 7), 4))

# 23.	Показать таблицу квадратов чисел от 1 до N

# num = int(input('Enter a number: '))
# for i in range(1, num + 1):
#     print('The square of the number | {} | - | {} |'.format(i, i ** 2))

# 24.	Найти кубы чисел от 1 до N

# number = int(input('Enter a number: '))
# for i in range(1, number + 1):
#     print('The cube of the number %d - %d' % (i, pow(i, 3)))

# 25.	Найти сумму чисел от 1 до А

# n = int(input('Enter a number: '))
# print(sum(range(1, n + 1)))
# print(n * (n + 1) // 2)

# 26.	Возведите число А в натуральную степень B используя цикл

# a = 2
# b = 8
# result = a
# k = 1
# while k < b:
#     result *= a
#     k += 1
# print(result)

# 27.	Определить количество цифр в числе

# number = input('Enter a number: ')
# print('The number of digits in a number %s = %d' % (number, len(number)))

# 28.	Подсчитать сумму цифр в числе

# num = list(map(int, input('Enter number: ')))
# number = ''.join(map(str, num))
# print(f'The sum of digits in a number {number} = {sum(num)}')

# 29.	Написать программу вычисления произведения чисел от 1 до N

# n = int(input('Enter a number: '))
# result = 1
# for i in range(1, n + 1):
#     result *= i
# print(result)

# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# 30.	Показать кубы чисел, заканчивающихся на четную цифру

# even_numbers = list(filter(lambda x: x % 2 == 0, map(lambda x: pow(x, 3), range(1, 13))))
# print(even_numbers)

# 31.	Задать массив из 8 элементов и вывести их на экран

# lst = list(range(8))
# print(lst)

# 32.	Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

# lst = [random.randint(0, 1) for _ in range(8)]
# print(lst)

# 33.	Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму
# положительных/отрицательных элементов массива

# li = [random.randint(-9, 10) for _ in range(12)]
# print(li)
# print(sum(list(filter(lambda x: x > 0, li))))
# print(sum(list(filter(lambda x: x < 0, li))))

# 34.	Написать программу замену элементов массива на противоположные

# lst = [2, 4, 8, 7, 1, 6, 9]
# print(lst)
# k = 0
# i = 0
# j = -1
# while k < len(lst) // 2:
#     lst[i], lst[j] = lst[j], lst[i]
#     i += 1
#     j -= 1
#     k += 1
#
# print(lst)

# 35.	Определить, присутствует ли в заданном массиве, некоторое число

# lst = [random.randint(1, 100) for _ in range(20)]
# print(lst)
# user_number = int(input('Enter a number: '))
# print(f'The number {user_number} is present in the specified array' if user_number in lst else
#       f'The number {user_number} is not present in the specified array')

# 36.	Задать массив, заполнить случайными положительными трёхзначными числами.
# Показать количество нечетных\четных чисел

# my_lst = [random.randint(100, 999) for _ in range(20)]
# print(my_lst)
# print(f'The number of even numbers in array = {len(list(filter(lambda x: x % 2 == 0, my_lst)))}')
# print(f'The number of even numbers in array = {len(list(filter(lambda x: x % 2 != 0, my_lst)))}')

# 37.	В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

# li = [random.randint(1, 200) for _ in range(123)]
# lst = [i for i in li if 10 <= i <= 99]
# print('The number of elements between 10 and 99 = %d' % (len(lst)))

# 38.	Найти сумму чисел одномерного массива стоящих на нечетной позиции

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# odd_positions_summa = sum([num for num in lst if lst.index(num) % 2 != 0])
# print('The sum of the array numbers standing in an odd position = {}'.format(odd_positions_summa))

# 39.	Найти произведение пар чисел в одномерном массиве.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result_lst = []
# i = 0
# j = -1
# k = 0
# while k < len(li) // 2:
#     result_lst.append(li[i] * li[j])
#     i += 1
#     j -= 1
#     k += 1
#
# print('The result of multiplying two pairs of numbers = %s' % result_lst)

# 40.	В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

# li = [round(random.uniform(0, 5), 2) for _ in range(10)]
# print(li)
# print('The difference between the maximum and minimum values = {}'.format(max(li) - min(li)))

