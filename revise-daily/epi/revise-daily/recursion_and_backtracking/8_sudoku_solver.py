import math
import itertools


def solve_sudoku(partial_assignment):

    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i+1, j)

        def valid_to_add(i, j, val):
            if any(val == partial_assignment[k][j] for k in range(len(partial_assignment))):
                return False

            if val in partial_assignment[i]:
                return False

            region_size = int(math.sqrt(len(partial_assignment)))

            I = i // region_size
            J = j // region_size

            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b]
                for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = empty_entry
        return False

    empty_entry = 0
    return solve_partial_sudoku(0, 0)


if __name__ == '__main__':
    print(solve_sudoku(
                 [[3, 6, 5, 1, 4],
                  [2, 1, 4, 3, 5],
                  [1, 2, 3, 4, 6],
                  [4, 5, 2, 6, 1],
                  [5, 4, 1, 2, 3]]
                 ))
