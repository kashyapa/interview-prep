# Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.


def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1

    if st[startIndex] == st[endIndex]:
        remaining_length = endIndex - startIndex - 1
        if remaining_length == find_LPS_length_recursive(st, startIndex + 1, endIndex - 1):
            return remaining_length + 2

    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)

    return max(c1, c2)


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))

if __name__ == "__main__":
    main()
