import math


def subarray_sort(nums):
    
    lo_index, hi_index = 0, len(nums)-1

    while lo_index < len(nums)-1 and nums[lo_index] <= nums[lo_index+1]:
        lo_index += 1
    while hi_index > 0 and nums[hi_index] > nums[hi_index-1]:
        hi_index -= 1

    max_subarray = -math.inf
    min_subarray = math.inf

    for i in range(lo_index, hi_index):
        max_subarray = max(max_subarray, nums[i])
        min_subarray = min(min_subarray, nums[i])

    while lo_index > 0 and nums[lo_index-1] > min_subarray:
        lo_index -= 1

    while hi_index < len(nums)-1 and nums[hi_index+1] < max_subarray:
        hi_index += 1

    return hi_index - lo_index + 1