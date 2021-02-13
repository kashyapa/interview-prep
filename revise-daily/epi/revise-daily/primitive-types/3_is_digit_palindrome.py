def is_palindrome(x):

    lsb, msb = 0, 0
    res = 1

    while res < x:
        div = res
        res *= 10

    while x > 0:
        lsb = x % 10
        msb = x // div
        if lsb != msb:
            return False
