def solve_n_queens(n):

    def solve(row_index):

        def is_valid_placement(col_placements, row_index):
            col = col_placements[row_index]

            for i in range(row_index):
                if abs(col_placements[i] - col) in (0, row_index-i):
                    return False
            return True

        if row_index == n:
            res.append(col_placements.copy())
        else:

            for col in range(n):
                col_placements[row_index] = col
                if is_valid_placement(col_placements, row_index):
                    solve(row_index+1)

        return


    res = []
    col_placements = [0] * n
    solve(0)
    return res

print(solve_n_queens(4))
