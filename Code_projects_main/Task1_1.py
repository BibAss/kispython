import math


def main(n):
    sun = 0
    y = len(n)
    for i in range(1, y + 1):
        sun += math.pow(1 + 41 * math.pow(n[y - i], 3) +
                        34 * math.pow(n[y - i], 2), 4) / 55
    return 54 * sun


print(main([-0.3, -0.63, 0.07]))
