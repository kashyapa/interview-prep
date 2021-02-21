# There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
# The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the
# security system. How should the thief maximize his stealing?

# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4


def find_max_steal(wealth):
    return find_max_steal_recursive(wealth, 0)


def find_max_steal_recursive(wealth, currentIndex):
    if currentIndex >= len(wealth):
        return 0

    # steal from current house and skip one to steal next
    stealCurrent = wealth[currentIndex] + find_max_steal_recursive(wealth, currentIndex + 2)
    # skip current house to steel from the adjacent house
    skipCurrent = find_max_steal_recursive(wealth, currentIndex + 1)

    return max(stealCurrent, skipCurrent)


def find_max_steal_recursive2(dp, wealth, currentIndex):
    if currentIndex >= len(wealth):
        return 0

    if dp[currentIndex] == 0:
        # steal from current house and skip one to steal next
        stealCurrent = wealth[currentIndex] + find_max_steal_recursive(dp, wealth, currentIndex + 2)
        # skip current house to steel from the adjacent house
        skipCurrent = find_max_steal_recursive(dp, wealth, currentIndex + 1)

        dp[currentIndex] = max(stealCurrent, skipCurrent)

    return dp[currentIndex]


def find_max_steal(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    dp = [0 for x in range(n + 1)]  # '+1' to handle the zero house
    dp[0] = 0  # if there are no houses, the thief can't steal anything
    dp[1] = wealth[0]  # only one house, so the thief have to steal from it

    # please note that dp[] has one extra element to handle zero house
    for i in range(1, n):
        dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])

    return dp[n]


def main():
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))


if __name__ == "__main__":
    main()
