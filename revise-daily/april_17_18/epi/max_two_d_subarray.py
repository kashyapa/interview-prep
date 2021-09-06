import math


def max_two_d_subarray(matrix):
    def largest_rectangle(heights):
        pillars = []
        max_area = -math.inf
        for i, h in enumerate(heights+[0]):
            while pillars and h < heights[-1]:
                idx = heights.pop()
                width = i if not pillars else i - 1 - heights[-1]
                height = heights[idx]
                area = height * width
                max_area = max(area, max_area)
            pillars.append(i)

        return max_area
    max_area = -math.inf

    table = [0 for _ in range(len(matrix))]
    for row in matrix:
        table = [x+y if y else 0 for x, y in zip(table, row)]
        max_area = max(max_area, largest_rectangle(table))
    return max_area
