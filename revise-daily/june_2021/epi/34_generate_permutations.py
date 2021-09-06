from collections import deque


def generate_permutations(nums):

    perms = deque([])
    perms.append([])

    # nums = [1, 2, 3]
    # perms [1]
    # perms [1,2],[2,1]
    # perms [3,1,2] [1,3,2], [1,2,3] [3,2,1] [2,3,1] [2,1,3]
    res = []
    for i in range(len(nums)):
        l = len(perms)
        for k in range(l):
            p = perms.popleft()

            for j in range(len(p)+1):
                new_perm = list(p)
                new_perm.insert(j, nums[i])
                if len(new_perm) == len(nums):
                    res.append(new_perm)
                else:
                    perms.append(new_perm)
    return res

print(generate_permutations([3,1,2,4]))