# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

from heapq import *


def kth_smallest_element_in_m_arrays(arr, k):
    min_heap = []
    for i in range(len(arr)):
        heappush(min_heap, (arr[i][0], 0, arr[i]))

    number_count, number = 0, 0

    while min_heap:
        val, i, list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break

        if len(list) > i+1:
            heappush(min_heap, (list[i+1], i+1, list))

    return val
