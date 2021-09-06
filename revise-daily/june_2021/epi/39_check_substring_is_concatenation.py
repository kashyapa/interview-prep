import collections


def substring_concatenation_of_words(str, words):
    unit_size = len(words[0])
    num_of_words = len(words)
    res = []

    for i in range(len(str) - num_of_words * unit_size + 1):
        if str[i:i + unit_size] in words:
            j = i
            word_count = collections.Counter(words)
            keywords_remaining = len(words)
            while True:
                word_count[str[j:j+unit_size]] -= 1
                if word_count[str[j:j+unit_size]] < 0:
                    return False
                else:
                    keywords_remaining -= 1
                if keywords_remaining == 0:
                    res.append(i)
                j += unit_size
    return res
