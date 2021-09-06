from collections import Counter


def find_string_anagrams(str1, pattern):
    char_counter = Counter()
    p_ctr = Counter(pattern)
    p_len = len(pattern)
    l = 0
    for i, c in enumerate(str1):
        char_counter[c] += 1

        while i - l + 1 > p_len:
            char_counter[str1[l]] -= 1
            if char_counter[str1[l]] == 0:
                del char_counter[str1[l]]
            l += 1

        if char_counter == p_ctr:
            return l, i

    return False


def find_anagrams(str, pattern):

    counter_p = Counter(pattern)
    keys_to_cover = len(counter_p)
    left = 0

    for i, c in enumerate(str):
        counter_p[c] -= 1
        if counter_p[c] == 0:
            keys_to_cover -= 1

        while keys_to_cover == 0:
            if i -left + 1 == len(pattern):
                return left
            if counter_p[str] == 0:
                keys_to_cover += 1
            counter_p[str[left]] += 1
            left += 1
    return False


def main():
    print(find_anagrams("ppqp", "pq"))
    print(find_anagrams("abbcabc", "abc"))


if __name__ == '__main__':
    main()
