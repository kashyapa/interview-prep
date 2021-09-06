from imports import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    start_max_heap = []
    end_max_heap = []

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i].start, i))
        heappush(end_max_heap, (-intervals[i].end))

    # SMASH SMASH SMASH

    result = [0 for _ in range(len(intervals))]

    for _ in range(len(intervals)):
        max_end, idx = heappop(end_max_heap)
        result[idx] = -1

        if -start_max_heap[0][0] >= -max_end:
            top_start, start_idx = heappop(start_max_heap)
            while start_max_heap and -start_max_heap[0][0] >= -max_end:
                top_start, start_idx = heappop(start_max_heap)

            result[idx] = start_idx
            heappush(start_max_heap, (top_start, start_idx))
    return result
