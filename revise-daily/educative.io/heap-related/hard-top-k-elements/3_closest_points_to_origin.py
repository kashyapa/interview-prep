from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, points[i])

    for i in range(k, len(points)):

        if points[i].distance_from_origin() < max_heap[0].distance_from_origin():
            heappop(max_heap)
            heappush(max_heap, points[i])

    return max_heap


if __name__ == "__main__":
    find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)

