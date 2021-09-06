def regular_expression_matching(ex, pattern):
    def rec(ex, pattern):

        if len(pattern) == 0:
            return True
        if pattern[0] == "$":
            return len(ex) == 0

        i = 0
        # dccd matches *cd
        if pattern[0] == "*" and len(pattern) > 1:
            while i < len(ex) and pattern[1] in (ex[i], "."):
                if rec(ex, pattern[2:]):
                    return True
                i += 1
            return rec(ex, pattern[2:])

        return rec(ex[1:], pattern[1:]) if pattern[0] in (".", ex[0]) else rec(ex[1:], pattern)

    if ex[0] == "^":
        return rec(ex[1:], pattern)
    return rec(ex, pattern)