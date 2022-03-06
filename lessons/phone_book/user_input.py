import csv
from collections import namedtuple

csv.register_dialect('excel-semicolon', delimiter=' ')
encoding = 'utf-8'
Phone = namedtuple('Phone', 'Name, Surname, Phone_number')


def one_line_input():
    csv.register_dialect('excel-semicolon', delimiter=';')
    while True:
        user_input = input('Enter name, surname, phone number: ')
        if user_input == 'q':
            break
        else:
            data = Phone._make(user_input.split())
        with open('phone_book.csv', 'a', encoding=encoding) as f:
            writer = csv.writer(f, dialect='excel-semicolon')
            writer.writerow(data)


# one_line_input()


def line_by_line_input():
    csv.register_dialect('excel-semicolon', delimiter=' ')
    while True:
        user_input = input('Enter name, surname, phone number: ')
        if user_input == 'q':
            break
        else:
            data = Phone._make(user_input.split())
        with open('phone_book2.csv', 'a', encoding=encoding) as f:
            writer = csv.writer(f, dialect='excel-semicolon')
            writer.writerows(data)


# line_by_line_input()


def one_line_output():
    with open('phone_book.csv') as f:
        reader = csv.reader(f, dialect='excel-semicolon')
        print(' '.join(Phone._fields))
        print('-' * 25)
        for el in reader:
            print('   '.join(el))


# one_line_output()


def line_by_line_output():
    csv.register_dialect('excel-semicolon', delimiter=';')
    with open('phone_book.csv') as f:
        reader = csv.reader(f, dialect='excel-semicolon')
        print('\n'.join(Phone._fields))
        print('-' * 25)
        for el in reader:
            print('\n'.join(el))


# line_by_line_output()


# Employee = namedtuple('Employee', 'name, age, department, pay')
#
# with open('employees.csv') as csvfile:
#     for emp in map(Employee._make, csv.reader(csvfile, dialect)):
#         print(emp.name, emp.pay)


# New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
# hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_3)
# print(hero_3.race)
#
# prop = ['name', '3race', 'health', '_mana', 'strength']
# New_Person_1 = namedtuple('New_Person_1', prop, rename=True) # переименование недопустимых имен (цифры и т.п)
# hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
# print(hero_4)
#
# print('*' * 50)
# Point = namedtuple('Point', 'x, y, z')
# p1 = Point(2, z=3, y=4)
# print(p1)
#
# t = [5, 10, 15]
# p2 = Point._make(t)
# print(p2)
# d2 = p2._asdict()
# print(d2)
#
# p3 = p2._replace(x=6)
# print(p3)
#
# print(p3._fields)
#
# print('*' * 50)
#
# New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
# p4 = New_Point(5)
# print(p4)
#
# print(p4._field_defaults)
#
# dct = {'x': 10, 'y': 20, 'z': 30}
# p5 = New_Point(**dct)
# print(p5)
