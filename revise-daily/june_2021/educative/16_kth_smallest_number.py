from heapq import *


def kth_smallest_number(nums):
    max_heap = []

    for i in range(len(nums)):
        if len(max_heap) < k:
            heappush(max_heap, (-nums[i]))
        else:
            if nums[i] < -max_heap[0]:
                heappush(max_heap, -nums[i])
                heappop(max_heap)

    return -max_heap[0]