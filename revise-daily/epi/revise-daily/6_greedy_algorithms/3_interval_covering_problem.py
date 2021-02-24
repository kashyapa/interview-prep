class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.end < other.end


def minimum_interval_covering_all_visits(intervals):
    intervals.sort()
    end = 0
    visits = 0

    for itvl in intervals:
        if end <= itvl.start:
            visits += 1
            end = itvl.end
    return visits


if __name__ == '__main__':
    intervals = [Interval(1,2), Interval(2,3), Interval(3,4), Interval(4, 5)]
    print(minimum_interval_covering_all_visits(intervals))