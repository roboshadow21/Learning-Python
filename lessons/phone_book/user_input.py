import csv

csv.register_dialect('excel-semicolon', delimiter=' ')


def user_input1():
    while True:
        user_input = input('Enter name, surname, phone number: ')
        if user_input == 'q':
            break
        else:
            data = user_input.split()
        encoding = 'utf-8'
        with open('phone_book.csv', 'a', encoding=encoding) as f:
            writer = csv.writer(f, dialect='excel-semicolon')
            writer.writerow(data)


user_input1()

