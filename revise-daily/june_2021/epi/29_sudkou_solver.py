def sudkou_solver(matrix):

    def rec(i, j):

        if i == len(matrix):
            i = 0
            j += 1
        if j == len(matrix[0]):
            return True

        if matrix[i][j] != -1:
            return rec(i+1, j)

        def check_valid_placement(i, j, val):

            if val in matrix[i]:
                return False

            if val in list(zip(*matrix))[j]:
                return False
            import math
            size_of_block = math.sqrt(len(matrix))
            block_index_i = i // size_of_block
            block_index_j = j // size_of_block

            for x in range(block_index_i * size_of_block , (block_index_i+1)*size_of_block):
                for y in range(block_index_j* size_of_block, (block_index_j+1)*size_of_block):
                    if matrix[x][y] == val:
                        return False
            return True

        for val in range(1, len(matrix)+1):
            if check_valid_placement(i, j, val):
                matrix[i][j] = val
                if rec(i+1, j):
                    return True
        matrix[i][j] = -1
        return False

    return rec(0, 0)