
# Given a set of investment projects with their respective profits, we need to find the most profitable projects.
# We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose
# projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the
# most profitable projects.
#
# We can start an investment project only when we have the required capital. Once a project is selected, we can assume
# that its profit has become our capital.

from heapq import *

def maximize_capital(profits, capitals, number_of_projects, initial_capital):
    min_heap = []
    max_heap = []

    for i in range(len(capitals)):
        heappush(min_heap, (capitals[i], i))

    available_capital = initial_capital

    for _ in range(number_of_projects):
        while len(min_heap) > 0 and min_heap[0][0] < available_capital:
            c, i = heappop(min_heap)
            heappush(max_heap, -profits[i])

        available_capital += -heappop(max_heap)[0]
    return available_capital


def max_capital(capitals, profits, number_of_projects, initial_capital):
    min_heap = []
    max_heap = []

    # push all capitals to minheap
    for i in range(len(capitals)):
        heappush(min_heap, (-capitals[i], i))

    available_capital = initial_capital

    for _ in range(number_of_projects):

        # put profits in max_heap that are coming from capitals less than available capital
        while len(min_heap) > 0 and min_heap[0][0] <= initial_capital:
            c, i = heappop(min_heap)
            heappush(max_heap, -profits[i])

        available_capital += -heappop(max_heap)
    return available_capital


# Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’
# its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.
#
# Write a function to return an array containing indices of the next interval of each input interval. If there is no
# next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

# Input: Intervals [[2,3], [3,4], [5,6]]
# Output: [1, 2, -1]

# Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6]
# having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.


def next_interval(intervals):
    start_max_heap = []
    end_max_heap = []

    for i in range(len(intervals)):
        heappush(start_max_heap, (-intervals[i][0], i))
        heappush(end_max_heap, (-intervals[i][1], i))

    n = len(intervals)
    res = [0 for x in range(n)]

    for _ in range(n):

        top_end, end_index = heappop(end_max_heap)
        res[end_index] = -1
        if -start_max_heap[0][0] > -top_end:
            top_start, start_index = heappop(start_max_heap)
            while start_max_heap and -start_max_heap[0][0] > -top_end:
                top_start, start_index = heappop(start_max_heap)

            res[end_index] = start_index
            heappush(start_max_heap, (top_start, start_index))
    return res
