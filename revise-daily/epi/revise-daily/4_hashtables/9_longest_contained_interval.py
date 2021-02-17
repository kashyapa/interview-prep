def longest_contained_interval(A):
    unprocessed_entries = set(A)
    longest_contained_interval = 0

    while unprocessed_entries:
        p = unprocessed_entries.pop()
        while p in unprocessed_entries:
            unprocessed_entries.remove(p)
            p -= 1

        q = n+1
        while q in unprocessed_entries:
            unprocessed_entries.remove(q)
            q += 1

        longest_contained_interval = max(longest_contained_interval, q-p-1)

    return longest_contained_interval