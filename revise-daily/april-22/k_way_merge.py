from heapq import *
import math

def smallest_number_range(nums):

    min_heap = []
    max_number = math.inf
    lowest, highest = -1, -1
    for i in range(len(nums)):

        heappush(min_heap, (nums[i][0], i, 0))
        max_number = max(max_number, nums[i][0])

    while min_heap:
        num, row_index, col_index = heappop(min_heap)
        range = max_number - num
        if range < min_range:
            min_range = range
            highest = max_number
            lowest = num
        if col_index + 1 <= len(nums[i]):
            heappush(min_heap, (nums[i][col_index+1], row_index, col_index+1))
            max_number = max(max_number, nums[i][col_index+1])

    return lowest, highest
