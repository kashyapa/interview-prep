
from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return self.x * self.x + self.y * self.y

    def __lt__(self, other):
        return self.distance() > other.distance()


def k_closest_points_to_origin(points, k):
    max_heap = []

    for i in range(len(points)):
        if i < k-1:
            heappush(max_heap, (points[i], i))
        else:
            if points[i].distance() < -max_heap[0][0].distance():
                heappop(max_heap)
                heappush(max_heap, (points[i], i))
    return max_heap
