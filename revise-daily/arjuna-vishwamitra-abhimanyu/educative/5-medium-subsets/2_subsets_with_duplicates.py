def subsets_with_duplicates(nums):

# 1, 2, 2, 3, 3, 4

# [[], [1], [2], [1, 2], [2,2], [1,2,2], [3], [1,3]

    subsets = []
    subsets.append([])
    end_index = 0

    for i in range(len(nums)):
        start_index = 0
        n = len(subsets)
        if i != 0 and nums[i] == nums[i-1]:
            start_index = end_index+1

        end_index = n

        for j in range(start_index, end_index):
            new_subset = list(subsets[j])
            new_subset.append(i)
            subsets.append(new_subset)
    return subsets
