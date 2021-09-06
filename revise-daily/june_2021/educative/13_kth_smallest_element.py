from heapq import *


def kth_smallest_element(matrix, k):
    min_heap = []
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))

    count = 0
    while min_heap:
        min_top, arr, idx = heappop(min_heap)
        count += 1
        if count == k+1:
            return min_top

        if idx+1 > len(arr):
            heappush(min_heap, (arr[idx+1], arr, idx+1))
