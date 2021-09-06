from collections import namedtuple
import heapq

BuildingPoint = namedtuple('BuildingPoint', ('point', 'height', 'is_start'))


def compute_skyline(buildings):
    max_heap = [0]
    building_points = [BuildingPoint(b[0], b[2], True) for b in buildings] + [BuildingPoint(b[1], b[2], False) for b in buildings]
    res = []
    building_points.sort(key=lambda x: x.point)
    for point in building_points:
        if point.is_start:
            if not max_heap or point.height > -max_heap[0]:
                res.append(point.height)
            heapq.heappush(max_heap, -point.height)
        else:
            ending_point_height = point.height
            max_heap.remove(-ending_point_height)
            heapq.heapify(max_heap)
            if ending_point_height > -max_heap[0]:
                res.append(-max_heap[0])
    return res


if __name__ == "__main__":
    print(compute_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))