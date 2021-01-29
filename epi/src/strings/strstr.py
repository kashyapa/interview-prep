#!/usr/bin/env python


def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle)):
        if needle[0] == haystack[i]:
            j = 0
            while j < len(needle) and needle[j] == haystack[i + j]:
                j += 1
            if j == len(needle):
                return i
    return -1


if __name__ == "__main__":
    res = strStr("Hello", "ll")
    print(res)
