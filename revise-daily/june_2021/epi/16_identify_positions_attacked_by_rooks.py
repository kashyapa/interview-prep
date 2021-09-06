def positions_identified_by_rooks(matrix):
    row_has_zero = [False if matrix[0][i] != 0 else True for i in range(len(matrix[0]))]
    col_has_zero = [False if matrix[i][0] != 0 else True for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(len(matrix)):
                matrix[i][j] = 0

    if row_has_zero:
        matrix[0] = 0 * len(matrix[0])

    if col_has_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    return matrix