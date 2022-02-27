import matrix as m


def check_row():
    i = 0
    status = False
    while i < m.size:
        count_x = 0
        count_zero = 0
        for el in m.field[i]:
            if el == 'x':
                count_x += 1
            elif el == '0':
                count_zero += 1
        if count_x == m.size or count_zero == m.size:
            status = True
        i += 1
    return status


def check_column():
    status = False
    i = 0
    j = 0
    while i < m.size:
        k = 0
        count_x = 0
        count_zero = 0
        while k < m.size:
            if m.field[k][j] == 'x':
                count_x += 1
            elif m.field[k][j] == '0':
                count_zero += 1
            k += 1
        if count_x == m.size or count_zero == m.size:
            status = True
        i += 1
        j += 1
    return status


def check_main_diagonal():
    status = False
    i = 0
    count_x = 0
    count_zero = 0
    while i < m.size:
        if m.field[i][i] == 'x':
            count_x += 1
        elif m.field[i][i] == '0':
            count_zero += 1
        if count_x == m.size or count_zero == m.size:
            status = True
        i += 1
    return status


def check_side_diagonal():
    status = False
    count_x = 0
    count_zero = 0
    i = 0
    j = 0
    while i < m.size:
        if m.field[i][-j - 1] == 'x':
            count_x += 1
        elif m.field[i][-j - 1] == '0':
            count_zero += 1
        if count_x == m.size or count_zero == m.size:
            status = True
        i += 1
        j += 1
    return status



