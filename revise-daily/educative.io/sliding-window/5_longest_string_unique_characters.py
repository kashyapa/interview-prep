def longest_string_with_unique_characters(s):
    char_index_map = {}
    left = 0
    max_length = 0

    for i, c in enumerate(s):
        if c in char_index_map:
            if char_index_map[c] >= left:
                left = char_index_map[c] + 1
        char_index_map[c] = i
        max_length = max(max_length, i - left + 1)
    return max_length