from heapq import *
from collections import defaultdict


class Element:

    def __init__(self, sequence_number, freq_count, ch):
        self.sequence_number = sequence_number
        self.freq_count = freq_count
        self.ch = ch

    def __lt__(self, other):
        if self.freq_count != other.freq_cout:
            return self.freq_count < other.freq_cout
        return self.sequence_number < other.sequence_number


class FrequencyStack:

    def __init__(self):
        self.freq_map = defaultdict(int)
        self.stack = []
        self.sequence_number = 0

    def push(self, num):
        self.freq_map[num] += 1
        self.sequence_number += 1
        heappush(self.stack, Element(self.sequence_number, -self.freq_map[num], num))

    def pop(self):
        elem = heappop(self.stack)
        self.freq_map[elem.ch] -= 1
        if self.freq_map[elem.ch] == 0:
            del self.freq_map[elem.ch]
        return elem.ch