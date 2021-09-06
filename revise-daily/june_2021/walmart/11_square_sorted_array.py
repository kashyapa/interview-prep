def make_squares(nums):
    squares = [0] * len(nums)
    w_index = len(squares) - 1
    left, right = 0, len(nums) - 1

    while left < right:
        l_squared = nums[left] * nums[left]
        r_squared = nums[right] * nums[right]

        if l_squared > r_squared:
            squares[w_index] = l_squared
            left += 1
        else:
            squares[w_index] = r_squared
            right -= 1
        w_index += 1

    return squares
