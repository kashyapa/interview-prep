from collections import Counter
import math


def minimum_window_subsequence(paragraph, words):
    min_window = math.inf
    w_count = len(words)

    for r, word in enumerate(paragraph):
        if word == words[0]:
            keyword_index_to_cover = 0

            for j in range(r, len(paragraph)):
                if paragraph[j] == words[keyword_index_to_cover]:
                    keyword_index_to_cover += 1
                    if keyword_index_to_cover == w_count:
                        min_window = min(min_window, j - r)
                        break

    return min_window


def minimum_window_subsequence_O_N(paragraph, words):
    """
    1) store the position of each keyword in a hashtable
    2) iterate over the paragraph and
        2a) if current word is a keyword, then find smallest subarray  that covers all keywords upto current keyword
        2b) otherwise store the index at which this keyword occurred in the paragraph

    """

    keyword_to_idx = {k: i for i, k in enumerate(words)}
    last_keyword_occurrence = [-1] * len(words)
    smallest_subarray_covering_keywords = [math.inf] * len(words)
    shortest_distance = math.inf

    for i, w in enumerate(paragraph):
        if w in keyword_to_idx:
            idx_position = keyword_to_idx[w]
            if idx_position == 0:
                smallest_subarray_covering_keywords[idx_position] = 0
            elif smallest_subarray_covering_keywords[idx_position-1] != math.inf:
                distance_from_previous_keyword_occurrence = i - last_keyword_occurrence[idx_position-1]
                smallest_subarray_covering_keywords[idx_position] = distance_from_previous_keyword_occurrence + \
                    smallest_subarray_covering_keywords[idx_position-1]

            last_keyword_occurrence[idx_position] = i

            if idx_position == len(words) - 1 and smallest_subarray_covering_keywords[-1] < shortest_distance:
                shortest_distance = smallest_subarray_covering_keywords[-1]

    return shortest_distance


if __name__ == '__main__':
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))
    print(minimum_window_subsequence_O_N(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    print(minimum_window_subsequence_O_N(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))
