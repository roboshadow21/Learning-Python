import operators as op


def calc(st):
    if 'j' in st:
        return eval(st)
    else:
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
                    li.insert(idx, str(result))

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


