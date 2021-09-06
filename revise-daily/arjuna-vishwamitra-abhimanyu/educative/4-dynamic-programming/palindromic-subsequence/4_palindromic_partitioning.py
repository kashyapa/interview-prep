def palindromic_partitioning(str):

    def is_palindromic(l, r):
        
        while l >=0 and r < len(str) and str[l] == str[r]:
            l += 1
            r -= 1
        return True if l >= r else False
    
    def rec(start_index, end_index):

        if start_index >= end_index or is_palindromic(start_index, end_index):
            return 0
            
        min_cuts = end_index - start_index
        
        for i in range(start_index, end_index+1):
            if is_palindromic(start_index, i):
                min_cuts = min(min_cuts, 1+rec(i+1, end_index))
        return min_cuts
    
