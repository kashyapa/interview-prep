#!/usr/bin/env python
from collections import Counter


def anonymous_letter_reconstructible(letter, magazine):
    counter = Counter(magazine)

    for ch in letter:
        if counter[ch] == 0:
            return False
        counter[ch] -= 1
    return True


def anonymous_letter_reconstructible_2(letter, magazine):
    counter = Counter(letter)
    for ch in magazine:
        if ch in counter:
            counter[ch] -= 1
            if counter[ch] == 0:
                del counter[ch]
                if not counter:
                    break

    return not counter


if __name__ == "__main__":
    import sys

    magazine = "excuse me, i'm here"
    letter = "meee"
    print(anonymous_letter_reconstructible_2(letter, magazine))

    letter = "mee'me"
    print(anonymous_letter_reconstructible_2(letter, magazine))

    letter = "excuse i''m here"
    print(anonymous_letter_reconstructible_2(letter, magazine))

    #letter = sys.argv[1]
    #magazine = sys.argv[2]
    #print(anonymous_letter_reconstructible_2(letter, magazine))
