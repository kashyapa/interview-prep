def count_inversion(nums):
    def count_inversion_subarray(l, r):

        def merge_sorted_count_inversions(l, m, r):
            sorted_A = []
            left_start, right_start, inversion_count = l, m, 0

            while left_start < m and right_start < r:

                if nums[left_start] >= nums[right_start]:
                    inversion_count += m - left_start
                    sorted_A.append(nums[right_start])
                    right_start += 1
                else:
                    sorted_A.append(nums[left_start])
                    left_start += 1
            nums[l:r] = sorted_A + nums[left_start:m] + nums[right_start:r]
            return inversion_count

        if r - l <= 1:
            return 0

        m = l + (r-l)//2
        return count_inversion_subarray(l, m) + count_inversion_subarray(m, r) + merge_sorted_count_inversions(l, m, r)

    return count_inversion_subarray(0, len(nums))


if __name__ == "__main__":
    print(count_inversion([1, 7, 3, 23, 6, 2, 8, 4]))
