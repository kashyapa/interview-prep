from heapq import *

def maximize_capital(capitals, profits, initial_capital, number_of_projects):
    max_heap = []
    min_heap = []

    for i in range(len(capitals)):
        heappush(min_heap, (capitals[i], i))

    available_capital = initial_capital
    for _ in range(number_of_projects):

        while min_heap and min_heap[0][0] <= available_capital:
            capital, index = heappop(min_heap)
            if capital <= available_capital:
                heappush(max_heap, -profits[i])

        available_capital += (heappop(max_heap) * -1)
    return available_capital
