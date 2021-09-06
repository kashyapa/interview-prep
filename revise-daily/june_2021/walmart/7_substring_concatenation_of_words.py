from collections import Counter


def substring_concatenation_of_words(str, words):

    unit_size = len(words[0])
    for i in range(len(str) - len(words)*unit_size + 1):
        if str[i:i +unit_size] in words:
            j = i
            keyword_count = len(words)
            words_counter = Counter(words)

            while True:
                substr = str[j: j+unit_size]
                if words_counter[substr] > 0:
                    words_counter[substr] -= 1
                    keyword_count -= 1
                    if keyword_count == 0:
                        return i
                    j += unit_size
                else:
                    break
    return -1

