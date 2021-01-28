from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    min_heap = []
    result = []
    for i in range(len(schedule)):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    previous_interval = min_heap[0].interval

    while min_heap:
        current_employee = heappop(min_heap)

        if previous_interval.end < current_employee.interval.start:
            result.append(Interval(previous_interval.end, current_employee.interval.start))
            previous_interval = current_employee.interval
        else:
            if previous_interval.end < current_employee.end:
                previous_interval = current_employee.interval

        employee_schedule = schedule[current_employee.employeeIndex]
        if len(employee_schedule) > current_employee.intervalIndex + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[current_employee.intervalIndex + 1],
                                                current_employee.employeeIndex,
                                                current_employee.intervalIndex + 1))

    return result


def main():

    input = [
        [Interval(1, 3), Interval(5, 6)],
        [Interval(2, 3), Interval(6, 8)]
    ]

    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


if __name__ == "__main__":
    main()
