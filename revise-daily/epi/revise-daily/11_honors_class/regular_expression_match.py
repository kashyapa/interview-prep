def regular_expression_match(regex, str):
    def is_match_here(regex, str):
        if not regex:
            return True

        if regex == "$":
            return not str

        # *bc c
        # *bc bbbbc
        # *bc cccdfdf
        # *bc bc

        if regex[1] == "*" and len(regex) >= 2:
            i = 1
            while i <= len(str) and regex[0] in (str[i-1], "."):
                if is_match_here(regex[2:], str[i:]):
                    return True
                i += 1
            return is_match_here(regex[2:], str)

        return bool(str and regex[0] in (str[0], ".") and is_match_here(regex[1:], str[1:]))

    if regex[0] == "^":
        return is_match_here(regex[1:], str)

    return is_match_here(regex, str)
