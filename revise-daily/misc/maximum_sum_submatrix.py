import math


def maximumSumSubmatrix2(matrix, size):
    # Write your code here.
    sums = compute_running_sum(matrix)
    total = 0
    max_total = -math.inf
    for i in range(size - 1, len(matrix)):
        for j in range(size - 1, len(matrix[0])):
            total = sums[i][j]

            touches_top_border = i - size < 0
            if not touches_top_border:
                total -= sums[i - size][j]

            touches_left_border = j - size < 0
            if not touches_left_border:
                total -= sums[i][j - size]

            touches_top_or_left_border = touches_left_border or touches_top_border
            if not touches_top_or_left_border:
                total += sums[i - size][j - size]

            max_total = max(total, max_total)

    return max_total


def compute_running_sum(matrix):
    sums = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    for j in range(1, len(matrix[0])):
        sums[0][j] = sums[0][j - 1] + matrix[0][j]
    for i in range(1, len(matrix)):
        sums[i][0] = sums[i - 1][0] + matrix[i][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i][j]
    return sums


def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]

            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]

            maxSubMatrixSum = max(maxSubMatrixSum, total)

    return maxSubMatrixSum


def createSumMatrix(matrix):
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    # Fill the first row.
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    # Fill the first column.
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    # Fill the rest of the matrix.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]

    return sums


if __name__ == "__main__":
    matrix = [[5, 3, -1, 5],
              [-7, 3, 7, 4],
              [12, 8, 0, 0],
              [1, -8, -8, 2]]

    print(maximumSumSubmatrix2(matrix, 2))