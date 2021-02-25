def compute_largest_rectangle(heights: list):
    pillar_indices = []
    max_rectangle_area = 0

    for i, h in enumerate(heights):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == '__main__':
    print(compute_largest_rectangle([]))
