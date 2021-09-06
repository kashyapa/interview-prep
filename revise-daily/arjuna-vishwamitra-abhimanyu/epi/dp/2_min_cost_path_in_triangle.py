def minimum_cost_path_in_triangle(triangle):
    min_path = [triangle[0][0]]

    for row in triangle:
        min_path = [row[j] +
                    min(min_path[max(j-1, 0)],
                        min_path(min(j, len(min_path)-1))
                        ) for j in range(len(row))]
    return min(min_path)
