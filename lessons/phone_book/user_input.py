import data


def data_import():
    info = input('Choose 1 for one line writing or 2 for line by line: ')
    if info == '1':
        data.one_line_input()
    elif info == '2':
        data.line_by_line_input()


# data_import()


def data_export():
    info = input('Choose 1 for one-line output or 2 for line-by-line: ')
    if info == '1':
        data.one_line_output()
    elif info == '2':
        data.line_by_line_output()


# data_export()


def user_choice():
    choice = input('Enter 1 for import data or 2 for export: ')
    if choice == '1':
        data_import()
    elif choice == '2':
        data_export()


user_choice()
