def palindromic_partitioning(s):
    def palindrome_cutting(start, palindrome_cuts):
        if start == len(s):
            res.append(palindrome_cuts[:])
            return

        for i in range(start+1, len(s) + 1):
            prefix = s[start: i ]
            if prefix == prefix[::-1]:
                palindrome_cutting(i, palindrome_cuts+[prefix])

        return

    res = []
    palindrome_cutting(0, [])
    return res


def partition(s):
    def backtrack(start, end, tmp):
        if start == end:
            ans.append(tmp[:])
        for i in range(start, end):
            cur = s[start:i + 1]
            if cur == cur[::-1]:
                tmp.append(cur)
                backtrack(i + 1, end, tmp)
                tmp.pop()

    ans = []
    backtrack(0, len(s), [])
    return ans


if __name__ == '__main__':
    print(palindromic_partitioning("slkklsffnn"))
