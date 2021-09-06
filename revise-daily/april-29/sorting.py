from heapq import *


def find_Kth_smallest_number(nums, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    print(max_heap)
    return -max_heap[0]


def find_closest_elements(arr, K, x):
    def binary_search(arr, x):

        start, end = 0, len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                return mid

            if arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return start

    res = []
    index = binary_search(arr, x)
    left_range = index - 1
    right_range = index

    while K > 0 and left_range >= 0 and right_range < len(arr):
        if abs(x-arr[left_range]) > abs(x-arr[right_range]):
            res.append(arr[right_range])
            K -= 1
            right_range += 1
        else:
            res.append(arr[left_range])
            K -= 1
            left_range -= 1

    while K > 0:
        if left_range < 0:
            res.append(arr[right_range])
            right_range += 1
            K -= 1
        else:
            res.append(arr[left_range])
            left_range -= 1
            K -= 1
    return res


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


if __name__ == "__main__":
    main()
