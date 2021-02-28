import math
import heapq


class Star:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, other: 'Star'):
        return self.distance < other.distance


def find_k_closest_starts(stars, k):
    max_heap = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)

    return [s[1] for s in heapq.nlargest(k, max_heap)]
