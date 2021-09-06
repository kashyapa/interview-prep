def maximum_2d_subarray(matrix):
    def compute_max_rectangle(table):
        max_rectangle = 0
        pillars = []
        for i, h in enumerate(table):
            while pillars and h < pillars[-1]:
                height = table[pillars.pop()]
                width = i if not pillars else i - pillars[-1] -1
                max_rectangle = max(max_rectangle, height*width)
            pillars.append(i)
        return max_rectangle

    table = [0 for _ in range(len(matrix))]
    max_2d_sub_array = 0
    for row in matrix:
        table = [x+y if x else 0 for x, y in zip(row, table)]
        max_2d_sub_array = max(max_2d_sub_array, compute_max_rectangle(table))
    return max_2d_sub_array
