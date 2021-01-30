# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

from heapq import *
from collections import Counter


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    min_heap = []
    count = Counter(nums)

    for c, v in count.items():
        heappush(min_heap, (v, c))
        if len(min_heap) > k:
            heappop(min_heap)

    while min_heap:
        topNumbers.append(heappop(min_heap)[1])

    return topNumbers


def main():

    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


if __name__ == '__main__':
    main()
