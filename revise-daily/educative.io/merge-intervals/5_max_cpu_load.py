from heapq import *


class job:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_loads(jobs):

    jobs.sort(key=lambda x: x.start)

    min_heap = []
    max_cpu_load, current_cpu_load = 0, 0

    for j in jobs:
        # remove jobs that have ended
        while len(min_heap) > 0 and j.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)

        # add job to the heap, which now contains jobs that are currently running
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load
