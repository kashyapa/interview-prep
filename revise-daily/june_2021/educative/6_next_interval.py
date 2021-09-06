class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq


def next_interval(intervals):
    start_max_heap = []
    end_max_heap = []
    for i in range(len(intervals)):
        heapq.heappush(start_max_heap, (-intervals[i][0], i))
        heapq.heappush(end_max_heap, (-intervals[i][1], i))

    res = [-1] * len(intervals)

    for _ in range(len(intervals)):
        top_end, idx = heapq.heappop(end_max_heap)
        if end_max_heap and -top_end < -start_max_heap[0][0]:
            top_start, start_idx = start_max_heap.pop()
            while -top_end < -start_max_heap[0][0]:
                top_start, start_idx = start_max_heap.pop()

            res[idx] = start_idx
            heapq.heappush(start_max_heap, (top_start, start_idx))
    return res
