def merge_intervals(intervals):

    start = intervals[0].start
    end = intervals[0].end
    res = []
    for i in range(1, len(intervals)):
        if intervals[i].start > end:
            res.append((start, end))
            start = intervals[i].start
            end = intervals[i].end
        else:
            end = max(end, intervals[i].end)
    res.append((start, end))
    return res
