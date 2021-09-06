from imports import *

def compute_enclosed_regions(matrix):

    m = len(matrix)-1
    n = len(matrix[0]) - 1
    queue = deque([(i, j) for k in range(m) for i, j in ((k, 0), (k, n - 1))] +
              [(i, j) for k in range(n) for i, j in ((0, k), (m - 1, k))])

    while queue:
        x, y = queue.popleft()
        if 0 <= x < m and 0 <= y < n and matrix[x][y] == "W":
            matrix[x][y] = "T"
        queue.extend([(x+1, y), (x-1, y), (x, y-1), (x, y+1)])

    matrix[:] = [["B" if c != "T" else "W" for c in row] for row in matrix]
    return matrix
