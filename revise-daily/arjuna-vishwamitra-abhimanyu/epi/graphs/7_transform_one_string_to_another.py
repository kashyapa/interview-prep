from imports import *
import string

class StringWithDistance:

    def __init__(self, str, distance):
        self.str = str
        self.distance = distance


def transform_one_string_to_another(src, dest, word_set):
    min_distance = inf
    queue = deque([StringWithDistance(src, 0)])
    while queue:

        p = queue.popleft()

        if p.str == dest:
            min_distance = min(min_distance, p.distance)

        for i, c in enumerate(p.str):
            for next_char in string.ascii_lowercase:
                next_word = p.str[:i] + next_char + p.str[i+1:]
                if next_word in word_set:
                    queue.append(StringWithDistance(next_word, p.distance+1))
                    word_set.remove(next_word)
    return -1
