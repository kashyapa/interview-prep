def minimum_path_triangle(triangle):
    minimum_path = [0]
    for row in triangle:
        minimum_path = [row[j] +
                        min(minimum_path[max(j-1, 0)], minimum_path[min(j, len(minimum_path) - 1)])
                        for j in range(len(row))]

    return min(minimum_path)


if __name__ == '__main__':
    triangle = [[2], [4,4], [8, 8, 6], [4, 2, 6, 2], [1, 5, 2, 3, 4]]

    print(minimum_path_triangle(triangle))
