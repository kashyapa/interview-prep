def delete_duplicates(arr):
    w = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[w] = arr[i-1]
            w += 1
    return w


if __name__ == '__main__':
    print(delete_duplicates([2, 3, 5, 5 ,5 ,7 , 11, 11, 13]))