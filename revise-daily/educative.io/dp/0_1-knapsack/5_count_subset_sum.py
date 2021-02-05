# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

def count_subsets_equal_to_s(nums, s):
    return count_subsets_equal_to_s_rec(nums, s, 0)


def count_subsets_equal_to_s_rec(nums, sum, index):
    if sum == 0:
        return 1

    if len(nums) == 0 or index >= len(nums):
        return 0

    count_with_num, count_without_num = 0, 0

    if sum >= nums[index]:
        count_with_num = count_subsets_equal_to_s_rec(nums, sum - nums[index], index + 1)
    count_without_num = count_subsets_equal_to_s_rec(nums, sum, index + 1)

    return count_with_num + count_without_num


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


if __name__ == "__main__":
    main()
