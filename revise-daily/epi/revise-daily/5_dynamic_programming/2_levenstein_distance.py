def edit_distance(s1, s2):
    return edit_distance_rec(s1,s2, len(s1)-1, len(s2)-1)


def edit_distance_rec(s1, s2, i1, i2):
    if i1 == 0:
        return i2
    elif i2 == 0:
        return i1

    if s1[i1] == s2[i2]:
        return edit_distance_rec(s1, s2, i1 - 1, i2 - 1)
    add_character_in_s1 = edit_distance_rec(s1, s2, i1, i2 - 1)
    delete_character_in_s1 = edit_distance_rec(s1, s2, i1 - 1, i2)
    replace_character = edit_distance_rec(s1, s2, i1 - 1, i2 - 1)

    return add_character_in_s1 + delete_character_in_s1 + replace_character


if __name__ == '__main__':
    print(edit_distance("tabactor", "badactor"))