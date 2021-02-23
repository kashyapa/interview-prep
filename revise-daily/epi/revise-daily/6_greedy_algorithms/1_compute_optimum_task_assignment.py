from collections import deque
from collections import namedtuple

PairedTasks = namedtuple('PairedTasks', ('task_1', 'task_2'))


def compute_task_assignment(task_durations: list):
    durations = deque(sorted(task_durations))

    total_time = 0
    while durations:
        total_time = max(total_time, durations.popleft() + durations.pop())
    # return total_time

    task_durations.sort()
    return [
            PairedTasks(task_durations[i], task_durations[~i]) for i in range(len(task_durations)//2)
    ]


if __name__ == '__main__':
    print(compute_task_assignment([3, 8, 1, 4,]))