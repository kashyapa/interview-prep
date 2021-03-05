def is_palindrome(x):

    res = 1

    while res < x:
        div = res
        res *= 10

    while x > 0:
        lsb = x % 10
        msb = x // div
        if lsb != msb:
            return False
        x = (x % div)//10
        div //= 100
    return True


if __name__ == "__main__":
    print(is_palindrome(323))
    print(is_palindrome(3323))
    print(is_palindrome(1323))
    print(is_palindrome(23323))
    print(is_palindrome(3))
