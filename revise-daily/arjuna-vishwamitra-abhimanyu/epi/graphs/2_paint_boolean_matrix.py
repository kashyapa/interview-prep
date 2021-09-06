import imports


def paint_boolean_matrix(x, y, matrix):

    color = matrix[x][y]
    queue = imports.deque([(x, y)])

    while queue:
        p, q = queue.popleft()
        matrix[p][q] = not matrix[p][q]

        queue.extend(
            [(i, j) for i, j in [(p+1, q), (p-1, q), (p, q+1), (p, q-1)] 
             if matrix[i][j] == color and i >= 0 and i < len(matrix) and j >= 0 and j < matrix[0]])
