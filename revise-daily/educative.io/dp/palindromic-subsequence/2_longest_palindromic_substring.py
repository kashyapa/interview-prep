# Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.


def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1

    if st[startIndex] == st[endIndex]:
        remaining_length = endIndex - startIndex - 1
        if remaining_length == find_LPS_length_recursive(st, startIndex + 1, endIndex - 1):
            return remaining_length + 2

    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)

    return max(c1, c2)


def find_LPS_length_recursive2(dp, st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    # every string with one character is a palindrome
    if startIndex == endIndex:
        return 1

    if dp[startIndex][endIndex] == -1:
        # case 1: elements at the beginning and the end are the same
        if st[startIndex] == st[endIndex]:
            remainingLength = endIndex - startIndex - 1
            # if the remaining string is a palindrome too
            if remainingLength == find_LPS_length_recursive(dp, st, startIndex + 1, endIndex - 1):
                dp[startIndex][endIndex] = remainingLength + 2
                return dp[startIndex][endIndex]

        # case 2: skip one character either from the beginning or the end
        c1 = find_LPS_length_recursive(dp, st, startIndex + 1, endIndex)
        c2 = find_LPS_length_recursive(dp, st, startIndex, endIndex - 1)
        dp[startIndex][endIndex] = max(c1, c2)

    return dp[startIndex][endIndex]


def find_LPS_length(st):
    n = len(st)
    # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    dp = [[False for _ in range(n)] for _ in range(n)]

    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True

    maxLength = 1
    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if st[startIndex] == st[endIndex]:
                # if it's a two character string or if the remaining string is a palindrome too
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    maxLength = max(maxLength, endIndex - startIndex + 1)

    return maxLength


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


if __name__ == "__main__":
    main()
