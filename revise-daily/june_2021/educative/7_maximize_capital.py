from heapq import *


def maximize_capital(capitals, profits, number_of_projects, initial_capital):
    min_heap = []
    max_heap = []

    for i in range(len(capitals)):
        heappush(min_heap, (capitals[i], i))

    available_capital = initial_capital
    for _ in range(number_of_projects):
        while min_heap and min_heap[0][0] <= available_capital:
            capital, idx = heappop(min_heap)
            heappush(max_heap, -profits[idx])

        available_capital += -(max_heap.pop())
    return available_capital

