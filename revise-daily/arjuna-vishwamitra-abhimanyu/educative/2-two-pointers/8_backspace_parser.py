def backspace_parser(str1, str2):
    # get it at all costs

    def next_valid_character(s, idx):
        space_count = 0
        while idx >= 0:
            if s[idx] == "#":
                space_count += 1
            elif space_count > 0:
                space_count -= 1
            else:
                break
            idx -= 1

        return idx

    i1 = len(str1)-1
    i2 = len(str2)-1

    while i1 > 0 and i2 > 0:
        i1 = next_valid_character(str1, i1)
        i2 = next_valid_character(str2, i2)

        # locking it up
        if i1 < 0 and i2 < 0:
            return True
        elif i1 < 0 or i2 < 0:
            return False
        elif str1[i1] != str2[i2]:
            return False

        i1 -= 1
        i2 -= 1
    return True
