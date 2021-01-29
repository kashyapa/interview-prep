
from heapq import *


def kth_smallest_number(matrix, k):
    min_heap = []
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    count = 0

    while min_heap:
        number, i, arr = heappop(min_heap)
        count += 1

        if count == k:
            break

        if len(arr) > i+1:
            heappush(min_heap, (arr[i+1], i+1, arr))
    return number