def regular_expression_match(regex, s):
    def is_match_here(regex, s):
        if not regex:
            return True

        if regex[0] == "$":
            return not s

        if len(regex) >= 2 and regex[1] == "*":
            i = 1
            while i < len(s) and regex[0] in (".", s[i-1]):
                if is_match_here(regex[2:], s[i:]):
                    return True
                i += 1
            return is_match_here(regex[2:], s)

        return bool(s and regex[0] in (".",s[0]) and is_match_here(regex[1:], s[1:]))

    if regex[0] == "^":
        return is_match_here(regex[1:], s)
    return any(is_match_here(regex, s[i:]) for i in range(len(s)+1))