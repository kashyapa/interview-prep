from collections import Counter


def minWindow(s: str, t: str) -> str:
    t_len = len(t)
    char_count_map_t = Counter(t)
    remaining_to_cover = t_len
    l = 0
    min_length = len(s)
    min_start, min_end = -1, -1

    for i, c in enumerate(s):
        if c in char_count_map_t:
            char_count_map_t[c] -= 1
            if char_count_map_t[c] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if min_length > i - l + 1:
                min_start, min_end = l, i
                min_length = i - l + 1

            if s[l] in char_count_map_t:
                char_count_map_t[s[l]] += 1
                if char_count_map_t[s[l]] > 0:
                    remaining_to_cover += 1

            l += 1

    return s[min_start: min_end+1]


if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC", "ABC"))