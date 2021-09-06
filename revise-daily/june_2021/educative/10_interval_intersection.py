def intersection_of_intervals(intervals_a, intervals_b):
    i, j = 0, 0

    result = []

    while i < len(intervals_a) and j < len(intervals_b):
        i1, i2 = intervals_a[i], intervals_b[j]

        i1_intersects_i2 = intervals_b[j][1] > intervals_a[i][0] > intervals_b[j][0]
        i2_intersects_i1 = intervals_a[i][1] > intervals_b[j][0] > intervals_a[i][0]

        if i1_intersects_i2 or i2_intersects_i1:
            result.append((max(i1[0], i2[0]), min(i1[1], i2[1])))

        if i1[1] < i2[1]:
            i += 1
        else:
            j += 1
    return result
