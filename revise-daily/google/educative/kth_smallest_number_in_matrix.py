from heapq import *

def kth_smallest_number_in_matrix(matrix, k):

    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))

    count = 0
    while min_heap:
        n, arr, index = heappop(min_heap)
        count += 1
        if count == k:
            break
        if index+1 < len(arr):
            heappush(min_heap, (arr[index+1], arr, index+1))
    return n


def kth_smallest_element_in_sorted_matrix(matrix, k):
    m = len(matrix)-1
    n = len(matrix[0])-1

    def count_less_than(mid):
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        row, col = m, 0
        count = 0

        smaller, larger = matrix[0][0], matrix[m][n]

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = matrix[row][col]
                row -= 1
            else:
                smaller = matrix[row][col]
                count += row+1
                col += 1
        return count, smaller, larger

    low, high = matrix[0][0], matrix[m][n]

    while low <= high:

        mid = (low + high) // 2
        count, smaller, larger = count_less_than(mid)

        if count == k:
            return smaller
        if count < k:
            low = larger
        else:
            high = smaller

