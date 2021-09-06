from heapq import *
import math

def find_smallest_range(lists):
    max_seen = -math.inf
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], lists[i], 0))
        max_seen = max(max_seen, lists[i][0])
    min_range = math.inf
    first, last = -1, -1
    while min_heap:
        num, l, idx = heappop(min_heap)
        if max_seen - num < min_range:
            min_range = max_seen - num
            first, last = num, max_seen

        if idx+1 > len(l):
            heappush(min_heap, (l[idx+1], l. idx+1))
            max_seen = max(max_seen, l[idx+1])

    return first, last
