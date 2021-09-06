import collections


def compute_enclosed_regions(matrix):

    m, n = len(matrix)-1, len(matrix[0])-1

    queue = collections.deque(
        [(i, j) for k in range(m) for (i, j) in [(k, 0), (k, n)]] +
        [(i, j) for k in range(n) for (i, j) in [(0, k), (m, k)]]
    )
    n, m = len(matrix), len(matrix[0])
    while queue:
        x, y = queue.popleft()

        if 0 <= x < n and 0 <= y < m and matrix[x][y] == "W":
            matrix[x][y] = "T"

            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                queue.extend((i, j))
    matrix[:] = [["B" if matrix[x][y] != "T" else "W" for x in range(len(matrix))] for y in range(len(matrix[0]))]
