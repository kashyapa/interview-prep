from collections import Counter


def length_of_longest_substring(s, k):
    char_index_map = Counter()
    max_repeat_count = 0
    l, max_length = 0, 0

    for i, c in enumerate(s):
        char_index_map[c] += 1
        max_repeat_count = max(max_repeat_count, char_index_map[c])
        while i - l + 1 - max_repeat_count > k:
            char_index_map[s[l]] -= 1
            l += 1

        max_length = max(max_length, i - l + 1)
    return max_length
