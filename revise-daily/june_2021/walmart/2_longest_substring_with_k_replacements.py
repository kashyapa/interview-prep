def longest_substring_with_k_distinct_characters(s, k):
    distinct = 0
    char_map = {}
    i = 0
    left = 0
    longest_substring = 0

    while i < len(s):
        c = s[i]
        if c not in char_map:
            distinct += 1
            char_map[c] = 0
            while distinct > k:
                char_map[left] -= 1
                if char_map[left] == 0:
                    distinct -= 1
                left += 1
        char_map[c] += 1
        longest_substring = max(longest_substring, i-left+1)
        i += 1
