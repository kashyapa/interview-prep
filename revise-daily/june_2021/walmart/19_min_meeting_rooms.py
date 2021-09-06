class Meeting:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


from heapq import *

def minimum_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    min_heap = []
    min_rooms = 0

    for m in meetings:
        while min_heap and min_heap[0].end <= m.start:
            heappop(min_heap)

        heappush(min_heap, m)
        min_rooms = max(len(min_heap), min_rooms)

    return min_rooms
