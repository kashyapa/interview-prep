from imports import *


def scheduling_tasks(tasks, K):
    task_counter = Counter(tasks)
    task_heap = []
    intervals = 0
    
    for k, v in task_counter.items():
        heappush(task_heap, (-v, k))

    res = []
    while task_heap:
        n = K
        wait_list = []
        while n > 0 and task_heap:
            f, item = heappop(task_heap)
            res.append(item)
            if f + 1 < 0:
                wait_list.append((f+1, item))
            n -= 1
            intervals += 1

        for i in range(len(wait_list)):
            heappush(task_heap, (wait_list[i][0], wait_list[i][1]))

        if task_heap:
            intervals += n

    return intervals

def scheduling_tasks(tasks, K):
    
    tc = Counter(tasks)
    max_heap = []
    
    for k, v in tc.items():
        heappush(max_heap, (-v, k))
    intervals = 0
    res = []
    while tc:
        n = K
        wait_list = []
        while n > 0 and tc:
            f, item = heappop(max_heap)
            res.append(item)
            if f + 1 < 0:
                wait_list.append((f+1, item))
            intervals += 1
            n -= 1
        for i in range(len(wait_list)):
            heappush(max_heap, (wait_list[i][0], wait_list[i][1]))

        if tc:
            intervals += n
    return intervals
