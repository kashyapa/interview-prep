from collections import Counter
import math


def minimum_window_subsequence(paragraph, words):
    min_window = math.inf

    for r, word in enumerate(paragraph):
        if word == words[0]:
            w_count = len(words)
            keyword_index_to_cover = 0

            for j in range(r, len(paragraph)):
                if paragraph[j] == words[keyword_index_to_cover]:
                    keyword_index_to_cover += 1
                    if keyword_index_to_cover == w_count:
                        min_window = min(min_window, j - r)
                        break

    return min_window


#def minimum_window_subsequence_O_N(paragraph, words)



if __name__ == '__main__':
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))
