class BalancedParentheses:
    def ___init__(self, lcount, rcount, str):
        self.lcount = lcount
        self.rcount = rcount
        self.str =str

import collections
def generate_parentheses(n):
    res =[]
    queue = collections.deque([])
    queue.append(BalancedParentheses(0, 0, ""))

    while queue:
        p = queue.popleft()

        if p.lcount == n and p.rcount ==n:
            res.append(p.str)
            continue

        if p.lcount < n:
            queue.append(BalancedParentheses(p.lcount+1, p.rcount, p.str + "("))

        if p.rcount < p.lcount:
            queue.append(BalancedParentheses(p.lcount, p.rcount+1, p.str+")"))

    return res