def merging_intervals(intervals):
    start, end = intervals[0][0], intervals[0][1]
    result = []
    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            result.append((start, end))
            start, end = intervals[i][0], intervals[i][1]
        else:
            end = max(end, intervals[i][1])
    return result
