# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater
# than a given ‘key’. Assume the given array is a circular list, which means that the last letter is assumed to be
# connected with the first letter. This also means that the smallest letter in the given array is greater than the
# last letter of the array and is also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.


def search_next_letter(letters, key):

    l, r = 0, len(letters) - 1

    while l <= r:
        m = l + (r-l)//2

        if key == letters[m]:
            return letters[(m+1) % len(letters)]

        if key < letters[m]:
            r = m - 1
        else:
            l = m + 1

    return letters[l % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


if __name__ == "__main__":
    main()
