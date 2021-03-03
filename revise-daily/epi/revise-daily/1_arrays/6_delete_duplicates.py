def delete_duplicates(arr):
    w = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[w] = arr[i-1]
            w += 1
    return w



def delete_dups(arr):

    write_index = 1
    for i in range(1, len(arr)):

        if arr[i] != arr[write_index-1]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]


if __name__ == '__main__':
    print(delete_duplicates([2, 3, 5, 5 ,5 ,7 , 11, 11, 13]))
    print(delete_dups([2, 3, 5, 5 ,5 ,7 , 11, 11, 13]))