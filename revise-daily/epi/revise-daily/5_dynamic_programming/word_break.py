#!/usr/bin/python

def word_break(s: str, d: dict):
    def word_break_rec(offset):
        if offset == len(s):
            print("can break")
            return True

        for w in d:
            if offset + len(w) > len(s):
                continue
            if s[offset:offset + len(w)] == w:
                return word_break_rec(offset + len(w))
        print("Can't break")
        return False

    def word_break_dp():
        mem[0]=True
        for i in range(len(s)):
            if mem[i] == True:
                for w in d:
                    if i +len(w)> len(s):
                        continue
                    mem[i+len(w)] = True
        return mem[-1]

    mem = [False]*(len(s)+1)
    print(word_break_dp())
    #word_break_rec(0)

    def word_break3(str, d):

        for i in range(len(str)+1):
            first = str[:i]
            if first in d:
                second = str[i:]
                if not second or second in d or word_break3(second, d):
                    return True
        return False


if __name__ == "__main__":
    dictionary = set()
    dictionary.add("leet")
    dictionary.add("code")
    print(word_break("leetcode", dictionary))
