import math


def find_line_through_most_points(points):
    result = 0
    for i, p1 in enumerate(points):
        slope = {}
        overlap_points = 1
        for j, p2 in enumerate(points[i+1:]):
            if p1 == p2:
                overlap_points += 1
            elif p1.x == p2.x:
                slope[(0, 1)] += 1
            else:
                x_diff, y_diff = p1.x - p2.x, p1.y - p2.y
                gcd = math.gcd(x_diff, y_diff)

                x_diff, y_diff = x_diff // gcd, y_diff // gcd

                if x_diff < 0:
                    x_diff, y_diff = -x_diff, -y_diff
                slope[(x_diff, y_diff)] += 1
        result = max(result, overlap_points+max(slope.values(), default=0))
    return result
