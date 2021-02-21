# Given a string, we want to cut it into pieces such that each piece is a palindrome.
# Write a function to return the minimum number of cuts needed.


def find_MPP_cuts(st):
    return find_MPP_cuts_recursive(st, 0, len(st) - 1)


def find_MPP_cuts_recursive(st, start_index, end_index):

    if start_index >= end_index or is_palindromic(st, start_index, end_index):
        return 0

    min_cuts = end_index - start_index
    for i in range(start_index, end_index+1):
        if is_palindromic(st, start_index, i):
            min_cuts = min(min_cuts, 1 + find_MPP_cuts_recursive(st, i+1, end_index))

    return min_cuts


def is_palindromic(st, start_index, end_index):
    while start_index < end_index and st[start_index] == st[end_index]:
        start_index += 1
        end_index -= 1

    return True if start_index >= end_index else False


def main():
    print(find_MPP_cuts("abdbca"))
    print(find_MPP_cuts("cdpdd"))
    print(find_MPP_cuts("pqr"))
    print(find_MPP_cuts("pp"))
    print(find_MPP_cuts("madam"))


if __name__ == "__main__":
    main()
