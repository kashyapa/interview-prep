def edit_distance(s1, s2):
    return edit_distance_rec(s1,s2, len(s1)-1, len(s2)-1)


def edit_distance_rec(s1, s2, i1, i2):
    if i1 == 0:
        return i2 + 1
    elif i2 == 0:
        return i1 + 1

    if s1[i1] == s2[i2]:
        return edit_distance_rec(s1, s2, i1 - 1, i2 - 1)

    add_character_in_s1 = edit_distance_rec(s1, s2, i1, i2 - 1)
    delete_character_in_s1 = edit_distance_rec(s1, s2, i1 - 1, i2)
    replace_character = edit_distance_rec(s1, s2, i1 - 1, i2 - 1)

    return 1 + min(add_character_in_s1, delete_character_in_s1, replace_character)


def edit_distance_dp(s1, s2):
    def compute_distance_between_prefixes(idx1, idx2):

        if idx1 < 0:
            return idx2 + 1

        elif idx2 < 0:
            return idx1 + 1

        if distance_between_prefixes[idx1][idx2] == - 1:
            if s1[idx1] == s2[idx2]:
                distance_between_prefixes[idx1][idx2] = compute_distance_between_prefixes(idx1-1, idx2-1)
            else:
                substitute_last = compute_distance_between_prefixes(idx1-1, idx2-1)
                add_last = compute_distance_between_prefixes(idx1-1, idx2)
                delete_last = compute_distance_between_prefixes(idx1, idx2-1)

                distance_between_prefixes[idx1][idx2] = 1 + min(substitute_last, add_last, delete_last)

        return distance_between_prefixes[idx1][idx2]

    distance_between_prefixes = [[-1] * len(s2) for _ in s1]
    return compute_distance_between_prefixes(len(s1)-1, len(s2)-1)


if __name__ == '__main__':
    print(edit_distance("tabactor", "badactor"))
    print(edit_distance_dp("tabactor", "badactor"))