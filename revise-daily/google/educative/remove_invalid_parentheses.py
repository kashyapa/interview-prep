from collections import deque

def remove_invalid_parentheses(str):

    def is_valid(s):
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
                if count < 0:
                    return False

        return count == 0



    res = []
    queue = deque([str])
    found = False
    visited = set()

    while queue:
        s = queue.popleft()

        if is_valid(s):
            found = True

        if found:
            res.append(s)
            continue

        for i in range(len(s)):

            if s[i] != "(" and s[i] != ")":
                continue

            next_try = s[:i] + s[i+1:]
            if next_try not in (visited, queue):
                queue.append(next_try)
                visited.add(next_try)
    return res
