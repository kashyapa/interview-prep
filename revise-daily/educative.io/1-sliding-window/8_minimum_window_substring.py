from collections import Counter
import collections
import math

def minWindow(s: str, t: str) -> str:
    t_len = len(t)
    chars_to_cover = Counter(t)
    remaining_to_cover = t_len
    window_start, window_end = -1, -1
    left = 0
    min_length = len(s)

    for r, c in enumerate(s):
        if c in chars_to_cover:
            chars_to_cover[c] -= 1
            if chars_to_cover[c] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if min_length > r - left + 1:
                window_start, window_end = left, r
                min_length = min(r - left + 1, min_length)

            left_char = s[left]
            if left_char in chars_to_cover:
                chars_to_cover[left_char] += 1
                if chars_to_cover[left_char] > 0:
                    remaining_to_cover += 1
            left += 1

    return s[window_start: window_end+1]



def min_window(s, t):
    t_map = Counter(t)
    remaining_chars = len(t)
    min_length = math.inf
    l = 0
    window_start, window_end = -1, -1

    for r, c in enumerate(s):
        t_map[c] -= 1
        if t_map[c] >= 0:
            remaining_chars -= 1
        while remaining_chars == 0:
            if r - l + 1 < min_length:
                window_start = l
                window_end = r

            min_length = min(min_length, r - l + 1)

            t_map[s[l]] += 1
            if t_map[s[l]] > 0:
                remaining_chars += 1
            l += 1

    return s[window_start:window_end+1]


def minWindow(s, t):
    char_counter = collections.Counter(t)
    remaining_chars = len(char_counter)
    min_length = math.inf
    min_start, min_end = -1, -1

    i, l = 0, 0
    for i, c in enumerate(s):
        char_counter[c] -= 1
        if char_counter[c] == 0:
            remaining_chars -= 1

        while remaining_chars == 0:
            if i - l + 1 < min_length:
                min_length = i - l + 1
                min_start, min_end = l, i
            char_counter[s[l]] += 1
            if char_counter[s[l]] > 0:
                remaining_chars += 1
            l += 1
    return s[min_start:min_end + 1]


if __name__ == '__main__':
    print(min_window("ADOBECODEBANC", "ABC"))