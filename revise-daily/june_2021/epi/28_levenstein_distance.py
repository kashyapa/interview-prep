def levenstein_distance(s1, s2):

    def rec(i1, i2):

        if i1 == len(s1):
            return len(s2) - i2
        elif i2 == len(s2):
            return len(s1) - i1

        if s1[i1] == s2[i2]:
            return rec(i1+1, i2+1)

        with_addition = 1 + rec(i1, i2+1)
        with_deletion = 1 + rec(i1+1, i2)
        with_edit = 1 + rec(i1+1, i2+1)

        return max(with_addition, with_deletion, with_edit)

    return rec(0, 0)

# cat
# cate

# caty
# cat
