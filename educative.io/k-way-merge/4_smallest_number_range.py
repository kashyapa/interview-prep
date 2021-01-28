# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

from math import inf
from heapq import *


def find_smallest_range(lists):
    min_heap = []
    current_max = -inf
    range_start, range_end = 0, inf

    for i in range(len(lists)):
        current_max = max(current_max, lists[i][0])
        heappush(min_heap, (lists[i][0], i, lists[i]))

    while min_heap:
        number, i, list = heappop(min_heap)
        if range_end - range_start > current_max - number:
            range_start = number
            range_end = current_max

        if i+1 < len(list):
            heappush(min_heap, list[i+1], i+1, list)
            current_max = max(list[i+1], current_max)

    return [range_start, range_end]
