def remove_element(arr, key):
    write_index = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]


if __name__ == '__main__':
    print(remove_element([3, 5, 3, 545, 3, 452, 3, 6547, 3, 3, 2, 3], 3))
