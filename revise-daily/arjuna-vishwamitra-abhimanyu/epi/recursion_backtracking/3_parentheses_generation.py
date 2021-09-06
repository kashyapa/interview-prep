class BalancedParentheses:
    def __init__(self, lcount, rcount, str):
        self.lcount = lcount
        self.rcount = rcount
        self.str = str

from imports import *


def generate_parentheses(n):

    queue = deque([BalancedParentheses(0, 0, "")])
    res = []
    while queue:
        bp = queue.popleft()

        if bp.lcount == bp.rcount:
            res.append(bp.str)
        elif bp.lcount < n:
            queue.append(BalancedParentheses(bp.lcount+1, bp.rcount, bp.str + "("))
        else:
            queue.append(BalancedParentheses(bp.lcount, bp.rcount+1, bp.str + ")"))
    return res
