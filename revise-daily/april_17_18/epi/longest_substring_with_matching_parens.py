def longest_substring_matching_parens(parens):
    left_bracket_indices = []
    start, end = 0, -1
    max_width = 0
    for i, c in enumerate(parens):
        if c == "(":
            left_bracket_indices.append(i)
        elif not left_bracket_indices:
            end = i
        else:
            left_bracket_indices.pop()
            width = i - left_bracket_indices[-1] if left_bracket_indices else i - end
            max_width = max(max_width, width)
    return max_width
