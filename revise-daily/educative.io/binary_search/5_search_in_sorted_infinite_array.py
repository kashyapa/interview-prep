import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    index = 1
    while reader.get(index) < key and reader.get(index) != math.inf:
        index = index * 2

    return binary_search(reader, key, index//2, index)


def binary_search(reader, key, start, end):

    l, r = start, end

    while l <= r:
        m = l + (r-l)//2
        if key < reader.get(m) or reader.get(m) == math.inf:
            r = m - 1
        elif key > reader.get(m):
            l = m + 1
        else:
            return m
    return l


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


if __name__ == "__main__":
    main()
