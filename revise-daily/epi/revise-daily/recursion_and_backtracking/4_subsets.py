from collections import deque


def generate_subsets(nums):
    subsets = deque()
    subsets.append([])

    for current_number in nums:
        n = len(subsets)
        for i in range(n):
            new_set = list(subsets[i])
            new_set.append(current_number)
            subsets.append(new_set)
    return subsets


if __name__ == '__main__':
    print(generate_subsets([1, 3, 5]))