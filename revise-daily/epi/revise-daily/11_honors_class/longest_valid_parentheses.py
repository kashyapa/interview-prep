def longest_valid_parentheses(parentheses):
    left_indices = []
    for i in range(len(parentheses)):
        if parentheses[i] == "(":
            left_indices.append(i)
        elif not left_indices: # or all lefts have been popped out because of a previously found valid parentheses string
            end = i
        else:
            left_indices.pop()
            start = left_indices[-1] if left_indices else end
            max_length = max(max_length, i - start + 1)
    return max_length

