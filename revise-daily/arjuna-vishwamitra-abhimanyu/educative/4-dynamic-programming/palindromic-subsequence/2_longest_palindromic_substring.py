def find_longest_palindromic_substring(str):

    def find_palindrome(l, r):
        while l >= 0 and r < len(str) and str[l] == str[r]:
            l -= 1
            r += 1
        return r - l

    max_length = 0

    for i in range(len(str)):
        even_length = find_palindrome(i, i+1)
        odd_length = find_palindrome(i, i)
        max_length = max(max_length, max(even_length, odd_length))

    return max_length


def find_palindromic_substring(str):

    def rec(l, r):
        if l > r:
            return -1
        if l == r:
            return 1

        if str[l] == str[r]:
            pl = rec(l+1, r-1)
            if pl + 2 == l - r + 1:
                return l - r + 1
        c1 = rec(l+1, r)
        c2 = rec(l, r-1)
        return max(c1, c2)
    