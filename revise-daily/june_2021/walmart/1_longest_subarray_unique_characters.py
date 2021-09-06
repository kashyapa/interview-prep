def longest_subarray_with_unique_characters(s):
    left = 0
    max_unique_char_count = 0
    last_seen = {}
    for i, c in enumerate(s):
        if c in last_seen:
            if last_seen[c] >= left:
                left = last_seen[c]+1
        max_unique_char_count = max(max_unique_char_count, i-left+1)
        last_seen[c] = i
    return max_unique_char_count
