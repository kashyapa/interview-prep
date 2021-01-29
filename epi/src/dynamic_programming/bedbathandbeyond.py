#!/usr/bin/python3
# Build Domain index (EPI)

# Respace (CCI)

def bed_bath_beyond(s: str, words: set):
    res = []
    mem = [-1] * (len(s)+1)

    for i in range(len(s)):
        prefix = s[:i + 1]
        if prefix in words:
            mem[i] = len(prefix)
            continue
        for j in range(i):
            if mem[j] != -1 and s[j + 1:i + 1] in words:
                mem[i] = i - j
    idx = len(s)-1

    while idx >= 0:
        res.append(s[idx - mem[idx]+1:idx+1])
        idx -= mem[idx]
    print(res)

set = set(["bed", "bath", "beyond"])

bed_bath_beyond("bedbathbeyond", set)
