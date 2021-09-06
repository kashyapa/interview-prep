def solve_n_queens(n):
    def solve(row):
        def is_valid_position(col_placements, row):
            c = col_placements[row]
            for i, val in enumerate(col_placements[:row]):
                if abs(val - c) in (0, row-i):
                    return False
            return True

        if row == n:
            res.append(col_placements.copy())
            return

        for col in range(n):
            col_placements[row] = col
            if is_valid_position(col_placements, row):
                solve(row+1)



    res = []
    col_placements = [-1 for _ in range(n)]
    solve(0)
    print(res)
    return


if __name__ == "__main__":
    solve_n_queens(4)