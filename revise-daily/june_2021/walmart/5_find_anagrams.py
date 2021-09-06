from collections import Counter

def find_anagrams(str, pattern):

    counter_p = Counter(pattern)
    keys_to_cover = len(counter_p)
    left = 0

    for i, c in enumerate(str):
        counter_p[c] -= 1
        if counter_p[c] == 0:
            keys_to_cover -= 1

        while keys_to_cover == 0:
            if i - left + 1 == len(pattern):
                return left
            if counter_p[str] == 0:
                keys_to_cover += 1
            counter_p[str[left]] += 1
            left += 1

