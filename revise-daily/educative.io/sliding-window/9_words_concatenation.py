from collections import Counter


def find_word_concatenation(str1, words):
    if not str1 or not words:
        return []
    word_size = len(words[0])
    word_count = len(words)
    result = []
    total_size = word_count * word_size
    for i in range(len(str1) - total_size + 1):
        j = i
        words_to_be_covered = word_count
        words_count = Counter(words)
        while True:
            substr = str1[j: j + word_size]
            if words_count[substr] > 0:
                words_count[substr] -= 1
                if words_count[substr] >= 0:
                    words_to_be_covered -= 1

                if words_to_be_covered == 0:
                    result.append(i)
                j += word_size
            else:
                break
    return result


if __name__ == '__main__':
    print(find_word_concatenation("wordgoodgoodgoodbestword", ["word","good","best","good"]))
