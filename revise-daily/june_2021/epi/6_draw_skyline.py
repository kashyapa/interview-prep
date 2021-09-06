from heapq import *
import collections

BuildingData = collections.namedtuple('BuildingData', ('point', 'height', 'is_start'))


def draw_skyline(buildings):
    start_points = [BuildingData(b[0], b[2], True) for b in buildings]
    end_points = [BuildingData(b[1], b[2], False) for b in buildings]

    building_points = [start_points] + [end_points]

    max_heap = [0]
    res = []
    for i, b in building_points:
        if b.is_start:
            if b.height > -max_heap[0]:
                res.append((b.height, b.point))
            heappush(-b.height)
        else:
            max_heap.remove(-b.height)
            heapify(max_heap)
            if b.height > -max_heap[0]:
                res.append((b.height, b.point))
    return res
