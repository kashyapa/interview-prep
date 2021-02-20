#!/usr/bin/python3
# Build Domain index (EPI)

# Respace (CCI)


def bed_bath_beyond(s: str, words: set):
    res = []
    mem = [-1] * (len(s))

    for i in range(1, len(s)):
        prefix = s[:i + 1]
        if prefix in words:
            mem[i] = len(prefix)
            continue
        for j in range(i):
            if mem[j] != -1 and s[j + 1:i + 1] in words:
                mem[i] = i - j
                break

    print(mem)

    if mem[-1] != -1:
        idx = len(s)-1

        while idx >= 0:
            res.append(s[idx - mem[idx]+1:idx+1])
            idx -= (mem[idx])
        res = res[::-1]
        # print(mem)
    print(res)
    return res


if __name__ == '__main__':
    set2 = {"bed", "bath", "bat", "beyond", "hand", "and"}
    print(bed_bath_beyond("bedbathandbeyond", set2))
