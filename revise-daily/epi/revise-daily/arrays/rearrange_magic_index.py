def magic_index_rearrange():

    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] != i:
            print(f"arr[{i}]={arr[i]} , arr[{arr[i]}] = {arr[arr[i]]}")
            print(arr)
            p = arr[arr[i]]

            arr[arr[i]] = arr[i]
            arr[i] = p

            print(arr)
        else:
            i += 1


if __name__ == "__main__":
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(f"arr[{i}]={arr[i]}" for i in range(len(arr)))
    magic_index_rearrange()
    print(arr)
