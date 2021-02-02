# static boolean isMatch(String v, String pattern)
# // cat   c*t      → true
# // cat   *t       → true
# // dog   c*t      → false

# catcat
# dlfjk;dasjfksdajfkajsdflkajs;dfkj; dogdog    catcat*dogdog    -> true

# catcatdlfjk;dasjfksdajfkajsdflkajs;dfkj;dogdogaldjfa;ld    catcat*dogdog    -> false


def is_match(p, s):
    i = 0
    if not p and not s:
        return True
    elif not p:
        return False

    # p -> regex pattern
    # s -> string
    j = i
    while j < len(p) and p[j] != '*':
        j += 1

    substr = p[i:j]
    # print(substr)
    if s[i:j] != substr:
        return False

    if j == len(p):
        return True

    elif j == len(s):
        return False

    last_part_of_regex = p[j + 1:]
    print(last_part_of_regex)
    j = len(s)
    i = len(last_part_of_regex)

    while i > 0:
        if s[j - 1] != last_part_of_regex[i - 1]:
            return False
        j -= 1
        i -= 1

    return True


if __name__ == '__main__':
    #print(is_match('c*t', 'cat'))
    #print(is_match('*t', 'cat'))
    #print(is_match('c*t', 'dog'))
    #print(is_match('catcat*dogdog', 'catcatdlfjk;dasjfksdajfkajsdflkajs;dfkj;dogdog'))
    #print(is_match('*', 'jkewfnwe'))
    #print(is_match('', '*'))
    #print(is_match('', ''))
    #print(is_match('cat', 'dog'))
    #print(is_match('cat', 'cat'))
    print(is_match('cat*cat', 'cat'))
