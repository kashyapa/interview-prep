# Given a string, find the length of the longest substring, which has no repeating characters.
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".


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

def longest_string_with_unique_chars(str):
    longest_length = 0
    last_dup_char_index = -1
    char_index = {}
    l = 0
    for i, c in enumerate(str):
        # dup seen
        if c in char_index:
            if char_index[c] > l:
                l = char_index[c] + 1
            char_index[c] = i
        longest_length = max(longest_length, i - l + 1)
    return longest_length

