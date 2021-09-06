class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x * self.x) + (self.y * self.y)

    def __lt__(self, other):
        return self.distance() < other.distance()

from imports import *


def closest_points_to_origin(points, k):

    max_heap = []

    for i in range(len(points)):
        if i <= k-1:
            heappush(max_heap, points[i])
        else:
            if max_heap and points[i].distance() < -max_heap[0].distance():
                heappop(max_heap)
                heappush(max_heap, points[i])
    return max_heap

from typing import List


def closest_points_to_origin(points: List[Point], k):
    max_heap = []

    for i in range(len(points)):
        if i <= k-1:
            heappush(max_heap, points[i])
        else:
            if points[i].distance() < max_heap[0].distance():
                heappop(max_heap)
                heappush(max_heap, points[i])

    return max_heap
