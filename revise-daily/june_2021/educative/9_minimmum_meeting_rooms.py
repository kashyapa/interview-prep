from heapq import *
import math


def minimum_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    min_heap = []
    min_meeting_rooms = math.inf
    for m in meetings:
        while min_heap and min_heap[0].end < m.start:
            heappop(min_heap)
        heappush(min_heap, m)
        min_meeting_rooms = max(len(min_heap), min_meeting_rooms)

    return min_meeting_rooms
