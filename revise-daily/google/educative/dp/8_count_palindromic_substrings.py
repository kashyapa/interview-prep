
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