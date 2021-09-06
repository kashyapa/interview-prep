def generate_pascal_triangle(n):
    rows = [[1] * (i+1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
    return rows