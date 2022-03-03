import calc


def user_input():
    result = 0
    choice = input('To select the type of calculations enter:\nFor integer: 1\nFor complex: 2\nFor rational: 3\n: ')
    if choice == '1':
        st = input('Enter an expression, separator = space: ')
        result = calc.calc_int(st)
    elif choice == '2':
        st = input('Enter an expression with complex numbers, separator = space: ')
        result = calc.calc_complex(st)
    elif choice == '3':
        st = input('Enter an expression with rational numbers, separator = space: ')
        result = calc.calc_rational(st)
    return result
