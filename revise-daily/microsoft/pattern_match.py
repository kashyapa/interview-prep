"""
match(pattern, input) bool

match("ab", "ab") -> true
match("ab", "abc") -> false
match("ab*", "abc") -> true
match("ab*d", "abcdcd") -> true
match("ab*d", "abcd") -> true
match("ab*d", "abcde") -> false
match("ab*cd*ef", "ab__cd___ef") -> true
match("ab*cd*ef", "ab__cd___e") -> false



"""

def match(str, pattern):
    i, j = len(str)-1, len(pattern)-1
    while i > 0 and j > 0:
        if pattern[j] != "*" and pattern[j] != str[i]:
            return False

        i -= 1
        j -= 1

        if pattern[j] == "*":
            while i != j:
                i -= 1

    return i == 0 and j == 0


#
# pat = dab*d
# str = dabcccdf
#
#
# startswith()

# if we reach end of string in str but not end of string in pat, then return false
# if any character before the *, does not match during character comparisons, we return false


# def match(str, pat):
    #
    # def rec(si, pi):
    #
    #     if si == len(str) and pi == len(pat):
    #         return True
    #
    #     if si == len(str):
    #         return False
    #
    #     if str[si] == pat[pi]:
    #         if rec(si+1, pi+1):
    #             return True
    #
    #     if pi+1 < len(pat) and pat[pi+1] == "*":
    #         if str[si] == pat[pi]:
    #             si += 1
    #             print("matched until *")
    #             while si < len(str) and pi+2 < len(pat) and str[si] != pat[pi+2]:
    #                 si += 1
    #             pi = pi + 2
    #             if pi < len(pat) and si < len(str) and str[si] == pat[pi]:
    #                 if rec(si+1, pi+1):
    #                     return True
    #             else:
    #                 return False
    #     return False
    #
    # return rec(0, 0)



if __name__ == "__main__":
    print(match("dabcccd", "dab*d"))
    print(match("ab*cd*ef", "ab__cd___e"))
    print(match("ab*cd*ef", "ab__cd___ef"))