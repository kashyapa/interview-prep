def insert(intervals, new_interval):
    merged = []
    i = 0
    while i < len(intervals) and new_interval[0] > intervals[i][1]:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] < new_interval[1]:
        start = min(intervals[i][0], new_interval[0])
        end = max(intervals[i][1], new_interval[1])
        merged.append([start, end])
        i += 1
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


if __name__ == "__main__":
    main()