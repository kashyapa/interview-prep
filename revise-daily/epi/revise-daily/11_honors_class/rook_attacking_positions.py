def rook_attacking_positions(matrix):
    row_has_zero = False

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            row_has_zero = True

    column_has_zero = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            column_has_zero = True

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(i, matrix)

    for j in range(len(matrix[0])):
        if matrix[0][i] == 0:
            nullify_column(i, matrix)

    if row_has_zero:
        nullify_row(0, matrix)

    if column_has_zero:
        nullify_column(0 , matrix)
