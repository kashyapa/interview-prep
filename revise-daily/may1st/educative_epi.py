# problem areas ---
# recursion, backtracking,
# intervals,
# two pointers
# heap,
# 2d matrix,
# dp,

def phone_mnemonics(phone_number):

    def rec(index, partial_res):

        if index == len(phone_number):
            res.append(''.join(partial_res.copy()))
            return
        else:

            str = MAPPING[int(phone_number[index])]

            for i in range(len(str)):
                partial_res.append(str[i])
                rec(index+1, partial_res)
                partial_res.pop()
        return

    MAPPING = ["", "","ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

    partial_res = []
    res = []
    rec(0, partial_res)
    return res


def n_queens(n):

    def solve_n_queens(row_index):

        def is_valid_placement(col_placement, row_index):
            col_value = col_placement[row_index]

            for i, c in enumerate(col_placement[:row_index]):
                if abs(c-col_value) in (0, row_index-i):
                    return False
            return True

        if row_index == n:
            res.append(col_placements.copy())
            return
        else:

            # solve for row == row_index
            for col in range(n):
                col_placements[row_index] = col
                if is_valid_placement(col_placements, row_index):
                    solve_n_queens(row_index+1)

    res = []
    col_placements = [-1] * n
    solve_n_queens(0)
    return res

import math


def sudoku_solver(board):
    def has_duplicate(arr):
        filtered_lst = list(filter(lambda x: x != 0, list(arr)))
        return len(filtered_lst) != len(set(filtered_lst))

    def is_value_valid(val, i, j):

        row = [board[i][y] for y in range(len(board[0]))]
        col = [board[x][j] for x in range(len(board))]

        if has_duplicate(row) or has_duplicate(col):
            return False

        block_index_i = int(i // math.sqrt(len(board)))
        block_index_j = int(j // math.sqrt(len(board[0])))

        I, J = int(math.sqrt(len(board))), int(math.sqrt(len(board[0])))

        block_elements = [board[x][y] for x in range(block_index_i * I, (block_index_i+1) * I) for y in range(block_index_j * J, (block_index_j+1) * J)]

        if has_duplicate(block_elements):
            return False

        return True

    def rec(i, j):

        if i == len(board):
            j += 1
            if j == len(board[0]):
                return True
            i = 0

        if board[i][j] != 0:
            return rec(i+1, j)

        for val in range(1, len(board)+1):
            board[i][j] = val
            if is_value_valid(val, i, j):
                if rec(i+1, j):
                    return True
        board[i][j] = 0
        return False

    return rec(0, 0)


def minimum_weight_path_triangle(triangle):
    min_path = [triangle[0]]
    for row in triangle[1:]:
        min_path = [row[j] + min(min_path[max(j-1, 0)], min_path[min(j, len(min_path)-1)]) for j in range(len(row))]

    return min(min_path)


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

from heapq import *


def next_interval(intervals):
    start_max_heap = []
    end_max_heap = []
    # start_points = [interval[0] for interval in intervals]
    # end_points = [interval[1] for interval in intervals]
    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i].start, i))
        heappush(end_max_heap, (-intervals[i].end, i))
    res = [0] * len(intervals)

    for _ in range(len(intervals)):
        max_end, idx = heappop(end_max_heap)
        res[idx] = -1

        if -start_max_heap[0][0] > max_end:
            top_start, start_idx = heappop(start_max_heap)
            while start_max_heap and -start_max_heap[0][0] >= -max_end:
                top_start, start_idx = heappop(start_max_heap)

            res[idx] = start_idx
            heappush(start_max_heap, (top_start, start_idx))

    return res


def find_next_interval(intervals):

    start_max_heap = []
    end_max_heap = []

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i].start, i))
        heappush(end_max_heap, (-intervals[i].end, i))

    res = [0] * len(intervals)
    for _ in range(len(intervals)):
        top_end, end_idx = heappop(end_max_heap)
        res[end_idx] = -1
        if start_max_heap and -start_max_heap[0][0] > top_end:
            top_start, idx = heappop(start_max_heap)
            while start_max_heap and -start_max_heap[0][0] >= -top_end:
                top_start, idx = heappop(start_max_heap)
            res[end_idx] = idx
            heappush(start_max_heap, (top_start, idx))


def maximize_capital(capitals, profits, number_of_projects, initial_capital):

    capital_min_heap = []
    profit_max_heap = []

    for i in range(number_of_projects):
        heappush(capital_min_heap, (-capitals[i], i))

    available_capital = initial_capital
    for _ in range(number_of_projects):

        while capital_min_heap and capital_min_heap[0][0] <= available_capital:
            capital, i = heappop(capital_min_heap)
            heappush(profit_max_heap, -profits[i])

        available_capital += (-heappop(profit_max_heap)[0])
    return available_capital


class SlidingWindowMedian:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        res = [0.0 for x in range(len(nums)-k+1)]
        for i, n in enumerate(nums):

            if not self.max_heap or n <= -self.max_heap[0]:
                heappush(self.max_heap, -n)
            else:
                heappush(self.min_heap, n)

            if len(self.max_heap) > len(self.min_heap) + 1:
                heappush(self.min_heap, -heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap) + 1:
                heappush(self.max_heap, -heappop(self.min_heap))

            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    res[i-k+1] = -self.max_heap[0]/2.0 + self.min_heap[0]/2.0
                else:
                    res[i-k+1] = -self.max_heap[0] / 1.0

                element_outside_window = nums[i-k+1]

                if element_outside_window <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_outside_window)
                else:
                    self.remove(self.min_heap, element_outside_window)
        return res

    def remove(self, heap, element):

        ind = heap.index(element)
        heap[ind] = heap[-1]

        if ind < len(heap):
            heapify(heap)


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class EmployeeSchedule:
    def __init__(self, interval, employee_index, schedule_index):
        self.interval = interval
        self.employee_index = employee_index
        self.schedule_index = schedule_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def employee_free_time(schedules):

    min_heap = []

    for i in range(len(schedules)):
        heappush(min_heap, (schedules[i][0], i, 0))

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

        employee_schedule = schedules[current_employee.employee_index]
        if len(employee_schedule) > current_employee.schedule_index+1:
            heappush(min_heap, EmployeeSchedule(
                employee_schedule[current_employee.schedule_index+1],
                current_employee.employee_index,
                current_employee.schedule_index+1
            ))
    return res

def max_cpu_load(jobs):

    min_heap = []
    cpu_load = 0
    max_cpu_load = 0
    for j in jobs:

        while not min_heap and j.start >= min_heap[0].end:
            cpu_load -= min_heap[0].load
            heappop(min_heap)

        heappush(min_heap, j)
        cpu_load += j.load
        max_cpu_load = max(max_cpu_load, cpu_load)

    return max_cpu_load


def merge(intervals_a, intervals_b):
    i, j = 0, 0
    start, end = 0, 1
    res = []
    a_overlaps_b, b_overlaps_a = False, False

    while i < len(intervals_a) and j < len(intervals_b):

        if intervals_a[i][0] < intervals_b[j][1] < intervals_a[i][1]:
            b_overlaps_a = True
        elif intervals_b[j][0] < intervals_a[i][1] < intervals_b[j][1]:
            a_overlaps_b = True

        if a_overlaps_b or b_overlaps_a:
            res.append((max(intervals_a[i][0], intervals_b[j][0]),
                       min(intervals_a[i][1], intervals_b[j][1])))

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

        return res


def merge_intervals(intervals):

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end
    res = []

    for i in range(1, len(intervals)):
        if intervals[i].start > end:
            res.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end
        else:
            end = max(end, intervals[i].end)

def insert_interval(intervals, new_interval):

    i = 0
    merged = []
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].start < new_interval.end:
        new_interval = Interval(min(intervals[i].start, new_interval.start),
                                max(intervals[i].end, new_interval.end))
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged

def pair_with_target_sum(nums, target):
    #
    # map = {}
    #
    # for i in range(len(nums)):
    #     if target - nums[i] in map:
    #         return i, map[target-nums[i]]
    #     map[nums[i]] = i

    nums.sort()
    res = []
    i, j = 0, len(nums)-1
    while i < j:
        if nums[i] + nums[j] == target:
            res.append((nums[i], nums[j]))
            i += 1
            j -= 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1


def search_triplets(nums):
    def pair_sum(start, target):
        res = []
        l, r = start+1, len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[start], nums[l], nums[r]])
                l += 1
                r -= 1
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

        return res
    result = []
    nums.sort()
    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        res = pair_sum(i, -nums[i])
        if res:
            result.extend(res)

    return result

import math.inf
def triplet_sum_close_to_target(arr, target):

    arr.sort()
    closest_target = math.inf

    for i in range(len(arr)-2):
        first = arr[i]
        l = i+1
        r = len(arr)-1
        while l < r:
            triplet_sum = first + arr[l] + arr[r]
            if triplet_sum - target == 0:
                return triplet_sum - target

            if abs(triplet_sum-target) < closest_target:
                closest_target = triplet_sum
            elif abs(triplet_sum) == abs(closest_target) and triplet_sum > closest_target:
                closest_target = triplet_sum
            if target - triplet_sum > 0:
                i += 1
            else:
                j -= 1
    return -1

def search_quadruplets(nums, target):
    def search_pairs(first, second, start, quadruplets):

        l, r = start, len(nums)-1
        while l < r:
            quad_sum = first+second + nums[l] + nums[r]
            if quad_sum == target:
                quadruplets.append()

    quadruplets = []

    for i in range(len(nums)-3):
        if i > 0 and nums[i] != nums[i-1]:
            first = nums[i]
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] != nums[j-1]:
                    second = nums[j]
                    search_pairs(first, second, j + 1, quadruplets)


from collections import Counter


def find_maximum_distinct_elements(nums, K):
    freq_count = Counter(nums)
    distinct = 0
    min_heap = []
    for k, v in freq_count.items():

        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (v, k))

    while K > 0 and min_heap:
        freq, number = heappop(min_heap)
        K -= (freq-1)
        if K >= 0:
            distinct += 1

    if K > 0:
        distinct -= K

    return distinct


from collections import deque
def rearrange_string(str):
    max_heap = []
    char_freq = Counter(str)

    for k, v in char_freq.items():
        heappush(max_heap, (-v, k))

    res = []
    prev_freq, prev_char = None, ''
    while max_heap:
        freq, char = heappop(max_heap)
        res.append(char)

        if prev_freq is not None and prev_freq + 1 < 0:
            heappush(max_heap, (prev_freq, prev_char))

        prev_char, prev_freq = char, freq+1

    return res


def reorganize_string(str, k):

    queue = deque()
    char_freq = Counter(str)
    max_heap = []

    for k, v in char_freq.items():
        heappush(max_heap, (-v, k))

    res = []

    while max_heap:
        freq, char = heappop(max_heap)
        res.append(char)

        queue.append((freq+1, char))

        if len(queue) == k:
            freq, char = queue.popleft()
            if -freq > 0:
                heappush(max_heap, (freq, char))
    return ''.join(res)



if __name__ == "__main__":
    print(phone_mnemonics("8583567273"))
    print(n_queens(8))
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))