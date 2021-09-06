def count_palindromic_substrings(str):

    def count_palindrome(l, r):
        count = 0
        while l >= 0 and r < len(str) and str[l] == str[r]:
            l -= 1
            r += 1
            count += 1
        return count

    count = 0
    for i in range(len(str)):
        count += count_palindrome(i, i)
        count += count_palindrome(i, i+1)
    return count


def count_palindromic_substring(str):
    n = len(str)

    dp = [[0 for _ in range(len(str))] for _ in range(len(str))]
    count = 0
    
    for i in range(n):
        dp[i][i] = True
        
    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):
            if str[start_index] == str[end_index]:
                if end_index - start_index == 1 or dp[start_index+1][end_index-1]:
                    dp[start_index][end_index] = True
                    count += 1
    return count
