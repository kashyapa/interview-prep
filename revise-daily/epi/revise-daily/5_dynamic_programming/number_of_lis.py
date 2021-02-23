class NumberOfLis(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1:
            return N
        lengths = [0] * N  # lengths[i] = longest ending in nums[i]
        counts = [1] * N  # count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


if __name__ == "__main__":
    number_of_lis = NumberOfLis()
    nums = [1,3,5,4,7]
    number_of_lis.findNumberOfLIS(nums)