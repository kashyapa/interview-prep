def find_min_operations(s1, s2):
    return find_min_operations_recursive(s1, s2, 0, 0)


def find_min_operations_dp(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # if s2 is empty, we can remove all the characters of s1 to make it empty too
    for i1 in range(n1 + 1):
        dp[i1][0] = i1

    # if s1 is empty, we have to insert all the characters of s2
    for i2 in range(n2 + 1):
        dp[0][i2] = i2

    for i1 in range(1, n1 + 1):
        for i2 in range(1, n2 + 1):
            # If the strings have a matching character, we can recursively match for the remaining lengths
            if s1[i1 - 1] == s2[i2 - 1]:
                dp[i1][i2] = dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = 1 + min(dp[i1 - 1][i2],  # delete
                                     min(dp[i1][i2 - 1],  # insert
                                         dp[i1 - 1][i2 - 1]))  # replace

    return dp[n1][n2]


def find_min_operations_recursive(s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    # if we have reached the end of s1, then we have to insert all the remaining characters of s2
    if i1 == n1:
        return n2 - i2

    # if we have reached the end of s2, then we have to delete all the remaining characters of s1
    if i2 == n2:
        return n1 - i1

    # If the strings have a matching character, we can recursively match for the remaining lengths
    if s1[i1] == s2[i2]:
        return find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

    # perform deletion
    c1 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2)
    # perform insertion
    c2 = 1 + find_min_operations_recursive(s1, s2, i1, i2 + 1)
    # perform replacement
    c3 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

    return min(c1, min(c2, c3))


def main():
    print(find_min_operations("bat", "but"))
    print(find_min_operations("abdca", "cbda"))
    print(find_min_operations("passpot", "ppsspqrt"))


main()
