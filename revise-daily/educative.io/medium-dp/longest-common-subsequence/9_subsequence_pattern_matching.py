# Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.
#
# Example 1: Input: string: “baxmx”, pattern: “ax”
# Output: 2
# Explanation: {baxmx, baxmx}.
#
# Example 2:
#
# Input: string: “tomorrow”, pattern: “tor”
# Output: 4
# Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.


def find_SPM_count(str, pat):
    return find_SPM_count_recursive(str, pat, 0, 0)


def find_SPM_count_recursive(str, pat, strIndex, patIndex):
    # if we have reached the end of the pattern
    if patIndex == len(pat):
        return 1

    # if we have reached the end of the string but pattern has still some characters left
    if strIndex == len(str):
        return 0

    c1 = 0
    if str[strIndex] == pat[patIndex]:
        c1 = find_SPM_count_recursive(str, pat, strIndex + 1, patIndex + 1)

    c2 = find_SPM_count_recursive(str, pat, strIndex + 1, patIndex)

    return c1 + c2


def main():
    print(find_SPM_count("baxmx", "ax"))
    print(find_SPM_count("tomorrow", "tor"))


main()
