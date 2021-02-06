# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward
# from that element, write a program to find the minimum number of jumps needed to reach the end of the array
# (starting from the first element). If an element is 0, then we cannot move through that element.

import math


def count_min_jumps(jumps):
    return count_min_jumps_recursive(jumps, 0)


def count_min_jumps_recursive(jumps, currentIndex):
    n = len(jumps)

    if currentIndex == n - 1:
        return 0

    if jumps[currentIndex] == 0:
        return math.inf

    start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
    total_jumps = math.inf

    while start < n and start <= end:
        min_jumps = count_min_jumps_recursive(jumps, start)
        start += 1
        if min_jumps != math.inf:
            total_jumps = min(min_jumps + 1, total_jumps)

    return total_jumps


def main():
    print(count_min_jumps([2, 1, 1, 1, 4]))
    print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


if __name__ == "__main__":
    main()
