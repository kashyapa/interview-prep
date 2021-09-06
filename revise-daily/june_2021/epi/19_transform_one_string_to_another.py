import collections
import string


def transform_one_string_to_another(words, s, t):
    queue = collections.deque([(s, 0)])

    while queue:
        p, dist = queue.popleft()

        if p == t:
            return dist

        for i in range(len(p)):
            for c in string.ascii_lowercase:
                next_word = p[:i] + c + p[i+1:]
                if next_word not in words:
                    queue.append((next_word, dist+1))
    return -1

