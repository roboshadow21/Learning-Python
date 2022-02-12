n = input('Enter number: ')


def digits_summa(s):
    if len(s) < 2:
        return int(s[0])
    return int(s[0]) + int(digits_summa(s[1::1]))


print(digits_summa(n))