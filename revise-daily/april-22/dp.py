import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        print(time.time()-start_time)
        return val
    return wrapper


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def fib2(n):

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]


@timer
def count_steps(n):
    def rec(n):
        if dp[n] != 0:
            return dp[n]

        dp[n] = rec(n-1) + rec(n-3) + rec(n-4)
        return dp[n]

    dp = [1, 1, 1, 2] + [0] * (n-1)
    return rec(n)

# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward
# from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting
# from the first element). If an element is 0, then we cannot move through that element.
import math

def minimum_jumps(jumps):

    def rec(i):

        if i == len(jumps)-1:
            return 0

        if jumps[i] == 0:
            return math.inf

        range_from_i = i + jumps[i]
        j = i + 1
        min_jumps = math.inf
        while j < len(jumps) and j <= range_from_i:
            num_jumps = 1+rec(j)
            j += 1
            if num_jumps != math.inf:
                min_jumps = min(min_jumps, num_jumps)
        return min_jumps

    return rec(0)

def min_jumps(jumps):

    def rec(index):
        n = len(jumps)
        if index == n - 1:
            return 0

        if jumps[index] == 0:
            return math.inf

        total_jumps = math.inf

        start_index = index + 1
        end_index = index + jumps[index]

        while start_index < n and start_index <= end_index:
            num_of_jumps = rec(start_index)
            if num_of_jumps != math.inf:
                total_jumps = min(num_of_jumps+1, total_jumps)
            start_index += 1

        return total_jumps

    return rec(0)

# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take
# the step. Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the
# top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that
# you are standing at the first step.

def minimum_fee(n, fees):

    def rec(step_index):
        if step_index == n:
            return 0

        if step_index > n-1:
            return 0

        fee_from_next_step = rec(step_index+1)
        fee_from_2_steps_forward = rec(step_index+2)
        fee_from_3_steps_forward = rec(step_index+3)

        return fees[step_index] + min(fee_from_next_step, fee_from_2_steps_forward, fee_from_3_steps_forward)

    return rec(0)


# There are n houses built in a line. A thief wants to steal the maximum possible money from these houses.
# The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert
# the security system. How should the thief maximize his stealing?
# Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can steal
# without alerting the security system.


def house_thief(n, arr):

    def rec(index):

        if index >= len(arr):
            return 0

        from_current_house = arr[index] + rec(index+2)
        from_next_house = rec(index+1)

        max_profit = max(from_current_house, from_next_house)
        return max_profit

    return rec(0)

# Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’.
# ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of
# letters is preserved too.

def find_SI(m, n, p):

    def rec(i, j, k):

        if k == len(p):
            return i == len(m) and j == len(n)

        if k == len(p):
            return False

        b1, b2 = False, False

        if i < len(m) and m[i] == p[k]:
            b1 = rec(i+1, j, k+1)
        if j < len(n) and n[j] == p[k]:
            b2 = rec(i, j+1, k+1)

        return b1 or b2

    return rec(0, 0, 0)


def find_min_operations(s1, s2):

    def rec(i1, i2):
        if i1 == len(s1):
            return len(s2) - i2

        if i2 == len(s2):
            return len(s1) - i1

        c1 = max(len(s1), len(s2))

        if s1[i1] == s2[i2]:
            c1 = rec(i1+1, i2+1)

        c2 = rec(i1, i2+1)
        c3 = rec(i1+1, i2)
        c4 = rec(i1+1, i2+1)

        return min(c1, 1 + min(c2, c3, c4))
    return rec(0, 0)


# Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
# A subsequence is considered alternating if its elements are in alternating order.
def find_LAS_length(nums):

    def rec(prev, cur, is_increasing):

        if cur == len(nums):
            return 0
        c1, c2 = 0, 0
        if is_increasing:
            if prev == -1 or nums[cur] > nums[prev]:
                c1 = 1 + rec(cur, cur+1, not is_increasing)
        else:
            if prev == -1 or nums[cur] > nums[prev]:
                c1 = 1 + rec(cur, cur+1, not is_increasing)

        c2 = rec(prev, cur+1, is_increasing)
        return max(c1, c2)

    return max(rec(-1, 0, True), rec(-1, 0, True))

def equal_subset_sum(s, nums):

    remaining_sum = sum(nums)//2

    def rec(remaining_sum, idx):
        if idx == len(nums):
            return True

    return rec(remaining_sum, 0)

if __name__ == "__main__":
    n = 4
    # dp = [0, 1, 1] + [-1] * (n+1)
    # start_time = time.time()
    # print(fib2(n))
    # print(time.time() - start_time)

    # print(count_steps(5))
    # jumps = [1, 3, 5, 1 , 2]
    # print(min_jumps(jumps))
    #

    # print(minimum_fee(4, [2, 3, 4, 5]))
    # print(house_thief(5, [2, 10, 14, 8, 1]))
    # print(house_thief(5, [2, 5, 1, 3, 6, 2, 4]))

    # print(find_SI("abd", "cef", "abcdef"))
    # print(find_SI("abd", "cef", "adcbef"))
    # print(find_SI("abc", "def", "abdccf"))
    # print(find_SI("abcdef", "mnop", "mnaobcdepf"))

    # print(find_min_operations("bat", "but"))
    # print(find_min_operations("abdca", "cbda"))
    # print(find_min_operations("passpot", "ppsspqrt"))


    print(find_LAS_length([1, 2, 3, 4]))
    print(find_LAS_length([3, 2, 1, 4]))
    print(find_LAS_length([1, 3, 2, 4]))