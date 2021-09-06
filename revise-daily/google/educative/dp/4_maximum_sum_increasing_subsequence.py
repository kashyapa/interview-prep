# Given a number sequence, find the increasing subsequence with the highest sum.
# Write a method that returns the highest sum.

def maximum_sum_increasing_subsequence(nums):

    def rec(prev_idx, cur_idx, running_sum):

        if cur_idx >= len(nums):
            return running_sum

        s1 = running_sum

        if prev_idx == -1 or nums[prev_idx] < nums[cur_idx]:
            s1 = rec(cur_idx, cur_idx+1, running_sum+nums[cur_idx])
        s2 = rec(prev_idx, cur_idx+1, running_sum)
        return max(s1, s2)
    return rec(-1, 0, 0)