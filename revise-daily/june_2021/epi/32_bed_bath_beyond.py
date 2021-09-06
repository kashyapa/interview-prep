def bed_bath_beyond(words, str):
    dp = [-1] * len(str)

    for i in range(len(str)):
        prefix = str[:i+1]
        if prefix in words:
            dp[i] = i+1

        for j in range(i+1):
            #if dp[i] == -1:
            suffix = str[j:i+1]
            if suffix in words:
                dp[i] = i-j+1
    print(dp)

    res = []
    idx = len(str) - 1
    while idx >= 0:
        if dp[idx] != -1:
            print(str[idx-dp[idx]+1:idx+1])
            res.append(str[idx-dp[idx]+1:idx+1])
            idx -= dp[idx]
    return res

if __name__ == "__main__":
    print(bed_bath_beyond(["bed", "bat", "hand", "bath", "and", "beyond"], "bedbathandbeyond"))