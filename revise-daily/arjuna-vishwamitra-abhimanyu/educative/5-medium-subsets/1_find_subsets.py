def find_subsets(nums):
    # [1, 2, 3]
    # [[], [1], [2], [1, 2], [3], [2, 3], [1, 2, 3]]
    subsets = []
    subsets.append([])

    for i in range(len(nums)):
        n = len(subsets)
        for j in range(n):
            new_subset = subsets[j]
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets

            

