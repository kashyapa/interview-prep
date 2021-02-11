# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

"""
Time complexity #
Since we’ll be going through at most ‘K’ elements among all the arrays, and we will remove/add one element in the heap
in each step, the time complexity of the above algorithm will be O(K*logM)O(K∗logM) where ‘M’ is the total number of
input arrays.

Space complexity #
The space complexity will be O(M)O(M) because, at any time, our min-heap will be storing one number from all the
 ‘M’ input arrays.
"""
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
