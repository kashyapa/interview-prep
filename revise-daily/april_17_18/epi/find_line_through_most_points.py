from collections import namedtuple, defaultdict

Points = namedtuple('Points', ('x', 'y'))

import math


def find_line_through_most_points(points: Points):
    slope = defaultdict(int)
    max_points = 0
    overlap_points = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i:]):
            x_diff, y_diff = 0, 0
            if p1 == p2:
                overlap_points += 1

            elif p1.x == p2.x:
                slope[(0, 1)] += 1
                x_diff, y_diff = (0, 1)
            else:
                x_diff = p1.x - p2.x
                y_diff = p1.y - p2.y

                gcd = math.gcd(x_diff, y_diff)
                x_diff = x_diff // gcd
                y_diff = y_diff // gcd

                if x_diff < 0:
                    y_diff *= -1
                    x_diff *= -1

                slope[(x_diff, y_diff)] += 1
            max_points = max(max_points, slope[(x_diff, y_diff)])
    return max_points + overlap_points
