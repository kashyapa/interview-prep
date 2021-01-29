# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.


from heapq import *


def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if min_heap[0] < nums[i]:
            heappush(min_heap, nums[i])
            heappop(min_heap)

    return min_heap
