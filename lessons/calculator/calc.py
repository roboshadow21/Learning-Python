import operators as op
from fractions import Fraction


def calc_int(st: str):
    li = st.split()
    while len(li) > 1:
        for el in li:
            if el == '(':
                idx = li.index(el)
                li.pop(idx)
                first = int(li.pop(idx))
                operator = li.pop(idx)
                second = int(li.pop(idx))
                li.pop(idx)
                result = op.operators_dict[operator](first, second)
                li.insert(idx, str(result))

        for el in li:
            if el == '*':
                idx = li.index(el) - 1
                first = int(li.pop(idx))
                operator = li.pop(idx)
                second = int(li.pop(idx))
                result = op.operators_dict[operator](first, second)
                li.insert(idx, str(result))

        for el in li:
            if el == '/':
                idx = li.index(el) - 1
                first = int(li.pop(idx))
                operator = li.pop(idx)
                second = int(li.pop(idx))
                result = op.operators_dict[operator](first, second)
                li.insert(idx, str(round(result, 2)))

        for el in li:
            if el == '+':
                idx = li.index(el) - 1
                first = int(li.pop(idx))
                operator = li.pop(idx)
                second = int(li.pop(idx))
                result = op.operators_dict[operator](first, second)
                li.insert(idx, str(result))

        for el in li:
            if el == '-':
                idx = li.index(el) - 1
                first = int(li.pop(idx))
                operator = li.pop(idx)
                second = int(li.pop(idx))
                result = op.operators_dict[operator](first, second)
                li.insert(idx, str(result))
    return ''.join(li)


def calc_complex(st: str) -> complex:
    li = st.split()
    result = 0
    lst = []
    for i in range(len(li)):
        if li[i] in op.operators_dict:
            real_number1, real_number2 = li[i - 2], li[i + 1]
            imaginary_number1, imaginary_number2 = li[i - 1], li[i + 2]
            temp1 = complex(int(real_number1), int(imaginary_number1))
            temp2 = complex(int(real_number2), int(imaginary_number2))
            lst.append(temp1)
            lst.append(li[i])
            lst.append(temp2)
    for i in range(len(lst)):
        if lst[i] in op.operators_dict:
            first = lst[i - 1]
            second = lst[i + 1]
            result = op.operators_dict[lst[i]](first, second)
    return result


def calc_rational(st: str):
    li = st.split()
    result = 0
    lst = []
    for i in range(len(li)):
        if li[i] in op.operators_dict:
            numerator1, numerator2 = li[i - 2], li[i + 1]
            denominator1, denominator2 = li[i - 1], li[i + 2]
            temp1 = Fraction(int(numerator1), int(denominator1))
            temp2 = Fraction(int(numerator2), int(denominator2))
            lst.append(temp1)
            lst.append(li[i])
            lst.append(temp2)
    for i in range(len(lst)):
        if lst[i] in op.operators_dict:
            first = lst[i - 1]
            second = lst[i + 1]
            result = op.operators_dict[lst[i]](first, second)
    return result
