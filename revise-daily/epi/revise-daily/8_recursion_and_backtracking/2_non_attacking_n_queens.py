def solve_n_queens(n):

    def solve_n_queens_rec(row_index):

        if row_index == n:
            result.append(col_placements.copy())
            return

        for col in range(n):
            col_placements[row_index] = col
            if is_valid_n_queens_placement(col_placements, row_index):
                solve_n_queens_rec(row_index + 1)

        return

    def is_valid_n_queens_placement(col_placement, row_index):
        col = col_placement[row_index]

        for i, c in enumerate(col_placement[:row_index]):
            if abs(col - c) in (0, row_index - i):
                return False

        return True

    col_placements = [0] * n
    result = []
    solve_n_queens_rec(0)
    return result


def solve_n_queens_2(n):
    def is_valid_queen_placement(col, row_index):
        last_added_col = col[row_index]
        for i, c in enumerate(col[:row_index]):
            if abs(c-last_added_col) in (0, row_index-i):
                return False
        return True

    def solve_rec(row_index):

        if row_index == n:
            res.append(col.copy())
            return
        for i in range(n):
            col[row_index] = i
            if is_valid_queen_placement(col, row_index):
                solve_rec(row_index + 1)
        return False
    col = [0] * n
    res = []
    solve_rec(0)
    return res



if __name__ == '__main__':
    print(solve_n_queens(4))
    print(solve_n_queens_2(4))



