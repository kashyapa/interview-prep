from collections import Counter
from heapq import *

def scheduling_tasks(tasks, k):

    task_counter = Counter(tasks)
    max_heap = []

    for k, v in task_counter.items():
        heappush(max_heap, (-v, k))
    interval_count = 0
    res = []
    while max_heap:
        n = k + 1
        wait_list = []
        while max_heap and n >= 0:
            freq, task = heappop(max_heap)
            res.append(task)
            if -freq+1 > 0:
                wait_list.append((freq+1, task))
            interval_count += 1
            n -= 1

        for freq, task in wait_list:
            heappush(max_heap, (freq, task))

        if max_heap:
            interval_count += n
    return interval_count
