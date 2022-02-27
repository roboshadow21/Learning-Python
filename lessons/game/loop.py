import matrix as m
import check_value as ch


def game_loop():
    m.show_field()
    status = False
    while not status:
        if ch.check_row() or ch.check_column() or ch.check_main_diagonal() or ch.check_side_diagonal():
            m.show_field()
            print('Game over!')
            status = True
        else:
            i, j = map(int, input('Enter num: ').split())
            m.field[i][j] = input('Enter x or 0: ')
            m.show_field()
            print()


game_loop()
