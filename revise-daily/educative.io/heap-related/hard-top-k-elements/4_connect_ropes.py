# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
# The cost of connecting two ropes is equal to the sum of their lengths.


# Input: [1, 3, 11, 5]
# Output: 33
# Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result, temp = 0, 0

    min_heap = []
    for i in range(len(ropeLengths)):
        heappush(min_heap, ropeLengths[i])

    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)

    return heappop(min_heap)
