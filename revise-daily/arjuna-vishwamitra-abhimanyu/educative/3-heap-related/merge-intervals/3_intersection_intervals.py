def intersection_of_intervals(intervals_a, intervals_b):
    i, j = 0, 0
    result = []

    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = intervals_b[j][0] < intervals_a[i][0] < intervals_b[j][1]
        b_overlaps_a = intervals_a[i][0] < intervals_b[j][0] < intervals_b[j][1]

        if a_overlaps_b or b_overlaps_a:
            result.append((max(intervals_a[i][0], intervals_b[j][0]),
                          min(intervals_a[i][1], intervals_b[j][1])))

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1

    return result
