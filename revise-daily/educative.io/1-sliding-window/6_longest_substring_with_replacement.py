from collections import Counter
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.
#
# Example 1:
#
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:
#
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:
#
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


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


def length_of_longest_Str_with_char_replace(s, k):
    char_counter = Counter()
    max_repeat_character = s[0]
    l = 0
    max_length = 0
    for i, c in enumerate(s):
        char_counter[c] += 1
        if char_counter[c] >= char_counter[max_repeat_character]:
            max_repeat_character = c
        while i - l + 1 - char_counter[max_repeat_character] > k:
            char_counter[s[l]] -= 1
            l += 1
        max_length = max(max_length, i - l + 1)
    return max_length
