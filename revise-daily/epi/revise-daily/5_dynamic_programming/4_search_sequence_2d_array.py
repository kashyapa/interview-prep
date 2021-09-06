def is_pattern_contained_in_grid(grid, pattern):

    def pattern_search(i, j, k):
        if k == len(pattern)-1:
            return True

        if 0 > i >= len(grid) or 0 > j >= len(grid):# or (i, j) in visited_cells:
            return False

        if grid[i][j] != pattern[k]:
            return False
       #  visited_cells.add((i, j))
        return any(
                (pattern_search(i+1, j, k + 1), pattern_search(i, j + 1, k + 1), pattern_search(i-1, j, k + 1),
                 pattern_search(i, j-1, k + 1))
        )

    # visited_cells = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == pattern[0]:
                if pattern_search(i, j, 0) is True:
                    return True
    return False


if __name__ == '__main__':
    grid = [
        [1, 2, 3, 4, 5],
        [9, 43, 65, 76, 34],
        [423, 65645, 723, 22, 765],
        [978, 45, 98, 324, 345],
        ]
    print(is_pattern_contained_in_grid(grid, [65645, 423, 9, 43]))
    print(is_pattern_contained_in_grid(grid, [65645, 433, 9, 43]))

