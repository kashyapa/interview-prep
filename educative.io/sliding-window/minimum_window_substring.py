from collections import Counter


def minWindow(s: str, t: str) -> str:
    t_count = Counter(t)
    s_count = Counter()
    t_len = len(t)
    l = 0
    min_length = len(s)

    for r in range(len(s)):
        s_count[s[r]] += 1
        while r - l + 1 > t_len:
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                del s_count[s[l]]

            l += 1
        if s_count == t_count:
            min_length = min(min_length, r - l + 1)

    return min_length


if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC", "ABC"))