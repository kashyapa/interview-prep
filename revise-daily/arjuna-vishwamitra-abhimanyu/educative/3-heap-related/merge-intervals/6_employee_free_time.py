class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class EmployeeInterval:

    def __init__(self, interval, employee_schedule, interval_index):
        self.interval = interval
        self.employee_schedule = employee_schedule
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start - other.interval.start

from imports import *


def find_free_time(schedule):

    min_heap = []
    for i in range(len(schedule)):
        heappush(min_heap, (EmployeeInterval(schedule[i][0], schedule[i], 0)))

    previous_interval = min_heap[0].interval
    res = []
    while min_heap:

        current_employee = heappop(min_heap)
        if previous_interval.end < current_employee.interval.start:
            res.append(Interval(previous_interval.end, current_employee.interval.start))
            previous_interval = current_employee.interval

        else:
            if previous_interval.end < current_employee.end:
                previous_interval = current_employee.interval

        if len(current_employee.employee_schedule) > current_employee.interval_index+1:
            heappush(min_heap, EmployeeInterval(current_employee.employee_schedule[current_employee.interval_index+1],
                                                current_employee.employee_schedule,
                                                current_employee.interval_index+1
                                                ))
    return res
