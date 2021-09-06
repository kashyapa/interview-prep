def palindromic_decompositions(str):

    def rec(start_idx, end_idx, palindromes):

        if start_idx == end_idx:
            res.append(palindromes[:])
            return

        for i in range(start_idx, end_idx+1):
            substr = str[start_idx:i+1]
            if substr == substr[::-1]:
                rec(i+1, end_idx, palindromes + [substr])

        return

    res = []
    rec(0, len(str), [])
    return res
