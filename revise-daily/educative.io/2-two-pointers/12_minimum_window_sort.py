import math


def minimum_window_sort(arr):

    low, high = 0, len(arr) - 1

    while low < len(arr) - 1 and arr[low] <= arr[low+1]:
        low += 1

    if low == len(arr)-1:
        return 0

    while high > 0 and arr[high] > arr[high - 1]:
        high -= 1

    subarray_min = math.inf
    subarray_max = -math.inf

    for k in range(low, high):
        subarray_min = min(subarray_min, arr[k])
        subarray_max = max(subarray_max, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1

