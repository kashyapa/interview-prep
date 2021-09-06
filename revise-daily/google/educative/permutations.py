from collections import deque

def permutations(nums):

    perms = deque([])
    res = []
    for i in range(len(nums)):
        n = len(perms)

        for j in range(n):
            p = perms.popleft()

            for k in range(len(p)+1):
                new_perm = list(p)
                new_perm.insert(k, nums[i])
                if len(new_perm) == len(nums):
                    res.append(new_perm)
                else:
                    perms.append(new_perm)

