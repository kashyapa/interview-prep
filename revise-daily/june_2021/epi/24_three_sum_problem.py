def three_sum_problem(nums, target):
    nums.sort()

    def two_sum(nums, i, t1):

        j = i+1
        k = len(nums) - 1

        while j < k:
            if nums[j] + nums[k] == t1:
                return nums[j], nums[k]
            elif nums[j] + nums[k] > t1:
                k -= 1
            else:
                j += 1
        return None

    three_sums = []
    for i in range(len(nums)-1):
        if i > 0 and nums[i] != nums[i-1]:
            res = two_sum(nums, i, target-nums[i])
            if res:
                three_sums.append((nums[i], three_sums[0], three_sums[1]))
    return res