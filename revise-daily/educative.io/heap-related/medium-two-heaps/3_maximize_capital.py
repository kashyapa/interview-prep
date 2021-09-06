from heapq import *


# Given a set of investment projects with their respective profits, we need to find the most profitable projects.
# We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose
# projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the
# most profitable projects.
#
# We can start an investment project only when we have the required capital. Once a project is selected, we can assume
# that its profit has become our capital.

#
#
"""

 1. push (capital[i], i) to min heap
 2.     capital, i --- pop out all items in min heap whose capital value is less than available capital
 3.     push profit[i] to maxheap
        repeat 2 and 3 until capital[i] < available_capital
 4. available_capital += profit[i]
 

"""


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    max_heap = []
    min_heap = []

    for i in range(numberOfProjects):
        heappush(min_heap, (capital[i], i))

    available_capital = initialCapital
    for _ in range(numberOfProjects):

        while len(min_heap) > 0 and min_heap[0][0] <= available_capital:
            capital, i = heappop(min_heap)
            heappush(max_heap, (-profits[i], i))

        available_capital += -heappop(max_heap)[0]
    return available_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


if __name__ == "__main__":
    main()
