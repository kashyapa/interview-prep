def maximum_sum_submatrix(matrix, size):

    def create_sum_submatrix():
        sums = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(1, len(matrix[0])):
            sums[0][i] = sums[0][i-1] + matrix[0][i]

        for i in range(1, len(matrix)):
            sums[i][0] = sums[i-1][0] + matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                sums[i][j] = sums[i-1][j] + sum[i][j-1] - sums[i-1][j-1] + matrix[i][j]

        return sums

    submatrix_sums = create_sum_submatrix()

    for i in range(size-1, len(matrix)):
        for j in range(size-1, len(matrix[0])):

            total = submatrix_sums[i][j]

            touches_top_border = i - size < 0
            if not touches_top_border:
                total -= submatrix_sums[i-size][j]

            touches_left_border = j - size < 0
            if not touches_left_border:
                total -= submatrix_sums[i][j-size]

            touches_top_or_left_border = touches_left_border or touches_top_border

            if not touches_top_or_left_border:
                total += submatrix_sums[i-size][j-size]

            max_total = max(max_total, total)
    return max_total