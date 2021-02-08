# Given a number sequence, find the increasing subsequence with the highest sum.
# Write a method that returns the highest sum.

# Input: {4,1,2,6,10,1,12}
# Output: 32
# Explanation: The increaseing sequence is {4,6,10,12}.
# Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.

def find_MSIS(arr):
    return find_MSIS_rec(arr, 0, 0)

def find_MSIS_rec(arr, i, sum):


def main():
    print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))


main()
