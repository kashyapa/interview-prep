from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_to_origin() > other.distance_to_origin()

    @property
    def distance_to_origin(self):
        return self.x * self.x + self.y * self.y


def closest_points_to_origin(points, k):
    max_heap = []

    for i in range(len(points)):
        if len(max_heap) < k:
            heappush(max_heap, (points[i].distance_to_origin(), points[i]))
        else:
            if points[i].distance_to_origin() < max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (points[i].distance_to_origin(), points[i]))
    return max_heap
