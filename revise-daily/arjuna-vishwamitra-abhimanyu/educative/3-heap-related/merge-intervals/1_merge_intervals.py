class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


def merge_intervals(intervals):
    start, end = intervals[0][0], intervals[0][1]
    res = []
    for i in range(1, len(intervals)):
        if end > intervals[i][0]:
            end = max(end, intervals[i][1])
        else:
            res.append(Interval(start, end))
            start = intervals[i][0]
            end = intervals[i][1]

