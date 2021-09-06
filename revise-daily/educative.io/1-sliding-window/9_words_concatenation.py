from collections import Counter
import collections

# Given a string and a list of words, find all the starting indices of substrings in the given string that are a
# concatenation of all the given words exactly once without any overlapping of words. It is given that all words
# are of the same length.

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".


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
            words_count[substr] -= 1
            if words_count[substr] >= 0:
                words_to_be_covered -= 1

                if words_to_be_covered == 0:
                    result.append(i)
                    break
                j += word_size
            else:
                break
    return result


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        unit_size = len(words[0])
        res = []
        for i, c in enumerate(s):
            j = i
            char_counter = collections.Counter(words)
            keyword_count = len(char_counter)
            while True:
                if j + unit_size > len(s):
                    break
                substr = s[j: j + unit_size]
                char_counter[substr] -= 1
                if char_counter[substr] < 0:
                    break
                if char_counter[substr] == 0:
                    keyword_count -= 1
                j += unit_size
                if keyword_count == 0:
                    res.append(i)
        return res



def word_break(str, word_dict):


    counter = Counter(word_dict)
    words_to_be_covered = len(word_dict)

    for i in range(len(str)):
        for w in word_dict:
            if str[i:i+len(w)] == w:
                counter[w] -= 1
                if counter[w] == 0:
                    words_to_be_covered -= 1
                    if words_to_be_covered == 0:
                        print("found all words")
                        return True
    return False


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "leet"]))

if __name__ == '__main__':
    print(find_word_concatenation("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("barfoothefoobarman", ["foo", "bar"]))
    print(find_word_concatenation("barfoofoobarthefoobarman", ["bar","foo","the"]))
