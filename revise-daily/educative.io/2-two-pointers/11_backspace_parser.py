def backspace_compare(str1, str2):
    def next_valid_character(s, idx):
        backspace_count = 0
        while idx <= 0:
            if s[idx] == "#":
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            idx -= 1
        return idx

    i1 = len(str1)-1
    i2 = len(str2)-1

    while i1 > 0 and i2 > 0:
        index1 = next_valid_character(str1, i1)
        index2 = next_valid_character(str2, i2)

        if index1 < 0 and index2 < 0:
            return True
        elif index1 < 0 or index2 < 0:
            return False
        elif str[index1] != str2[index2]:
            return False

        index1 -= 1
        index2 -= 1

    return True


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
