from heapq import *


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
