from imports import *



class SlidingWindowMedian:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums)-k+1)]
        for i in range(len(nums)):
            if not self.max_heap or -self.max_heap[0] > -nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            if len(self.max_heap) > len(self.min_heap)+1:
                heappush(self.min_heap, -heappop(self.max_heap))
            elif len(self.max_heap) < len(self.min_heap):
                heappush(self.max_heap, -heappop(self.min_heap))

            if i > k-1:
                if len(self.max_heap) == len(self.min_heap):
                    result[i-k+1] = self.max_heap[0] / 2.0 + \
                        self.min_heap[0] / 2.0
                else:
                    result[i-k+1] = self.max_heap[0] / 1.0

            element_outside_window = nums[i-k+1]
            if element_outside_window < self.max_heap[0]:
                self.remove(self.max_heap, element_outside_window)
            else:
                self.remove(self.min_heap, element_outside_window)

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq.siftdown(heap, 0, ind)


