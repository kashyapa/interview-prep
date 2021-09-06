def permutations_swapcase(str):

    perms = [str]

    for i in range(len(str)):
        if str[i].isalpha():
            for j in range(len(perms)):
                chs = list(perms[j])
                chs[i] = chs[i].swapcase()
                perms.append("".join(chs))
    return perms
