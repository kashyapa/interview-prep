from imports import *


def frequency_sort(nums):

    max_heap = []
    freq_counter = Counter(nums)
    for k, v in freq_counter.items():
        heappush(max_heap, (-v, k))

    result = []
    while max_heap:
        count, item = heappop(max_heap)
        result.extend([item]*count)
    
    return result
