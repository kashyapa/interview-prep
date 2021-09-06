def square_sorted_array(nums):
    res = [-1] * len(nums)
    start, end = 0, len(nums)-1
    idx = 0
    while start < end:
        left_square = nums[start] * nums[start]
        right_square = nums[end] * nums[end]

        if left_square < right_square:
            res[idx] = left_square
            start += 1
        else:
            res[idx] = right_square
            end -= 1

        idx += 1
    return res
