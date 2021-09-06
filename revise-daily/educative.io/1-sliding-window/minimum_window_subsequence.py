from collections import Counter

import math

def minimum_window_subsequence(s, t):
    t_map = Counter(t)
    min_length = math.inf

    window_start, window_end = -1, -1
    for i, c in enumerate(s):
        if s[i] == t[0]:
            j = i
            count = 0
            while j < len(s) and count < len(t):
                if s[j] == t[count]:
                    count += 1
                    if count == len(t):
                        if min_length > j - i + 1:
                            min_length = j - 1 + 1
                            window_start = i
                            window_end = j
                        break
                j += 1

    return s[window_start: window_end+1]

import math

def min_window_subsequence(string, pattern):
    min_length = math.inf
    for i, c in enumerate(string):

        if c == pattern[0]:
            count = 0
            j = i
            while j < len(string) and count < len(pattern):
                if string[j] == pattern[count]:
                    count += 1
                while count == len(pattern):
                    min_length = min(j - i + 1, min_length)

                j += 1


if __name__ == '__main__':
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    print(minimum_window_subsequence(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))
    # print(minimum_window_subsequence_O_N(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["banana", "apple"]))
    # print(minimum_window_subsequence_O_N(["apple", "sdhgfb", "asdlkfnasdj", "d;jksbfds;", "banana", "apple"], ["apple", "banana"]))
