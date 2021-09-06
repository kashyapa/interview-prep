from heapq import *
def next_interval(intervals):

    max_start_heap = []
    max_end_heap = []

    for i in range(len(intervals)):
        heappush(max_start_heap, (-intervals[i][0], i))
        heappush(max_end_heap, (-intervals[i][1], i))

    res = [-1] * len(intervals)

    for i in range(len(intervals)):

        end_interval, idx = heappop(max_start_heap)
        if -max_start_heap[0][0] > -end_interval:
            top_start, start_idx = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] > -end_interval:
               top_start, start_idx = heappop(max_start_heap)
            res[idx] = start_idx
            heappush(max_start_heap, (top_start, start_idx))
    return res


def maximize_capital(number_of_projects, capitals, profits, initial_capital):

    capital_min_heap = []
    profits_max_heap = []

    for i in range(number_of_projects):
        heappush(capital_min_heap, (capitals[i], i))

    available_capital = initial_capital

    for _ in range(number_of_projects):
        while capital_min_heap[0][0] <= available_capital:
            c, i = heappop(capital_min_heap)
            heappush(profits_max_heap, -profits[i])

        available_capital += (-heappop(profits_max_heap)[0])
    return available_capital


def sliding_window_median(nums, k):

    def remove(heap, elem):
        idx = heap.index(elem)
        heap[idx] = heap[-1]

        if idx < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


    res = [0] * (len(nums)-k+1)

    max_heap = []
    min_heap = []

    for i in range(len(nums)):
        if not max_heap or nums[i] < max_heap[0]:
            heappush(max_heap, -nums[i])
        else:
            heappush(min_heap, nums[i])

        if len(max_heap) > len(min_heap)+1:
            heappush(-1 * heappop(min_heap))
        elif len(min_heap) > len(max_heap)+1:
            heappush(-1 * heappop(max_heap))

        if i > k-1:
            if len(max_heap) == len(min_heap):
                res[i-k+1] = (min_heap[0]//2 + max_heap[0]//2)
            else:
                res[i-k+1] = max_heap[0] // 2


            element_outside_window = nums[i-k+1]
            if element_outside_window <= -max_heap[0]:
                remove(max_heap, -element_outside_window)
            else:
                remove(min_heap, element_outside_window)


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
    res = []
    for i in range(len(schedules)):
        heappush(min_heap, EmployeeInterval(schedules[i][0], i, 0))

    prev_interval = min_heap[0].interval
    while min_heap:

        while min_heap and prev_interval.end > min_heap[0].interval.start:
            e = heappop(min_heap)
            if e.interval.end > prev_interval.end:
                prev_interval = e.interval
            if e.interval_index+1 > len(schedules[e.employee_index]):
                heappush(min_heap, EmployeeInterval(schedules[e.employee_index][e.interval_index+1], e.employee_index, e.interval_index+1))
        res.append((prev_interval.end, min_heap[0].interval.start))
        prev_interval = min_heap[0].interval


def employee_interval2(schedules):
    min_heap = []

    for i in range(len(schedules)):
        heappush(min_heap, EmployeeInterval(schedules[i][0], i, 0))

    res = []
    prev = min_heap[0].interval
    while min_heap:
        cur = heappop(min_heap)
        if prev.end < cur.interval.start:
            res.append((prev.end, cur.interval.start))
            prev = cur.interval
        else:
            if prev.end < cur.interval.end:
                prev = cur.interval

        if len(schedules[cur.employee_index]) > cur.interval_index + 1:
            heappush(min_heap, EmployeeInterval(schedules[cur.employee_index][cur.interval_index+1],
                                                cur.employee_index, cur.interval_index+1))
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
    cpu_load = 0
    jobs.sort(key=lambda x: x.start)
    max_cpu_load = 0

    for j in jobs:

        while min_heap and j.start > min_heap[0].end:
            expired_job = heappop(min_heap)
            cpu_load -= expired_job.load

        cpu_load += j.load
        max_cpu_load = max(max_cpu_load, cpu_load)
        heappush(min_heap, j)

    return max_cpu_load

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end  = end

    def __lt__(self, other):
        return self.end < other.end


def minimum_meetings(meetings):
    min_heap = []
    meetings.sort(key=lambda x:x.start)
    min_rooms = 0

    for m in meetings:

        while min_heap and m.start > meetings[0].end:
            heappop(min_heap)
        heappush(min_heap, m)
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms


def merge_intervals(l1, l2):
    i, j = 0, 0
    res = []

    while i < len(l1) and j < len(l2):
        i_intersects_j = l2[j][0] < l1[i][0] <= l2[j][1]
        j_intersects_i = l1[i][0] < l2[j][0] <= l1[i][1]

        if i_intersects_j or j_intersects_i:
            res.append([max(l1[i][0], l2[j][0]),
                        min(l1[i][1], l2[j][1])])
        if l1[i][1] < l2[j][1]:
            i += 1
        else:
            j += 1
    return res


def insert_interval(intervals, new_interval):

    i = 0
    res = []
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    while intervals[i][0] < new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    res.append(new_interval)

    res.append(intervals[i:])
    return res


def merge_intervals(intervals):
    start = intervals[0][0]
    end = intervals[0][1]
    res = []
    i = 1
    while i < len(intervals):
        if intervals[i][0] > end:
            res.append((start, end))
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
        i += 1
    res.append((start, end))
    return res


def merge_sort(nums):

    if len(nums) == 1:
        return nums

    def merge(l1, l2):
        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        res.append(l1[i:])
        res.append(l2[j:])
        return res

    start, end = 0, len(nums)-1
    mid = start + (end-start) //2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge_k_sorted_arrays(lists):

    if len(lists):
        return lists

    def merge(l1, l2):
        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        res.append(l1[i:])
        res.append(l2[j:])
        return res

    start, end = 0, len(lists)-1
    intermediate_list = []
    while start < end:
        merged_list = merge(lists[start], lists[end])
        intermediate_list.append(merged_list)
        start += 1
        end -= 1
    if start == end:
        intermediate_list.append(lists[start])

    return merge_k_sorted_arrays(intermediate_list)


def k_pairs_with_largest_sum(nums1, nums2, k):
    min_heap = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if k < len(min_heap):
                heappush(min_heap, (nums1[i]+nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappush(min_heap, (nums1[i]+nums2[j], i, j))
                    heappop(min_heap)
    result = []
    for num, i, j in min_heap:
        result.append([nums1[i], nums2[j]])


import math
def smallest_range(nums):
    min_heap = []
    max_val = -math.inf
    for i in range(len(nums)):
        heappush(min_heap,  (nums[i][0], nums[i], 0))
        max_val = max(max_val, nums[i][0])
    left, right = -1, -1
    while min_heap:
        p, l, idx = heappop(min_heap)
        if abs(p-max_val) < abs(left-right):
            left = p
            right = max_val
        if len(l) > idx+1:
            heappush(min_heap, (l[idx+1], l, idx+1))
            max_val = max(max_val, l[idx+1])

    return [left, right]


def kth_smallest_number(matrix, k):
    min_heap = []

    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))

    count = 0
    while min_heap:
        n, l, idx = heappop(min_heap)
        count += 1
        if count == k:
            return n
        if len(l) > idx+1:
            heappush(min_heap, (l[idx+1], l, idx+1))

def find_kth_smallest_number(matrix, k):

    def count_less_than_equal(mid):
        count = 0
        smaller = matrix[0][0]
        larger = matrix[m][n]

        row, col = m, 0

        while smaller <= larger:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row
                col += 1
        return smaller, larger, count

    m = len(matrix)-1
    n = len(matrix[0])-1
    left, right = matrix[0][0], matrix[m][n]

    while left < right:
        mid = (left+right) // 2
        smaller, larger, count = count_less_than_equal(mid)
        if count == k:
            return smaller

        if count < k:
            left = larger+1
        else:
            right = smaller-1
    return left


from collections import defaultdict


def scheduling_tasks(tasks, k):
    task_counter = defaultdict(int)
    max_heap = []
    for i in range(len(tasks)):
        task_counter[tasks[i]] += 1

    for k in task_counter:
        heappush(max_heap, (-task_counter[k], k))

    res = []
    intervals = 0
    while max_heap:
        n = k
        wait_list = []
        while n > 0 and max_heap:
            count, ch = heappop(max_heap)
            n -= 1
            intervals += 1
            res.append(ch)

            if count < -1:
                wait_list.append((ch, count+1))

        for i in range(len(wait_list)):
            heappush(max_heap, (wait_list[i][1], wait_list[i][0]))

        if max_heap:
            intervals += n
    return intervals


from collections import Counter
from collections import deque


def rearrange_strings_k_distance_apart(str, k):

    char_counter = Counter(str)
    max_heap = []
    for c in char_counter:
        heappush(max_heap, (-char_counter[c], c))

    queue = deque()
    res = []
    while max_heap:
        count, ch = heappop(max_heap)
        res.append(ch)

        if len(queue) == k:
            count, ch = queue.popleft()
            if -count > 0:
                heappush(max_heap, (count, ch))

        queue.append((count+1, ch))
    return "".join(res) if res == len(str) else ""


def rearrange_strings(str):

    max_heap = []
    prev_freq, prev_char = -1, None

    char_counter = Counter(str)

    for k, v in char_counter.items():
        heappush(max_heap, (-v, k))
    res = []

    while max_heap:
        freq, ch = heappop(max_heap)

        res.append(ch)
        if prev_char and -(prev_freq+1) > 0:
            heappush(max_heap, (prev_freq+1, prev_char))
        prev_freq = -(freq+1)
        prev_char = ch
    return ''.join(res) is len(res) == len(str) else ""


def sum_of_elements(nums, k1, k2):

    max_heap = []
    for i in range(len(nums)):
        if len(max_heap) == k2:
            if -max_heap[0] > nums[i]:
                heappush(max_heap, -nums[i])
                heappop(max_heap)
            else:
                heappush(max_heap, -nums[i])
    count = k2 - k1 - 1
    sum_of_items = 0
    while count > 0:
        sum_of_items += (-heappop(max_heap))
    return sum_of_items

def maximum_distinct_elements(nums, k):
    freq_counter = Counter(nums)

    distinct = 0
    min_heap = []
    for k, v in freq_counter.items():
        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (-v, k))

    while k > 0 and min_heap:
        f,v = heappop(min_heap)
        k = k - (f-1)
        if k > 0:
            distinct += 1
    if k > 0:
        distinct -= k

    return distinct

def find_closest_elements(nums, target, k):

    def find_idx(nums, key):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == key:
                return mid
            elif nums[mid] > key:
                r = mid-1
            else:
                l = mid+1

    res = []
    idx = find_idx(nums, target)
    i, j = idx, idx+1
    for _ in range(k):
        if i >= 0 and j < len(nums):
            lesser, greater = nums[i], nums[j]
            diff1 = abs(lesser-target)
            diff2 = abs(greater-target)

            if diff1 < diff2:
                res.append(lesser)
                i -= 1
            else:
                res.append(greater)
                j += 1

        elif i >= 0:
            res.append(nums[i])
            i -= 1
        elif j <= len(nums):
            res.append(nums[j])
            j += 1
    return res

def top_k_frequent_numbers(nums, k):
    min_heap = []
    frequency_counter = Counter(nums)

    for k, v in frequency_counter.items():
        heappush(min_heap, (-v, k))
        if len(min_heap) > k:
            heappop(min_heap)

    res = []
    while min_heap:
        res.append(min_heap.pop()[1])

    return res

def connect_ropes(ropes):
    min_heap = []
    for i in range(len(ropes)):
        heappush(min_heap, (ropes[i], i))
    total_cost = 0

    while len(min_heap) > 1:
        t = heappop(min_heap) + heappop(min_heap)
        total_cost += t
        heappush(min_heap, t)
    return heappop(min_heap)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_to_origin() < other.distance_to_origin()

    def distance_to_origin(self):
        return self.x * self.x + self.y * self.y


def closest_points_to_origin(points):
    max_heap = []
    for i in range(len(points)):
        if len(max_heap) < k:
            heappush(max_heap, (-points[i].distance_to_origin(), i))
        else:
            if points[i].distance_to_origin() < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-points[i].dirsince_to_oriing()))

    return max_heap