#!/usr/bin/env python
# check if a string can be permuted to form a palindrome
import collections


def check_palindromic_permutation_possible(s):
    c = collections.Counter()
    count_odd: [int] = 0
    for ch in s:
        if c[ch] == 0:
            count_odd += 1
            c[ch] += 1
        else:
            count_odd -= 1
            c[ch] -= 1

    return "yes" if count_odd <= 1 else "no"


if __name__ == "__main__":
    s = "lssal"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = ""
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "lsl"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "lafdsfddsl"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "ll"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "l"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "laaaaa"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
