from collections import Counter

def longest_substring_after_replacement(s, k):
    i , left = 0, 0
    char_count = Counter()
    longest_substring = 0
    max_repeating_count = 0
    while i < len(s):
        c = s[i]
        char_count[c] += 1

        max_repeating_count = max(max_repeating_count, char_count[c])

        while i - left + 1 - max_repeating_count > k:
            char_count[s[left]] -= 1
            left += 1
        longest_substring = max(longest_substring, i-left+1)
    return longest_substring
