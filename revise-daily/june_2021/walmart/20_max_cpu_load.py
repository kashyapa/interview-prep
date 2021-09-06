class Job:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.load = None

    def __lt__(self, other):
        return self.end < other.end


from heapq import *


def max_cpu_load(jobs):

    min_heap = []
    jobs.sort(key=lambda x:x.start)
    max_cpu_util = 0
    cpu_load = 0
    for j in jobs:
        while min_heap and j.start >= min_heap[0].end:
            cpu_load -= heappop(min_heap).load
        cpu_load += j.load
        heappush(min_heap, j)
        max_cpu_util = max(max_cpu_util, cpu_load)