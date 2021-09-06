from imports import *

def permutations(nums):
    # []
    # [1],
    # [1,2], [2, 1]
    # [3, 1, 2], [2,3,1], [2,1,3], [3,2,1], [2,3,1], [2,1,3]]
    perms = deque([])
    perms.append([])
    res = []

    for i in range(len(nums)):

        n = len(perms)
        for j in range(n):
            p = perms.popleft()

            for idx in range(len(p)+1):
                new_perm = list(p)
                new_perm.insert(idx, nums[i])

                perms.append(new_perm)
                if len(new_perm) == len(nums):
                    res.append(new_perm)
    return res
