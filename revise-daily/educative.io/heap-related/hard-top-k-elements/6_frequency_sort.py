# Given a string, sort it based on the decreasing frequency of its characters.

from collections import Counter
from heapq import *


def sort_character_by_frequency(str):
    char_frequency = Counter(str)
    max_heap = []

    for k, v in char_frequency.items():
        heappush(max_heap, (-v, k))

    result = []

    while max_heap:
        count, c = heappop(max_heap)
        for i in range(-count):
            result.append(c)

    return ''.join(result)


def main():

    print("String after sorting characters by frequency: " + sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " + sort_character_by_frequency("abcbab"))


if __name__ == "__main__":
    main()