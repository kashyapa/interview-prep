def delete_duplicates(arr):
    w = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[w-1]:
            arr[w] = arr[i]
            w += 1
    return w