# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

from math import inf
from heapq import *


def find_smallest_range(lists):
    range_start, range_end = 0, inf
    current_max = -inf
    min_heap = []

    for i, list in enumerate(lists):
        heappush(min_heap, (list[i], i, list))
        current_max = max(current_max, list[i])

    while min_heap:
        num, i, lst = heappop(min_heap)

        if range_end - range_start > current_max - num:
            range_start = num
            range_end = current_max

        if i+1 < len(lst):
            heappush(min_heap, (lst[i+1], i+1, lst))
            current_max = max(current_max, lst[i+1])

    return [range_start, range_end]
