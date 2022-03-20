from manage import *

change = {
    '1': add_new_employee,
    '2': add_new_position,
    '3': change_status,
    '4': add_new_contacts,
    '5': change_contacts,
    '6': add_new_address
}
show = {
    '1': show_contacts,
    '2': show_addresses,
    '3': show_all_stuff_salary,
    '4': show_employee_salary,
    '5': show_all_employees_contacts,
    '6': find_employee_contacts,
    '7': count_stuff,
    '8': show_employee_age,
    '9': show_status,
    '10': show_positions
}


def user():
    while True:
        data = input('Продолжить работу? Y/N: ').lower()
        if data == 'n':
            break
        elif data == 'y':
            data = input('Выберите "1" для изменения данных, "2" для получения данных: ')
            if data == '1':
                query = input(
                    'Выберите:\n'
                    '1 - Добавить нового сотрудника\n'
                    '2 - Добавить новую должность\n'
                    '3 - Изменить статус сотрудника\n'
                    '4 - Добавить новые контактные данные\n'
                    '5 - Изменить контактные данные\n'
                    '6 - Добавить новый адрес сотрудника\n: '
                )
                change[query]()
            elif data == '2':
                query = input(
                    'Выберите:\n'
                    '1 - Показать контакты сотрудника\n'
                    '2 - Показать адреса сотрудников\n'
                    '3 - Показать зарплату всего персонала\n'
                    '4 - Показать зарплату сотрудника\n'
                    '5 - Показать контакты всех сотрудников\n'
                    '6 - Показать должность и контакты сотрудника\n'
                    '7 - Показать количество сотрудников\n'
                    '8 - Показать возраст сотрудников\n'
                    '9 - Показать статус\n'
                    '10 - Показать перечень должностей\n: ')
                show[query]()


# user()

conn.close()
