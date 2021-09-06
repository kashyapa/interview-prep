def underscorifySubstring(string, substring):
    # Write your code here.
    dp = [False for i in range(len(string) + 1)]
    dp[0] = True
    left = 1
    for i in range(len(string) - len(substring) + 1):
        if dp[i]:
            for j in range(i, len(string)):
                if string.startswith(substring, j): #and dp[j-len(substring)] is False:
                    dp[j] = True
                    k = j+len(substring)
                    while k < len(string) and string.startswith(substring, k):
                        k += len(substring)
                    dp[k] = True
                    break

    res = []
    left = 0
    for i in range(1, len(dp)):
        if dp[i] == True:

            res.append("_")
            res.append(string[left:i])
            left = i
            #res.append("_")
            #res.append(substring)
    res.append(string[left:])
    return ''.join(res)


if __name__ == "__main__":
    print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))