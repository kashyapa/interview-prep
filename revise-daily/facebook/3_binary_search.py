######################################################################################################################################################
#
#                Binary Search
#
#######################################################################################################################################################


def rotation_count(nums):
    l, r = 0, len(nums) - 1

    if nums[l] < nums[r]:
        return 0

    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]:
            return m + 1

        elif nums[m] > nums[l]:
            l = m + 1
        else:
            r = m - 1
    return l


def search_number_range(nums, k):
    def binary_search1(nums, k, increasing):
        last_idx = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > k:
                r = m - 1
            elif nums[m] < k:
                l = m + 1
            else:
                if increasing:
                    l = m + 1
                else:
                    r = m - 1
                last_idx = m
        return last_idx

    l, r = 0, len(nums) - 1
    res = [-1, -1]

    idx1 = binary_search1(nums, k, True)
    if idx1 != -1:
        idx2 = binary_search1(nums, k, False)
    res = [idx1, idx2]


def search_sorted_infinite_array(arr, target):
    l, r = 0, 0

    while arr[r] < target and arr[r] != math.inf:
        r = r * 2

    l = r // 2
    while l < r:
        m = l + (r - l) // 2
        if arr[m] == math.inf:
            r = m - 1
        elif arr[m] > K:
            r = m - 1
        else:
            l = m + 1
    return l


def search_next_letter(letters, key):
    l, r = 0, len(letters) - 1

    while l < r:
        m = l + (r - l) // 2
        if key == letters[m]:
            return letters[(m + 1) % len(letters)]

        if letters[m] > key:
            r = m - 1
        elif letters[m] < key:
            l = m + 1

    return letters[l % len(letters)]

import math

def find_element_with_minimum_difference_with_given_key(nums, key):
    
    l, r = 0, len(nums) - 1
    last_seen_idx = -1
    min_diff = math.inf
    while l < r:
        m = l + (r-l)//2
        
        if nums[m] == key:
            return m
        
        elif nums[m] > key:
            r = m - 1
        else:
            l = m + 1
        if diff > abs(nums[m]-key)
            diff = abs(nums[m]-key)
            last_seen_idx = m
    return nums[last_seen_idx]
    