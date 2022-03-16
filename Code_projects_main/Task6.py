def main(x):
    return f2(x)


def f0_1(x):
    if x[0] == 'SLASH':
        return 0
    elif x[0] == 'DM':
        return 1
    elif x[0] == 'IDL':
        return 2


def f0_2(x):
    if x[0] == 'SLASH':
        return f3_1(x)
    elif x[0] == 'DM':
        return f3_2(x)
    elif x[0] == 'IDL':
        return 10


def f4(x):
    if x[4] == 1969:
        return 3
    elif x[4] == 1961:
        return f0_1(x)


def f1(x):
    if x[1] == 'HTML':
        return f4(x)
    elif x[1] == 'SQL':
        return f0_2(x)


def f2(x):
    if x[2] == 2012:
        return 11
    elif x[2] == 1969:
        return 12
    elif x[2] == 2001:
        return f1(x)


def f3_1(x):
    if x[3] == 'IDRIS':
        return 4
    elif x[3] == 'SCALA':
        return 5
    elif x[3] == 'MINID':
        return 6


def f3_2(x):
    if x[3] == 'IDRIS':
        return 7
    elif x[3] == 'SCALA':
        return 8
    elif x[3] == 'MINID':
        return 9
