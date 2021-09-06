def count_trees(n):
    def rec(start, end):
        if start >= end:
            return 0
        count = 0
        for i in range(start, end+1):
            left_count = rec(start, i)
            right_count = rec(i+1, end)
            count += (left_count * right_count)
        return count

    return rec(1, n)
