import imports


def smallest_subarray_covering_all_values(str, str2):
    smaller_str_counter = imports.Counter(str)
    chars_to_cover = len(smaller_str_counter)
    left = 0
    min_length = imports.inf
    start, end = -1, -1

    for i, c in enumerate(str2):
        smaller_str_counter[c] -= 1
        if smaller_str_counter[c] == 0:
            chars_to_cover -= 1
        while chars_to_cover == 0:
            if i - left + 1 < min_length:
                start = left
                end = i
                min_length = i - left + 1
            c = str2[left]
            smaller_str_counter[c] += 1
            if smaller_str_counter[c] > 0:
                chars_to_cover += 1
            left += 1
    return min_length, start, end


if __name__ == '__main__':
    print(smallest_subarray_covering_all_values(["apple", "banana", "apple"],
                                                ["apple", "fsdlgk", "afsdkfb", "banana", "apple",
                                                 "sdjhfbsdfb", "apple", "sdkjv", "banana"],
                                                ))