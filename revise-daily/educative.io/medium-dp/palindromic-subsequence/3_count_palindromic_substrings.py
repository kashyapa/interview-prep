# Given a string, find the total number of palindromic substrings in it.
# Please note we need to find the total number
# of substrings and not subsequences.

def count_PS(st):

    return count_PS_dp(st)


def count_PS_dp(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]

    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1

    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):

            if st[start_index] == st[end_index]:
                if end_index - start_index == 1 or dp[start_index+1][end_index-1] is True:
                    dp[start_index][end_index] = True
                    count += 1

    return count


def countSubstrings(st: str) -> int:
    def count_palindrome(st, l, r):
        count = 0
        while l >= 0 and r < len(st) and st[l] == st[r]:
            count += 1
            l -= 1
            r += 1
        return count

    count = 0

    for i in range(len(st)):
        count += count_palindrome(st, i, i)
        count += count_palindrome(st, i, i + 1)
    return count


def count_palindromic_substrings(s):
    n = len(s)

    def is_palindrome(t):
        return t == t[::-1]

    count = 0

    for i in range(n):
        for j in range(i+1):
            substr = s[j:i+1]
            if is_palindrome(substr):
                count += 1
    return count

def main():
    print(count_PS("abdbca"))
    print(count_PS("cddpd"))
    print(count_PS("pqr"))
    print(count_PS("qqq"))
    print(count_PS("aaa"))
    print("*******")
    print(countSubstrings("abdbca"))
    print(countSubstrings("cddpd"))
    print(countSubstrings("pqr"))
    print(countSubstrings("qqq"))
    print(countSubstrings("aaa"))

    print("*******")

    print(count_palindromic_substrings("abdbca"))
    print(count_palindromic_substrings("cddpd"))
    print(count_palindromic_substrings("pqr"))
    print(count_palindromic_substrings("qqq"))
    print(count_palindromic_substrings("aaa"))




if __name__ == "__main__":
    main()
