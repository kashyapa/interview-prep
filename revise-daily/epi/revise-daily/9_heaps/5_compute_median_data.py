import heapq


def online_median_(sequence):
    min_heap = []
    max_heap = []
    result = []

    for x in sequence:
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])

    return result
