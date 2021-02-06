def calculateFibonacci(n):
    if n < 2:
        return n

    return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def calculateFibonacci_memo(n):
    memoize = [-1 for x in range(n + 1)]
    return calculateFibonacciRecur(memoize, n)


def calculateFibonacciRecur(memoize, n):
    if n < 2:
        return n

    # if we have already solved this subproblem, simply return the result from the cache
    if memoize[n] >= 0:
        return memoize[n]

    memoize[n] = calculateFibonacciRecur(
        memoize, n - 1) + calculateFibonacciRecur(memoize, n - 2)
    return memoize[n]


def calculateFibonacci_bottom_up(n):
    if n < 2:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


def calculateFibonacci_memory_optimized(n):
    if n < 2:
        return n

    n1, n2, temp = 0, 1, 0
    for i in range(2, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp

    return n2


def main():
    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
