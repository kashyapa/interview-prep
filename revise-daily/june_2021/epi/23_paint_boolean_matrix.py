import collections


def paint_boolean_matrix(x, y, matrix):
    color = matrix[x][y]
    matrix[x][y] = not matrix[x][y]
    queue = collections.deque([(x, y)])

    while queue:
        i, j = queue.popleft()

        for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == color:
                matrix[x][y] = not matrix[x][y]
                queue.append((x, y))
    return
