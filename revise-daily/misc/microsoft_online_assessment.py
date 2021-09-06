import string
from collections import defaultdict


# write your code in Python 3.6
import string
import math
from collections import defaultdict
def solution(s):
    # write your code in Python 3.6
    seen_chars = defaultdict(int)
    min_length = math.inf
    balanced_characters = 0
    l = 0
    for i, c in enumerate(s):
        if ((c in string.ascii_uppercase and c.lower() in s) or (c in string.ascii_lowercase and c.upper() in s)):
            seen_chars[c] += 1
            balanced_characters += 1
        else:
            while l < i and balanced_characters > 0:
                p = s[l]
                min_length = min(i - l + 1, min_length)
                if (p.islower() and p.upper() in seen_chars) or (p.isupper() and p.lower() in seen_chars):
                    seen_chars[c] -= 1
                    if seen_chars[c] == 0:
                        del seen_chars[c]
                        balanced_characters -= 1
                l += 1
    return min_length





# def subset_sum(A):
#
#     def rec(i, sum):
#         if sum == 0:
#             return 1
#         if i >= len(A):
#             return 0
#
#         with_num = rec(i+1, sum+A[i])
#
#         without_num = rec(i+1, sum)
#
#         return with_num + without_num
#
#     return rec(1, A[0])
#
if __name__ == "__main__":
    print(solution("azABaabza"))