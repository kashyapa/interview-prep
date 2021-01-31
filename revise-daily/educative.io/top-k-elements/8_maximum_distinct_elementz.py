# Given an array of numbers and a number ‘K’,
# we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

from collections import Counter
from heapq import *


def find_maximum_distinct_elements(nums, k):
    freq_count = Counter(nums)
    min_heap = []
    distinct_elements = 0

    for num, v in freq_count.items():
        if v == 1:
            distinct_elements += 1
        else:
            heappush(min_heap, (v, num))

    while k > 0 and min_heap:
        frequency, num = heappop(min_heap)

        k -= frequency - 1
        if k >= 0:
            distinct_elements += 1

    if k > 0:
        distinct_elements -= k

    return distinct_elements


def main():

    print("Maximum distinct numbers after removing K numbers: " + str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " + str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " + str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


if __name__ == "__main__":
    main()
