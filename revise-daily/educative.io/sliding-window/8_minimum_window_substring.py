from collections import Counter


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


if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC", "ABC"))