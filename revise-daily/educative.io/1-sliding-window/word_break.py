from collections import Counter

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
