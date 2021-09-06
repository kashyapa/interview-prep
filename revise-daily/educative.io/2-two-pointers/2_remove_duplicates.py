def remove_duplicates(arr):
    write_index = 0
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[write_index-1]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index


def remove_dups(nums):
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_dups([2, 3, 3, 3, 6, 9, 9]))
    print(remove_dups([2, 2, 2, 11]))


if __name__ == '__main__':
    main()
