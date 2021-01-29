# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms
# required to hold all the meetings.

from heapq import *


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

        # remove meetings that ended before the current meeting starts
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)

        # add meeting to heap , which now contains all the meetings that are currently in progress
        heappush(min_heap, meeting)

        min_rooms = max(min_rooms, len(min_heap))

    return min_rooms


def min_meeting_rooms2(meetings):
    start_times = [meeting.start for meeting in meetings]
    end_times = [meeting.end for meeting in meetings]
    i = 0
    start_times.sort()
    end_times.sort()
    concurrent_events = 0
    min_rooms = 0
    while i < len(start_times):
        if start_times[i] < end_times[j]:
            concurrent_events += 1
            i += 1
            min_rooms = max(concurrent_events, min_rooms)
        else:
            concurrent_events -= 1
            j += 1
    return min_rooms