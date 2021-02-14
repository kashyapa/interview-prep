def int_to_string(x):
    is_negative = False
    str = []

    while True:
        str.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ''.join(reversed(str))


if __name__ == '__main__':
    print(int_to_string(98))
