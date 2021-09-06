def int_to_string(x):

    str = []
    while True:
        str.append(chr(ord('0')+x % 10))
        x //= 10
        if x == 0:
            break
    return "".join(reversed(str))

