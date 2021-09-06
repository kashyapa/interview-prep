from imports import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)

    min_heap = [meetings[0]]
    min_rooms = 0

    for meeting in meetings:

        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        
        heappush(min_heap, meeting)
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms

