from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):

    def rec(start, end):

        if start > end:
            return 0
        res = []
        for i in range(start, end):
            left_trees = rec(start, i-1)
            right_trees = rec(i+1, end)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
    return rec(0, n)


class Parentheses:
    def __init__(self, lcount, rcount, str):
        self.lcount = lcount
        self.rcount = rcount
        self.str = str


def balanced_parentheses(n):

    queue = deque([Parentheses(0, 0, "")])
    res = []
    while queue:

        p = queue.popleft()
        if p.lcount == p.rcount:
            res.append(p.str)

        if p.lcount < n:
            queue.append(Parentheses(p.lcount+1, p.rcount, p.str + "("))
        if p.rcount < p.lcount:
            queue.append(Parentheses(p.lcount, p.rcount + 1, str + ")"))

    return


def letter_case_permutation(str):

    perms = []
    perms.append(str)

    for i in range(len(str)):

        if str[i].isalpha():
            n = len(perms)
            for j in range(n):
                new_p = list(perms[j])
                new_p[i] = new_p[i].swapcase()
                perms.append(''.join(new_p))
    return perms


def permutations(str):
    perms = deque([])
    res = []
    for i in range(len(str)):

        n = len(perms)
        for _ in range(n):
            cur_item = perms.popleft()

            for j in range(len(cur_item)+1):
                next_perm = list(cur_item)
                next_perm.insert(j, str[i])
                if len(next_perm) == len(str):
                    res.append(next_perm)
                else:
                    perms.append(next_perm)
    return res
