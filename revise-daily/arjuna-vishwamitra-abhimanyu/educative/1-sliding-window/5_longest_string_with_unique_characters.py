def longest_string_with_unique_characters(s):
    char_index = {}
    left = 0
    max_length = 0

    for i, c in enumerate(s):
        if c in char_index:
            last_seen_index = char_index[c]
            if last_seen_index >= left:
                left = last_seen_index + 1
        char_index[c] = i
        max_length = max(i-left+1, max_length)

    return max_length
