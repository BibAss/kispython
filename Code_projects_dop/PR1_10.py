def FastMul():
    a = int(input("enter your numbers:\n"))
    b = int(input())
    n = 0
    m = 0
    w = 0
    #################
    if a > b:
        n = a
        m = b
    else:
        n = b
        m = a
    #################
    while m != 1:
        if (m % 2) != 0:
            w += n
        m //= 2
        n *= 2
        if m == 1:
            w += n
    #################
    print("your num is: " + str(w) + '\n')


def FastPow():
    n = int(input("enter your number: "))
    m = int(input("enter pow you need: "))
    w = 1
    #################
    while m != 1:
        if (m % 2) != 0:
            w *= n
        m //= 2
        n = n * n
        if m == 1:
            w *= n
    #################
    print("your num is: " + str(w) + '\n')


FastPow()
FastMul()
