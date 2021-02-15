def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0

    return ''.join(result)


def encoding(s):
    count = 0
    result = []
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1
    return ''.join(result)
