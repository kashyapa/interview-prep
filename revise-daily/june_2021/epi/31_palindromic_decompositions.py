def generate_palindromic_decompositions(str):

    def rec(start_idx, end_idx):
        if start_idx > end_idx:
            return None

        for i in range(start_idx, end_idx):
            substr = str[start_idx:i]
            if substr == substr[::-1]:
                palindromic_decompositions.append(substr)
                rec(i, end_idx)

    palindromic_decompositions = []
    return rec(0, len(str))