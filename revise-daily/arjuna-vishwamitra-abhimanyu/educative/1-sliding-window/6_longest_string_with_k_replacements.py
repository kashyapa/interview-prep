# not letting this opportunity go 
# grabbing this by the throat
# this is mine, mine and only mine

import imports


def longest_string_with_K_replacements(s, K):
    max_repeating_count = 0
    left = 0
    max_length = 0
    char_counter = imports.Counter()
    for i, c in enumerate(s):
        char_counter[c] += 1
        if char_counter[c] > max_repeating_count:
            max_repeating_count = char_counter[c]
        while i - left - max_repeating_count > K:
            char_counter[s[left]] -= 1
            left += 1
        max_length = max(max_length, i - left+1)

    return max_length
