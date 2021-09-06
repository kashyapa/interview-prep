class Job:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.load = None

    def __lt__(self, other):
        return self.end < other.end


from imports import *


def max_cpu_load(jobs):

    min_heap = [jobs[0]]
    cur_load = 0
    cpu_load = 0

    for j in jobs[1:]:
        while j.start >= min_heap[0].end:
            cur_load -= j.load
        heappush(min_heap, j)
        cur_load += j.load
        
        cpu_load = max(cpu_load, cur_load)
    return cpu_load
