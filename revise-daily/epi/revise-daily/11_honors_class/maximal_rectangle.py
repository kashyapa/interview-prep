import math


def compute_rectangles( heights):
    pillars = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while pillars and h <= heights[pillars[-1]]:
            height = heights[pillars.pop()]
            width = i if not pillars else i - pillars[-1] - 1
            max_area = max(max_area, height * width)
            #print(heights, max_area)
        pillars.append(i)
    return max_area


def maximalRectangle(matrix):
    table = [0 for _ in range(len(matrix[0]))]
    max_rectangle_area = 0
    for row in matrix:
        row = list(map(int, [x for x in row]))

        table = [x + y if y else 0 for x, y in zip(table, row)]
        print(table, row)
        max_rectangle_area = max(max_rectangle_area, compute_rectangles(table))
    return max_rectangle_area


if __name__ == "__main__":
    #print(maximalRectangle([["1", "1", "1"], ["1", "1", "0"], ["0", "1", "1"]]))
    print(maximalRectangle([["1","0","1","0","0"],
                            ["1","0","1","1","1"],
                            ["1","1","1","1","1"],
                            ["1","0","0","1","0"]]))
