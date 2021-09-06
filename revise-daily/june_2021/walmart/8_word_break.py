def word_break(str, words):
    dp = [False] * (len(str)+1)
    dp[0] = True

    for i in range(len(str)):
        if dp[i]:
            for w in words:
                if i + len(w) > len(str):
                    return False

                if str[i: i +len(w)] == w:
                    dp[i+len(w)] = True
                    break
    return dp[-1]
