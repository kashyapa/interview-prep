def longest_consecutive_ones_with_k_flips(nums, k):
    ones = 0
    l = 0
    longest_seq = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            ones += 1

            while i - l - ones + 1 > k:
                if nums[l] == 1:
                    ones -= 1
                l += 1
        longest_seq = max(longest_seq, i - l + 1)


def longest_consecutive_ones_with_utmost_one_flip(nums):
    last_seen_zero = -1
    l = 0
    longest_sequence = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            l = last_seen_zero + 1
            last_seen_zero = i
        longest_sequence = max(longest_sequence, i - l + 1)
    return longest_sequence

