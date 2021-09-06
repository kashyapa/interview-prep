def find_closest_elements(nums, k, X):
    def binary_search(nums, X):

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == X:
                return m

            if nums[m] > X:
                r = m - 1
            else:
                l = m + 1
        return r

    index = binary_search(nums, X)
    i = index
    j = index + 1
    res = []
    for _ in range(k):
        if i >= 0 and j < len(nums):
            i_distance_from_X = abs(nums[i] - X)
            j_distance_from_X = abs(nums[j] - X)

            if i_distance_from_X < j_distance_from_X:
                res.append(nums[i])
                i -= 1
            else:
                j += 1
        elif i >= 0:
            res.append(nums[i])
            i -= 1
        elif j < len(nums):
            res.append(nums[j])
            j += 1
    return res

from collections import Counter
from heapq import *

def maximum_distinct_elems(nums, K):
    distinct = 0
    num_counter = Counter(nums)
    min_heap = []
    for key, v in num_counter.items():
        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (v, key))
    while min_heap:
        v, k = heappop(min_heap)
        K = K - (v-1)
        if K > 0:
            distinct += 1

        else:
            break
    if K > 0:
        distinct -= K
    return distinct


def rearrangement_of_letters(s):
    s_count = Counter(s)
    max_heap = []
    prev_char, prev_freq = None, None
    res = []
    for k, v in s_count.items():
        heappush(max_heap, (-v, k))

    while max_heap:
        v, k = heappop(max_heap)
        res.append(k)
        if prev_char is not None and prev_freq < 0:
              heappush(max_heap, (prev_freq+1, prev_char))
        prev_char, prev_freq = k, v
    return ''.join(res)

from collections import deque

def rearrange_characters_K_distance_apart(s, K):
    max_heap = []
    s_count = Counter(s)

    for k, v in s_count.items():
        heappush(max_heap, (-v, k))

    k_size_queue = deque([])
    res = []
    while max_heap:
        char, freq = heappop(max_heap)

        res.append(char)
        k_size_queue.append((char, freq))
        if len(k_size_queue) == K:
            prev_char, prev_freq = k_size_queue.popleft()
            if prev_freq < 0:
                heappush(max_heap, (prev_freq+1, prev_char))
    return ''.join(res)

# You are given a list of tasks that need to be run, in any order, on a server.
# Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during
# which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals,
# find the minimum number of CPU intervals that the server needs to finish all tasks.
#
# If at any time the server can’t execute any task then it must stay idle.


def scheduling_tasks(tasks, K):

    max_heap = []
    task_count = Counter(tasks)

    for k, v in task_count.items():
        heappush(max_heap, (-v, k))

    res = []
    intervals = 0
    while max_heap:
        n = k+1
        k_size_queue = deque([])
        while n > 0 and max_heap:
            intervals += 1
            c, t = heappop(max_heap)
            if -c < 1:
                k_size_queue.append((c+1, t))
            n -= 1

        for _ in range(len(k_size_queue)):
            c, t = k_size_queue.popleft()
            heappush(max_heap, (c, t))

        if max_heap:
            intervals += n


def scheduling_tasks2(tasks, K):
    max_heap = []
    task_count = Counter(tasks)

    for k, v in task_count.items():
        heappush(max_heap, (-v, k))

    intervals = 0

    while max_heap:
        n = k+1
        wait_list = []
        while n > 0 and max_heap:
            c, t = heappop(max_heap)
            if -c > 1:
                wait_list.append((c, t))
            n -= 1
            intervals += 1

        for c, t in wait_list:
            heappush(max_heap, (c+1, t))

        if max_heap:
            intervals += n

    return intervals
