from imports import *


def maximum_distinct_elements(nums, K):

    freq_counter = Counter(nums)
    min_heap = []
    distinct = 0

    for k, v in freq_counter.items():
        if v == 1:
            distinct += 1
        else:
            heappush(min_heap, (v, k))

    while k > 0 and min_heap:
        freq, item = heappop(min_heap)
        K = K - freq + 1
        if K >= 0:
            distinct += 1

    if K > 0:
        distinct -= K
    return distinct
