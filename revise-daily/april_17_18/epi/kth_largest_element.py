import random
def kth_largest_element(arr, k):

    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        larger = left
        for i in range(left, right):
            if arr[i] > pivot:
                arr[larger], arr[i] = arr[i], arr[larger]
                larger += 1
        arr[larger], arr[right] = arr[right], arr[larger]

        return larger

    l, r = 0, len(arr)-1

    while l < r:
        pivot = partition(l, r)
        if pivot == k - 1:
            return arr[pivot]
        if pivot > k-1:
            r = pivot - 1
        else:
            l = pivot + 1
    return -1


if __name__ == "__main__":

    print(kth_largest_element([8, 5, 2, 9, 5, 6, 3], 2))