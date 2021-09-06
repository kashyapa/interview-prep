import imports


def permutation_in_string(str, pattern):
    if len(str) < len(pattern):
        return permutation_in_string(pattern, str)
    p_counter = imports.Counter(pattern)
    keys_to_be_covered = len(pattern)

    left = 0

    for i, c in enumerate(str):
        p_counter[c] -= 1
        if p_counter[c] >= 0:
            keys_to_be_covered -= 1

        while keys_to_be_covered == 0:
            if i - left + 1 == len(pattern):
                return True
            p_counter[str[left]] += 1
            if p_counter[str[left]] > 0:
                keys_to_be_covered += 1
            left += 1
    return False

# def permutation_in_string(str, pattern):
#
#     p_counter = imports.Counter(pattern)
#     keys_covered = 0
#     for i,c in enumerate(str):
#         if c in p_counter:
#             p_counter[c] -= 1
#             if p_counter[c] >= 0:
#                 keys_covered += 1
#         if i >= len(pattern)-1:
#             if keys_covered == len(pattern):
#                 return True
#
#             p_counter[str[i+1-len(pattern)]] += 1
#             if p_counter[str[i+1-len(pattern)]] > 0:
#                 keys_covered -= 1
#     return False
#




# p_counter = Counter(pattern)
# keys_to_be_covered = len(pattern)
#
# left = 0
#
# for i, c in enumerate(str):
#     if c in p_counter:
#         p_counter[c] -= 1
#         if p_counter[c] >= 0:
#             keys_to_be_covered -= 1
#     while keys_to_be_covered == 0:
#         if i - left + 1 == len(pattern):
#             return True
#
#         left_char = str[left]
#         p_counter[left_char] += 1
#         if p_counter[left_char] > 0:
#             keys_to_be_covered += 1
#         left += 1
# return False
#


def find_permutation(str, pattern):
    p_counter = imports.Counter(pattern)
    left, right = 0, 0
    keys_to_cover = len(pattern)

    while right < len(str):
        rc = str[right]
        p_counter[rc] -= 1
        if p_counter[rc] >= 0:
            keys_to_cover -= 1

        while keys_to_cover == 0:
            if right - left + 1 == len(pattern):
                return True

            p_counter[left] += 1
            if p_counter[left] > 0:
                keys_to_cover += 1

            left += 1
        right += 1

    return False

def find_anagram(str, pattern):
    p_counter = imports.Counter(pattern)
    str_counter = imports.Counter()
    for i, c in enumerate(str):
        str_counter[c] += 1
        if i >= len(pattern)-1:
            if str_counter == p_counter:
                return True
            str_counter[i-len(pattern)+1] -= 1
            if str_counter[i-len(pattern)+1] == 0:
                del str_counter[i-len(pattern)+1]
    return False


def main():
    # print(permutation_in_string("ppqp", "pq"))
    # print(permutation_in_string("abbcabc", "abc"))

    print(find_anagram("ab", "eidboaoo"))
    print(find_anagram("ab", "eidbaooo"))
    print(find_anagram("ab", "a"))


if __name__ == '__main__':
    main()
