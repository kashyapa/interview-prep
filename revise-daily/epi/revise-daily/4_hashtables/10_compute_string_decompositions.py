from collections import Counter


def is_substring_concatenation_of_words(big_string, list_of_words):
    unit_size = len(list_of_words[0])
    keywords_count = len(list_of_words)
    result = []
    for i in range(len(big_string) - unit_size * keywords_count + 1):
        keyword_counter = Counter(list_of_words)
        substr = big_string[i: i+unit_size]
        if keyword_counter[substr] > 0:
            j = i
            keywords_covered = 0
            while j < i + unit_size * keywords_count:
                substr = big_string[j: j + unit_size]
                if keyword_counter[substr] > 0:
                    keyword_counter[substr] -= 1
                    keywords_covered += 1
                else:
                    break

                if keywords_covered == len(list_of_words):
                    result.append(i)

                j += unit_size
    return result


if __name__ == '__main__':
    print(is_substring_concatenation_of_words("amanaplanacanal", ["ana", "pla"]))
    print(is_substring_concatenation_of_words("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(is_substring_concatenation_of_words("catfoxcat", ["cat", "fox"]))
    print(is_substring_concatenation_of_words("barfoothefoobarman",["foo", "bar"]))
    print(is_substring_concatenation_of_words("barfoofoobarthefoobarman", ["bar","foo","the"]))
