from manage import *

user = input('Enter num: ')
if user == '1':
    show_all_employees_contacts()
elif user == '2':
    show_all_stuff_salary()


conn.close()