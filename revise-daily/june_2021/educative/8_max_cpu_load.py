class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

from heapq import *


def max_cpu_load(jobs):
    min_heap = []
    cpu_load = 0
    max_cpu_load = 0

    jobs.sort(key=lambda x:x.start)

    for j in jobs:
        while min_heap and min_heap[0].end < j.start:
            completed_job = heappop(min_heap)
            cpu_load -= completed_job.load

        cpu_load += j.load
        heappush(min_heap, j)
        max_cpu_load = max(max_cpu_load, cpu_load)
    return max_cpu_load
