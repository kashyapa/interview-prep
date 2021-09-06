# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

def find_max_sum(arr, k):
    sum = 0
    max_sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if i > k-1:
            sum -= arr[i-k]
        max_sum = max(max_sum, sum)
    return max_sum

#Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
def smallest_subarray_with_sum(arr, target):
    left = 0
    min_length = len(arr)
    for i in range(len(arr)):
        sum += arr[i]
        while sum > target:
            min_length = min(min_length, i - left + 1)
            sum -= arr[left]
            left += 1
    return min_length

from collections import Counter

# Given a string, find the length of the longest substring in it with no more than K distinct characters.
def longest_substring_with_k_distinct_characters(s, k):
    left = 0
    char_count = Counter()
    distinct = 0
    max_length = 0
    for i, c in enumerate(s):
        if char_count[c] == 0:
            distinct += 1
        char_count[c] += 1
        while distinct > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
                distinct -= 1
            left += 1
        max_length = max(max_length, i - left + 1)

    return max_length

# Given a string, find the length of the longest substring, which has no repeating characters.


def longest_length_with_unique_characters(s):
    char_count = {}
    left = 0
    max_l = 0
    for i, c in enumerate(s):
        if c in char_count:
            if char_count[c] >= left:
                left = char_count[c] + 1
        max_l = max(i - left + 1, max_l)
        char_count[c] = i
    return max(max_l, len(s) - left)

# Longest Substring with Same Letters after Replacement
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.

def find_longest_substring_with_same_characters_after_k_replacements(s, k):
    # find window that has k characters that are not the character with max count
    char_count = {}
    max_count = 0
    l = 0
    max_l = 0
    for i, c in enumerate(s):
        if c in char_count:
            char_count[c] += 1
            if char_count[c] > max_count:
                max_count = char_count[c]
        else:
            char_count[c] = 1
        while i - l - max_count > k:
            char_count[s[l]] -= 1
            if char_count[s[l]] == 0:
                del char_count[s[l]]
            l += 1
        max_l = max(max_l, i-l+1)
    return max_l

# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

def find_length_of_array_having_ones_with_k_replacements(arr, k):
    max_l = 0
    left = 0
    ones_counter = 0
    zeros = 0
    for i, n in enumerate(arr):
        if n == 1:
            ones_counter+=1
        else:
            zeros += 1
        while i - left - ones_counter > k:
            if arr[left] == 1:
                ones_counter -= 1
            left += 1

        max_l = max(max_l, i - left + 1)
    return max_l

def permutation_in_a_string(s, perm):
    p_count = Counter(perm)
    s_count = Counter()
    for i, c in enumerate(s):
        s_count[c] += 1
        if i >= len(perm)-1:
            s_count[i-len(perm)] -=1
            if s_count[i-len(perm)] == 0:
                del s_count[i-len(perm)]
        if s_count == p_count:
            return True

import math

def min_window_substring(s, t):
    t_char_count = Counter(t)
    keys_to_cover = len(t)
    left = 0
    min_length = math.inf
    start, end = -1, -1

    for i, c in enumerate(s):
        if c in t_char_count:
            t_char_count[c] -= 1
            keys_to_cover -= 1
            if t_char_count[c] == 0:
                del t_char_count[c]
        while keys_to_cover == 0:
            if i -left +1 < min_length:
                min_length = min(min_length, i - left + 1)
                start = left
                end = i
            if s[left] in t_char_count:
                t_char_count[s[left]] += 1
                keys_to_cover += 1
            left += 1
    return s[start:end]


def check_if_word_concatenation_of_substrings(s, words):
    words_count = Counter(words)
    words_to_cover = len(words)
    unit_size = len(words[0])
    res = []

    for i in range(0, len(s) - words_to_cover * unit_size +1):
        substr = s[i:i+unit_size]
        print("start checking at index ", i, substr)
        if substr in words_count:
            j = i
            mapper = Counter(words)
            words_to_cover = len(words)
            print("before while loop: ")
            while True:
                print(s[j:j+unit_size])
                print(mapper)
                if s[j:j+unit_size] in mapper:
                    mapper[s[j:j+unit_size]] -= 1
                    words_to_cover -= 1
                    if mapper[s[j:j+unit_size]] == 0:
                        del mapper[s[j:j+unit_size]]
                    if words_to_cover == 0:
                        res.append(i)
                else:
                    break
                print("after while loop: ", mapper, "\n****")
                j += unit_size
    return res


if __name__ == '__main__':
    print(check_if_word_concatenation_of_substrings("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(check_if_word_concatenation_of_substrings("bagfoxcat", ["cat", "fox"]))
    print(check_if_word_concatenation_of_substrings("barfoothefoobarman", ["foo", "the"]))
    print(check_if_word_concatenation_of_substrings("barfoofoobarthefoobarman", ["bar","foo","the"]))