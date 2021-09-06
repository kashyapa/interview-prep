from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Employee:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def employee_free_time(schedules):
    max_heap = []
    for i in range(len(schedules)):
        heappush(max_heap, Employee(schedules[i], i, 0))

    previous_employee_end = max_heap[0].interval.end

    res = []
    while max_heap:
        cur_employee = heappop(max_heap)

        if previous_employee_end < cur_employee.interval.start:
            res.append((previous_employee_end, cur_employee.interval.start))
        if len(schedules[cur_employee.employee_index] > cur_employee.interval_index+1):
            heappush(max_heap, Employee(schedules[cur_employee.employee_index][cur_employee.interval_index+1], ))
        previous_employee_end = max(previous_employee_end, cur_employee.interval.end)
    return res

