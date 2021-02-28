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


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


if __name__ == '__main__':
    main()
