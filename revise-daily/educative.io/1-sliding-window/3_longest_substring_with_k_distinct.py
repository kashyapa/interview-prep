import math
from collections import Counter

# Given a string, find the length of the longest substring in it with no more than K distinct characters.


def longest_substring_with_k_distinct(str, k):

    l = 0
    char_frequency = Counter()
    distinct = 0
    max_length = 0

    for r in range(len(str)):
        if char_frequency[str[r]] == 0:
            distinct += 1
        char_frequency[str[r]] += 1

        while distinct > k:
            char_frequency[str[l]] -= 1
            if char_frequency[str[l]] == 0:
                distinct -= 1
            l += 1
        max_length = max(max_length, r - l+1)

    return max_length


if __name__ == '__main__':
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))