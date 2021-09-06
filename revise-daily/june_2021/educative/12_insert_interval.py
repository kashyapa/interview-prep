def insert_interval(new_interval, intervals):
    result = []
    i = 0
    while i < len(intervals):
        if new_interval.start > intervals[i][1]:
            result.append(intervals[i])
            i += 1
        else:
            break

    while i < len(intervals) and new_interval.end > intervals[i][0]:
        new_interval = (min(new_interval[0], intervals[i][0]) , max(new_interval[1], intervals[i][1]))
        i += 1
    result.append(new_interval)

    result.append(intervals[i:])
    return result
