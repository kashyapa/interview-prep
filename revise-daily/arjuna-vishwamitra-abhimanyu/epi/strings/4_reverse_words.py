def reverse_words(s):
    def reverse_string(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1
    reverse_string(s, 0, len(s)-1)

    start, end = 0, 0
    while end < len(s):
        while end < len(s) and s[end] == " ":
            end += 1
        if end == len(s):
            break

        start = end
        while end < len(s) and s[end] != " ":
            end += 1

        reverse_string(s, start, end-1)
    return s


if __name__ == '__main__':
    print(''.join(reverse_words(list("this is a  ,     test for reversing"))))
