def contiguous_longest_subarray(nums):
    def rec(cur_idx, count):
        if cur_idx == len(nums):
            return count
        c1 = 0
        if cur_idx == 0 or nums[cur_idx] > nums[cur_idx - 1]:
            return rec(cur_idx + 1, count + 1)
        else:
            c1 = rec(cur_idx + 1, 1)
        return max(c1, count)

    return rec(0, 0)


def longest_contiguous_subsequence(nums):
    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count if len(nums) > 0 else 0


if __name__ == "__main__":
    print(contiguous_longest_subarray([1, 4, 2, 5, 7, 5, 9, 10]))
