size = 3
field = [['-' for _ in range(size)] for _ in range(size)]


def show_field():
    for i in field:
        print(*i)