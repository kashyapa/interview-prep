def bed_bath_beyond(str, words):

    mem = [-1] * len(str)

    for i in range(len(str)):
        prefix = str[:i+1]
        if prefix in words:
            mem[i] = len(prefix)
            continue
        for j in range(i):
            if mem[j] != -1 and str[j+1:i+1] in words:
                mem[i] = i - j
                
    res = []
    if mem[-1] != -1:
        idx = len(mem)-1
        while idx >= 0:
            res.append(str[idx - mem[idx]+1: idx+1])
            idx -= mem[idx]
        res = res[::-1]
    return res


if __name__ == '__main__':
    set2 = {"bed", "bath", "bat", "beyond", "hand", "and"}
    print(bed_bath_beyond("bedbathandbeyond", set2))