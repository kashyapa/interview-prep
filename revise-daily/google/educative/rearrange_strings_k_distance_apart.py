from collections import Counter
from heapq import *
from collections import deque

def rearrange_strings_k_distance_apart(str, k):
    char_count = Counter(str)
    max_heap = []
    for k, v in char_count.items():
        heappush(max_heap, (-v, k))
    queue = deque([])
    res = []
    while max_heap:
        freq, char = heappop(max_heap)
        res.append(char)

        if freq+1 < 0:
            queue.append((freq+1, char))

        if len(queue) == k:
            freq, task = queue.popleft()
            heappush(max_heap, (freq, task))

    return res
