from heapq import *


def next_interval(intervals):
    start_max_heap = []
    end_max_heap = []

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i][0], i))
        heappush(end_max_heap, (-intervals[i][1], i))

    res = [-1] * len(intervals)

    for i in range(len(intervals)):
        top_end, idx = heappop(end_max_heap)
        if start_max_heap and -start_max_heap[0][0] > -top_end:
            top_start, start_idx = heappop(start_max_heap)
            while start_max_heap and -start_max_heap[0][0] > -top_end:
                top_start, start_idx = heappop(start_max_heap)
            res[idx] = start_idx
            heappush(start_max_heap, (top_start, start_idx))
    return res
