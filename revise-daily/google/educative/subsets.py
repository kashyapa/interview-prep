import collections

def subsets(nums):

    subsets = collections.deque([])
    subsets.append([])

    for i, n in enumerate(nums):

        length = len(subsets)

        for i in range(length):
            new_subset = list(subsets[i])
            new_subset.append(n)
            subsets.append(new_subset)
    return subsets

