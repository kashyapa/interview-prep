from collections import deque


def fill_surrounded_regions(board):
    """
        flatten the matrix to add border cells to a queue

        process the cells in the queue
        if it is white, Mark it as "T"
        add it's neighbours back to the queue

    """
    m, n = len(board), len(board[0])

    q = deque([(i, j) for k in range(m) for i, j in ((k, 0),  (k, n-1))] +
              [(i, j) for k in range(n) for i, j in ((0, k), (m-1, k))])

    while q:
        x, y = q.popleft()
        if 0 <= x < m and 0 <= y < n and board[x][y] == "W":
            board[x][y] = "T"

            q.extend([(x+1, y), (x-1, y), (x, y-1), (x, y+1)])
    board[:] = [["B" if c != "T" else "W" for c in row] for row in board]
    return board
