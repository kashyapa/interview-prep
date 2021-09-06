class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def insert_interval(intervals, new_interval):
    merged = []

    i = 0
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    start = new_interval[0]
    end = new_interval[1]

    while i < len(intervals) and intervals[i][0] < end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
    merged.append(Interval(start, end))

    while i < len(intervals):
        merged.append(intervals[i])

    return merged


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x.start)
    start = intervals[0][0]
    end = intervals[0][1]
    merged = []
    
    for i in range(1, len(intervals)):
        if end < intervals[i][0]:
            merged.append(Interval(start, end))
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])
    
    merged.append(Interval(start, end))
    
from heapq import *

def next_interval(intervals):
    
    start_max_heap = []
    end_max_heap = []
    
    result = [-1] * len(intervals)
    
    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i][0], i))
        heappush(end_max_heap, (-intervals[i][1], i))

    res = []

    for _ in range(len(intervals)):
        top_end, end_index = heappop(end_max_heap)
        res[end_index] = -1
        if -start_max_heap[0] > -top_end:
            top_start, start_index = heappop(start_max_heap)
            while -start_max_heap[0] > -top_end:
                top_start, start_index = heappop(start_max_heap)
            res[end_index] = start_index
            heappush(start_max_heap, top_start, start_index)
    return res


def maximize_capital(capitals, profits, number_of_projects, available_capital):

    capital_min_heap = []
    profits_max_heap = []

    for i in range(len(capitals)):
        # if capitals[i] < available_capital:
        heappush(capital_min_heap, (capitals[i], i))

    for _ in range(number_of_projects):
        while capital_min_heap[0][0] < available_capital:
            capital, index = heappop(capital_min_heap)
            heappush(profits_max_heap, -profits[index])
            
        available_capital += (-heappop(profits_max_heap))
    return available_capital

# You are given a list of tasks that need to be run, in any order, on a server.
# Each task will take one CPU interval to execute but once a task has finished, it has a
# cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals,
# find the minimum number of CPU intervals that the server needs to finish all tasks.
#
# If at any time the server can’t execute any task then it must stay idle.

from collections import Counter
from collections import deque
from heapq import *

def scheduling_tasks(tasks, K):
    counter = Counter(tasks)
    task_heap = []

    intervals = 0
    for k, v in counter.items():
        heappush(task_heap, (-v, k))

    res = []
    while task_heap:
        n = K
        wait_list = []
        while n > 0 and task_heap:
            frequency, task = heappop(task_heap)
            res.append(task)
            intervals += 1
            if frequency+1 < 0:
                wait_list.append((frequency+1, task))
            n -= 1

        for i in range(len(wait_list)):
            heappush(task_heap, (wait_list[i][0], wait_list[i][1]))

        if task_heap:
            intervals += n
    return intervals

# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’
# distance apart from each other.

def rearrange_string_k_distance_apart(s, K):

    queue = deque([])
    max_heap = []
    char_count = Counter(s)

    res = []

    for i in range(len(s)):
        heappush(max_heap, (-char_count[s[i]], i))

    while max_heap:
        freq, index = heappop(max_heap)

        res.append(s[i])
        if freq + 1 < 0:
            queue.append((freq+1, i))

        if len(queue) >= K:
            freq, i = queue.popleft()
            heappush(max_heap, (freq, i))

def rearrange_characters(s):
    char_count = Counter(s)

    max_heap = []
    for i, c in enumerate(s):
        heappush(max_heap, (-char_count[c], c))

    res = []
    prev_char, prev_frequency = None, None

    while max_heap:

        freq, char = heappop(max_heap)
        res.append(char)

        if prev_char is not None:
            heappush(max_heap, (-prev_frequency, prev_char))

        if freq+1 < 0:
            prev_frequency = freq+1
            prev_char = char

    return ''.join(res)
