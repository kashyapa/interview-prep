 # Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"


def find_letter_case_string_permutations(str):
    permutations = []

    permutations.append(str)

    for i in range(len(str)):

        if str[i].isalpha():
            for j in range(len(permutations)):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))
    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("abc")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


if __name__ == "__main__":
    main()
