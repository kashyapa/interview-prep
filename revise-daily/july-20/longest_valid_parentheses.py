def longest_valid_parentheses(str):

    left_indices = []
    length = 0
    start = -1
    for i in range(len(str)):
        if str[i] == "(":
            left_indices.append(i)
        elif not left_indices:
            start = i
        else:
            begin = left_indices[-1] if left_indices else start
            length = max(length, i-begin+1)
    return length