from imports import *


def sudoku_solver(matrix):

    def block_valid(i, j, val, matrix):

        block_size = sqrt(len(matrix))

        block_I = i // int(sqrt(len(matrix)))
        block_J = j // int(sqrt(len(matrix[0])))

        for x in range(block_I * block_size, (block_I+1) * block_size):
            for y in range(block_J*block_size, (block_J+1)*block_size):
                if val == matrix[x][y]:
                    return False
        return True

    def is_placement_valid(i, j, val, matrix):
        if val in matrix[i]:
            return False
        if val in [matrix[k][j] for k in range(len(matrix))]:
            return False
        elif block_valid(i, j, val, matrix):
            return False

        return True

    def solve(i, j, matrix):

        if i == len(matrix):
            i = 0
            j += 1
            if j == len(matrix[0]):
                return True

        if matrix[i][j] != 0:
            return solve(i+1, j)


        for val in range(1, len(matrix)+1):
            if is_placement_valid(i, j, val):
                matrix[i][j] = val
                if solve(i+1, j):
                    return True
        matrix[i][j] = 0
        return False