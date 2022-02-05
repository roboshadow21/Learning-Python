# Семинар 1-2: примерный список задач

# 1. По двум заданным числам проверить является ли одно квадратом второго

x = 2
y = 8
if x * x == y:
    print(f'{y} is a square of {x}')
else:
    print(f'{y} is not square of {x}')

# 2. Найти максимальное из пяти чисел

lst = [2, 17, 6, 34, 12]
# print(max(lst))
maximum = 0
for i in range(len(lst) - 1):
    maximum = lst[i]
    if lst[i + 1] > maximum:
        maximum = lst[i + 1]
print(maximum)

# 3. Вывести на экран числа от -N до N

numbers = range(-10, 11)
for i in numbers:
    print(i, end=' ')

# 4. Показать первую цифру дробной части числа
print()
x = 32.86793
y = int(x)
z = x - y
print(int(z * 10))

# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

number = 40
if number % 5 == 0 and number % 10 == 0 and number % 30 != 0:
    print(f'{number} multiply 5 and 10 but 30')
else:
    print(f'{number} not multiply')

# 6. Дано число обозначающее день недели. Вывести его название и указать является ли
# он выходным.

day = 5
week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
if week.get(day) and day == 6 or day == 7:
    print(week[day], " - Weekend!")
else:
    print(week[day])
