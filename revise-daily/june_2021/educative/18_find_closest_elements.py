def find_closest_elements(nums, key, k):

    def binary_search(nums, key):

        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left) // 2

        return left

    res = []

    idx = binary_search(nums, key)
    left, right = idx, idx+1
    for _ in range(k):
        if left >= 0 and right < len(nums):
            num1, num2 = nums[left], nums[right]
            diff1, diff2 = abs(num1-key), abs(num2-key)
            if diff1 > diff2:
                res.append(num2)
                right += 1
            else:
                res.append(num1)
                left -= 1
        elif left >= 0:
            res.append(nums[left])
            left -= 1
        else:
            res.append(nums[right])
            right += 1