class BuildingPoints:
    def __init__(self, point, height, is_start):
        self.point = point
        self.height = height
        self.is_start = is_start

    def __lt__(self, other):
        return self.point < other.point

    @staticmethod
    def print_obj(e):
        print(e.point, e.height, e.is_start)

import heapq

def getSkyline(buildings):
    # end_points = [(BuildingPoints(row[0], row[2], True), BuildingPoints(row[1], row[2], False)) for row in buildings]
    #
    # single_list = [((e1.point, e1.height, e1.is_start), (e2.point, e2.height, e2.is_start)) for e1, e2 in end_points]
    # print(single_list)
    # p = [s for t in single_list for s in t]

    building_points = []

    for b in buildings:
        building_points.append(BuildingPoints(b[0], b[2], True))
        building_points.append(BuildingPoints(b[1], b[2], False))

    building_points.sort(key=lambda x: x.point)

    res = []
    max_heap = [0]
    for p in building_points:
        if p.is_start:
            if not max_heap or p.height > -max_heap[0]:
                res.append((p.point, p.height))
            heapq.heappush(max_heap, (-p.height))
        else:
            max_heap.remove(-p.height)
            heapq.heapify(max_heap)
            if p.height > -max_heap[0]:
                res.append((p.point, -max_heap[0]))

    print(res)
    return res


class BuildingData:
    def __init__(self, p, height, is_start):
        self.point= p
        self.height = height
        self.is_start = is_start


def get_sky_line(buildings):

    start_points = [BuildingPoints(b[0], b[2], True) for b in buildings]
    end_points = [BuildingPoints(b[1], b[2], False) for b in buildings]

    build_points = start_points + end_points
    build_points.sort(key=lambda x: x.point)
    max_heap = [0]
    res = []
    for i in range(len(build_points)):
        if build_points[i].is_start:
            if not max_heap or build_points[i].height > -max_heap[0]:
                res.append((build_points[i].point, build_points[i].height))
            heapq.heappush(max_heap, -build_points[i].height)
        else:
            max_heap.remove(-build_points[i].height)
            heapq.heapify(max_heap)
            if build_points[i].height > -max_heap[0]:
                res.append((build_points[i].point, -max_heap[0]))
    return res


if __name__ == "__main__":
    print(get_sky_line([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))