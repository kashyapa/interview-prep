def calculate_fibonacci(n):
    if n < 2:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)


def calculate_fibonacci_memo(n):
    memo = [-1 for _ in range(n+1)]
    return calculate_fibonacci_memo(memo, n)


def calculate_fibonacci_recur(memo, n):
    if n < 2:
        return n

    if memo[n] >= 0:
        return memo[n]

    memo[n] = calculate_fibonacci_memo(memo, n-1) + calculate_fibonacci_memo(memo, n-2)
    return memo[n]


def calculate_fibonacci_bottom_up(n):
    if n < 2:
        return n
    
    dp = [0, 1]
    
    for i in range(2, n+1):
        dp.append(dp[i-1]+dp[i-2])
        
    return dp[n]

