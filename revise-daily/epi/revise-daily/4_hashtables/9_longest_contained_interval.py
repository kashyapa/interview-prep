def longest_contained_interval_func(A):
    unprocessed_entries = set(A)
    longest_contained_interval = 0

    while unprocessed_entries:
        a = unprocessed_entries.pop()
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(p)
            lower_bound -= 1

        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(q)
            upper_bound += 1

        longest_contained_interval = max(longest_contained_interval, upper_bound - lower_bound -1)

    return longest_contained_interval
