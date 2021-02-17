from math import inf


def longest_subarray_with_distinct_entries(A):
    key_index = {}
    l = 0
    max_length = -inf

    for r, c in enumerate(A):
        if c in key_index:
            last_seen = key_index[c]
            if last_seen > l:
                l = last_seen + 1
        key_index[c] = r
        max_length = max(max_length, r - l + 1)

    return max_length


if __name__ == '__main__':
    print(longest_subarray_with_distinct_entries(['a', 's', 'w', 'd', 's', 'a', 't']))
