from imports import *


def rearrange_string(str):
    max_heap = []
    freq_counter = Counter(str)
    for k, v in freq_counter.items():
        heappush(max_heap, (-v, k))
    prev_char, prev_freq = None, -1

    res = []
    while max_heap:
        f, item = heappop(max_heap)
        res.append(item)

        if prev_char and -prev_freq > 0:
            heappush(max_heap, (prev_freq, prev_char))

        prev_char, prev_freq = item, f+1
    return "".join(res) if len(res) == len(str) else ""
