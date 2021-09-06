from collections import deque

def case_sensitive_permutation(str):
    perms = deque([])
    perms.append(str)

    for i, c in enumerate(str):
        if c.isalpha():
            n = len(perms)
            for j in range(n):
                next_perm = list(perms[j])
                next_perm[i] = next_perm[i].swapcase()
                perms.append(''.join(next_perm))

    return perms
