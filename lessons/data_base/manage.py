import sqlite3

conn = sqlite3.connect("office.db")
cursor = conn.cursor()


def add_new_employee():
    while True:
        data = input('Enter name, surname, sex, birthday, marital status, position id, status id\n'
                     'or enter "q" to exit: ').split()
        if data == ['q']:
            break
        else:
            cursor.execute("""insert into stuff(
            name, surname, sex, birthday_at, marital_status, position_id, status_id) values(
            ?, ?, ?, ?, ?, ?, ?);""", data)
            cursor.execute("select max(id) from stuff;")
            emp_id = cursor.fetchone()
            print(f'The new employee id is {emp_id[0]}')
            contacts = input('Enter employee id, phone, description phone, email, description email: ').split()
            cursor.execute("""insert into contacts(stuff_id, phone, description_phone, email, description_email) values(
                          ?, ?, ?, ?, ?);
                          """, contacts)
            address = input('Enter employee id, address, description: ').split()
            cursor.execute("""insert into addresses(stuff_id, address, description) values(
              ?, ?, ?);
              """, address)
            conn.commit()


# add_new_employee()


def add_new_position():
    pos, salary = map(str, input('Enter new position, salary: ').split())
    cursor.execute("insert into position(position, salary) values(?, ?);", (pos, salary))
    conn.commit()


# add_new_position()


def change_status():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute("select id, status_id, name, surname from stuff where name=? and surname=?;", (name, surname))
    view = cursor.fetchall()
    print(f'The current status_id of the employee is {view[0][1]}')
    status = int(input('Enter new status of the employee: '))
    cursor.execute("""update stuff set status_id=? where name=? and surname=?;""", (status, name, surname))
    conn.commit()


# change_status()


def add_new_contacts():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute("select id from stuff where name=? and surname=?;", (name, surname))
    emp_id = cursor.fetchone()
    phone, ph_descr, email, emp_descr = map(str, input('Enter phone, description, email, description: ').split())
    cursor.execute("insert into contacts(stuff_id, phone, description_phone, email, description_email) values("
                   "?, ?, ?, ?, ?);", (int(emp_id[0]), phone, ph_descr, email, emp_descr))
    conn.commit()


# add_new_contacts()


def change_contacts():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute(
        "select phone, description_phone, email, description_email from contacts "
        "where stuff_id=(select id from stuff where name=? and surname=?);", (name, surname))
    result = cursor.fetchall()
    print(result)
    while True:
        data = input('Enter 1 to change phone number, 2 to change email, 3 to quit: ')
        if data == '3':
            break
        elif data == '1':
            old, new = map(str, input('Enter the old phone number and the new phone number: ').split())
            cursor.execute("update contacts set phone=? where phone=?;", (new, old))
        elif data == '2':
            old, new = map(str, input('Enter the old email and the new email: ').split())
            cursor.execute("update contacts set email=? where email=?;", (new, old))
    conn.commit()


# change_contacts()


def add_new_address():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute("select id from stuff where name=? and surname=?", (name, surname))
    emp_id = cursor.fetchone()
    address, descr = map(str, input('Enter address, description: ').split())
    cursor.execute("insert into addresses(stuff_id, address, description) values("
                   "?, ?, ?);", (int(emp_id[0]), address, descr))
    conn.commit()


# add_new_address()


def show_contacts():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute(
        "select phone, description_phone, email, description_email from contacts "
        "where stuff_id=(select id from stuff where name=? and surname=?);", (name, surname))
    result = cursor.fetchall()
    print(result)


# show_contacts()


def show_addresses():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute(
        "select address, description from addresses "
        "where stuff_id=(select id from stuff where name=? and surname=?);", (name, surname))
    result = cursor.fetchall()
    print(result)


# show_addresses()


def show_all_stuff_salary():
    cursor.execute("select stuff.name, stuff.surname, position, position.salary "
                   "from stuff left join position on stuff.position_id=position.id;")
    res = cursor.fetchall()
    for el in res:
        print(el)


# show_all_stuff_salary()


def show_employee_salary():
    name, surname = map(str, input('Enter name, surname: ').split())
    cursor.execute("select stuff.name, stuff.surname, position, position.salary "
                   "from stuff left join position on stuff.position_id=position.id;")
    result = cursor.fetchall()
    for item in result:
        if name in item and surname in item:
            print(item)


# show_employee_salary()


def show_all_employees_contacts():
    cursor.execute("select name, surname, position, phone, email "
                   "from stuff left join contacts, position on stuff.id=contacts.stuff_id and "
                   "stuff.position_id=position.id;")
    emp = cursor.fetchall()
    for el in emp:
        print(el)


# show_all_employees_contacts()


def find_employee_contacts():
    surname = input('Enter surname: ')
    cursor.execute("select name, surname, position, phone, email "
                   "from stuff left join contacts, position on stuff.id=contacts.stuff_id and "
                   "stuff.position_id=position.id;")
    emp = cursor.fetchall()
    for el in emp:
        if surname in el:
            print(el)


# find_employee_contacts()


def count_stuff():
    cursor.execute("select count(id) from stuff;")
    result = cursor.fetchall()
    print(f'The total number of the stuff is {result[0][0]}')


# count_stuff()


def show_employee_age():
    cursor.execute("select name, surname, (datetime() - birthday_at) as age from stuff;")
    result = cursor.fetchall()
    for el in result:
        print(el)


# show_employee_age()


def show_status():
    status = input('Enter the status to find: ')
    cursor.execute(
        "select name, surname, position, description "
        "from stuff left join status, position on stuff.status_id=status.id and stuff.position_id=position.id;")
    result = cursor.fetchall()
    for item in result:
        if status in item:
            print(item)


# show_status()


# cursor.execute("select * from addresses")
# res = cursor.fetchall()
# print(res)

# Join tables

# cursor.execute("select stuff.name, stuff.surname, position.salary "
#                "from stuff left join position on stuff.position_id=position.id;")
#
# res = cursor.fetchall()
# print(res)

cursor.execute("select name, surname, position, description "
               "from stuff left join status, position on stuff.status_id=status.id and "
               "stuff.position_id=position.id;")

# res = cursor.fetchall()
# print(res)

cursor.execute("select name, surname from stuff where status_id=(select id from status where description='отпуск');")

# res = cursor.fetchall()
# print(res)

# conn.close()
