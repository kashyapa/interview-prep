import math


def has_duplicate(block):
    block = filter(lambda x: x !=0, block)
    return len(block) != len(set(block))


def is_valid_sudoku(partial_assignment):
    n = len(partial_assignment)
    if any(has_duplicate([partial_assignment[i][j] for j in range(n)]) or
            has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    regions_size = int(math.sqrt(n))

    return all(not has_duplicate(
                    [partial_assignment[a][b]
                     for b in range(regions_size * I, regions_size * (I+1))
                     for a in range(regions_size * J, regions_size * (J+1))
                     ]) for I in range(regions_size) for J in range(regions_size))
