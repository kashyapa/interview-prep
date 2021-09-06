def longest_substring_with_k_distinct_characters(s, k):
    import imports
    distinct = 0
    char_count = imports.Counter()
    left = 0
    max_length = 0

    for i, c in enumerate(s):
        if char_count[c] == 0:
            distinct += 1

        char_count[c] += 1
        while distinct > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                distinct -= 1
            left += 1
        max_length = max(i-left+1, max_length)
    return max_length
