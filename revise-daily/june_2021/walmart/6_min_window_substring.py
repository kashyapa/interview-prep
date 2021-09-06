from collections import Counter
import math


def minimum_window_substring(str, pattern):
    counter_p = Counter(pattern)
    keys_to_cover = len(counter_p)
    min_length = math.inf

    l, r = 0, 0

    while r < len(str):
        counter_p[str[r]] -= 1

        if counter_p[str[r]] == 0:
            keys_to_cover -= 1

        while keys_to_cover == 0:
            min_length = min(min_length, r - l + 1)
            counter_p[str[l]] += 1
            if counter_p[str[l]] > 0:
                keys_to_cover += 1
            l += 1
        r += 1
    return min_length
