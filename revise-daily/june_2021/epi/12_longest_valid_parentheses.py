from collections import deque


def longest_valid_parentheses(str):
    stack = deque()
    start, end = -1, -1
    max_length = 0
    for i in range(len(str)):
        if str[i] == "(":
            stack.append(i)
        elif not stack:
            end = i
        else:
            stack.pop()
            cur_length = i - end if not stack else i - stack[-1]
            max_length = max(max_length, cur_length)
    return max_length
