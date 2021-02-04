# Given a string and a number ‘K’, find if the string can be rearranged such that the same
# characters are at least ‘K’ distance apart from each other.

from collections import Counter
from collections import deque
from heapq import *


def reorganize_string(str, k):
    max_heap = []

    char_frequency_counter = Counter(str)

    for c, v in char_frequency_counter.items():
        heappush(max_heap, (-v, c))

    queue = deque()
    result_string = []

    while max_heap:
        frequency, char = heappop(max_heap)
        result_string.append(char)
        queue.append((frequency + 1, char))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(max_heap, (frequency, char))

    return ''.join(result_string) if len(result_string) == len(str) else ""


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))
