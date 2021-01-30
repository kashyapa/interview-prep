from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, (-points[i].distance_from_origin()))

    for i in range(k, len(points)):

        if -points[i].distance_from_origin() > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -points[i].distance_from_origin())

    return max_heap
