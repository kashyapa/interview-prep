from imports import *


def count_min_jumps(jumps):
    return count_min_jumps_recursive(jumps, 0)


def count_min_jumps_recursive(jumps, cur_index):
    n = len(jumps)

    if cur_index == n-1:
        return 0

    if jumps[cur_index] == 0:
        return inf

    start, end = cur_index + 1, cur_index + jumps[cur_index]
    total_jumps = inf

    while start < n and start <= end:
        min_jumps = count_min_jumps_recursive(jumps, start)
        start += 1
        if min_jumps != inf:
            total_jumps = min(min_jumps + 1, total_jumps)

    return total_jumps

