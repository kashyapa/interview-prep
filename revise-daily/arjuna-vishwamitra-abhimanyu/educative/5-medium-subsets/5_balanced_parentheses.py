class Parentheses:
    def __init__(self, lcount, rcount, str):
        self.lcount = lcount
        self.rcount = rcount
        self.str = str

from imports import *


def generate_balanced_parentheses(n):
    queue = deque([Parentheses(0, 0 , "")])
    res = []

    while queue:

        p = queue.popleft()
        if p.lcount == p.rcount:
            res.append(p.str)
        else:

            if p.lcount < n:
                queue.append(Parentheses(p.lcount+1, p.rcount, p.str+'('))

            if p.lcount > p.rcount:
                queue.append(Parentheses(
                    p.lcount, p.rcount+1, p.str + ")"
                ))
    return res
