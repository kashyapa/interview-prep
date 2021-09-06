import imports


def anonymous_letter_reconstructible_2(str, magazine):
    str_counter = imports.Counter(str)
    key_to_cover = len(str_counter)
    for c in magazine:
        str_counter[c] -= 1
        if str_counter[c] == 0:
            key_to_cover -= 1
            del str_counter[c]
    return not(key_to_cover > 0)



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
