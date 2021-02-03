def merge(intervals_a, intervals_b):
    i, j = 0, 0
    start, end = 0, 1
    result = []

    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = intervals_b[j][start] < intervals_a[i][start] <= intervals_b[j][end]

        b_overlaps_a = intervals_a[i][start] < intervals_b[j][start] <= intervals_a[i][end]

        if a_overlaps_b or b_overlaps_a:
            result.append([max(intervals_a[i][start], intervals_b[j][start]),
                          min(intervals_b[j][end], intervals_a[i][end])])
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


if __name__ == '__main__':
    main()

