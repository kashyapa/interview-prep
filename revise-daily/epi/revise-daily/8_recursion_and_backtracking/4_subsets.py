from collections import deque


"""
 
 Iterate over the length of input array
 
 for each iteration over the input array, iterate over all the elements in subset array
 append the current number indexed by input array to each subset element
 

"""


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