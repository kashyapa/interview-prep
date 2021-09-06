
def permutation_swapcase(str):

# abcd, Abcd, aBcd, ABcd, abCd, AbCd, aBCd, ABCd, abcD, AbcD, aBcD, ABcD, abCD, AbCD, aBCD, ABCD

    perms = []
    perms.append(str)

    for i in range(len(str)):

        n = len(perms)
        if str[i].isalpha():
            for j in range(n):
                new_perm = perms[j]
                chs = list(new_perm)
                chs[i] = chs[i].swapcase()
                perms.append("".join(new_perm))
    return perms

