def subset_with_duplicates(nums):

    subsets = []
    subsets.append([])
    start_idx, end_idx = 0, 0

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i-1]:
            start_idx = end_idx+1

        end_idx = len(subsets)-1

        for j in range(start_idx, end_idx+1):
            new_subset = list(subsets[j])
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets

