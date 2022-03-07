import csv
from collections import namedtuple

csv.register_dialect('excel-semicolon', delimiter=' ')
encoding = 'utf-8'
Phone = namedtuple('Phone', 'Name, Surname, Phone_number')


def one_line_input():
    csv.register_dialect('excel-semicolon', delimiter=' ')
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
    with open('phone_book2.csv') as f:
        reader = csv.reader(f, dialect='excel-semicolon')
        print('\n'.join(Phone._fields))
        print('-' * 25)
        for el in reader:
            print('\n'.join(el))


# line_by_line_output()

# with open('phone_book.csv') as f:
#     reader = csv.reader(f, dialect='excel-semicolon')
#     data = [el for el in reader if el]
#     for el in map(Phone._make, data):
#         print(el.Name)
#         print(el.Surname)
