# Find the Smallest Missing Positive Number (medium) #
# Given an unsorted array containing numbers, find the smallest missing positive number in it.
#
# Example 1:
#
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:
#
# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:
#
# Input: [3, 2, 5, 1]
# Output: 4

def find_first_smallest_missing_positive(nums):
    i = 0
    while i < len(nums):
        adjusted_index = nums[i] - 1
        if len(nums) >= nums[i] > 0 and nums[i] != nums[adjusted_index]:
            nums[i], nums[adjusted_index] = nums[adjusted_index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums) + 1


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))


if __name__ == "__main__":
    main()
