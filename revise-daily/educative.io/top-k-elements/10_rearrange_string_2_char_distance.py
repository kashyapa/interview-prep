# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.

from collections import Counter
from heapq import *


def rearrange_string(str):
    max_heap = []
    previous_char, previous_frequency = None, 0

    char_frequency = Counter(str)

    for char, frequency in char_frequency.items():
        heappush(max_heap, (-frequency, char))

    result_string = []
    while max_heap:

        frequency, char = heappop(max_heap)

        if previous_char and -previous_frequency > 0:
            heappush(max_heap, (previous_frequency, previous_char))

        result_string.append(char)
        previous_char = char
        previous_frequency = frequency + 1

    return ''.join(result_string) if len(result_string) == len(str) else ""


def main():
        print("Rearranged string:  " + rearrange_string("aappp"))
        print("Rearranged string:  " + rearrange_string("Programming"))
        print("Rearranged string:  " + rearrange_string("aapa"))


if __name__ == "__main__":
    main()
