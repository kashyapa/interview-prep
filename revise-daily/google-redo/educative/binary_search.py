def find_key_in_sorted_array(nums, key)

    ascending = True

    if len(nums) > 1 and  nums[0] > nums[1]:
        ascending = False
    l, r = 0, len(nums)-1
    while l <= r:
        m = l + (r-l)//2
        if key == nums[m]:
            return m
        if ascending:
            if key > nums[m]:
                l = m+1
            else:
                r = m-1
        else:
            if key < nums[m]:
                l = m+1
            else:
                r = m-1
    return l

def search_next_letter(letters, key):

    l, r = 0, len(letters)-1

    while l <= r:
        m = l + (r-l) // 2

        if letters[m] == key:
            return letters[(m+1) % len(letters)]

        elif letters[m] > key:
            r = m-1
        else:
            l = m+1
    return letters[l % len(letters)]

def number_range(nums, key, find_higher):

    l, r = 0, len(nums)-1
    last_seen_index = -1
    while l <= r:
        m = l+(r-l)//2

        if nums[m] == key:
            last_seen_index = m
            if find_higher:
                l = m+1
            else:
                r = m-1
        elif nums[m] > key:
            r = m-1
        else:
            l= m+1

    return last_seen_index

import math


def search_in_sorted_infinite_array(nums, key):

    l, r = 0, 1

    def binary_search(l, r):
        while l <= r:
            m = l+ (r-l)//2
            if key < nums[m] or nums[m] == math.inf:
                r = m-1
            elif key > nums[m]:
                l = m+1
            else:
                return m
        return l

    while nums[r] < key and nums[r] != math.inf:
        r = r * 2

    return binary_search(r // 2, r)

def minimum_difference_element(nums, key):

    last_seen_closest_index = -1

    l, r = 0, len(nums)-1
    diff = math.inf
    while l <= r:
        m = l + (r-l) // 2

        if nums[m] == key:
            return m
        elif nums[m] > key:
            r = m-1
        else:
            l = m+1

        if abs(nums[m]-key) < diff:
            last_seen_closest_index = m
            diff = abs(nums[m]-key)

    return last_seen_closest_index

def find_max_in_bitonic_array(arr):

    l, r = 0, len(arr)-1

    while l < r:
        m = l + (r-l) // 2

        if arr[m] < arr[m+1]:
            l = m+1
        else:
            r = m
    return arr[l]


def search_bitonic_array(nums, key):

    def find_peak_index(nums):
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l) // 2

            if nums[m] < nums[m+1]:
                l = m+1
            elif nums[m]>nums[m+1]:
                r = m
        return l

    def binary_search(nums, start, end):

        while start <= end:
            m = start + (end-start)//2

            if nums[m] == key:
                return m
            if nums[start] < nums[end]:
                if nums[m] > key:
                    end = m-1
                else:
                    start = m+1
            else:
                if nums[m]< key:
                    start = m+1
                else:
                    end = m-1
        return -1


    idx = find_peak_index(nums)

    i = binary_search(nums, 0, idx)
    if i == -1:
        return binary_search(nums, idx+1, len(nums-1))

def search_rotated_array(nums, key):

    l, r = 0, len(nums)-1

    while l <= r:
        m = l + (r-l)//2

        if nums[m] == key:
            return m

        if nums[m] > nums[l]:
            if nums[m] > key >= nums[l]:
                r = m-1
            else:
                l = m+1
        else:
            if nums[m] < key <= nums[r]:
                l = m+1
            else:
                r = m-1
    return -1


def rotation_count(nums):

    l, r = 0, len(nums)-1
    count = 0

    while l < r:
        m = l + (r-l)//2

        if nums[l] < nums[r]:
            return l
        if nums[m] > nums[l]:
            l = m+1
        else:
            r = m
        count = l
    return count+1


def rotation_count2(nums):
    l, r = 0, len(nums)-1
    count = 0

    while l < r:

        m = l + (r-l)//2

        if nums[l] < nums[r]:
            return l
        elif nums[m] > nums[l]:
            l = m+1
        else:
            r = m
        count = l
    return count


