from collections import  Counter
from heapq import *


def maximum_distinct_elements(elements, k):
    min_heap = []
    freq_count = Counter(elements)
    distinct = 0
    for k,v in freq_count.items():
        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (v, k))

    while min_heap:
        freq, char = heappop(min_heap)
        if freq > 1:
            k -= (freq-1)
        if k > 0:
            distinct += 1

    if k > 0:
        distinct -= k
    return distinct
