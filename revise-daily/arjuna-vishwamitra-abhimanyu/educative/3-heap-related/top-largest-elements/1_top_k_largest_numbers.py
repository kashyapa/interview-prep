import random

def top_k_largest_numbers(nums, k):
    start, end = 0, len(nums)-1

    def partition(nums, start, end, pivot_idx):
        pivot = nums[pivot_idx]
        #nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
        smaller, equal, larger = start, start, end

        while equal < larger:
            if nums[equal] < pivot:
                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                smaller += 1
                equal += 1
            elif nums[equal] > pivot:
                nums[larger], nums[equal] = nums[equal], nums[larger]
                larger -= 1
            else:
                equal += 1
        return equal

    while start < end:
        pivot_idx = random.randrange(start, end)
        pivot_idx = partition(nums, start, end, pivot_idx)
        if pivot_idx == k-1:
            break
        elif pivot_idx > k-1:
            end = pivot_idx-1
        else:
            start = pivot_idx+1
    return nums[:k]


from imports import *


def top_k_largest(nums, k):
    min_heap = []

    for i in range(len(nums)):
        if i <= k-1:
            heappush(min_heap, nums[i])
        else:
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap)
    return min_heap
