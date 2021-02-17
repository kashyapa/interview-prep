import math


def find_closest_repeated_entries(paragraph):

    word_index_map = {}
    min_length = math.inf
    for i, word in enumerate(paragraph):
        if word in word_index_map:
            last_index = word_index_map[word]
            if i - last_index < min_length:
                min_length = i - last_index
        word_index_map[word] = i

    print(word_index_map)
    return min_length


if __name__ == '__main__':
    print(find_closest_repeated_entries(["this", "is", "test", "this", "what", "are", "you", "upto", "you"]))

