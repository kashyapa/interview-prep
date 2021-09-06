import imports


def minimum_window_sort(nums):
    low, high = 0, len(nums)-1

    while low < len(nums)-1 and nums[low] < nums[low+1]:
        low += 1

    while high > 0 and nums[high] > nums[high-1]:
        high -= 1


    subarray_min = imports.inf
    subarray_max = -imports.inf

    for k in range(low, high):
        subarray_min = min(subarray_min, nums[k])
        subarray_max = max(subarray_max, nums[k])

    while low > 0 and nums[low-1]>subarray_min:
        low -= 1

    while high < len(nums)-1 and nums[high+1] < subarray_max:
        high += 1

    return high - low + 1
