# rearrange numbers so that the numbers in array are sorted alternatedly


def rearrange(arr):
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=bool(i % 2))

    print(arr)
    return arr


if __name__ == "__main__":
    rearrange([1,32,43,123,465, 243, 32, 44])