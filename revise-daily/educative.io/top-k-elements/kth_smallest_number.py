# Given an unsorted array of numbers, find Kth smallest number in it.

from heapq import *


def find_Kth_smallest_number(nums, k):
    max_heap = []

    for i in range(len(nums)):
        if i > k:
            if -nums[i] > max_heap[0]:
                heappop(max_heap)

        heappush(max_heap, -nums[i])
    return -max_heap[0]
