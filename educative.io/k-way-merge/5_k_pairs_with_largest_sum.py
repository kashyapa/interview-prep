# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair
# consists of numbers from both the arrays.

from heapq import *


def k_pairs_with_largest_sum(nums1, nums2, k):
    min_heap = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))
    result = []
    for num, i, j in heappop(min_heap):
        result.append([i, j])
