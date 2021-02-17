from collections import Counter
import math


def find_minimum_window(str_arr, words_set):
    words_counter = Counter(words_set)
    keywords_remaining = len(words_set)
    left = 0
    min_window = math.inf
    min_start = -1
    min_end = -1
    for r, word in enumerate(str_arr):
        words_counter[word] -= 1
        if words_counter[word] >= 0:
            keywords_remaining -= 1
            if words_counter[word] == 0:
                del words_counter[word]
        while keywords_remaining == 0:
            words_counter[str_arr[left]] += 1
            if words_counter[str_arr[left]] > 0:
                keywords_remaining += 1
            if r - left < min_window:
                min_window = r - left
                min_start = left
                min_end = r
            left += 1
    return min_window, min_start, min_end


if __name__ == '__main__':
    print(find_minimum_window(["apple", "fsdlgk", "afsdkfb", "banana", "apple", "sdjhfbsdfb", "apple", "sdkjv", "banana"], ["apple", "banana", "apple"]))