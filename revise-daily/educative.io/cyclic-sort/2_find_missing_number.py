# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’
# numbers out of the total ‘n+1’ numbers, find the missing number.
#
# Example 1:
#
# Input: [4, 0, 3, 1]
# Output: 2


def find_missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i+1 and nums[i] > 0:
            actual_index = nums[i]-1
            nums[i], nums[actual_index] = nums[actual_index], nums[i]

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1

    return len(nums)


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


if __name__ == "__main__":
    main()
