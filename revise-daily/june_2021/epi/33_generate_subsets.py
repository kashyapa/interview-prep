def generate_subsets(nums):
    subsets = []
    subsets.append([])

    for n in nums:
        l = len(subsets)

        for i in range(l):
            prev = subsets[i]
            next_subset = list(prev)
            next_subset.append(n)
            subsets.append(next_subset)
    return subsets
