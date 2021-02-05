# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]


def find_subsets(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])

    start_index, end_index = 0, 0
    for i, current_num in enumerate(nums):
        start_index = 0

        if i > 0 and nums[i] == nums[i-1]:
            start_index = end_index + 1

        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


if __name__ == "__main__":
    main()
