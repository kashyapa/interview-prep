from imports import *


def find_sum_of_elements(nums, k1, k2):
    max_heap = []

    for i in range(k2):
        if i < k2-1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    
    sum = 0
    for i in range(k2-k1-1):
        sum += -heappush(max_heap)
    
    return sum

