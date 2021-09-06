def longest_bitonic_sequence(nums):
    max_length = 0

    def longest_increasing_sequence(prev_index, cur_index):
        if cur_index == len(nums):
            return 0
        c1 = 0

        if prev_index == -1 or nums[cur_index] > nums[prev_index]:
            c1 = 1 + longest_increasing_sequence(cur_index, cur_index+1)
        c2 = longest_increasing_sequence(prev_index, cur_index+1)
        return max(c1, c2)

    def longest_decreasing_sequence(prev_index, cur_index):
        if cur_index < 0:
            return 0
        c1 = 0

        if prev_index == -1 or nums[cur_index] < nums[prev_index]:
            c1 = 1 + longest_decreasing_sequence(cur_index, cur_index - 1)
        c2 = longest_decreasing_sequence(prev_index, cur_index - 1)
        return max(c1, c2)

    for i in range(len(nums)):
        c1 = longest_increasing_sequence(i, -1)
        c2 = longest_decreasing_sequence(i, -1)
        max_length = max(max_length, c1+c2-1)
    return max_length


def longest_bitonic_sequence(nums):

    lds = [0] * len(nums)
    lds_rev = [0] * len(nums)

    for i in range(len(nums)):
        for j in range(i-1, -1, -1):
            if nums[i] > nums[j]:
                lds[i] = lds[j] + 1

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if  nums[j] < nums[i]:
                lds_rev[i] = lds_rev[j]+1

    max_length = 0
    for i in range(len(lds)):
        max_length = max(max_length, lds[i]+lds_rev[i]-1)