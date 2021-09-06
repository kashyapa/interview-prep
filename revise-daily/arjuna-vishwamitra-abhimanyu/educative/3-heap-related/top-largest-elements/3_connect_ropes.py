from imports import *


def connect_ropes(ropes):
    min_heap = []
    for i in range(len(ropes)):
        heappush(ropes[i])
    cost = 0

    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        cost += temp
        heappush(min_heap, temp)

    return heappop(min_heap)
