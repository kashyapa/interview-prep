import heapq


def sort_almost_sorted_array(sequence, k):
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, (sequence[i]))

    result = []
    for i in range(k, len(sequence)):
        smallest = heapq.heappushpop(min_heap, sequence[i])
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
