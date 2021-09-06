import random, math
from heapq import *
from collections import Counter
from collections import deque


def find_k_largest_numbers(nums, k):

    def partition(l, r, pivot_index):

        pivot = nums[pivot_index]
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]

        new_pivot_idx = l

        for i in range(l, r):
            if nums[i] > pivot:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx] , nums[i]
                new_pivot_idx += 1

        nums[new_pivot_idx], nums[r] = nums[r], nums[new_pivot_idx]
        return new_pivot_idx

    low, high = 0, len(nums)-1
    while low < high:
        pivot_index = random.randint(low, high)
        pivot_index = partition(low, high, pivot_index)

        if pivot_index == k-1:
            return nums[:pivot_index+1]
        elif pivot_index > k-1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    return []


def find_k_largest_elements(nums, k):
    min_heap = []

    for i in range(k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappush(min_heap, nums[i])
            heappop(min_heap)
    return min_heap


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, points[i])

    for i in range(k, len(points)):

        if points[i].distance_from_origin() < max_heap[0].distance_from_origin():
            heappop(max_heap)
            heappush(max_heap, points[i])

    return max_heap

from typing import *

# [3, 3, 4, 4]
# 3+3 = 6
# 4+4 = 8
# 
def minimum_cost(ropes: List):
    min_heap = []
    for i in range(len(ropes)):
        heappush(min_heap, ropes[i])
        
    result, temp = 0, 0
    while min_heap:
        temp = heappop(min_heap) + heappop(min_heap)
        heappush(min_heap, temp)
        result += temp
    return result

import math

def find_closest_elements(arr, K, X):

    def binary_search(arr, X):

        low, high = 0, len(arr)-1

        while low <= high:
            mid = low + (high-low)//2

            if arr[mid] == X:
                return mid

            if arr[mid] > K:
                high = mid-1
            else:
                low = mid+1
        return low

    res = []
    idx = binary_search(arr, X)
    l, r = idx, idx-1
    for i in range(K):
        if l >= 0 and r < len(arr):
            if math.abs(arr[l]-X) < math.abs(arr[r]-X):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        elif r == len(arr):
            res.append(arr[l])
            l -= 1
        else:
            res.append(arr[r])
            r += 1


def find_maximum_distinct_elements(nums, K):
    counter = Counter(nums)
    min_heap = []
    distinct = 0
    for k, v in counter.items():
        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (v, k))

    while min_heap:
        v, k = heappop(min_heap)
        K -= (v-1)

        if K >= 0:
            distinct += 1
        else:
            break
    if K > 0:
        distinct -= K

    return distinct


def sum_of_elements(nums, k1, k2):
    max_heap = []

    for i in range(k2):
        heappush(max_heap, -nums[i])

    for i in range(k2, len(nums)):
        if nums[i] < -max_heap[0]:
            heappush(max_heap, -nums[i])
            heappop(max_heap)
    sum = 0
    for i in range(k2-k1+1):
        sum += (-heappop(max_heap)[0])

    return sum


def rearrange_strings_two_characters_apart(s):
    char_counter = Counter(s)

    max_heap = []

    for k, v in char_counter.items():
        heappush(max_heap, (-v, k))

    res = []
    prev_char, prev_freq = None, None
    while max_heap:
        v, k = heappop(max_heap)
        res.append(k)

        if prev_char and prev_freq <= -1:
            heappush(max_heap, (prev_freq, prev_char))

        prev_char, prev_freq = k, v+1
    return "".join(res) if len(res) == len(s) else ""


def rearrange_string_k_distance_apart(s, k):

    max_heap = []
    res = []
    char_counter = Counter(s)
    queue = deque()

    for k, v in char_counter.items():
        heappush(max_heap, (-v, k))

    while max_heap:

        v, k = heappop(max_heap)

        res.append(k)

        queue.append((k, v+1))

        if len(queue) == k:
            k, v = queue.popleft()
            if v <= -1:
                heappush(max_heap, (v, k))

    return "".join(res) if len(res) == len(s) else ""


def minimum_intervals_for_K_tasks(tasks, K):

    task_counter = Counter(tasks)
    max_heap = []
    for k, v in task_counter.items():
        heappush(max_heap, (-v, k))
    interval_count = 0
    res = []
    while max_heap:
        n = K
        wait_list = []
        while n > 0 and max_heap:
            v, k = heappop(max_heap)
            res.append(k)
            wait_list.append((v+1, k))
            n -= 1
            interval_count += 1

        for k, v in wait_list:
            if v <= -1:
                heappush(max_heap, (v+1, k))

        if max_heap:
            interval_count += n

    return interval_count

#########################################
#             K-way -merge            #
#########################################


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def merge_k_sorted_lists(lists):
    l, r = 0, len(lists)-1

    def merge_lists(l, r):
        head, tail = None, ListNode(-1) 
        l1, l2 = lists[l], lists[r]
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            if head is None:
                head = tail.next
            tail = tail.next
        tail.next = l1 or l2
        return head

    if len(lists) == 1:
        return lists[0]

    res = []
    while l < r:
        merged_res = merge_lists(l, r)
        res.append(merged_res)
        l += 1
        r -= 1
    if l == r:
        res.append(lists[l])
    return merge_k_sorted_lists(res)


def kth_smallest_element_in_matrix(matrix, k):

    min_heap = []
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], i, 0))

    elem = None

    count = 0
    while min_heap:
        elem, list_idx, elem_idx = heappop(min_heap)
        count += 1
        if count == k:
            break
        if elem_idx +1 < len(list_idx):
            heappush(min_heap, (matrix[list_idx][elem_idx+1], list_idx, elem_idx))

    return elem

def kth_smallest_element_in_sorted_matrix_binary_search(matrix, K):

    def count_elements_less_than_mid(matrix, mid):

        rows = len(matrix) -1
        cols = 0
        count = 0
        smaller, larger = matrix[0][0], matrix[len(matrix)-1][len(matrix[0]-1)]

        while rows >= 0 and cols < len(matrix[0]-1):
            if matrix[rows][cols] > mid:
                larger = min(matrix[rows][cols], larger)
                rows -= 1
            else:
                smaller = max(smaller, matrix[rows][cols])
                cols += 1
                count += rows
        return smaller, larger, count

    m = len(matrix)-1
    n = len(matrix[0])-1

    low, high = matrix[0][0], matrix[len(matrix)-1][len(matrix[0]-1)]

    while low < high:
        mid = low + (high-low) // 2

        smaller, larger, count = count_elements_less_than_mid(matrix, mid, low, high)
        if count > K:
            high = smaller
        else:
            low = larger

    return low


def smallest_number_range(matrix):
    largest_seen = -math.inf
    min_heap = []
    smallest, largest = None, None
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))
        largest_seen = max(largest_seen, matrix[i][0])
    smallest_range = math.inf
    while min_heap:
        next_elem, l, idx = heappop(min_heap)
        if abs(next_elem-largest_seen) < smallest_range:
            smallest_range = abs(next_elem-largest_seen)
            smallest = next_elem
            largest = largest_seen

        if idx+1 < len(l):
            heappush(min_heap, (l[idx+1], l, idx+1))
            largest_seen = max(largest_seen, l[idx+1])
    return smallest, largest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start - other.start

class EmployeeInterval:

    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index


def employee_free_time(schedule):
    min_heap = []
    for i in range(len(schedule)):
        heappush(min_heap, (schedule[i][0], schedule[i], 0))

    prev_interval = min_heap[0]
    res = []
    while min_heap:
        interval, employee, index = heappop(min_heap)
        if interval.start > prev_interval.end:
            res.append(prev_interval.end, interval.start)
            prev_interval = interval
        else:
            prev_interval.end = max(prev_interval.end, interval.end)

        if index+1 < len(employee):
            heappush(min_heap, EmployeeInterval(employee[index+1], employee, index+1))

    return min_heap


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
    max_load = 0
    jobs.sort()
    for j in jobs:
        while j.start >= min_heap[0].end:
            cpu_load -= heappop(min_heap).load

        heappush(min_heap, j)
        cpu_load += j.load
        max_load = max(max_load, cpu_load)
    return max_load


def maximal_capital(capitals, profits, number_of_projects, initial_capital):
    capital_min_heap = []
    profit_max_heap = []

    for i in range(len(capitals)):
        heappush(capital_min_heap, (capitals[i], i))

    available_capital = initial_capital

    for _ in range(number_of_projects):
        while capital_min_heap:
            if capital_min_heap[0][0] <= available_capital:
                c, i = heappop(capital_min_heap)
                heappush(profit_max_heap, -profits[i])
        available_capital += (heappop(profit_max_heap) * -1)
    return available_capital


def next_interval(intervals):

    start_max_heap = []
    end_max_heap = []

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i][0], i))
        heappush(end_max_heap, (-intervals[i][1], i))

    res = [0 for _ in range(len(intervals))]
    for _ in range(len(intervals)):
        top_end, idx = heappop(end_max_heap)
        res[idx] = -1
        if top_end > -start_max_heap[0][0]:
            top_start, start_idx = heappop(start_max_heap)
            while start_max_heap and -top_end > -start_max_heap[0][0]:
                top_start, start_idx = heappop(start_max_heap)
            res[idx] = start_idx
            heappush(start_max_heap, (top_start, start_idx))

    return res

#

from collections import deque

def subsets(nums):

    subsets = deque([])
    subsets.append([])

    for i in range(len(nums)):

        n = len(subsets)
        for j in range(n):
            p = subsets[j]
            new_subset = list(p)
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets


def subsets_with_duplicates(nums):
    subsets = []
    subsets.append([])
    start_index, end_index = 0, 0

    for i in range(len(nums)):
        start_index = 0
        if i >= 1 and nums[i] == nums[i-1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1

        for j in range(start_index, end_index+1):
            new_subset = list(subsets[j])
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets


def permutations(nums):

    perms = deque([])
    perms.append([])

    res = []
    for i, num in enumerate(nums):
        for j in range(len(perms)):
            p = perms.popleft()

            for j in range(len(p)+1):
                new_perm = list(p)
                new_perm.insert(j, nums[i])
                perms.append(new_perm)
                if len(new_perm) == len(nums):
                    res.append(new_perm)
    return res






def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_k_sorted_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


if __name__ == "__main__":
    main()
