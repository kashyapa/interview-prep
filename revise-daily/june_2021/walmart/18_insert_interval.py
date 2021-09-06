def insert_interval(intervals, new_interval):
    i = 0
    res = []
    while intervals[i].end < new_interval.start:
        res.append(intervals[i])
        i += 1
    while intervals[i].start < new_interval.end:
        new_interval.start = min(new_interval.start, intervals[i].start)
        new_interval.end = max(new_interval.end, intervals[i].end)
        i += 1
    res.append(new_interval)
    res.append(intervals[i:])
    return res
