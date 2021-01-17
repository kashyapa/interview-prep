# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
# intervals.


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


def merge(intervals):

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval.start:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals
