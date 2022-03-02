import operators as op
from fractions import Fraction


def calc_int(st: str):
    li = list(st)
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
    li = []
    result = 0
    for i in range(len(st)):
        if st[i] == ',':
            first = st[i - 1]
            second = st[i + 1]
            temp = complex(int(first), int(second))
            li.append(temp)
        elif st[i] in op.operators_dict:
            li.append(st[i])

    for i in range(len(li)):
        if li[i] in op.operators_dict:
            first = li[i - 1]
            second = li[i + 1]
            result = op.operators_dict[li[i]](first, second)
    return result


def calc_rational(st: str):
    li = []
    result = 0
    for i in range(len(st)):
        if st[i] == ',':
            first = st[i - 1]
            second = st[i + 1]
            temp = Fraction(int(first), int(second))
            li.append(temp)
        elif st[i] in op.operators_dict:
            li.append(st[i])

    for i in range(len(li)):
        if li[i] in op.operators_dict:
            first = li[i - 1]
            second = li[i + 1]
            result = op.operators_dict[li[i]](first, second)
    return result
