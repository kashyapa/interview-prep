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


if __name__ == '__main__':
    print(solve_n_queens(4))
