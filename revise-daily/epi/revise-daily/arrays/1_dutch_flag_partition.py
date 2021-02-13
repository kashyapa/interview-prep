def dutch_flag_partition(pivot, arr):
    small = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[small] = arr[small], arr[i]
            small += 1

    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1


def dutch_flag_sort(pivot, arr):
    small, equal, large = 0, 0, len(arr) - 1
    while equal < large:
        if arr[equal] < pivot:
            arr[small], arr[equal] = arr[equal], arr[small]
            small += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            large -= 1
            arr[equal], arr[large] = arr[large], arr[equal]


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()