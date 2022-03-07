import csv
from collections import namedtuple

# csv.register_dialect('excel-semicolon', delimiter=' ')
encoding = 'utf-8'
Phone = namedtuple('Phone', 'Name, Surname, Phone_number, Description')


def one_line_input():
    csv.register_dialect('excel-semicolon', delimiter=';')
    while True:
        user_input = input('Enter name, surname, phone number, description: ')
        if user_input == 'q':
            break
        else:
            data = Phone._make(user_input.split())
        with open('phone_book.csv', 'a', encoding=encoding) as f:
            writer = csv.writer(f, dialect='excel-semicolon')
            writer.writerow(data)


def line_by_line_input():
    csv.register_dialect('excel-semicolon', delimiter=' ')
    while True:
        user_input = input('Enter name, surname, phone number, description: ')
        if user_input == 'q':
            break
        else:
            data = Phone._make(user_input.split())
        with open('phone_book2.csv', 'a', encoding=encoding) as f:
            writer = csv.writer(f, dialect='excel-semicolon')
            writer.writerows(data)


def one_line_output():
    csv.register_dialect('excel-semicolon', delimiter=' ')
    with open('phone_book.csv') as f:
        reader = csv.reader(f, dialect='excel-semicolon')
        print(' '.join(Phone._fields))
        print('-' * 35)
        for el in reader:
            print('  '.join(el))


def line_by_line_output():
    csv.register_dialect('excel-semicolon', delimiter=';')
    with open('phone_book2.csv') as f:
        reader = csv.reader(f, dialect='excel-semicolon')
        print('\n'.join(Phone._fields))
        print('-' * 25)
        for el in reader:
            print('\n'.join(el))


# with open('phone_book.csv') as f:
#     reader = csv.reader(f, dialect='excel-semicolon')
#     data = [el for el in reader if el]
#     for el in map(Phone._make, data):
#         print(el.Name)
#         print(el.Surname)
