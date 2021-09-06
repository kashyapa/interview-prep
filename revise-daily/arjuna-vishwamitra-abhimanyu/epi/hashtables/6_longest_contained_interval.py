def longest_contained_interval(A):
    unprocessed_entries = set(A)

    a = unprocessed_entries.pop()
    lower_bound = a - 1
    upper_bound = a + 1
    longest_interval = 0
    while unprocessed_entries:
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        longest_interval = max(longest_interval, upper_bound-lower_bound-1)

    return longest_interval
