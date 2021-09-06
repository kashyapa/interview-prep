def positions_attacked_by_rooks(matrix):
    row_has_zero = False
    col_has_zero = False

    for i in range(len(matrix)):
        row_has_zero = row_has_zero or (matrix[0][i] == 0)
    for i in range(len(matrix[0])):
        col_has_zero = col_has_zero or (matrix[i][0] == 0)

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            for j in range(len(matrix)):
                matrix[j][i] = 0
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    if row_has_zero:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    if col_has_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0
