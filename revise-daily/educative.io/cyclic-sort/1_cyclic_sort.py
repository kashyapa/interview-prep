# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’
# based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the
# object with sequence number ‘4’.
#
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra
# space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though
# each number is actually an object.

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]


def cyclic_sort(nums):
    for i in range(len(nums)):
        if nums[i] != i+1:
         while nums[i] != i+1 and nums[i+1] < len(nums):
            actual_index = nums[i] - 1
            value_at_actual_index = nums[actual_index]
            nums[actual_index] = nums[i]
            nums[i] = value_at_actual_index

    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))

if __name__ == "__main__":
    main()
