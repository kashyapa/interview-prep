from collections import deque


class Parentheses:

    def __init__(self, s, lcount, rcount):
        self.parentheses = s
        self.l_count = lcount
        self.r_count = rcount


def balanced_parentheses(n):
    p = deque()
    p.append(Parentheses("", 0, 0))
    res = []
    while p:
        s = p.popleft()
        if s.l_count == n and s.r_count == n:
            res.append(s.parentheses)
        else:
            if s.l_count < n:
                p.append(Parentheses(s.parentheses + "(", s.l_count+1, s.r_count))

            if s.l_count > s.r_count:
                p.append(Parentheses(s.parentheses + ")", s.l_count, s.r_count+1))

    return res


if __name__ == '__main__':
    print(balanced_parentheses(2))
    print(balanced_parentheses(6))
