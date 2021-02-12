# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates,
# which means some numbers will be missing. Find all those missing numbers.

# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.


def find_missing_numbers(nums):
    i = 0
    while i < len(nums):



def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


if __name__ == "__main__":
    main()
