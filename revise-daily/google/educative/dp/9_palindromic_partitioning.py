def palindromic_partitioning(s):

    def rec(start_idx, end_idx):
        if start_idx >= end_idx or s[start_idx:end_idx+1] == s[start_idx:end_idx+1:-1]:
            return 0

        count = end_idx - start_idx
        for i in range(start_idx, end_idx+1):
            substr = s[start_idx:i+1]
            if substr == substr[::-1]:
                count = min(count, 1+rec(i+1, end_idx))
        return count

    return rec(0, len(s)-1)