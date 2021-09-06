def merge_intervals(intervals):
    start = intervals[0].start
    end = intervals[0].end
    res =[]
    for i in range(1, len(intervals)):
        if end < intervals[i].start:
            res.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

        else:
            end = max(end, intervals[i].end)
    return res
