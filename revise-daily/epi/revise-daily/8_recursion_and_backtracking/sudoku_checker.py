import math


def is_valid(val, r, c, board):
    for i in range(len(board)):
        if board[r][i] == val:
            print(val, " in", "row=", r, "col=", c)
            return False
        if board[i][c] == val:
            print(val, " in", "row=", r, "col=", c)
            return False
    region_size = int(math.sqrt(len(board)))
    I = r // region_size
    J = c // region_size
    for i in range(I*region_size, (I+1) * region_size):
        for j in range(J*region_size, (J+1) * region_size):
            if board[i][j] == val:
                return False
    return True


def solveSudoku(board):
    # Write your code here.
    def solve(i, j, board):
        if i == len(board):
            i = 0
            j += 1
            if j == len(board):
                print(board)
                return True
        if board[i][j] != 0:
            return solve(i + 1, j, board)

        for val in range(1, len(board) + 1):
            if is_valid(val, i, j, board):
                board[i][j] = val
                if solve(i + 1, j, board):
                    return True
        board[i][j] = 0
        return False

    if solve(0, 0, board):
        return board
    return [[0]]


if __name__ == "__main__":
    board = [
        [0, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 0, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 0, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 0, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
    print(solveSudoku(board))

