# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
#
# Example 1:
#
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
#
# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0


from heapq import *
import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            if len(self.maxHeap) > len(self.minHeap) + 1:
                heappush(self.minHeap, -heappop(self.maxHeap))
            elif len(self.minHeap) > len(self.maxHeap):
                heappush(self.maxHeap, -heappop(self.minHeap))

            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    # we have even number of elements, take the average of middle two elements
                    result[i - k + 1] = -self.maxHeap[0] / \
                                        2.0 + self.minHeap[0] / 2.0
                else:  # because max-heap will have one more element than the min-heap
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                element_outside_window = nums[i - k + 1]
                if element_outside_window <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -element_outside_window)
                else:
                    self.remove(self.minHeap, element_outside_window)

        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


if __name__ == "__main__":
    main()
