import math


def sudoku_solver(matrix):
    def has_duplicates(block):
        block = filter(lambda x:x!=0, block)
        return list(block) != set(block)


    for i in range(len(matrix)):
        if has_duplicates(matrix[i]):
           return False

    for col in list(zip(*matrix)):
        if has_duplicates(col):
            return False
    n = len(matrix)
    block_size = int(math.sqrt(n))

    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            square = [matrix[x][y] for x in range(i, i+block_size) for y in range(j, j+block_size)]
            if has_duplicates(square):
                return False

    return True