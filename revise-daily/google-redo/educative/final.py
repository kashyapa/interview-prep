from collections import Counter
from heapq import *


def next_interval(intervals):
    start_points_max_heap = []
    end_points_max_heap = []
    for i in range(len(intervals)):
        heappush(start_points_max_heap, (-intervals[i][0], i))
        heappush(end_points_max_heap, (-intervals[i][1], i))

    res = [-1] * len(intervals)

    for i in range(len(intervals)):
        top_end, idx = heappop(end_points_max_heap)

        if -start_points_max_heap[0][0] >= -top_end:
            top_start, start_idx = heappop(start_points_max_heap)
            while -start_points_max_heap[0][0] > -top_end:
                top_start, start_idx = heappop(start_points_max_heap)

            res[idx] = start_idx
            heappush(start_points_max_heap, (top_start, start_idx))
    return res

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class EmployeeInterval:

    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def employee_free_time(schedules):
    min_heap = []
    for i in range(len(schedules)):
        heappush(min_heap, EmployeeInterval(schedules[i][0], i, 0))

    previous_interval = min_heap[0].interval
    res = []

    while min_heap:
        cur_employee = heappop(min_heap)
        if cur_employee.interval.start > previous_interval.end:

            res.append(Interval(previous_interval.end, cur_employee.interval.start))
            previous_interval = cur_employee.interval
        else:
            if previous_interval.end < cur_employee.interval.end:
                previous_interval = cur_employee.interval
        if cur_employee.interval_index +1 < len(schedules[cur_employee.employee_index]):
            heappush(min_heap, EmployeeInterval(schedules[cur_employee.employee_index][cur_employee.interval_index+1],
                                                cur_employee.employee_index,
                                                cur_employee.interval_index+1
                                                ))
    return res


def maximize_capital(capitals, profits, initial_capital, number_of_projects):
    capitals_min_heap = []
    profits_max_heap = []

    for i in range(len(capitals)):
        heappush(capitals_min_heap, (capitals[i], i))

    available_capital = initial_capital
    for _ in range(number_of_projects):

        while capitals_min_heap[0][0] <= available_capital:
            capital, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, -profits[i])

        available_capital += (-heappop(profits_max_heap)[0])
    return available_capital


class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


def max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    min_heap = []
    running_load = 0
    max_load = 0
    for j in jobs:

        while min_heap and min_heap[0].end < j.start:
            expired_job = heappop(min_heap)
            running_load -= expired_job.load

        heappush(min_heap, j)
        running_load += j.load
        max_load = max(max_load, running_load)
    return max_load


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    min_meeting_rooms = len(meetings)
    min_heap = []
    for m in meetings:
        while min_heap and min_heap[0].end < m.start:
            heappop(min_heap)
        heappush(min_heap, m)
        min_meeting_rooms = max(len(min_heap), min_meeting_rooms)
    return min_meeting_rooms


def intersection_intervals(intervals_a, intervals_b):
    i, j = 0, 0
    res = []
    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = intervals_b[j][0] < intervals_a[i][0] < intervals_b[j][1]
        b_overlaps_a = intervals_a[i][0] < intervals_b[j][0] < intervals_a[j][1]

        if a_overlaps_b or b_overlaps_a:
            res.append((max(intervals_b[j][0], intervals_a[i][0]),
                       min(intervals_b[j][1], intervals_a[i][1])))

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return res


class Element:
    def __init__(self, sequence_number, frequency, element):
        self.sequence = 0
        self.frequency = 0
        self.element = None

    def __lt__(self, other):
        return self.frequency > other.frequency


class FrequencyStack:

    def __init__(self):
        self.stack = []
        self.sequence_number = 0
        self.freq_counter = {}

    def push(self, item):
        self.freq_counter[item] += 1
        self.sequence_number += 1
        heappush(self.stack, Element(self.sequence_number, self.freq_counter[item], item))

    def pop(self):
        element = heappop(self.stack)
        self.freq_counter[element.element] -= 1
        if self.freq_counter[element.element] == 0:
            del self.freq_counter[element.element]

        return element.element



def increasing_decreasing_array(nums)

