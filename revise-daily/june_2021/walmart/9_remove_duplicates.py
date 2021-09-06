def remove_dups(nums):

    w_index = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            nums[w_index] = nums[i]
            w_index += 1
    return nums[:w_index]


def main():
    # print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    # print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_dups([2, 3, 3, 3, 6, 9, 9]))
    print(remove_dups([2, 2, 2, 11]))


if __name__ == '__main__':
    main()
