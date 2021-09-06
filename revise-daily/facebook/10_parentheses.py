from typing import List
from collections import deque


def removeInvalidParentheses(s: str) -> List[str]:
    def is_valid(t):
        count = 0
        for i in range(len(t)):
            if t[i] == "(":
                count += 1
            elif t[i] == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0

    queue = deque([s])
    visited = set()
    res = []
    found = False

    while queue:
        s = queue.popleft()
        if is_valid(s):
            res.append(s)
            found = True

        if found:
            continue

        for i in range(len(s)):
            if s[i] not in ("(", ")"):
                continue
            next_try = s[:i] + s[i + 1:]
            print(next_try)
            if next_try not in visited:
                queue.append(next_try)
                visited.add(s)
    return res


if __name__ == "__main__":
    removeInvalidParentheses(")(")