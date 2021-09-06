from imports import *


def kth_smallest_number(matrix, k):
    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))

    count = 0

    while min_heap:
        item, arr, idx = heappop(min_heap)
        count += 1
        if count == k:
            break

        if len(arr) > idx+1:
            heappush(min_heap, (arr[idx+1], arr, idx+1))

    return item


def find_kth_smallest_sorted_matrix(matrix, k):

    def count_less_than_mid(mid, start, end):
        n = len(matrix)
        smaller, larger = matrix[0][0], matrix[n-1][n-1]
        row, col = n-1, 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row
                col += 1
        return count

    start, end = 0, len(matrix)-1
    while start < end:
        mid = start + (end-start)//2

        count, smaller, larger = count_less_than_mid(mid, start, end)

        if count == k:
            return smaller
        elif count > k:
            end = larger
        else:
            start = smaller
    return start
