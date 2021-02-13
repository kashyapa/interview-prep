def reverse_digits(x):
    rev = 0
    sign = 1
    if x < 0:
        sign = -1
    while x > 0:
        rem = x % 10
        x //= 10
        rev = rev * 10 + rem
    return sign * rev


if __name__ == "__main__":
    print(reverse_digits(1234))
