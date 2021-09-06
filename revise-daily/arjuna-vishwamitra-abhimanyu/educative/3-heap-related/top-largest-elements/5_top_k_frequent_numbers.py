from imports import *


def top_k_frequent_numbers(nums):
    min_heap = []
    freq_counter = Counter(nums)
    
    for k, v in freq_counter.items():
        heappush(min_heap, (v, k))
        if len(min_heap) > k:
            heappop(min_heap)

    result = []
    while min_heap:
        result.append(heappop(min_heap)[1])
    return result
