def f(x):
    d = 0x00000000
    temp = x & 0x0000000f  # A
    temp = temp << 28
    d = d | temp
    temp = x & 0x00100000  # C
    temp = temp << 7
    d = d | temp
    temp = x & 0xf0000000  # H
    temp = temp >> 5
    temp = temp & 0x07800000
    d = d | temp
    temp = x & 0x04000000  # F
    temp = temp >> 4
    d = d | temp
    temp = x & 0x03800000  # E
    temp = temp >> 4
    d = d | temp
    temp = x & 0x08000000  # G
    temp = temp >> 9
    d = d | temp
    temp = x & 0x000ffff0  # B
    temp = temp >> 2
    d = d | temp
    temp = x & 0x00600000  # D
    temp = temp >> 21
    d = d | temp
    return d


print(f(0x8854acb9))
