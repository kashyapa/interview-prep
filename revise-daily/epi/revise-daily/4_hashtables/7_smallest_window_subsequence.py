from collections import Counter
import math


def minimum_window_subsequence(paragraph, words):
    min_window = math.inf

    for r, word in enumerate(paragraph):
        if word == words[0]:
            w_count = len(words)
            keywords_remaining = w_count

            for j in range(r, len(paragraph)):
                if paragraph[j] == words[w_count-keywords_remaining]:
                    keywords_remaining -= 1

                    if keywords_remaining == 0:
                        min_window = min(min_window, j - r)
                        break

    return min_window


if __name__ == '__main__':
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))