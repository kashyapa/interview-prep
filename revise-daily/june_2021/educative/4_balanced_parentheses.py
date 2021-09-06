class BalancedParentheses:
    def __init__(self, str, lc, rc):
        self.str = ""
        self.l_count = lc
        self.r_count = rc

import collections


def balanced_parentheses(n):
    queue = collections.deque([(BalancedParentheses("", 0, 0))])
    res = []

    while queue:
        p = queue.popleft()

        if p.l_count == p.r_count:
            res.append(p.str)
        if p.l_count < n:
            queue.append(BalancedParentheses(p.str + "(", p.l_count+1, p.r_count))
        if p.r_count < p.l_count:
            queue.append(BalancedParentheses(p.str+")", p.l_count, p.r_count+1))

    return res
