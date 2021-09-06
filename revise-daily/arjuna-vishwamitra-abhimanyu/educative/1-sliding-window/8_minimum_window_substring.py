import imports

# efffing nailed it

def minimum_window_substring(str, pattern):
    min_length = imports.inf
    p_counter = imports.Counter()
    keys_to_cover = len(pattern)
    left = 0
    for i, c in enumerate(str):
        p_counter[c] -= 1
        if p_counter[c] >= 0:
            keys_to_cover -= 1

        while keys_to_cover == 0:
            min_length = min(min_length, i - left + 1)
            left_char = str[left]
            p_counter[left_char] += 1
            if p_counter[left_char] > 0:
                keys_to_cover += 1
            left += 1
    return min_length
