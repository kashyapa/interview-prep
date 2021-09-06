from imports import *


def rearrange_characters_k_distance_apart(str, K):
    max_heap = []
    queue = deque()
    freq_counter = Counter(str)

    for k, v in freq_counter.items():
        heappush(max_heap, (-v, k))
    res = []

    while max_heap:

        f, item = heappop(max_heap)
        res.append(f)
        queue.append((f+1, item))
 
        if len(queue) == K:
            f, item = queue.popleft()
            if -f > 0:
                heappush(max_heap, (f, item))
    return "".join(res) if len(res) == len(res) else ""

