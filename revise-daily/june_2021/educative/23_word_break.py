def word_break(str, words):

    def rec(idx):
        if idx == len(str):
            return True
        for w in words:
            if idx+len(w) <= len(str):
                if str[idx: idx+len(w)] == w:
                    return rec(idx+len(w))
        return False
    return rec(0)

print(word_break("leetcode", ["leet", "code"]))