import imports

def word_concatenation(str, word_list):

    unit_size = len(word_list[0])
    total_len = unit_size * len(word_list)

    for i in range(len(str)-total_len+1):

        substr = str[i:i+unit_size]
        if substr in word_list:
            j = i
            words_covered = len(word_list)
            char_counter = imports.Counter(word_list)
            while True:
                substr = str[j:j+unit_size]
                if char_counter[substr] > 0:
                    char_counter[substr] -= 1
                    if char_counter[substr] == 0:
                        words_covered -= 1
                        if words_covered == 0:
                            return True
                else:
                    break
                j += unit_size
    return False
