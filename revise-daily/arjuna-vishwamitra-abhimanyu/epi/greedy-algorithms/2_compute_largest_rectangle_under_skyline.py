def max_rectangle_under_skyline(heights):

    pillars = []
    max_area = 0
    for i, h in enumerate(heights):
        while pillars and h <= heights[pillars[-1]]:
            height = heights[pillars.pop()]
            width = i - pillars[-1] -1 if pillars else i
            area = height * width
            max_area = max(area, max_area)
        pillars.append(i)
    return max_area
