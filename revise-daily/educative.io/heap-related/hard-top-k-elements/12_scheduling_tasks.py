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
