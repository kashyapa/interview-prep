# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair
# consists of numbers from both the arrays.

from heapq import *


def k_pairs_with_largest_sum(nums1, nums2, k):
    min_heap = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if k > len(min_heap):
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:

                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappush(min_heap, (nums1[i] + nums2[j], i,  j))
                    heappop(min_heap)
    result = []
    for num, i, j in min_heap:
        result.append([nums1[i], nums2[j]])

    return result