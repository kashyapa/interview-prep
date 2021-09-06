from collections import Counter


def shortest_supersequence(s1, s2):

    def rec(i1, i2, n1, n2):

        if i1 == len(s1):
            return n2-i2
        elif i2 == len(s2):
            return n1-i1

        if s1[i1] == s2[i2]:
            return 1 + rec(i1+1, i2+1, n1, n2)
        c1 = 1 + rec(i1+1, i2, n1, n2)
        c2 = 1+ rec(i1, i2+1, n1, n2)
        return max(c1, c2)


def shortest_supersequence2(s1, s2):
    s1_count = Counter(s1)
    s2_count = Counter(s2)

    super_sequence = []
    for k in s1_count:
        super_sequence.append(k * max(s1_count[k], s2_count[k]))
        if k in s2_count:
            del s2_count[k]

    for k in s2_count:
        super_sequence.append(k * max(s1_count[k], s2_count[k]))
        if k in s1_count:
            del s1_count[k]
    print("".join(super_sequence))
    print(len("".join(super_sequence)))


def main():
    shortest_supersequence2("abcf", "bdcf")
    shortest_supersequence2("dynamic", "programming")


if __name__ == "__main__":
    main()
