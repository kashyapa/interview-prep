import array as array


def even_odd(arr2):
    next_even, next_odd = 0, len(arr2) - 1
    print(arr2)
    while next_even < next_odd:

        if arr2[next_even] % 2 == 0:
            next_even += 1
        else:
            arr2[next_even], arr2[next_odd] = arr2[next_odd], arr2[next_even]
            next_odd -= 1
    print(arr2)

    return arr2


def print_hello_world():
    print("hello world")


if __name__ == "__main__":
    arr = array.array('l')
    arr = [1, 2, 4, 5342, 45, 534, 23, 35, 5, 4, 23]
    arr = even_odd(arr)
    assert arr[4] % 2 == 0
