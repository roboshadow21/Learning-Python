import math
import random
from collections import deque, Counter
from itertools import count

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

# for x in range(0, 2):
#     for y in range(0, 2):
#         a = not (x or y)
#         b = not x and not y
#         print(f'{x} - {y}', a == b)

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
# assert len(number) == 5, 'The number is not five-digit!'
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

# 41.	Выяснить являются ли три числа сторонами треугольника

# first_number = int(input('Enter first number: '))
# second_number = int(input('Enter second number: '))
# third_number = int(input('Enter third number: '))
#
# if first_number + second_number <= third_number:
#     print('It\'s not a triangle!')
# elif first_number + third_number <= second_number:
#     print('It\'s not a triangle!')
# elif second_number + third_number <= first_number:
#     print('It\'s not a triangle!')
# else:
#     print('It\'s a triangle!')

# 42.	Определить сколько чисел больше 0 введено с клавиатуры

# count = 0
# for num in range(5):
#     spam = int(input('Enter a number: '))
#     if spam > 0:
#         count += 1
# print(f'{count} numbers greater then zero')

# 43.	Написать программу преобразования десятичного числа в двоичное

# number = int(input('Enter a number to convert to binary: '))
# deq = deque()
# while number:
#     deq.appendleft(number % 2)
#     number //= 2
#
# print(''.join(list(map(str, deq))))

# 44.	Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2,
# b1 k1 и b2 и k2 заданы

# k1, b1, k2, b2 = map(float, input('Enter num: ').split())
# if k1 == k2:
#     print('Straight lines don\'t intersect!')
# else:
#     x = (b2 - b1) / (k1 - k2)
#     y = k1 * x + b1
#     print(f'Coordinates of the intersection of the lines x = {x}, y = {y}')

# 45.	Показать числа Фибоначчи


# def fib(number):
#     n = 0
#     m = 1
#     for _ in range(number):
#         temp = m + n
#         n = m
#         m = temp
#         print(temp, end=' ')
#
#
# fib(15)
#
#
# def fib_rec(n):
#     if n < 1:
#         return 1
#     if n < 2:
#         return 1
#     return fib_rec(n - 1) + fib_rec(n - 2)
#
#
# print()
#
# for i in range(16):
#     print(fib_rec(i), end=' ')

# 46.	Написать программу масштабирования фигуры
# чтобы задавались вершины фигуры списком (одной строкой)
# например: "(0,0) (2,0) (2,2) (0,2)"
# коэффициент масштабирования k задавался отдельно - 2 или 4 или 0.5
# В результате показать координаты, которые получатся.
# при k = 2 получаем "(0,0) (4,0) (4,4) (0,4)"

# coord_string = "(0,0) (2,0) (2,2) (0,2)"
# k = 2
# coord_list = list(map(int, [symbol for symbol in coord_string if symbol.isdigit()]))
# new_coord = [coord * k for coord in coord_list]
# x1, y1, x2, y2, x3, y3, x4, y4 = new_coord
# print(f'New coordinates = ({x1},{y1}) ({x2},{y2}) ({x3},{y3}) ({x4},{y4})')

# 47.	Написать программу копирования массива

# arr = [1, 2, 5, 4, 9, 8]
# new_arr = arr[:]
# print(new_arr)

# lst = []
# for el in arr:
#     lst.append(el)
# print(lst)

# 48.	Показать двумерный массив размером m×n заполненный целыми числами

# m = 4
# n = 3
# matrix = [[i for i in range(m)] for i in range(n)]
#
# for i in matrix:
#     print(*i)

# 49.	Показать двумерный массив размером m×n заполненный вещественными числами

# m = 4
# n = 4
# matrix = [[round(random.uniform(0, 6), 1) for _ in range(m)] for _ in range(n)]
#
# for i in matrix:
#     print(*i)

# 50.	В двумерном массиве n×k заменить четные элементы на противоположные

# matrix = [[i for i in range(6)] for i in range(6)]
# for i in matrix:
#     print(*i)
#
# for row in matrix:
#     for j in range(len(row) - 1):
#         if j % 2 == 0:
#             row[j], row[j + 1] = row[j + 1], row[j]
#
# print()
# for i in matrix:
#     print(*i)

# 51.	Задать двумерный массив следующим правилом: Aₘₙ = m+n

# matrix = [[0 * i for i in range(4)] for i in range(4)]
# for i, row in enumerate(matrix):
#     for j in range(len(row)):
#         matrix[i][j] = i + j
#
# print()
# for i in matrix:
#     print(*i)

# 52.	В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты

# matrix = [[random.randint(2, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# for i, row in enumerate(matrix):
#     for j in range(len(row)):
#         if i % 2 == 0 and j % 2 == 0:
#             matrix[i][j] = matrix[i][j] ** 2
#
# print()
# for i in matrix:
#     print(*i)

# 53.	В двумерном массиве показать позиции числа, заданного пользователем или указать, что такого элемента нет

# user_number = int(input('Enter number: '))
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for i, row in enumerate(matrix, start=1):
#     if user_number not in row:
#         continue
#     elif user_number in row:
#         print(f'The position of the element = raw {i}, column {row.index(user_number) + 1}')
#         break
# else:
#     print('There is no such element')

# 54.	В матрице чисел найти сумму элементов главной диагонали

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# summa = 0
# for i, row in enumerate(matrix):
#     for j in range(len(row)):
#         if i == j:
#             summa += matrix[i][j]
#
# print()
# print(summa)

# 55.	Дан целочисленный массив. Найти среднее арифметическое каждого из столбцов.

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# sum_list = [None] * len(matrix[0])
#
# for i, row in enumerate((list(zip(*matrix)))):
#     sum_list[i] = sum(row) / len(row)
#     print(f'The arithmetic average of the column N {i} = {sum_list[i]}')

# 56.	Написать программу, которая обменивает элементы первой строки и последней строки

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# for j in range(len(matrix[0])):
#     matrix[0][j], matrix[-1][j] = matrix[-1][j], matrix[0][j]
#
# print()
# for i in matrix:
#     print(*i)

# 57.	Написать программу, упорядочивания по убыванию элементов каждой строки двумерного массива.

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# for i in range(len(matrix)):
#     matrix[i] = sorted(matrix[i], reverse=True)
#
# print()
# for i in matrix:
#     print(*i)

# 58.	Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
#
# assert len(matrix) == len(matrix[0]), 'The number of rows is not equal to the number of columns'
# transposed_matrix = list(zip(*matrix))
# for i in transposed_matrix:
#     print(*i)

# 59.	В прямоугольной матрице найти строку с наименьшей суммой элементов.

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(3)]
# for i in matrix:
#     print(*i)
#
# summa = list(map(lambda x: sum(x), matrix))
# print(f'Line number with the minimum amount = {summa.index(min(summa))}')

# 60.	Составить частотный словарь элементов двумерного массива

# matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# for i in matrix:
#     print(*i)
#
# rate = Counter()
# for i, row in enumerate(matrix):
#     for j in range(len(row)):
#         rate[matrix[i][j]] += 1
#
# for key, value in rate.items():
#     print(f'The number of element {key} = {value}')

# 61.	Найти произведение двух матриц

# m1 = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# m2 = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
# length = len(m1)
# m_sum = [[0 for _ in range(length)] for _ in range(length)]
#
# for i in range(length):
#     for j in range(length):
#         for k in range(length):
#             m_sum[i][j] += m1[i][k] * m2[k][j]
#
# for i in m_sum:
#     print(*i)

# 62.	В двумерном массиве целых чисел. Удалить строку и столбец, на пересечении которых расположен наименьший элемент.

# matrix = [
#     [2, 6, 3, 6],
#     [4, 2, 8, 3],
#     [7, 4, 1, 5],
#     [9, 2, 4, 6]
# ]
# minimum_list = list(map(lambda x: min(x), matrix))
# smallest_element = min(minimum_list)
# smallest_element_row_idx = minimum_list.index(smallest_element)
# smallest_element_column_idx = matrix[smallest_element_row_idx].index(min(matrix[smallest_element_row_idx]))
# new_matrix = matrix[:smallest_element_row_idx] + matrix[smallest_element_row_idx + 1:]
# list(map(lambda x: x.pop(smallest_element_column_idx), new_matrix))
#
# for i in new_matrix:
#     print(*i)

# 63.	Сформировать трехмерный массив не повторяющимися двузначными числами
# показать его построчно на экран выводя индексы соответствующего элемента

# c = count(11, 1)
# three_dimensional_matrix = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
# length = len(three_dimensional_matrix)
#
#
# def show_matrix(matrix):
#     for i in range(length):
#         for j in range(length):
#             for k in range(length):
#                 matrix[i][j][k] = next(c)
#                 print(f'Indexes: i={i} - j={j} - k={k} of the element {matrix[i][j][k]}')
#
#
# show_matrix(three_dimensional_matrix)

# for i in three_dimensional_matrix:
#     print(*i)


# 64.	Показать треугольник Паскаля *Сделать вывод в виде равнобедренного треугольника

# n = int(input("Enter the number of rows: "))
#
# for i in range(n):
#     print(' ' * (n - i), end='')
#     print(' '.join(map(str, str(11 ** i))))


# 65.	Спирально заполнить двумерный массив:

# size = int(input("Enter the size of the matrix: "))
# matrix = [[0] * size for i in range(size)]
# value, k = 1, 0
#
# for v in range(size):
#     for i in range(size - k):
#         matrix[v][i + v] = value
#         value += 1
#     for i in range(v + 1, size - v):
#         matrix[i][-v - 1] = value
#         value += 1
#     for i in range(v + 1, size - v):
#         matrix[-v - 1][-i - 1] = value
#         value += 1
#     for i in range(v + 1, size - (v + 1)):
#         matrix[-i - 1][v] = value
#         value += 1
#     k += 2
#
# for i in matrix:
#     print(*i)

# 66.	Показать натуральные числа от 1 до N, N задано

# N = int(input('Enter number: '))
#
#
# def show_numbers(n):
#     m = 1
#     if n < 2:
#         return 1
#     return m + show_numbers(n - 1)
#
#
# for i in range(1, N + 1):
#     print(show_numbers(i), end=' ')

# 67.	Показать натуральные числа от N до 1, N задано

# N = int(input('Enter number: '))
#
#
# def show_reversed_numbers(n):
#     m = 1
#     if n < 2:
#         return 1
#     return m + show_reversed_numbers(n - 1)
#
#
# k = N
# while k > 0:
#     print(show_reversed_numbers(k), end=' ')
#     k -= 1

# 68.	Показать натуральные числа от M до N, N и M заданы


# def show_sequence(a, b):
#     if a == b:
#         return b
#     return show_sequence(a, b - 1)
#
#
# m = 3
# n = 10
#
#
# for i in range(m, n + 1):
#     print(show_sequence(i, n), end=' ')

# 69.	Найти сумму элементов от M до N, N и M заданы

# def show_summa(a, b):
#     if a == b:
#         return b
#     return b + show_summa(a, b - 1)
#
#
# m = 3
# n = 12
#
# print(show_summa(m, n))

# 70.	Найти сумму цифр числа

# n = input('Enter number: ')


# def digits_summa(s):
#     if len(s) < 2:
#         return int(s[0])
#     return int(s[0]) + int(digits_summa(s[1::1]))
#
#
# print(digits_summa(n))









