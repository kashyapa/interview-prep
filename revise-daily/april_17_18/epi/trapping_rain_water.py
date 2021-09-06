import math


def trapping_water(arr):
    max_water = 0
    highest_height_seen = -math.inf
    for i in range(len(arr)):
        highest_height_seen = max(highest_height_seen, arr[i])
        max_water += highest_height_seen - arr[i]
    return max_water


def compute_max_water(heights):
    max_height_index = heights.index(max(heights))
    return trapping_water(heights[:max_height_index]) + trapping_water(heights[max_height_index + 1:])