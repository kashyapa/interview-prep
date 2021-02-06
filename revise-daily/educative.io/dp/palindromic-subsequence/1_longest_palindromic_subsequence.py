# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence,
# elements read the same backward and forward.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without
# changing the order of the remaining elements.

# Input: "abdbca"
# Output: 5
# Explanation: LPS is "abdba".

def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    if startIndex == endIndex:
        return 1
    n = len(st)

    if st[startIndex] == st[endIndex]:
        return 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1)

    c1 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
    c2 = find_LPS_length_recursive(st, startIndex + 1, endIndex)

    return max(c1, c2)


def find_LPS_length_recursive(dp, st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    # every sequence with one element is a palindrome of length 1
    if startIndex == endIndex:
        return 1

    if (dp[startIndex][endIndex] == -1):
        # case 1: elements at the beginning and the end are the same
        if st[startIndex] == st[endIndex]:
            dp[startIndex][endIndex] = 2 + find_LPS_length_recursive(dp, st, startIndex + 1, endIndex - 1)
        else:
            # case 2: skip one element either from the beginning or the end
            c1 = find_LPS_length_recursive(dp, st, startIndex + 1, endIndex)
            c2 = find_LPS_length_recursive(dp, st, startIndex, endIndex - 1)
            dp[startIndex][endIndex] = max(c1, c2)

    return dp[startIndex][endIndex]


def find_LPS_length(st):
    n = len(st)
    # dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and the end are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:  # case 2: skip one element either from the beginning or the end
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n - 1]


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
