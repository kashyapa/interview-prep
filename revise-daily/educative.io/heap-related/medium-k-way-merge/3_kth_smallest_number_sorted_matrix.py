
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


def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) // 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


if __name__ == "__main__":
    main()