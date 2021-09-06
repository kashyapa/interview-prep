# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours.
# Our goal is to determine if there is a free interval which is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.

# sort based on earliest start time
# keep track of last ending time
# if the next start time is after the ending time
# it is a free interval

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start - other.start


def employee_free_time(employee_schedule):
    min_heap = []

    for i, interval in enumerate(employee_schedule):
        heappush(min_heap, (interval, i, 0))
    res = []
    previous_interval, employee_index, interval_index = min_heap[0]
    while min_heap:
        current_employee, employee_index, interval_index  = heappop(min_heap)
        if current_employee.start > previous_interval.end:
            res.append((previous_interval.end, current_employee.start))
        if current_employee.end > previous_interval.end:
            previous_interval = current_employee.interval

        if len(employee_schedule[employee_index]) > interval_index+1:
            heappush(min_heap, (employee_schedule[employee_index][interval_index+1]),
                     employee_index, interval_index+1)
    return res


class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


def max_cpu_load(jobs):
    min_heap = []
    current_load = 0
    max_load = 0
    jobs.sort(key=lambda x:x.start)
    for j in jobs:
        while min_heap and min_heap[0].end <= j.start:
            removed_job = heappop(min_heap)
            current_load -= removed_job.load
        heappush(min_heap, j)
        current_load += j.load
        max_load = max(max_load, current_load)
    return max_load


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def interval_intersection(intervals):
    start, end = intervals[0].start, intervals[0].end
    res = []
    intervals.sort(key=lambda x:x.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < end:
            res.append((max(intervals[i].start, start), min(intervals[i].end, end)))
        end = max(end, intervals[i].end)
    return res

