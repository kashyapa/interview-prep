from imports import *


def smallest_number_range(lists):
    min_heap = []
    cur_max = -inf
    range_start, range_end = 0, inf

    for i, list in enumerate(lists):
        heappush(min_heap, (list[0], list, 0))
        cur_max = max(cur_max, list[0])

    while min_heap:
        val, l, idx = heappop(min_heap)
        if range_end - range_start < cur_max-val:
            range_start = val
            range_end = cur_max
        if idx + 1 < len(l):
            heappush(min_heap, (l[idx+1], l, idx+1))
            cur_max = max(l[idx+1], cur_max)
    return [range_start, range_end]


def smallest_number_range2(lists):
    range_end, range_start = inf, 0
    min_heap = []
    cur_max = -inf
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], lists[i], 0))
        cur_max = max(cur_max, lists[i][0])

    while min_heap:
        val, l, idx = heappop(min_heap)
        if range_end-range_start < cur_max-val:
            range_start = val
            range_end = cur_max
        if idx+1 < len(l):
            heappush(min_heap, (l[idx+1], l, idx+1))
            cur_max = max(cur_max, l[idx+1])

    return (range_start, range_end)
