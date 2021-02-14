import functools


def ss_decode_col(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
