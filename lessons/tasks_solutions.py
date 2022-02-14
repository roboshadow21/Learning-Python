import random
import math
from decimal import Decimal
# Семинар 1-2: примерный список задач

# 1. По двум заданным числам проверить является ли одно квадратом второго

# x = 2
# y = 8
# if x * x == y:
#     print(f'{y} is a square of {x}')
# else:
#     print(f'{y} is not square of {x}')

# 2. Найти максимальное из пяти чисел

# lst = [2, 17, 6, 34, 12]
# # print(max(lst))
# maximum = 0
# for i in range(len(lst) - 1):
#     maximum = lst[i]
#     if lst[i + 1] > maximum:
#         maximum = lst[i + 1]
# print(maximum)

# 3. Вывести на экран числа от -N до N

# numbers = range(-10, 11)
# for i in numbers:
#     print(i, end=' ')

# 4. Показать первую цифру дробной части числа
# print()
# x = 32.86793
# y = int(x)
# z = x - y
# print(int(z * 10))

# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# number = 40
# if number % 5 == 0 and number % 10 == 0 and number % 30 != 0:
#     print(f'{number} multiply 5 and 10 but 30')
# else:
#     print(f'{number} not multiply')

# 6. Дано число обозначающее день недели. Вывести его название и указать является ли
# он выходным.

# day = 5
# week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
# if week.get(day) and day == 6 or day == 7:
#     print(week[day], " - Weekend!")
# else:
#     print(week[day])

# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений
# предикат

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             a = not (x or y or z)
#             b = not x and not y and not z
#             print(f'{x} - {y} - {z}', a == b)

# k = 0
# while k != 1:
#     X, Y, Z = 0, 0, 0
#     a = not (X or Y or Z)
#     b = not X and not Y and not Z
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     X += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     X -= 1
#     Y += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     Y -= 1
#     Z += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     Z -= 1
#     X += 1
#     Y += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     Y -= 1
#     Z += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     Z -= 1
#     Y += 1
#     Z += 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     X -= 1
#     print(f'{X} - {Y} - {Z} - {a == b}')
#     k += 1

# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка
# с координатами Х и У


# def show_quarter(coord_x, coord_y):
#     if coord_x > 0 and coord_y > 0:
#         print('the point is in the first quarter')
#     elif coord_x < 0 and coord_y > 0:
#         print('the point is in the second quarter')
#     elif coord_x < 0 and coord_y < 0:
#         print('the point is in the third quarter')
#     elif coord_x > 0 and coord_y < 0:
#         print('the point is in the fourth quarter')
#     elif coord_x == 0:
#         print('the point is on the Y-axis')
#     elif coord_y == 0:
#         print('the point is on the X-axis')
#
#
# show_quarter(3, -4)

# 9. Указав номер четверти прямоугольной системы координат , показать допустимые
# значения координат для точек этой четверти


# def show_coordinate(quarter_number):
#     if quarter_number == 1:
#         print('x > 0 and y > 0')
#     elif quarter_number == 2:
#         print('x < 0 and y > 0')
#     elif quarter_number == 3:
#         print('x < 0 and y < 0')
#     elif quarter_number == 4:
#         print('x > 0 and y < 0')
#
#
# show_coordinate(1)

# 10. Найти расстояние между двумя точками пространства


# def point_distance(x1, x2, y1, y2):
#     distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#     return distance
#
#
# print(point_distance(2, 5, 3, 6))

# Семинар 3-4: примерный список задач

# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т .д.


# def create_list(n):
#     lst = []
#     spam = 1
#     for _ in range(n):
#         lst.append(spam)
#         spam *= -3
#     return lst
#
#
# print(create_list(5))


# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# def create_dict(sequence_of_keys):
#     my_dict = {d: d * 3 + 1 for d in range(1, sequence_of_keys + 1)}
#     return my_dict
#
#
# print(create_dict(6))

# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в
# другой.

# first_str = input('Enter first string: ')
# second_str = input('Enter second string: ')
# count = first_str.count(second_str)
# print(f'Substring "{second_str}" occurs {count} times')

# 14. Подсчитать сумму цифр в вещественном числе.


# def digits_summa(num: str) -> int:
#     dot_number = Decimal(num)
#     num_list = []
#     while dot_number != 0:
#         spam = int(dot_number)
#         num_list.append(spam)
#         dot_number -= spam
#         dot_number *= 10
#     return sum(num_list) if num_list else -1
#
#
# print(digits_summa('1.1111'))

# N = str(random.random() * 100)
# print(N)
# summa = 0
# for i in N:
#     if i.isdigit():
#         summa += int(i)
#
# print(summa)


# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# def mutliply_numbers(n):
#     if n < 2:
#         return 1
#     return n * (mutliply_numbers(n - 1) * mutliply_numbers(n - 2))
#
#
# for i in range(5):
#     print(mutliply_numbers(i), end=' ')


# 16. Задать список из n чисел последовательности (1 + 1/n) ** n и вывести на экран их сумму

# lst = []
# n = 5
# for i in range(1, n + 1):
#     lst.append((1 + 1 / i) ** i)
#
# print(lst)
# print(sum(lst))

# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке
# одно число




# 18. Реализовать алгоритм перемешивания списка.
# li = [1, 2, 3, 4, 5, 6]
#
# k = 0
# while k != len(li) // 2:
#     for i in range(len(li) - 1):
#         spam = li[i]
#         eggs = li[i + 1]
#         li[i], li[i + 1] = eggs, spam
#     k += 1
# else:
#     li[0], li[-1] = li[-1], li[0]
# print(li)

# 20. Определить, присутствует ли в заданном списке строк, некоторое число

# li = ['az', 'zb', 'c', 'asd', '5', 'qwerty', '89']
# num = str(89)
# print(f'Number {num} is in list' if num in li else f'Number {num} not found')


