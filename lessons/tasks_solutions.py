import random
import math
import time
import re
import sympy
from decimal import Decimal
from collections import deque
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


# N = str(1.1111)
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


# def multiply_sequence(num):
#     lst = [1]
#     for i in range(1, num):
#         lst.append(lst[-1] * (i + 1))
#     return lst
#
#
# print(multiply_sequence(4))


# 16. Задать список из n чисел последовательности (1 + 1/n) ** n и вывести на экран их сумму


# def numbers_sequence(n):
#     lst = []
#     for i in range(1, n + 1):
#         lst.append((1 + 1 / i) ** i)
#     return sum(lst)
#
#
# print(numbers_sequence(5))


# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# pos = '7\n9'
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(pos)

# n = 5
# lst = [i for i in range(-n, n + 1)]
# print(lst)
# res = 1
#
# with open('test.txt', encoding='utf-8') as f:
#     for idx in f.readlines():
#         print(f'Number on positions {idx}')
#         res *= lst[int(idx)]
#
# print(f'The result of multiplication = {res}')


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

# 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного
# генератора псевдослучайных чисел


# def rand_numbers(start, stop):
#     num = time.time()
#     delta = stop - start
#     rnd = float(str(num)[::-1][:3]) / 1000
#     return round(rnd * delta)
#
#
# print(rand_numbers(1, 20))

# 20. Определить, присутствует ли в заданном списке строк, некоторое число

# li = ['az', 'zb', 'c', 'asd', '5', 'qwerty', '89']
# num = str(5)
# print(f'Number {num} is in list' if num in li else f'Number {num} not found')


# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет .
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# li = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# li = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# li = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# li = ["123", "234", 123, "567"]
# li = []
# sub_str = 'qwe'
# sub_str = "йцу"
# sub_str = "123"


# if not li:
#     print('-1')
# else:
#     for line in li:
#         try:
#             first = li.index(sub_str)
#             second = li[first + 1:].index(sub_str) + 1
#             print(f'The index of the second match - {second}')
#             break
#         except ValueError as err:
#             print(err)


# 22. Найти сумму чисел списка стоящих на нечетной позиции2, 3, 5, 6] => [12,15]
#
# li = [2, 3, 4, 5, 6]
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# res = sum(list(filter(lambda x: lst.index(x) % 2 != 0, lst)))
# print(res)

# 23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент ,
# второй и предпоследний и т .д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [
# li = [2, 3, 4, 5, 6]
# li = [2, 3, 5, 6]
#
# length = len(li) // 2
# i = 0
# j = -1
# res = []
# while i <= length:
#     temp = li[i] * li[j]
#     res.append(temp)
#     i += 1
#     j -= 1
# print(sorted(list(set(res))))

# 24. В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# li = [1.1, 1.2, 3.1, 5, 10.01]
# li1 = []
# for i in range(len(li)):
#     temp = abs(int(li[i]) - li[i])
#     li1.append(temp)
#
# res = str(max(li1) - min(li1))
# print(res[0:4])
#
# # 25. Написать программу преобразования десятичного числа в двоичное

# number = int(input('Enter a number to convert to binary: '))
# deq = deque()
# while number:
#     deq.appendleft(number % 2)
#     number //= 2
#
# print(''.join(list(map(str, deq))))


# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def nega_fib(k):
#     li = []
#     m = 1
#     n = 1
#     for i in range(k + 1):
#         temp = m - n
#         li.append(temp)
#         m = n
#         n = temp
#     return list(reversed(li))
#
#
# negative = nega_fib(8)
#
#
# def fib(k):
#     li2 = []
#     m = 1
#     n = 1
#     li2.append(m)
#     li2.append(n)
#     for i in range(k - 2):
#         temp = m + n
#         li2.append(temp)
#         m = n
#         n = temp
#     return li2
#
#
# positive = fib(8)
# negative.extend(positive)
# print(negative)

# 27. Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

# s = '12 4 7 2 56 3 21 89 32 17'
# li = list(map(lambda x: int(x), s.split()))
# print(f'Larger number = {max(li)}, smaller number = {min(li)}')

# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
# a. Математикой
# b. Используя дополнительные библиотеки*

# def quadratic_equation(a, b, c):
#     discriminant = b ** 2 - (4 * a * c)
#     if discriminant < 0:
#         return f'No roots'
#     elif discriminant == 0:
#         x = (-b) / 2 * a
#         return x
#     else:
#         x1 = (-b - (discriminant ** 0.5)) / (2 * a)
#         x2 = (-b + (discriminant ** 0.5)) / (2 * a)
#         return x1, x2

# print(quadratic_equation(2, 5, -7))

# def quadratic_equation_lib(a, b, c):
#     discriminant = math.pow(b, 2) - (4 * a * c)
#     if discriminant < 0:
#         return f'No roots'
#     elif discriminant == 0:
#         x = (-b) / 2 * a
#         return x
#     else:
#         x1 = (-b - math.sqrt(discriminant)) / (2 * a)
#         x2 = (-b + math.sqrt(discriminant)) / (2 * a)
#         return x1, x2
#
#
# print(quadratic_equation_lib(2, 5, -7))

# 29. Найти НОК двух чисел

# def find_divider(m, n):
#     while m != n:
#         if m > n:
#             m -= n
#         else:
#             n -= m
#     return m
#
#
# print(find_divider(25, 75))

# 30. Вычислить число c заданной точностью d π
# Пример: при 𝑑  =  0. 001,  π  =  3. 141.  10−1≤ 𝑑 ≤ 10 −10

# d = int(input('Enter d: '))
# pi = math.pi
# print(str(pi)[:d])

# 31. Составить список простых множителей натурального числа

# def prime_factors(n):
#     li = []
#     count = 2
#     while n > 1:
#         if n % count != 0:
#             count += 1
#         else:
#             n /= count
#             li.append(count)
#     return li
#
#
# print(prime_factors(99))


# 32. Дана последовательность чисел. Получить список неповторяющихся элементов
# исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# li = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(set(li)))

# 33. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = 3
# lst = [random.randint(0, 100) for i in range(k + 1)]
# print(lst)
#
# li = []
# for i in range(len(lst)):
#     li.append(str(lst[i]) + '*x ^ ' + str(k - i) + ' + ')
#
# li.pop()
# li.append(str(lst[-1]))
# li.append(' = 0')
# text = ''.join(li)
# print(text)
#
#
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(text)

# 34. Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.

# s1 = '73*x^4+4*x^3+6*x^2+3*x+5=0'
# s2 = '5*x^3+2*x^2+4*x+5=0'

# with open('poly1.txt', encoding='utf-8') as f:
#     poly1 = f.read().replace('=0', '')
#
# with open('poly2.txt', encoding='utf-8') as f:
#     poly2 = f.read().replace('=0', '')
#
#
# def create_poly_list(st: str) -> list:
#     poly_lst = []
#     for i in range(len(st)):
#         if st[i] == 'x' and st[i - 1] != '*':
#             poly_lst.append('1')
#             poly_lst.append('*')
#             poly_lst.append('x')
#         else:
#             poly_lst.append(st[i])
#     return poly_lst
#
#
# poly_lst1 = create_poly_list(poly1)
# poly_lst2 = create_poly_list(poly2)
#
#
# def check_length(p1: list, p2: list):
#     res = []
#     if p1 > p2:
#         delta = len(p1) - len(p2)
#         res.append(p1[:delta])
#         p1 = p1[delta:]
#     elif p2 > p1:
#         delta = len(p2) - len(p1)
#         res.append(p2[:delta])
#         p2 = p2[delta:]
#     return p1, p2, res
#
#
# pol1, pol2, res = check_length(poly_lst1, poly_lst2)
#
#
# def poly_summa(p1: list, p2: list, result_list: list) -> list:
#     for i in range(len(p1)):
#         if p1[i].isdigit() and p1[i - 1] != '^':
#             temp = int(p1[i]) + int(p2[i])
#             result_list.append(str(temp))
#         else:
#             result_list.append(p1[i])
#     return result_list
#
#
# summa = ''.join(poly_summa(pol1, pol2, *res)) + ' = 0'
# print(summa)
#
# with open('poly_summa.txt', 'w', encoding='utf-8') as f:
#     f.write(summa)


# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 =  A[i-1]. Найти его.

# with open('numbers.txt', encoding='utf-8') as f:
#     s = f.read().split()
#
# print(s)
#
# for i in range(1, len(s)):
#     if int(s[i]) - 1 != int(s[i - 1]):
#         print(f'Missing number is - {int(s[i]) - 1}')
#         break

# 36. Дан список чисел. Создать список, в который попадают числа, описываемые
# возрастающую последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4] или [1, 7]
# или [1, 6, 7] и т.д. Порядок элементов менять нельзя

# li = [1, 5, 2, 3, 4, 6, 1, 7]
# lst = []

# for i in range(len(li) - 1):
#     if li[i] < li[i + 1] and li[i] not in lst:
#         lst.append(li[i])

# i = 1
# lst.append(li[0])
# while i < len(li) - 1:
#     if li[i - 1] < li[i] < li[i + 1]:
#         lst.append(li[i])
#     i += 1

# print(lst)

# 37. Дан список чисел. Создать список в который попадают числа, описываемые
# возрастающую последовательность и содержащие максимальное количество
# элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

# li = [1, 5, 2, 3, 4, 6, 1, 7]
li = [5, 2, 3, 4, 6, 1, 7]

lst = [i for i in range(len(li) - 1) if li[i] > li[i + 1]]
# print(lst)

seq1 = li[:lst[0] + 1]
seq2 = li[lst[0] + 1:lst[1] + 1]
seq3 = li[lst[1] + 1:]

# print(seq1)
# print(seq2)
# print(seq3)

res = [seq1, seq2, seq3]
for i in range(len(res)):
    if len(res[0]) < len(res[i]):
        res[0].pop(-1)
        res[0].extend(res[i])
    elif len(res[0]) > len(res[i]):
        res[i].pop(0)
        res[0].extend(res[i])


# print(res[0])

# 38. Напишите программу , удаляющую из текста все слова содержащие "абв".

# text = 'абвгд про укпллвд молекабв цукыв фвррв укабвнел'
# print(text)
# pattern = 'абв'
# li = text.split()
#
# lst = [li[i] for i in range(len(li)) if not re.findall(pattern, li[i])]
# print(' '.join(lst))

# 39. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую
# игру для игры человек против человека
# a. Добавьте игру против бота
# b. Подумайте как наделить бота "интеллектом"

# def game(total):
#     print(f'There ara {total} candies')
#     while total > 0:
#         num = int(input('Select the number in the range 3 to 6: '))
#         total -= num
#         if total <= 0:
#             print('You loose!')
#         else:
#             print(f'There ara {total} candies left')
#
#
# game(20)

# def game_with_bot(total):
#     minimum = 3
#     maximum = 6
#     print(f'There are {total} candies')
#     while total > 0:
#         num = int(input('Select the number in the range 3 to 6: '))
#         total -= num
#         if total <= 0:
#             print('You loose!')
#             break
#         else:
#             print(f'There are {total} candies left')
#         time.sleep(1)
#         print('AI is running')
#         time.sleep(1)
#         if total <= maximum:
#             num = minimum
#             time.sleep(1)
#             print(f'AI choice is - {num}')
#             total -= num
#             time.sleep(1)
#             if total <= 0:
#                 print('AI loose!')
#                 break
#             else:
#                 print(f'There are {total} candies left')
#         else:
#             num = random.choice(range(minimum, maximum + 1))
#             print(f'AI choice is - {num}')
#             total -= num
#             time.sleep(1)
#             print(f'There are {total} candies left')
#
#
# game_with_bot(20)


# 41. Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4;
# 1+2*3 => 7; 1-2*3 => -5;
# a. Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def summa(x, y):
    return x + y


operators = {'*': mul, '-': sub, '+': summa}

s = '2*3+3'
elements = [el for el in s]
# print(elements)


# temp = 0
# for el in s:
#     if operators.get('*'):
#         temp = operators['*'](int(s[s.index('*') - 1]), int(s[s.index('*') + 1]))
#
# # print(temp)
# s = str(temp) + s[s.index('*') + 2:]
# # print(s)
# for el in s:
#     if operators.get('+'):
#         temp = operators['+'](int(s[s.index('+') - 1]), int(s[s.index('+') + 1]))
#
# s = str(temp)
# # print(s)

# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a. входные и выходные данные хранятся в отдельных файлах

# with open('encoding_string.txt', encoding='utf-8') as f:
#     text = f.read()
#
#
# def encode(s: str):
#     st = ''
#     count = 0
#     previous = ''
#     for i in range(len(s) - 1):
#         previous = s[i]
#         count += 1
#         if s[i + 1] != previous:
#             st += str(count) + s[i]
#             previous = s[i + 1]
#             count = 0
#     else:
#         count += 1
#         st += str(count) + previous
#     return st
#
#
# print(encode(text))
# encode_st = encode(text)
#
# with open('decoding_string.txt', 'w', encoding='utf-8') as f:
#     f.write(encode_st)
#
# with open('decoding_string.txt', encoding='utf-8') as f:
#     decode_st = f.read()
#
#
# def decode(s: str):
#     st = ''
#     for i in range(len(s)):
#         if s[i].isdigit():
#             st += s[i + 1] * int(s[i])
#     return st
#
#
# print(decode(decode_st))




# 43. Дана последовательность чисел. Получить список уникальных элементов заданной
# последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

li = [1, 2, 3, 5, 1, 5, 3, 10]

# res = list(filter(lambda x: li.count(x) == 1, li))
# print(res)

# lst = []
# for i in range(len(li)):
#     if li.count(li[i]) > 1:
#         continue
#     else:
#         lst.append(li[i])
# print(lst)
