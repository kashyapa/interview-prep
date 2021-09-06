def triplet_sum_to_zero(nums):

# go to the extreme

    def find_pair_sum(start, target):
        end = len(nums)-1
        res = []
        while start < end:
            pair_sum = nums[start] + nums[end]
            if pair_sum == target:
                res.append((start, end))
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1

            elif pair_sum > target:
                end -= 1
            else:
                start += 1
        return None

    nums.sort()
    results = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            res = find_pair_sum(i+1, -nums[i])
            if res:
                results.append((res[0], res[1]))
    return results
