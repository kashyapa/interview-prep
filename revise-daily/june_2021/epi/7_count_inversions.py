def count_inversions(nums):

    def count_inversion(nums, start, end):
        def merged_arr_inversion_count(nums, start, mid, end):
            inversion_count = 0
            l = start
            l1 = mid
            r = end

            sorted_array = []
            while l < mid and l1 < r:
                if nums[l] > nums[l1]:
                    inversion_count += mid-l
                    sorted_array.append(nums[l1])
                    l1 += 1
                else:
                    sorted_array.append(nums[l])
                    l += 1
            nums[start:end] = sorted_array + nums[l:mid] + nums[l1:end]
            return inversion_count

        if end - start <= 1:
            return 0
        mid = (start+end) // 2

        return count_inversion(nums, start, mid) + count_inversion(nums, mid, end) + merged_arr_inversion_count(nums, start, mid, end)
    return count_inversion(nums, 0, len(nums))


if __name__ == "__main__":
    print(count_inversions([2, 3, 3, 1, 9, 5, 6]))